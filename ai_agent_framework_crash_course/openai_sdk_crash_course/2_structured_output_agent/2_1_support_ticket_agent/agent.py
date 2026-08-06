from typing import List, Optional
from enum import Enum
from agents import Agent
from pydantic import BaseModel, Field

from pathlib import Path
import sys

_OPENAI_SDK_ROOT = Path(__file__).resolve()
while _OPENAI_SDK_ROOT.name != "openai_sdk_crash_course" and _OPENAI_SDK_ROOT.parent != _OPENAI_SDK_ROOT:
    _OPENAI_SDK_ROOT = _OPENAI_SDK_ROOT.parent
if str(_OPENAI_SDK_ROOT) not in sys.path:
    sys.path.insert(0, str(_OPENAI_SDK_ROOT))

from openai_client_config import configure_openai_client

configure_openai_client()

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SupportTicket(BaseModel):
    title: str = Field(description="A concise summary of the issue")
    description: str = Field(description="Detailed description of the problem")
    priority: Priority = Field(description="The ticket priority level")
    category: str = Field(description="The department this ticket belongs to")
    steps_to_reproduce: Optional[List[str]] = Field(
        description="Steps to reproduce the issue (for technical problems)",
        default=None
    )
    estimated_resolution_time: str = Field(
        description="Estimated time to resolve this issue"
    )

root_agent = Agent(
    name="Support Ticket Creator",
    instructions="""
    You are a support ticket creation assistant that converts customer complaints 
    into well-structured support tickets.
    
    Based on customer descriptions, create structured support tickets with:
    - Clear, concise titles
    - Detailed problem descriptions
    - Appropriate priority levels (low/medium/high/critical)
    - Correct categories (technical/billing/account/product/general)
    - Steps to reproduce for technical issues
    - Realistic resolution time estimates
    
    IMPORTANT: Response must be valid JSON matching the SupportTicket schema.
    """,
    output_type=SupportTicket
)
