from fastapi import FastAPI

from app.users.router import router as users_router


app = FastAPI()


@app.get('/', summary='home page')
async def home_page():
    return {'message': 'Congrats!'}


app.include_router(users_router)