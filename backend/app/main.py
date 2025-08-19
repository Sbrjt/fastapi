from app.routes.auth import router as auth_routes
from app.routes.note import router as admin_routes
from dotenv import load_dotenv

from fastapi import FastAPI

load_dotenv()

app = FastAPI()


@app.get('/')
def hello():
    return {'message': 'Hello world!'}


app.include_router(auth_routes, prefix="/auth")
app.include_router(admin_routes, prefix="/note")
