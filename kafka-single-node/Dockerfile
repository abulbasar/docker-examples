FROM ubuntu
RUN apt-get update && apt-get install openjdk-8-jdk curl vim -y
RUN curl http://mirrors.wuchna.com/apachemirror/kafka/2.0.0/kafka_2.11-2.0.0.tgz | tar xz -C /opt
RUN useradd -m kafka
RUN chown -R kafka:kafka /opt/kafka_2.11-2.0.0
ENV KAFKA_HOME=/opt/kafka_2.11-2.0.0 
ENV PATH=$KAFKA_HOME/bin:$PATH
COPY . /
EXPOSE 2181 9092
CMD ["bash", "/start-service.sh"]








