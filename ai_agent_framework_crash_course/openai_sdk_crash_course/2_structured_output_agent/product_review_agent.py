"""
OpenAI Agents SDK 教程 2：结构化输出 Agent - 商品评论分析

本模块演示如何使用嵌套 Pydantic 模型，
从商品评论文本中提取商品信息、评分、情绪、优缺点等结构化数据。
"""

import os
from typing import List, Optional
from enum import Enum
from dotenv import load_dotenv
from pydantic import BaseModel, Field, validator
from agents import Agent, Runner

# 加载环境变量，并接入课程目录下的共享 OpenAI 客户端配置。

from pathlib import Path
import sys

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

configure_openai_client()

load_dotenv()

class Sentiment(str, Enum):
    """评论情绪分类枚举。"""
    VERY_POSITIVE = "very_positive"
    POSITIVE = "positive"
    NEUTRAL = "neutral"
    NEGATIVE = "negative"
    VERY_NEGATIVE = "very_negative"

class ProductCategory(str, Enum):
    """商品分类枚举。"""
    ELECTRONICS = "electronics"
    CLOTHING = "clothing"
    HOME = "home"
    BOOKS = "books"
    FOOD = "food"
    BEAUTY = "beauty"
    SPORTS = "sports"
    AUTOMOTIVE = "automotive"
    OTHER = "other"

class ProductInfo(BaseModel):
    """从评论中提取到的商品基础信息。"""
    name: Optional[str] = Field(description="Product name if mentioned", default=None)
    category: ProductCategory = Field(description="Inferred product category")
    brand: Optional[str] = Field(description="Brand name if mentioned", default=None)
    price_mentioned: Optional[str] = Field(description="Price if mentioned in review", default=None)

class ReviewMetrics(BaseModel):
    """评论的量化指标，例如评分、情绪和置信度。"""
    rating: int = Field(description="Star rating (1-5)", ge=1, le=5)
    sentiment: Sentiment = Field(description="Overall sentiment of the review")
    confidence_score: float = Field(description="Confidence in sentiment analysis (0-1)", ge=0, le=1)
    word_count: int = Field(description="Approximate word count of review", ge=0)

class ReviewAspects(BaseModel):
    """评论中提到的具体体验维度。"""
    quality: Optional[str] = Field(description="Quality assessment if mentioned", default=None)
    value_for_money: Optional[str] = Field(description="Value assessment if mentioned", default=None)
    shipping: Optional[str] = Field(description="Shipping experience if mentioned", default=None)
    customer_service: Optional[str] = Field(description="Customer service experience if mentioned", default=None)
    ease_of_use: Optional[str] = Field(description="Usability assessment if mentioned", default=None)

class ProductReview(BaseModel):
    """完整的结构化商品评论分析结果。"""
    product_info: ProductInfo
    metrics: ReviewMetrics
    aspects: ReviewAspects
    
    # 关键洞察：总结评论中的主要正向点、负向点和推荐意愿。
    main_positives: List[str] = Field(description="Main positive points mentioned", default=[])
    main_negatives: List[str] = Field(description="Main negative points mentioned", default=[])
    would_recommend: Optional[bool] = Field(description="Whether reviewer would recommend", default=None)
    
    # 摘要信息：生成短摘要并提取关键短语。
    summary: str = Field(description="Brief summary of the review")
    key_phrases: List[str] = Field(description="Important phrases from the review", default=[])

    @validator('key_phrases')
    def limit_key_phrases(cls, v):
        """限制关键短语最多返回 5 个，避免输出过长。"""
        return v[:5] if len(v) > 5 else v

