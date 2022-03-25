## FIAP Challenge - Hospital Moinhos de Vento

#### Configurar ambiente AWS EC2

Instalar máquina EC2 na AWS para utilizar ambiente Linux
- Foi utilizada uma máquina Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type 
- Selecionar a t2.medium (A máquina free tier t2.micro não suporta o kafka)
- Adicionar novas regras ao security group
    - Custom TCP | port 9021 | anywhere
    - Custom TCP | port 9092 | anywhere

- Como usar máquina EC2 com SSH
    - Baixar o arquivo .pem
    - Vá até o diretório em que se encontra o .pem
    - chmod 400 kafkamachine.pem
    - ssh -i "kafkamachine.pem" ec2-user@ec2-44-202-5-136.compute-1.amazonaws.com


#### Instalando o Docker, Docker Compose e Git

    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    sudo yum install git -y
    git version
    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose version

####  Baixando o repositório git na máquina EC2

    git clone https://github.com/lucascoimbr/fiap-challenge.git

#### Vá até o diretório

    cd fiap-challenge/

Note que há na pasta o arquivo [docker-compose.yml](docker-compose.yml)

#### Executando o docker-compose

    docker-compose up -d
    docker-compose ps

##### Erros comuns:

###### Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?

    sudo dockerd

###### Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock

    sudo chmod 666 /var/run/docker.sock

##### Verificação de funcionamento

Verifique se o docker estiver executando

    docker-compose ps

Se sim, execute:

    docker-compose down

Suba os containers novamente, zerando-os:

    docker-compose up -d

Verifique se está executando

    docker-compose logs zookeeper | grep -i binding
    docker-compose logs kafka | grep -i started
    docker-compose logs connect

#####  Criar um tópico 

    docker-compose exec kafka  \
    kafka-topics --create --topic hmv-anwers --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092

#####  Abrir consumer localmente no EC2

    docker-compose exec kafka  \
    kafka-console-consumer --bootstrap-server localhost:29092 --topic meu-topico --from-beginning --max-messages 100


