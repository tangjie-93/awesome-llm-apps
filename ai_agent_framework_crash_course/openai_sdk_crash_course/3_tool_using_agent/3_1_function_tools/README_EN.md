# Function Tools Agent

Demonstrates how to create custom function tools with the `@function_tool` decorator.

## What This Demonstrates

- **Custom Function Tools**: Create tools with the `@function_tool` decorator
- **Tool Descriptions**: Provide clear docstrings so the LLM understands each tool
- **Parameter Handling**: Use type hints and default parameters
- **Error Handling**: Handle tool failures gracefully

## Quick Start

1. **Install the OpenAI Agents SDK**:
   ```bash
   pip install openai-agents
   ```

2. **Set up the environment**:
   ```bash
   cp ../env.example .env
   # Edit .env and add your OpenAI API key
   ```

3. **Run the agent**:
   ```python
   from agents import Runner
   from agent import root_agent

   result = Runner.run_sync(root_agent, "What time is it in New York?")
   print(result.final_output)
   ```

## Key Concepts

- **`@function_tool` Decorator**: Convert Python functions into agent tools
- **Tool Docstrings**: Help the LLM understand when to use each tool
- **Type Hints**: Provide parameter validation and documentation
- **Tool Registration**: Add tools to the agent configuration

## Available Tools

### `get_current_time(timezone: str = "UTC")`

- Returns the current time in the specified timezone
- Handles timezone validation and error cases

### `greet_user(name: str)`

- A simple greeting tool demonstrating basic tool usage
- Shows how parameters are passed from the LLM to a tool

## Next Steps

- [Built-in Tools](../3_2_builtin_tools/README.md) - Use WebSearch and CodeInterpreter
- [Agents as Tools](../3_3_agents_as_tools/README.md) - Explore advanced agent orchestration
