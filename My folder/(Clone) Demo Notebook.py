# Databricks notebook source
print("Hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World" 

# COMMAND ----------

# MAGIC %md
# MAGIC # Title

# COMMAND ----------

# MAGIC %md
# MAGIC ### Title

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------

# MAGIC %fs ls /'databricks-datasets'

# COMMAND ----------