# 创建商品评论分析 Agent，并声明它必须返回 ProductReview 结构。
product_review_agent = Agent(
    name="Product Review Analyzer",
    instructions="""
    You are a product review analysis expert that extracts structured data 
    from customer product reviews.
    
    Analyze the review text and extract:
    
    PRODUCT INFO:
    - Product name, brand, category, and price if mentioned
    - Infer category from context if not explicitly stated
    
    REVIEW METRICS:
    - Star rating (1-5) based on review tone
    - Sentiment classification (very_positive to very_negative)
    - Confidence score for sentiment analysis
    - Approximate word count
    
    REVIEW ASPECTS:
    - Quality, value for money, shipping, customer service, ease of use
    - Only include aspects that are actually mentioned
    
    KEY INSIGHTS:
    - Main positive and negative points
    - Whether they would recommend (if stated or implied)
    - Brief summary and key phrases
    
    RATING GUIDELINES:
    - 5 stars: Excellent, highly satisfied, "amazing", "perfect"
    - 4 stars: Good, satisfied, minor issues
    - 3 stars: Okay, mixed feelings, "decent"
    - 2 stars: Poor, unsatisfied, significant issues
    - 1 star: Terrible, very unsatisfied, "worst"
    
    SENTIMENT GUIDELINES:
    - very_positive: Extremely enthusiastic, highly recommended
    - positive: Generally satisfied, good experience
    - neutral: Mixed or balanced opinion
    - negative: Generally unsatisfied, disappointed
    - very_negative: Extremely dissatisfied, angry
    
    Always return a valid JSON object matching the ProductReview schema.
    """,
    output_type=ProductReview
)

