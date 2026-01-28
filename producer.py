from kafka import KafkaProducer
import json
import time
import requests
from datetime import datetime, timezone

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

COINS = ["bitcoin", "ethereum", "solana"]

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    response = requests.get(url)
    r = response.json()
    print(r)

    if coin in r and "usd" in r[coin]:
        return r[coin]["usd"]
    else:
        print("⚠️ API issue — skipping this round")
        return None

while True:
    for coin in COINS:
        price = get_price(coin)

        if price is None:
            continue

        data = {
            "coin": coin,
            "price": price,
            "event_time": datetime.now(timezone.utc).isoformat()
        }

        producer.send("crypto_prices", value=data)
        print("Sent:", data)

    time.sleep(5)
