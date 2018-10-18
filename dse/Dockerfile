FROM ubuntu
RUN apt-get update && apt-get install openjdk-8-jdk curl vim python -y
RUN apt-get install libaio1 -y
ENV DSE_HOME=/pv/dse-6.0.3
ENV PATH=$DSE_HOME/bin:$PATH
CMD dse cassandra -R -f -ss
