from fastapi import APIRouter

from src.portfolio import DriftTrade

# router to getch information from the class portflio
#

router = APIRouter()
DriftTrade = DriftTrade()
DriftTrade.get_markets()
DriftTrade.get_positions()
DriftTrade.get_profit_n_loss()


@router.get("/markets")
def get_markets():
    response = {"response": DriftTrade.markets, "status": "success"}
    return response


@router.get("/positions")
def get_positions():
    response = {"response": DriftTrade.positions, "status": "success"}
    return response


@router.get("/profit_n_loss")
def get_profit_n_loss():
    return {"profit_n_loss": DriftTrade.profit_n_loss, "status": "success"}


@router.get("/liquidation_price")
def get_liquidation_price():
    return {"liquidation_price": DriftTrade.liquidation_price, "status": "success"}
