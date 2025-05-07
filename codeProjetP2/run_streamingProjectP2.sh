#!/bin/bash

# 1. Copier CSV dans HDFS
hdfs dfs -mkdir -p /user/maria_dev/logs
hdfs dfs -put -f ./csv/natDpt2022_valid.csv /user/maria_dev/logs/

# 2. Supprimer l ancien dossier de sortie
hdfs dfs -rm -r /user/maria_dev/logs/output

# 3. Rendre les scripts executables localement
chmod +x mapper.py
chmod +x reducer.py

# 4.  Lancer Hadoop Streaming
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapreduce.job.reduces=4 \
-input /user/maria_dev/logs/natDpt2022_valid.csv \
-output /user/maria_dev/logs/output \
-mapper "python mapper.py" \
-reducer "python reducer.py" \
-file mapper.py \
-file reducer.py