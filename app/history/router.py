from fastapi import APIRouter, Depends, HTTPException, status
from app.history.service import HistoryService
from app.history.schemas import HistoryPublic, HistoryAdd, HistoryRB


router = APIRouter(prefix='/history', tags=['History'])


@router.get('/', summary='Returs history of a given user by id')
async def get_history(user_id: int) -> list[HistoryPublic] | dict:
    history = await HistoryService.get_history(user_id)
    
    return history


@router.get('/filtered', summary='Gets users')
async def get_filtered_history(filter_by: HistoryRB = Depends()) -> list[HistoryPublic] | dict:
    history = await HistoryService.get_all(**filter_by.to_dict())

    return history


@router.post('/add', summary='Adds new record to user history')
async def add_history(history: HistoryAdd = Depends()):
    check = await HistoryService.add(**history.dict())

    if check:
        return {
            'message': 'Record was sucessfully created',
            'history': history,
        }
