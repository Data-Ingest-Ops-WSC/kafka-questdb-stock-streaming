# Kafka + QuestDB Streaming

## 📁 Repository Structure
```
├── docker-compose.yml
├── kafka
│   └── producer.py
├── questdb
│   └── consumer_to_questdb.py
├── requirements.txt
└── README.md
```


This repository simulates real-time stock tick data using Apache Kafka and persists it in QuestDB for SQL-based analytics.

## 🧱 Architecture
- **Kafka**: Data streaming backbone with 50 partitions for horizontal scalability
- **Python Producer**: Generates simulated stock ticks and publishes them to Kafka
- **Python Consumer**: Reads from Kafka and writes to QuestDB using Influx Line Protocol (ILP)
- **QuestDB**: High-performance time-series database with SQL support

## ▶️ Getting Started

### 1. Start all services (includes automatic topic creation with 50 partitions)
```bash
docker-compose up -d
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the stock producer
```bash
python kafka/producer.py
```

### 4. Start the consumer to pipe data into QuestDB
```bash
python questdb/consumer_to_questdb.py
```

### 5. Query data in QuestDB
Go to [http://localhost:9000](http://localhost:9000) and run:
```sql
SELECT * FROM stocks;
```

## ✅ Verify topic partition count
To ensure the topic was created correctly with 50 partitions:
```bash
docker-compose exec kafka bash
kafka-topics --bootstrap-server kafka:29092 --describe --topic stock-ticks
```

You should see output confirming `PartitionCount: 50`.

---

This system is designed for real-time financial data ingestion and can easily be extended to include analytics dashboards, stream processing, or alerting systems.