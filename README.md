# FIAP Challenge - Hospital Moinhos de Vento

## Configurar ambiente AWS EC2

Instalar máquina EC2 na AWS para utilizar ambiente Linux
- Foi utilizada uma máquina Amazon Linux (free tier AWS)
- Como usar máquina EC2 com SSH
    - Baixar o arquivo .pem
    - Vá até o diretório em que se encontra o .pem
    - chmod 400 challengefiap.pem
    - ssh -i "challengefiap.pem" ec2-user@ec2-3-91-144-144.compute-1.amazonaws.com
##  Instalando o Docker, Docker Compose e Git
    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    sudo yum install git -y
    git version
    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose version

##  Instalando e Iniciando o Kafka

#####  Instalando o Kafka

    git clone https://github.com/confluentinc/cp-docker-images
#####  Vá até o diretório do Kafka
    cd cp-docker-images/examples/kafka-single-node

Este docker-compose inicializa o Zookeeper e o Kafka:

    version: '2'
    services:
    zookeeper:
        image: confluentinc/cp-zookeeper:latest
        network_mode: host
        environment:
        ZOOKEEPER_CLIENT_PORT: 32181
        ZOOKEEPER_TICK_TIME: 2000
        extra_hosts:
        - "moby:127.0.0.1"

    kafka:
        image: confluentinc/cp-kafka:latest
        network_mode: host
        depends_on:
        - zookeeper
        environment:
        KAFKA_BROKER_ID: 1
        KAFKA_ZOOKEEPER_CONNECT: localhost:32181
        KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:29092
        KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
        extra_hosts:
        - "moby:127.0.0.1"

#####  Execute o comando
    docker-compose up -d

#####  Para verificar se está tudo correto:
    docker-compose ps

##### O resultado deve ser como:

    Name                         Command            State   Ports
    ----------------------------------------------------------------
    kafka-single-node_kafka_1       /etc/confluent/docker/run   Up
    kafka-single-node_zookeeper_1   /etc/confluent/docker/run   Up

#####  Para verificar o log do zookeeper:
    docker-compose logs zookeeper | grep -i binding

#####  Resultado esperado:

    zookeeper_1  | [2018-06-26 01:06:59,447] INFO binding to port 0.0.0.0/0.0.0.0:32181 (org.apache.zookeeper.server.NIOServerCnxnFactory)

#####  Analisar a saúde do Kafka:

    docker-compose logs kafka | grep -i started

#####  Resultado esperado:

    kafka_1      | [2018-06-27 20:03:50,641] INFO [SocketServer brokerId=1] Started 1 acceptor threads (kafka.network.SocketServer)
    kafka_1      | [2018-06-27 20:03:50,898] INFO [SocketServer brokerId=1] Started processors for 1 acceptors (kafka.network.SocketServer)
    kafka_1      | [2018-06-27 20:03:50,900] INFO [KafkaServer id=1] started (kafka.server.KafkaServer)
    kafka_1      | [2018-06-27 20:03:50,911] INFO [ReplicaStateMachine controllerId=1] Started replica state machine with initial state -> Map() (kafka.controller.ReplicaStateMachine)
    kafka_1      | [2018-06-27 20:03:50,914] INFO [PartitionStateMachine controllerId=1] Started partition state machine with initial state -> Map() (kafka.controller.PartitionStateMachine)

####  Testando o Kafka

#####  Criando um Topic