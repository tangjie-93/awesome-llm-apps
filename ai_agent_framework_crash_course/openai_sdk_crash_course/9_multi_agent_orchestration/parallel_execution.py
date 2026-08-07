import asyncio
from agents import Agent, ItemHelpers, Runner, trace

# Create specialized translation agent
# 创建专门负责西班牙语翻译的 Agent

from pathlib import Path
import sys

# 定位 openai_sdk_crash_course 根目录，方便导入共享配置。
_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

# 在创建和运行 Agent 前，先完成 OpenAI 客户端配置。
configure_openai_client()

# 基础翻译 Agent：每次调用都把用户输入翻译成自然流畅的西班牙语。
spanish_agent = Agent(
    name="Spanish Translator",
    instructions="You translate the user's message to Spanish. Provide natural, fluent translations."
)

# Create translation quality picker
# 创建翻译质量评估 Agent，用于从多个候选译文中选择最佳版本。
translation_picker = Agent(
    name="Translation Quality Picker",
    instructions="""
    You are an expert in Spanish translations. 
    Given multiple Spanish translation options, pick the most natural, accurate, and fluent one.
    Explain briefly why you chose that translation.
    """
)

# Example 1: Basic parallel execution with quality selection
async def parallel_translation_example():
    """并行运行同一个翻译 Agent 多次，并用评估 Agent 选择最佳结果。"""
    
    print("=== Parallel Translation with Quality Selection ===")
    
    # 原始英文消息，后续会被并行翻译三次。
    msg = "Hello, how are you today? I hope you're having a wonderful time!"
    print(f"Original message: {msg}")
    
    # Ensure the entire workflow is a single trace
    # 用一个 trace 包住完整流程，便于在追踪中查看并行调用和评估步骤。
    with trace("Parallel Translation Workflow") as workflow_trace:
        print("Running 3 parallel translation attempts...")
        
        # Run 3 parallel translations
        # 同时发起三次翻译请求，用于获得多个候选结果。
        res_1, res_2, res_3 = await asyncio.gather(
            Runner.run(spanish_agent, msg),
            Runner.run(spanish_agent, msg), 
            Runner.run(spanish_agent, msg)
        )
        
        # Extract text outputs from results
        # 从每次运行结果中提取最终文本输出。
        outputs = [
            ItemHelpers.text_message_outputs(res_1.new_items),
            ItemHelpers.text_message_outputs(res_2.new_items),
            ItemHelpers.text_message_outputs(res_3.new_items)
        ]
        
        # Combine all translations for comparison
        # 把多个候选译文合并成一个提示词，交给评估 Agent 对比。
        translations = "\n\n".join([f"Translation {i+1}: {output}" for i, output in enumerate(outputs)])
        print(f"\nAll translations:\n{translations}")
        
        # Use picker agent to select best translation
        # 评估 Agent 根据原文和候选译文选出质量最高的一版。
        best_translation = await Runner.run(
            translation_picker,
            f"Original English: {msg}\n\nTranslations to choose from:\n{translations}"
        )
    
    print(f"\nBest translation selected: {best_translation.final_output}")
    print(f"Workflow trace ID: {workflow_trace.trace_id}")
    
    return best_translation

# Example 2: Parallel execution with different specialized agents
async def parallel_specialized_agents():
    """并行运行不同风格的翻译 Agent，对比正式、口语和地区化译法。"""
    
    print("\n=== Parallel Execution with Specialized Agents ===")
    
    # Create different specialized agents
    # 创建正式风格翻译 Agent。
    formal_translator = Agent(
        name="Formal Spanish Translator",
        instructions="Translate to formal, polite Spanish using 'usted' forms."
    )
    
    # 创建口语风格翻译 Agent。
    casual_translator = Agent(
        name="Casual Spanish Translator", 
        instructions="Translate to casual, friendly Spanish using 'tú' forms."
    )
    
    # 创建墨西哥地区化西班牙语翻译 Agent。
    regional_translator = Agent(
        name="Mexican Spanish Translator",
        instructions="Translate to Mexican Spanish with regional expressions and vocabulary."
    )
    
    # 这句话适合展示不同语气和地区表达之间的差异。
    msg = "Hey friend, want to grab some coffee later?"
    print(f"Original message: {msg}")
    
    with trace("Multi-Style Translation") as style_trace:
        print("Running parallel translations with different styles...")
        
        # Run different translation styles in parallel
        # 同时运行三个不同风格的翻译 Agent。
        formal_result, casual_result, regional_result = await asyncio.gather(
            Runner.run(formal_translator, msg),
            Runner.run(casual_translator, msg),
            Runner.run(regional_translator, msg)
        )
        
        # Extract and display all results
        # 分别提取三个 Agent 的翻译结果。
        formal_text = ItemHelpers.text_message_outputs(formal_result.new_items)
        casual_text = ItemHelpers.text_message_outputs(casual_result.new_items)
        regional_text = ItemHelpers.text_message_outputs(regional_result.new_items)
        
        print(f"\nFormal style: {formal_text}")
        print(f"Casual style: {casual_text}")
        print(f"Regional style: {regional_text}")
        
        # Let user choose preferred style
        # 把不同风格放在同一个上下文中，让评估 Agent 推荐最合适的版本。
        style_comparison = f"""
        Original: {msg}
        
        Formal Spanish: {formal_text}
        Casual Spanish: {casual_text}
        Mexican Spanish: {regional_text}
        """
        
        style_recommendation = await Runner.run(
            translation_picker,
            f"Compare these translation styles and recommend which is most appropriate for the context: {style_comparison}"
        )
    
    print(f"\nStyle recommendation: {style_recommendation.final_output}")
    print(f"Multi-style trace ID: {style_trace.trace_id}")
    
    return style_recommendation

