from fastapi import APIRouter, Query
from services.auction_service import get_players_auction_data

router = APIRouter()

@router.get("/")
async def get_auction_data(
    player: str = Query(None), 
    nationality: str = Query(None), 
    type: str = Query(None), 
    team: str = Query(None), 
    min_price: int = Query(None),
    max_price: int = Query(None),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = None,
    sort_order: str = None,
    ):
    return get_players_auction_data(player, nationality, type, team, min_price, max_price, sort_by, sort_order, limit)
