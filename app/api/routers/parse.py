from fastapi import APIRouter

router = APIRouter()


@router.get("/parse")
def parse():
    return {"message": "CV Parser API is working!"}