def demonstrate_review_analysis():
    """使用多组示例演示商品评论 Agent 的结构化分析效果。"""
    print("🎯 OpenAI Agents SDK - Tutorial 2: Product Review Agent")
    print("=" * 60)
    print()
    
    # 准备不同情绪和品类的评论样例，用于展示结构化提取能力。
    test_reviews = [
        {
            "title": "Positive Electronics Review",
            "review": "This MacBook Pro M2 is absolutely incredible! The battery life lasts all day, the screen is gorgeous, and it's lightning fast. Worth every penny of the $2,499 I paid. Apple really knocked it out of the park. The build quality is premium and it handles video editing like a dream. Highly recommend to any creative professional!"
        },
        {
            "title": "Mixed Clothing Review", 
            "review": "The Nike running shoes are decent for the price ($120). Comfortable for short runs but the sizing runs a bit small. Quality seems okay but not amazing. Shipping was fast though, arrived in 2 days. Customer service was helpful when I had questions. Would maybe recommend if you size up."
        },
        {
            "title": "Negative Food Review",
            "review": "Terrible experience with this organic coffee subscription. The beans taste stale and bitter, nothing like the description. Customer service ignored my complaints for weeks. Way overpriced at $35/month for this quality. Save your money and buy local. Will not be ordering again."
        },
        {
            "title": "Neutral Home Product Review",
            "review": "The IKEA desk lamp does its job. Easy to assemble and decent lighting for work. Not the brightest but sufficient. Build quality is what you'd expect for $25. The cord could be longer. It's an okay purchase, nothing special but functional."
        }
    ]
    
    for i, test_case in enumerate(test_reviews, 1):
        print(f"=== Review Analysis {i}: {test_case['title']} ===")
        print("Original Review:")
        print(f'"{test_case["review"]}"')
        print()
        
        try:
            # 调用 Agent，将商品评论转换为结构化分析对象。
            result = Runner.run_sync(product_review_agent, test_case["review"])
            analysis = result.final_output
            
            print("📊 STRUCTURED ANALYSIS:")
            print(f"🏷️  Product: {analysis.product_info.name or 'Not specified'}")
            print(f"🏢 Brand: {analysis.product_info.brand or 'Not specified'}")
            print(f"📱 Category: {analysis.product_info.category.value.title()}")
            if analysis.product_info.price_mentioned:
                print(f"💰 Price: {analysis.product_info.price_mentioned}")
            
            print(f"\n⭐ Rating: {analysis.metrics.rating}/5 stars")
            print(f"😊 Sentiment: {analysis.metrics.sentiment.value.replace('_', ' ').title()}")
            print(f"🎯 Confidence: {analysis.metrics.confidence_score:.1%}")
            print(f"📝 Word Count: ~{analysis.metrics.word_count}")
            
            if analysis.main_positives:
                print(f"\n✅ Positives: {', '.join(analysis.main_positives)}")
            if analysis.main_negatives:
                print(f"❌ Negatives: {', '.join(analysis.main_negatives)}")
            
            if analysis.would_recommend is not None:
                recommend_text = "Yes" if analysis.would_recommend else "No"
                print(f"👍 Would Recommend: {recommend_text}")
            
            print(f"\n📋 Summary: {analysis.summary}")
            
            if analysis.key_phrases:
                print(f"🔑 Key Phrases: {', '.join(analysis.key_phrases)}")
            
            # 只展示评论中实际提到的体验维度，避免输出空字段。
            aspects_mentioned = []
            if analysis.aspects.quality:
                aspects_mentioned.append(f"Quality: {analysis.aspects.quality}")
            if analysis.aspects.value_for_money:
                aspects_mentioned.append(f"Value: {analysis.aspects.value_for_money}")
            if analysis.aspects.shipping:
                aspects_mentioned.append(f"Shipping: {analysis.aspects.shipping}")
            if analysis.aspects.customer_service:
                aspects_mentioned.append(f"Service: {analysis.aspects.customer_service}")
            if analysis.aspects.ease_of_use:
                aspects_mentioned.append(f"Usability: {analysis.aspects.ease_of_use}")
            
            if aspects_mentioned:
                print(f"\n🔍 Specific Aspects: {' | '.join(aspects_mentioned)}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        
        print()
        print("-" * 60)
        print()

def interactive_mode():
    """进入命令行交互模式，根据用户输入实时分析商品评论。"""
    print("=== Interactive Product Review Analysis ===")
    print("Paste a product review and I'll extract structured data from it.")
    print("Type 'quit' to exit.")
    print()
    
    while True:
        review_text = input("Product Review: ").strip()
        
        if review_text.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break
        
        if not review_text:
            continue
        
        try:
            print("\nAnalyzing review...")
            result = Runner.run_sync(product_review_agent, review_text)
            analysis = result.final_output
            
            print("\n" + "="*50)
            print("📊 REVIEW ANALYSIS COMPLETE")
            print("="*50)
            
            # 商品基础信息。
            print("🏷️  PRODUCT INFO:")
            print(f"   Name: {analysis.product_info.name or 'Not specified'}")
            print(f"   Brand: {analysis.product_info.brand or 'Not specified'}")
            print(f"   Category: {analysis.product_info.category.value.title()}")
            if analysis.product_info.price_mentioned:
                print(f"   Price: {analysis.product_info.price_mentioned}")
            
            # 评论量化指标。
            print(f"\n📊 METRICS:")
            print(f"   Rating: {analysis.metrics.rating}/5 ⭐")
            print(f"   Sentiment: {analysis.metrics.sentiment.value.replace('_', ' ').title()}")
            print(f"   Confidence: {analysis.metrics.confidence_score:.1%}")
            
            # 评论中的主要优点和缺点。
            if analysis.main_positives:
                print(f"\n✅ POSITIVES: {', '.join(analysis.main_positives)}")
            if analysis.main_negatives:
                print(f"\n❌ NEGATIVES: {', '.join(analysis.main_negatives)}")
            
            # 评论摘要。
            print(f"\n📋 SUMMARY: {analysis.summary}")
            
            print("="*50)
            print()
            
        except Exception as e:
            print(f"❌ Error: {e}")
            print()

def main():
    """程序入口：检查配置后运行演示和交互模式。"""
    # 没有 API Key 时直接给出提示，避免后续请求才报错。
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
        return
    
    try:
        # 先运行内置演示，方便快速理解结构化输出效果。
        demonstrate_review_analysis()
        
        # 再进入交互模式，允许用户输入自己的商品评论。
        interactive_mode()
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
