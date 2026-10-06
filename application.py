import uvicorn 
from helpers.configapp import config_app


app = config_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    