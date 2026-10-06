from fastapi import APIRouter
from pydantic import BaseModel

weightconversion_router = APIRouter(prefix="/weightconversion")

class WeightConversionModel(BaseModel):
    operation: str
    weight_data: float

@weightconversion_router.get("/")
async def get_weight_conversion_methods():
    """ This returns all the methods of weight conversion. """
    result = ["pounds_to_kilograms", "kilograms_to_pounds"]
    return result

@weightconversion_router.post("/")
async def perform_weight_conversion(data: WeightConversionModel):
    """ This function performs the specified weight conversion operation on the given weight data. """
    operation = data.operation.lower()
    weight_data = data.weight_data

    if operation == "pounds_to_kilograms":
        return weight_data * 0.453592  # Conversion factor from pounds to kilograms
    elif operation == "kilograms_to_pounds":
        return weight_data / 0.453592  # Conversion factor from kilograms to pounds
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}

