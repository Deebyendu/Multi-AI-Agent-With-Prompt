from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_response_from_ai_agent
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger=get_logger(__name__)

app = FastAPI(title="Multi AI Agent")

class RequestState(BaseModel):
    model_name:str
    system_prompt:str
    messages:List[str]
    allow_search:bool
    
@app.post("/chat")
def chat_endpoint(request:RequestState):  
    """Chat with the AI Agent."""

    logger.info(f"Request state is {request.model_name}.")
    if request.model_name not in settings.ALLOWED_MODEL_NAME:
        logger.warning("Invalid model name detected!")
        raise HTTPException(status_code=400, detail="Invalid model name detected!")
    
    try:
        # Extract the last user message as the query
        query = request.messages[-1] if request.messages else ""
        
        response=get_response_from_ai_agent(
            request.model_name,
            query,
            request.allow_search,
            request.system_prompt
        )
        logger.info(f"Sucessfully get response from ai agent! {request.model_name}")
        return {"response":response}
    except Exception as e:
        logger.error("Failed to chat with the AI Agent!")
        raise HTTPException(
            status_code=500,
            detail=str(CustomException("Failed to get AI response", error_details=e))
            )
