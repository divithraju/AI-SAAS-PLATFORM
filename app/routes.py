from fastapi import APIRouter, HTTPException
from .schemas import QueryRequest, QueryResponse
from .llm import query_llm
from .utils import estimate_tokens

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def ask_ai(request: QueryRequest):
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Empty query")

    answer = await query_llm(request.question)
    tokens = estimate_tokens(answer)

    return QueryResponse(
        answer=answer,
        tokens_used=tokens
    )
