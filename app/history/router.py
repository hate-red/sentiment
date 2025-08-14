from fastapi import APIRouter, Depends
from app.history.service import HistoryService
from app.history.schemas import HistoryPublic, HistoryFilter, HistoryAdd, HistoryUpdate, HistoryDelete

router = APIRouter(prefix='/history', tags=['History'])


@router.get('/', summary='Returns history of a given user_id')
async def get_history(user_id: int) -> list[HistoryPublic] | dict:
    history = await HistoryService.get_history(user_id)
    
    return history


@router.get('/filtered', summary='Returns filtered history')
async def get_filtered_history(filter_by: HistoryFilter = Depends()) -> list[HistoryPublic] | dict:
    history = await HistoryService.get_all(**filter_by.to_dict())

    return history


@router.post('/add', summary='Adds new history to user')
async def add_history(history: HistoryAdd = Depends()):
    check = await HistoryService.create(**history.model_dump())

    if check:
        return {
            'message': 'Record was successfully created',
            'history': history,
        }

    return {'detail': 'Error when adding history'}


@router.put('/update', summary='Updates history by its id')
async def update_history(history_id: int, history_info: HistoryUpdate = Depends()) -> HistoryPublic | dict:
    check = await HistoryService.update(filter_by={'id': history_id}, **history_info.model_dump())

    if check:
        history = await HistoryService.get_one_or_none_by_id(id=history_id)
        return history

    return {'detail': 'Error when updating history'}

@router.delete('/delete', summary='Deletes history')
async def delete_history(history: HistoryDelete = Depends()) -> dict:
    check = await HistoryService.delete(**history.to_dict())

    if check:
        return {'message': 'History was successfully deleted'}

    return {'detail': 'Error when deleting history'}
