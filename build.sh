#!/bin/bash

# Clone the GitHub repository
git clone https://github.com/drift-labs/gateway.git

# Navigate into the repository directory
cd gateway

# Build the Docker image
docker build -f Dockerfile . -t drift-gateway

# Run the Docker container
# Replace <BASE58_SEED> with your actual Base58-encoded seed key.
docker run -d -e DRIFT_GATEWAY_KEY=<BASE58_SEED> -p 8080:8080 drift-gateway https://api.mainnet-beta.solana.com --host 0.0.0.0

# Run the API server
pip install -r requirements.txt
python main.py
