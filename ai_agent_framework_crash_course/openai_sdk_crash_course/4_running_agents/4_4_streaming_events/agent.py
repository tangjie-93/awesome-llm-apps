from agents import Agent, Runner
from agents.stream_events import RawResponsesStreamEvent
from openai.types.responses.response_text_delta_event import ResponseTextDeltaEvent
import asyncio
import time

# Create agents for demonstrating streaming events
# 创建用于演示流式事件处理的 Agent

from pathlib import Path
import sys

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

configure_openai_client()

root_agent = Agent(
    name="Streaming Demo Agent",
    instructions="""
    You are a helpful assistant that demonstrates streaming capabilities.
    
    When asked to write long content, be comprehensive and detailed.
    When asked technical questions, provide thorough explanations.
    """
)

# Example 1: Basic streaming with event processing
# 示例 1：基础流式执行和事件处理
async def basic_streaming_example():
    """Demonstrates basic streaming event handling"""
    
    print("=== Basic Streaming Events ===")
    print("Requesting a detailed explanation...")
    
    full_response = ""
    start_time = time.time()
    
    # Use run_streamed to get real-time events
    # 使用 run_streamed 获取实时事件流
    streaming_result = Runner.run_streamed(
        root_agent, 
        "Write a comprehensive explanation of how machine learning works, including examples."
    )
    async for event in streaming_result.stream_events():
        # Process different types of streaming events
        # 根据事件类型分别处理文本增量和生命周期事件
        if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
            # This is a text content event
            # 文本增量事件：追加内容并立即打印
            full_response += event.data.delta
            print(event.data.delta, end='', flush=True)
        
        if hasattr(event, 'type'):
            # Handle different event types
            # 处理响应开始、完成等生命周期事件
            if event.type == "response_start":
                print(f"\n[EVENT] Response started")
            elif event.type == "response_complete":
                print(f"\n[EVENT] Response completed")
                
    elapsed_time = time.time() - start_time
    print(f"\n\nStreaming completed in {elapsed_time:.2f} seconds")
    print(f"Total response length: {len(full_response)} characters")
    
    return full_response

# Example 2: Advanced streaming with RunResultStreaming
# 示例 2：使用 RunResultStreaming 进行高级流式处理
async def advanced_streaming_example():
    """Shows how to work with RunResultStreaming object"""
    
    print("\n=== Advanced Streaming with RunResultStreaming ===")
    print("Generating a long story with progress tracking...")
    
    # Track streaming progress
    # 记录事件数量和已接收的内容块，用于展示进度
    events_count = 0
    chunks_received = []
    
    # Get the streaming result generator
    # 获取流式结果对象
    streaming_result = Runner.run_streamed(
        root_agent,
        "Write a creative short story about a robot who discovers emotions. Make it at least 500 words."
    )
    
    print("Processing streaming events:")
    
    async for event in streaming_result.stream_events():
        events_count += 1
        
        # Collect content chunks
        # 收集文本内容块，并每 10 个块报告一次进度
        if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
            chunks_received.append(event.data.delta)
            # Show progress every 10 chunks
            # 每收到 10 个内容块后显示一次进度
            if len(chunks_received) % 10 == 0:
                print(f"\n[PROGRESS] Received {len(chunks_received)} chunks...")
            print(event.data.delta, end='', flush=True)
        
        # Handle specific event types
        # 处理工具调用等特定事件
        if hasattr(event, 'type'):
            if event.type == "tool_call_start":
                print(f"\n[EVENT] Tool call started")
            elif event.type == "tool_call_complete":
                print(f"\n[EVENT] Tool call completed")
    
    print(f"\n\nStreaming summary:")
    print(f"- Total events processed: {events_count}")
    print(f"- Content chunks received: {len(chunks_received)}")
    print(f"- Final story length: {sum(len(chunk) for chunk in chunks_received)} characters")
    
        # Access the final result
        # 获取最终拼接结果
    final_result = "".join(chunks_received)
    return final_result

