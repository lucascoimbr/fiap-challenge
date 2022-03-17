# FIAP Challenge - Hospital Moinhos de Vento

## Configurar ambiente AWS EC2

Instalar máquina EC2 na AWS para utilizar ambiente Linux
- Foi utilizada uma máquina Amazon Linux (free tier AWS)
- Como usar máquina EC2 com SSH
    - Baixar o arquivo .pem
    - Vá até o diretório em que se encontra o .pem
    - chmod 400 challengefiap1.pem
    - ssh -i "challangefiap1.pem" ec2-user@ec2-44-202-75-248.compute-1.amazonaws.com
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

    git clone https://github.com/lucascoimbr/fiap-challenge.git
#####  Vá até o diretório do Kafka
    cd fiap-challenge/

Note que há na pasta o arquivo [docker-compose.yml](docker-compose.yml)

##### Executando o docker-compose

    docker-compose up -d
    docker-compose ps

#####  Logs do Zookeeper:

    docker-compose logs zookeeper | grep -i binding

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


    docker-compose exec kafka  \
    kafka-topics --create --topic meu-topico-legal --partitions 1 --replication-factor 1 --if-not-exists --zookeeper localhost:32181

    docker-compose exec kafka  \
    kafka-topics --bootstrap-server localhost:9092 --topic meu-topico-legal --create --partitions 1 --replication-factor 1

    

