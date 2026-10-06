from fastapi import APIRouter
from pydantic import BaseModel  


liquidconversion_router = APIRouter(prefix="/liquidconversion")


class LiquidConversionModel(BaseModel):
    operation: str
    value: float

class Config:
    schema_extra = {
        "example": {
            "operation": "convert",
            "value": 100.0
        }
    }

@liquidconversion_router.post("/convert")
async def convert_liquid(data: LiquidConversionModel):
    if data.operation == "convert":
        # Perform conversion logic here
        result = data.value * 3.78541  # Example conversion (liters to gallons)
        return {"result": result}
    return {"error": "Invalid operation"}


