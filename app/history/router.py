from fastapi import APIRouter, Depends, HTTPException, status
from app.history.service import HistoryService
from app.history.schemas import HistoryPublic


router = APIRouter(prefix='/history', tags=['works with history'])

@router.get('/', summary='Returs history of a given user by id')
async def get_history(user_id: int) -> list[HistoryPublic]:
    history = await HistoryService.get_history(user_id)
    
    return history    
