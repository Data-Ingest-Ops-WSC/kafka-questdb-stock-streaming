import json
import random
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    key_serializer=lambda k: k.encode('utf-8'),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

symbols = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]

def generate_stock(symbol):
    return {
        "symbol": symbol,
        "price": round(random.uniform(100, 1500), 2),
        "volume": random.randint(100, 10000),
        "timestamp": int(time.time() * 1000)
    }

while True:
    symbol = random.choice(symbols)
    data = generate_stock(symbol)
    producer.send("stock-ticks", key=symbol, value=data)
    print(f"Sent: {data}")
    time.sleep(0.5)