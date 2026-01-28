# Real-Time Crypto Analytics Pipeline

Kafka → Spark → Snowflake → Streamlit

An end-to-end real-time data engineering project that ingests live cryptocurrency prices, processes streaming data with Apache Spark, stores analytics-ready data in Snowflake, and visualizes insights through an interactive Streamlit dashboard.

This project demonstrates modern data engineering architecture used in production-grade streaming analytics systems.


# Tech Stack

Python 3.10+

Apache Kafka – Real-time data ingestion

Apache Spark Structured Streaming – Stream processing

Snowflake – Cloud data warehouse

Streamlit – Interactive analytics dashboard

Git & GitHub – Version control


# Architecture

Crypto Price API
      ↓
Kafka Producer
      ↓
Kafka Topic
      ↓
Spark Structured Streaming
      ↓
Snowflake Data Warehouse
      ↓
Streamlit Dashboard


# Features

Live ingestion of multi-cryptocurrency prices (Bitcoin, Ethereum, Solana)

Real-time message streaming with Kafka

Stream processing using Spark Structured Streaming

Automatic loading into Snowflake cloud warehouse

Interactive dashboard for real-time analytics

Modular and scalable pipeline design

# Setup Instructions
1. Start Kafka & Zookeeper

Run Kafka locally (or via Docker) and create topic:

crypto_prices

2. Run Kafka Producer
python producer/kafka_producer.py


Fetches live prices from CoinGecko API and streams to Kafka.

3. Start Spark Streaming Job
spark-submit spark_stream/spark_stream_to_snowflake.py


Consumes Kafka stream and writes processed data into Snowflake.

4. Launch Dashboard
streamlit run dashboard/dashboard.py


View real-time crypto analytics in your browser.

# Learning Outcomes

Built real-time streaming ingestion systems

Implemented Spark Structured Streaming pipelines

Integrated cloud data warehousing with Snowflake

Designed end-to-end production-style data workflows

Created analytics dashboard for business insights


# Future Enhancements

Add alerting system for price thresholds

Deploy pipeline on cloud infrastructure

Add historical trend analytics

Integrate Airflow/Prefect for orchestration
