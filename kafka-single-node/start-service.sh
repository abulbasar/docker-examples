#!/bin/bash
export KAFKA_HOME=/opt/kafka_2.11-2.0.0
export PATH=$KAFKA_HOME/bin:$PATH
cd $KAFKA_HOME
echo "Starting local zookeeper"
nohup zookeeper-server-start.sh config/zookeeper.properties &
echo "Waiting for 10 seconds before starting kafka broker"
sleep 10
echo "Starting kafka broker"
kafka-server-start.sh config/server.properties
