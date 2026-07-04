"""
Assembles the LangGraph StateGraph from individual nodes.
"""


from box import ConfigBox
from langgraph.graph import StateGraph, START, END

from blogforge_ai import logger
from blogforge_ai.graph.state import AgentState
from blogforge_ai.graph.nodes import (
    router_node,
    route_next,
    research_node, 
    orchestrator_node,
    fanout,
    worker,
    merge_content,
    decide_images,
    generate_and_place_images,
)
from blogforge_ai.utils import load_config_file


class GraphBuilder:
    """
    Builds and compiles a LangGraph StateGraph.

    Usage:
        builder = GraphBuilder(config)
        blogforge_ai = builder.build()
    """

    def __init__(self, config: ConfigBox):
        self.config = config
        self.builder = StateGraph(AgentState)
        self.reducer_graph = StateGraph(AgentState)

    # ── Public API ────────────────────────────────────────────────────

    def build(self):
        """
        Orchestrates node registration, edge wiring, and compilation.
        Returns a compiled graph ready for .invoke() or .stream().
        """
        try:
            self._register_reducer_nodes()
            self._wire_reducer_edges()
            self._register_nodes()
            self._wire_edges()
            graph = self.builder.compile()
            logger.info("LangGraph chatbot compiled successfully.")
            return graph
        except Exception as e:
            logger.error(f"Failed to build the LangGraph: {e}")
            raise

    # ── Private helpers ───────────────────────────────────────────────

    def _register_nodes(self):
        """Adds always-on and feature-gated nodes to the graph."""
        try:
            # Always-on nodes
            self.builder.add_node("router", router_node)
            self.builder.add_node("research", research_node)
            self.builder.add_node("orchestrator", orchestrator_node)
            self.builder.add_node("worker", worker)
            self.builder.add_node("reducer", self._wire_reducer_edges())
            logger.info("All graph nodes registered successfully.")
        except Exception as e:
            logger.error(f"Unexpected error while registering nodes: {e}")
            raise

    def _wire_edges(self):
        """
        Connects nodes in the correct order.
        """
        try:            
            self.builder.add_edge(START, "router")
            self.builder.add_conditional_edges("router", route_next, {"research": "research", "orchestrator": "orchestrator"})
            self.builder.add_edge("research", "orchestrator")
            self.builder.add_conditional_edges("orchestrator", fanout, ["worker"])
            self.builder.add_edge("worker", "reducer")
            self.builder.add_edge("reducer", END)
            logger.info("Graph edges wired successfully.")
        except Exception as e:
            logger.error(f"Unexpected error while wiring edges: {e}")
            raise
    
    def _register_reducer_nodes(self):
        """
        Add Reducer sub-graph edges.
        """
        try:
            self.reducer_graph.add_node("merge_content", merge_content)
            self.reducer_graph.add_node("decide_images", decide_images)
            self.reducer_graph.add_node("generate_and_place_images", generate_and_place_images)
        except Exception as e:
            logger.error(f"Unexpected error while registering nodes: {e}")
            raise

    def _wire_reducer_edges(self):
        """
        Connects reducer sug-graph nodes in the correct order.
        """
        self.reducer_graph.add_edge(START, "merge_content")
        self.reducer_graph.add_edge("merge_content", "decide_images")
        self.reducer_graph.add_edge("decide_images", "generate_and_place_images")
        self.reducer_graph.add_edge("generate_and_place_images", END)
        reducer_subgraph = self.reducer_graph.compile()
        return reducer_subgraph
    

# ── Module-level compiled graph instance ─────────────────────────────


def get_blogforge_app():
    """
    Loads config and builds the compiled LangGraph app.
    Call this once at app startup via st.cache_resource.
    """

    try:
        _config = load_config_file(__file__)
    except Exception as e:
        raise

    try:
        blogforge_app = GraphBuilder(_config).build()
        logger.info(f"Blog Forge App is ready.")
        return blogforge_app
    except Exception as e:
        logger.error(f"Failed to initialize Blog Forge App graph")
        raise