from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType

spark = SparkSession.builder \
    .appName("CryptoKafkaStream") \
    .config("spark.jars.packages",
            "org.apache.spark:spark-sql-kafka-0-10_2.13:3.5.2") \
    .getOrCreate()

schema = StructType() \
    .add("coin", StringType()) \
    .add("price", FloatType()) \
    .add("event_time", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "crypto_prices") \
    .load()

value_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

query = value_df.writeStream \
    .format("console") \
    .outputMode("append") \
    .start()

query.awaitTermination()
