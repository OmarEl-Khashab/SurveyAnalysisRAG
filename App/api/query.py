from fastapi import APIRouter, HTTPException
from App.api.models.validators import QueryRequest, QueryResponse
from RAG.rag_pipeline import RAGPipeline
from fastapi import Body
from fastapi.responses import JSONResponse

data_path = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data"
embeddings_dir = "/Users/omarelkhashab/PycharmProjects/SurveyAnalysisRAG/Data/Text_Embeddings"

router = APIRouter()


@router.post("/query", response_model=QueryResponse)
async def get_response(request: QueryRequest):
    try:
        # Initialize the RAG pipeline
        # Run the query and get the answer
        print(f"Received request with source: {request.source} and query: {request.query}")
        rag_pipeline = RAGPipeline(data_path, embeddings_dir, source=request.source)
        output = rag_pipeline.run(query=request.query)
        print(f"RAG Pipeline output: {output}")
        # return JSONResponse(content={"answer": output})
        return QueryResponse(answer=output)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
