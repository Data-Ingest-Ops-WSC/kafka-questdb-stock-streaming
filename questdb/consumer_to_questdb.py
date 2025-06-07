import json
import socket
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'acciones-ticks',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    key_deserializer=lambda k: k.decode('utf-8') if k else None
)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9009))

for msg in consumer:
    stock = msg.value
    ilp = f"stocks,symbol={stock['symbol']} price={stock['price']},volume={stock['volume']} {stock['timestamp']}000000\n"
    sock.sendall(ilp.encode('utf-8'))
    print(f"Inserted into QuestDB: {ilp.strip()}")