from fastapi import FastAPI

from handlers.distanceconversionhandler import distanceconversion_router
from handlers.liquidconversionhandler import liquidconversion_router
from handlers.weightconversionhandler import weightconversion_router

all_routes = [distanceconversion_router, liquidconversion_router, weightconversion_router]
def config_app():
    """ This function configures the FastAPI application. """
    app = FastAPI(title="Python Datatype Microservice", description="A microservice for Python datatypes", version="1.0.0")
    for route in all_routes:
        app.include_router(route)
    
    return app