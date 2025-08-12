from fastapi import FastAPI

from app.users.router import router as users_router
from app.history.router import router as history_router


app = FastAPI()


@app.get('/', summary='Home page')
async def home_page():
    return {'message': 'Congrats!'}


app.include_router(users_router)
app.include_router(history_router)
