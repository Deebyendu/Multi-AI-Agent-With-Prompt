from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableConfig

##state schema
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode, tools_condition

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt):
    # Initialize LLM and tools
    tools = [TavilySearchResults(max_results=5)] if allow_search else []
    llm = ChatGroq(model=llm_id)
    
    # Bind tools to LLM if search is enabled
    if tools:
        llm_with_tools = llm.bind_tools(tools)
    else:
        llm_with_tools = llm
    
    # Define state schema
    class State(TypedDict):
        messages: Annotated[list, add_messages]
    
    # Initialize memory saver
    memory = MemorySaver()
    
    ### Node definitions
    
    # Default system prompt if none provided
    default_system_prompt = """You are a helpful AI assistant. You can answer questions and use available tools when needed.
When using search tools, provide clear and concise answers based on the search results."""
    
    # Agent node: calls the LLM with tools
    def agent(state: State):
        messages = state["messages"]
        
        # Add system prompt at the beginning if not already present
        active_system_prompt = system_prompt if system_prompt else default_system_prompt
        if not any(isinstance(m, SystemMessage) for m in messages):
            messages = [SystemMessage(content=active_system_prompt)] + messages
        
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}
    
    # Build the graph
    graph = StateGraph(State)
    
    # Add nodes
    graph.add_node("agent", agent)
    
    # Add tool node if tools are enabled
    if tools:
        tool_node = ToolNode(tools)
        graph.add_node("tools", tool_node)
    
    # Add edges
    graph.add_edge(START, "agent")
    
    if tools:
        # Conditional edge: if agent calls tools, go to tools node
        # otherwise, end the conversation
        graph.add_conditional_edges(
            "agent",
            tools_condition,
            {
                "tools": "tools",
                END: END
            }
        )
        # After tools execute, return to agent
        graph.add_edge("tools", "agent")
    else:
        # No tools, just end after agent
        graph.add_edge("agent", END)
    
    # Compile the graph with memory
    builder = graph.compile(checkpointer=memory)
    
    # Invoke the graph with the query
    config: RunnableConfig = {"configurable": {"thread_id": "default"}}
    result = builder.invoke(
        {"messages": [{"role": "user", "content": query}]},
        config=config
    )
    
    # Return the last AI message content
    return result["messages"][-1].content