# Example 3: Parallel execution for content generation diversity
async def parallel_content_generation():
    """并行生成不同写作风格的内容，并综合优点生成最终版本。"""
    
    print("\n=== Parallel Content Generation for Diversity ===")
    
    # Create content generation agents with different approaches
    # 创意写作 Agent：强调画面感和叙事性。
    creative_agent = Agent(
        name="Creative Writer",
        instructions="Write creative, engaging content with vivid imagery and storytelling."
    )
    
    # 信息型写作 Agent：强调清晰、事实和重点信息。
    informative_agent = Agent(
        name="Informative Writer", 
        instructions="Write clear, factual, informative content focused on key information."
    )
    
    # 说服型写作 Agent：强调行动动机和说服力。
    persuasive_agent = Agent(
        name="Persuasive Writer",
        instructions="Write compelling, persuasive content that motivates action."
    )
    
    # 同一个主题会被三个不同风格的 Agent 并行处理。
    topic = "The benefits of learning a new language"
    print(f"Content topic: {topic}")
    
    with trace("Diverse Content Generation") as content_trace:
        print("Generating content with different writing styles in parallel...")
        
        # Generate different content approaches simultaneously
        # 并行生成创意型、信息型和说服型三个版本。
        creative_result, informative_result, persuasive_result = await asyncio.gather(
            Runner.run(creative_agent, f"Write a short paragraph about: {topic}"),
            Runner.run(informative_agent, f"Write a short paragraph about: {topic}"),
            Runner.run(persuasive_agent, f"Write a short paragraph about: {topic}")
        )
        
        # Extract content
        # 从三个运行结果中提取文本内容。
        creative_content = ItemHelpers.text_message_outputs(creative_result.new_items)
        informative_content = ItemHelpers.text_message_outputs(informative_result.new_items)
        persuasive_content = ItemHelpers.text_message_outputs(persuasive_result.new_items)
        
        print(f"\nCreative approach:\n{creative_content}")
        print(f"\nInformative approach:\n{informative_content}")
        print(f"\nPersuasive approach:\n{persuasive_content}")
        
        # Synthesize best elements from all approaches
        # 创建综合 Agent，用于融合三个版本中的优点。
        synthesis_agent = Agent(
            name="Content Synthesizer",
            instructions="Combine the best elements from multiple content pieces into one cohesive, high-quality paragraph."
        )
        
        # 把三个候选版本整理成一个输入，交给综合 Agent 生成最终内容。
        combined_content = f"""
        Topic: {topic}
        
        Creative version: {creative_content}
        
        Informative version: {informative_content}
        
        Persuasive version: {persuasive_content}
        """
        
        synthesized_result = await Runner.run(
            synthesis_agent,
            f"Create the best possible paragraph by combining elements from these approaches: {combined_content}"
        )
    
    print(f"\nSynthesized content: {synthesized_result.final_output}")
    print(f"Content generation trace ID: {content_trace.trace_id}")
    
    return synthesized_result

# Main execution
async def main():
    """依次运行所有并行多 Agent 编排示例。"""
    print("🎼 OpenAI Agents SDK - Parallel Multi-Agent Execution")
    print("=" * 60)
    
    # 示例 1：同一个 Agent 并行多次，提高候选质量。
    await parallel_translation_example()
    # 示例 2：多个专用 Agent 并行，获得不同视角。
    await parallel_specialized_agents()
    # 示例 3：并行生成多种内容版本，再做综合。
    await parallel_content_generation()
    
    print("\n✅ Parallel execution tutorial complete!")
    print("Parallel execution enables quality improvement through diversity and selection")

if __name__ == "__main__":
    asyncio.run(main())
