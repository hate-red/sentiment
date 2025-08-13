from fastapi import FastAPI

from app.users.router import router as users_router
from app.history.router import router as history_router


tags_metadata = [
    {
        'name': 'Home page',
        'description': 'Nothing special...'
    },
    {
        'name': 'Users',
        'description': 'Provides methods to work with users'
    },
    {
        'name': 'History',
        'description': "Provides methods to work with users' history"
    },
]


app = FastAPI(openapi_tags=tags_metadata)


@app.get('/', tags=['Home page'])
async def home_page():
    return {'message': 'Congrats!'}


app.include_router(users_router)
app.include_router(history_router)
