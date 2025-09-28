# Uniswap V2 Swap Bot (Python - Demo/Stub)

A reference skeleton for a Uniswap V2 swap bot using `web3.py`.  
This repo is for educational/demo purposes (NOT for production).

## What it does
- Loads a private key from `.env` (DO NOT commit real keys).
- Connects to an RPC (Infura/Alchemy/etc.).
- Estimates amounts and prepares a swap via Uniswap V2 Router.

## Files
- `bot.py` – main skeleton
- `.env.example` – environment variable template
- `requirements.txt` – dependencies

## Quick Start
```bash
pip install -r requirements.txt
cp .env.example .env  # fill in values
python bot.py --token-in WETH --token-out USDC --amount-in 0.01
```

> This skeleton avoids broadcasting real transactions by default. Read the code and uncomment the `send_raw_transaction` part if you truly want to send.
