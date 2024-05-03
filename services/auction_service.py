from typing import Optional
from utils.data import ipl_auction_data

def get_players_auction_data(
            player: Optional[str] = None,
            nationality: Optional[str] = None,
            type: Optional[str] = None,
            team: Optional[str] = None,
            min_price: Optional[int] = None,
            max_price: Optional[int] = None,
            sort_by: Optional[str] = None,
            sort_order: Optional[str] = None,
            limit: Optional[int] = None
            ):
        filtered_data = ipl_auction_data

        if player:
            filtered_data = [item for item in filtered_data if item["player"] == player]

        if nationality:
            filtered_data = [item for item in filtered_data if item["nationality"] == nationality]

        if type:
            filtered_data = [item for item in filtered_data if item["type"] == type]

        if team:
            filtered_data = [item for item in filtered_data if item["team"] == team]

        if min_price:
            filtered_data = [item for item in filtered_data if item["price"] >= min_price]

        if max_price:
            filtered_data = [item for item in filtered_data if item["price"] <= max_price]

        if sort_by:
            if sort_order and sort_order.lower() == "desc":
                reverse = True
            else:
                reverse = False
            filtered_data = sorted(filtered_data, key=lambda x: x[sort_by], reverse=reverse)


        if limit:
            filtered_data = filtered_data[:limit]

        return filtered_data
