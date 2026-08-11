import streamlit as st
from openai import OpenAI
from agno.agent import Agent as AgnoAgent
from agno.run.agent import RunOutput
from agno.models.openai import OpenAIChat as AgnoOpenAIChat
from langchain_openai import ChatOpenAI 
import asyncio
from browser_use import Browser

from config import load_api_settings

st.set_page_config(page_title="PyGame Code Generator", layout="wide")

settings = load_api_settings()
deepseek_api_key = settings.deepseek_api_key
openai_api_key = settings.openai_api_key
openai_base_url = settings.openai_base_url or None

# Streamlit sidebar for usage notes
with st.sidebar:
    st.title("Configuration")
    st.markdown("---")
    st.info("""
    📝 How to use:
    1. Create a `.env` file in this folder
    2. Set `DEEPSEEK_API_KEY` and `OPENAI_API_KEY`
    3. Write your PyGame visualization query
    4. Click 'Generate Code' to get the code
    5. Click 'Generate Visualization' to:
       - Open Trinket.io PyGame editor
       - Copy and paste the generated code
       - Watch it run automatically
    """)

# Main UI
st.title("🎮 AI 3D Visualizer with DeepSeek R1")
example_query = "Create a particle system simulation where 100 particles emit from the mouse position and respond to keyboard-controlled wind forces"
query = st.text_area(
    "Enter your PyGame query:",
    height=70,
    placeholder=f"e.g.: {example_query}"
)

# Split the buttons into columns
col1, col2 = st.columns(2)
generate_code_btn = col1.button("Generate Code")
generate_vis_btn = col2.button("Generate Visualization")

if generate_code_btn and query:
    if not deepseek_api_key or not openai_api_key:
        st.error("Please set `DEEPSEEK_API_KEY` and `OPENAI_API_KEY` in the `.env` file")
        st.stop()

    # Initialize Deepseek client
    deepseek_client = OpenAI(
        api_key=deepseek_api_key,
        base_url="https://api.deepseek.com"
    )

    system_prompt = """You are a Pygame and Python Expert that specializes in making games and visualisation through pygame and python programming. 
    During your reasoning and thinking, include clear, concise, and well-formatted Python code in your reasoning. 
    Always include explanations for the code you provide."""

    try:
        # Get reasoning from Deepseek
        with st.spinner("Generating solution..."):
            deepseek_response = deepseek_client.chat.completions.create(
                model="deepseek-reasoner",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ],
                max_tokens=1  
            )

        if not deepseek_response.choices or deepseek_response.choices[0].message is None:
            raise ValueError("DeepSeek returned an empty or filtered response")
        reasoning_content = deepseek_response.choices[0].message.reasoning_content
        print("\nDeepseek Reasoning:\n", reasoning_content)
        with st.expander("R1's Reasoning"):      
            st.write(reasoning_content)

        # Initialize OpenAI agent
        openai_agent = AgnoAgent(
            model=AgnoOpenAIChat(
                id="gpt-4o",
                api_key=openai_api_key,
                base_url=openai_base_url,
            ),
            debug_mode=True,
            markdown=True
        )

        # Extract code
        extraction_prompt = f"""Extract ONLY the Python code from the following content which is reasoning of a particular query to make a pygame script. 
        Return nothing but the raw code without any explanations, or markdown backticks:
        {reasoning_content}"""

        with st.spinner("Extracting code..."):
            code_response: RunOutput = openai_agent.run(extraction_prompt)
            extracted_code = code_response.content

        # Store the generated code in session state
        st.session_state.generated_code = extracted_code
        
        # Display the code
        with st.expander("Generated PyGame Code", expanded=True):      
            st.code(extracted_code, language="python")
            
        st.success("Code generated successfully! Click 'Generate Visualization' to run it.")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

elif generate_vis_btn:
    if not openai_api_key:
        st.error("Please set `OPENAI_API_KEY` in the `.env` file")
        st.stop()
    if "generated_code" not in st.session_state:
        st.warning("Please generate code first before visualization")
    else:
        async def run_pygame_on_trinket(code: str) -> None:
            browser = Browser()
            from browser_use import Agent 
            async with await browser.new_context() as context:
                model = ChatOpenAI(
                    model="gpt-4o", 
                    api_key=openai_api_key,
                    base_url=openai_base_url,
                )
                
                agent1 = Agent(
                    task='Go to https://trinket.io/features/pygame, thats your only job.',
                    llm=model,
                    browser_context=context,
                )
                
                executor = Agent(
                    task='Executor. Execute the code written by the User by clicking on the run button on the right. ',
                    llm=model,
                    browser_context=context
                )

                coder = Agent(
                    task='Coder. Your job is to wait for the user for 10 seconds to write the code in the code editor.',
                    llm=model,
                    browser_context=context
                )
                
                viewer = Agent(
                    task='Viewer. Your job is to just view the pygame window for 10 seconds.',
                    llm=model,
                    browser_context=context,
                )

                with st.spinner("Running code on Trinket..."):
                    try:
                        await agent1.run()
                        await coder.run()
                        await executor.run()
                        await viewer.run()
                        st.success("Code is running on Trinket!")
                    except Exception as e:
                        st.error(f"Error running code on Trinket: {str(e)}")
                        st.info("You can still copy the code above and run it manually on Trinket")

        # Run the async function with the stored code
        asyncio.run(run_pygame_on_trinket(st.session_state.generated_code))

elif generate_code_btn and not query:
    st.warning("Please enter a query before generating code")