# Example 3: Streaming with custom processing
# 示例 3：自定义流式处理和实时统计
async def custom_streaming_processing():
    """Demonstrates custom streaming event processing"""
    
    print("\n=== Custom Streaming Processing ===")
    print("Analyzing streaming patterns...")
    
    # Custom streaming analytics
    # 保存响应速度、块大小和总词数等统计指标
    analytics = {
        "words_per_second": [],
        "chunk_sizes": [],
        "response_time": None,
        "total_words": 0
    }
    
    start_time = time.time()
    last_update = start_time
    current_content = ""
    
    streaming_result = Runner.run_streamed(
        root_agent,
        "Explain the benefits and challenges of renewable energy in detail."
    )
    async for event in streaming_result.stream_events():
        current_time = time.time()
        
        if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
            # Track chunk size
            # 记录当前文本块的字符数
            chunk_size = len(event.data.delta)
            analytics["chunk_sizes"].append(chunk_size)
            
            # Update content
            # 累积当前响应内容
            current_content += event.data.delta
            
            # Calculate words per second every few chunks
            # 每收到几个文本块后，计算一次词语输出速度
            if len(analytics["chunk_sizes"]) % 5 == 0:
                time_diff = current_time - last_update
                if time_diff > 0:
                    words_in_chunk = len(event.data.delta.split())
                    wps = words_in_chunk / time_diff
                    analytics["words_per_second"].append(wps)
                    last_update = current_time
            
            print(event.data.delta, end='', flush=True)
    
    # Final analytics
    # 计算并输出最终统计结果
    analytics["response_time"] = time.time() - start_time
    analytics["total_words"] = len(current_content.split())
    
    print(f"\n\nStreaming Analytics:")
    print(f"- Total response time: {analytics['response_time']:.2f} seconds")
    print(f"- Total words: {analytics['total_words']}")
    print(f"- Average chunk size: {sum(analytics['chunk_sizes'])/len(analytics['chunk_sizes']):.1f} chars")
    
    if analytics["words_per_second"]:
        avg_wps = sum(analytics["words_per_second"]) / len(analytics["words_per_second"])
        print(f"- Average words per second: {avg_wps:.1f}")
    
    return analytics

# Example 4: Streaming with error handling
# 示例 4：带错误处理的流式执行
async def streaming_with_error_handling():
    """Shows proper error handling for streaming operations"""
    
    print("\n=== Streaming with Error Handling ===")
    
    try:
        response_parts = []
        
        streaming_result = Runner.run_streamed(
            root_agent,
            "What are the top 3 programming languages and why?"
        )
        async for event in streaming_result.stream_events():
            try:
                if isinstance(event, RawResponsesStreamEvent) and isinstance(event.data, ResponseTextDeltaEvent):
                    response_parts.append(event.data.delta)
                    print(event.data.delta, end='', flush=True)
                    
            except Exception as chunk_error:
                print(f"\n[ERROR] Error processing chunk: {chunk_error}")
                # Continue with the next chunk after a processing error
                # 当前块处理失败时继续处理后续块
                continue
                
        print(f"\n\nStreaming completed successfully!")
        print(f"Collected {len(response_parts)} response parts")
        
        return "".join(response_parts)
        
    except Exception as streaming_error:
        print(f"\n[ERROR] Streaming failed: {streaming_error}")
        return None

# Main execution
# 主执行入口
async def main():
    print("🚀 OpenAI Agents SDK - Streaming Events")
    print("=" * 60)
    
    await basic_streaming_example()
    await advanced_streaming_example()
    await custom_streaming_processing()
    await streaming_with_error_handling()
    
    print("\n✅ Streaming events tutorial complete!")
    print("Streaming enables real-time response processing for better user experience")

if __name__ == "__main__":
    asyncio.run(main())
