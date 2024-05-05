# Fetch Perp Drift.trade Market Data for User

Follow these instructions to set up and run the project successfully. If you encounter any issues, feel free to contact the developer at ksajan12@gmail.com

### Service Prerequisites

Ensure you have the following software installed on your system:

- **Docker**
- **Git**
- **Python 3**

### Python Requiements

- FastAPI (Creating the API for use)
- requests (For HTTPs requests to drift gateway)

### Running the Project

1. Make the script executable: `chmod +x build.sh`
2. Run the Script: `./build.sh`

### Explanation

Here I have used drift gateway for interacting with drift.trade for fetching information of the user and market.
In the build.sh file we first build the docker image and run which is basically building the drift gateway. You are required to provide the
`DRIFT_GATEWAY_SEED` for interacting with the chain and fetching user information, plus also `RPC URL`. Current value should work for most of
the cases.
Now, after the docker is up and running we interact with it using the apis we have built for fetching the following infomation

1. Market: `localhost:8000/markets`
2. Positions: `localhost:8000/positions`
3. PnL: `localhost:8000/profit_n_loss`
4. Liquidation Price: `localhost:8000/liquidation_price`
