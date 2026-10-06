from fastapi import APIRouter
from pydantic import BaseModel

distanceconversion_router = APIRouter(prefix="/distanceconversion")

class DistanceConversionModel(BaseModel):
    operation: str
    distance_data: float

@distanceconversion_router.get("/")
async def get_distance_conversion_methods():
    """ This returns all the methods of distance conversion. """
    result = ["miles_to_kilometers", "kilometers_to_miles"]
    return result


@distanceconversion_router.post("/")
async def perform_distance_conversion(data: DistanceConversionModel):
    """ This function performs the specified distance conversion operation on the given distance data. """
    operation = data.operation.lower()
    distance_data = data.distance_data

    if operation == "miles_to_kilometers":
        return distance_data * 1.60934  # Conversion factor from miles to kilometers
    elif operation == "kilometers_to_miles":
        return distance_data / 1.60934  # Conversion factor from kilometers to miles
    else:
        return {"error": "Invalid operation specified."}

    return {"error": "Invalid operation specified."}

