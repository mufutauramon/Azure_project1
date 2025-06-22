from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL").getOrCreate()
df = spark.read.csv("path_to_bronze", header=True)
df_cleaned = df.dropna().dropDuplicates()
df_cleaned.write.mode("overwrite").csv("path_to_gold")