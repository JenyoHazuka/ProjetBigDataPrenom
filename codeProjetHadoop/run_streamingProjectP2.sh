#!/bin/bash

# 1. Copier CSV dans HDFS
hdfs dfs -mkdir -p /user/maria_dev/logsProject
hdfs dfs -put -f ./csv/nat2022_valid.csv /user/maria_dev/logsProject/

# 2. Supprimer l ancien dossier de sortie
hdfs dfs -rm -r /user/maria_dev/logsProject/output

# 3. Rendre les scripts executables localement
chmod +x mapper.py
chmod +x reducer.py
chmod +x postprocess.py

# 4.  Lancer Hadoop Streaming
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-D mapreduce.job.reduces=3 \
-input /user/maria_dev/logsProject/nat2022_valid.csv \
-output /user/maria_dev/logsProject/output \
-mapper "python2 mapper.py" \
-reducer "python2 reducer.py" \
-file mapper.py \
-file reducer.py