from fastapi import FastAPI, Response, status
from starlette import status

app = FastAPI()

@app.get("/")
async def root(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"message": "Hello World"}

if __name__ == '__main__':
    print("Hello World")