import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "Hello, World!"}  # json response

@app.get("/hello_world")
async def hello_world_2():
    return {"message": "Hello, World_2!"}  # json response

if __name__ == "__main__":
    uvicorn.run("helloworld:app", reload=True)