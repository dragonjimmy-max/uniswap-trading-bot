import argparse, os
from dotenv import load_dotenv
from web3 import Web3

# Uniswap V2 Router (Mainnet)
ROUTER = Web3.to_checksum_address("0x7a250d5630b4cf539739df2c5dacb4c659f2488d")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--token-in', default='WETH')
    ap.add_argument('--token-out', default='USDC')
    ap.add_argument('--amount-in', type=float, default=0.01)
    args = ap.parse_args()

    load_dotenv()
    rpc = os.getenv("RPC_URL")
    w3 = Web3(Web3.HTTPProvider(rpc))
    assert w3.is_connected(), "RPC not connected"

    print("Connected. This is a demo skeleton; add ABIs and call router methods to simulate a swap.")
    print(f"Intended swap: {args.amount_in} {args.token_in} -> {args.token_out}")
    print("⚠️ Do NOT use real keys on a public repo.")

if __name__ == "__main__":
    main()
