import requests

import loader as loader


class DriftTrade:
    def __init__(self):
        self.positions = None
        self.profit_n_loss = None
        self.liquidation_price = None
        self.drift_http_url = loader.constants.DRIFT_API_URL

    def get_markets(self):
        url = f"{self.drift_http_url}/v2/markets"
        response = requests.get(url)
        self.markets = response.json()
        return self.markets

    def get_positions(self, marketIndex=None, marketType=None):
        url = f"{self.drift_http_url}/v2/positions"
        if marketIndex is not None and marketType is not None:
            payload = {"marketIndex": marketIndex, "marketType": marketType}
        else:
            payload = {"marketType": "perp"}
        response = requests.get(url, params=payload)
        self.positions = response.json()
        return self.positions

    def get_profit_n_loss(self):
        self.get_positions()
        profit_n_loss = 0
        liquidation_price = 0
        for position in self.positions["perp"]:
            temp_url = (
                f"{self.drift_http_url}/v2/positionInfo/{position['marketIndex']}"
            )
            response = requests.get(temp_url)
            position_info = response.json()
            profit_n_loss += (
                position_info["unrealizedPnl"] + position_info["unsettledPnl"]
            )
            liquidation_price = position_info["liquidationPrice"]
        self.profit_n_loss = profit_n_loss
        self.liquidation_price = liquidation_price
        return
