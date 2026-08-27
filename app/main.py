from fastapi import FastAPI, Response, status
from sqlmodel import SQLModel
from app.routers import ticket_router
from app.database import engine

app = FastAPI(title="Ticket API")

@app.on_event("startup")
def on_startup():
    """create the tables """
    SQLModel.metadata.create_all(engine)
app.include_router(ticket_router.router)

@app.get("/")
async def root(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"message": "Hello World"}

if __name__ == '__main__':
    print("Hello World")