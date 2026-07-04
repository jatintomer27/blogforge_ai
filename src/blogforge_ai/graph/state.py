"""
Defines the shared state object that flows through every node in the graph.
Add new fields here as you add new features — nodes just ignore fields they
don't need, so this is always backward-compatible.
"""

import operator
from typing import Annotated, TypedDict, List, Optional
from blogforge_ai.graph.schemas import Plan, EvidenceItem


class AgentState(TypedDict):
    """
    The central state passed between all LangGraph nodes.

    Fields
    ------
    topic            : Topic on which the blog will be generated
    """
    
    topic: str

    # routing
    needs_research: bool
    mode: str
    queries: List[str]

    # research
    evidence: List[EvidenceItem]

    # orchestration
    plan: Optional[Plan]

    # recency
    as_of: str
    recency_days: int

    # workers
    sections: Annotated[List[tuple[int, str]], operator.add] # (task_id, section_md)
    
    # reducer
    merged_md: str
    md_with_placeholders: str
    image_specs: List[dict]
    
    final: str


