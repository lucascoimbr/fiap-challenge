# FIAP Challenge - Hospital Moinhos de Vento

## Configurar ambiente AWS EC2

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


## Instalando o Docker, Docker Compose e Git

    sudo yum update -y
    sudo amazon-linux-extras install docker
    sudo service docker start
    sudo usermod -a -G docker ec2-user
    sudo yum install git -y
    git version
    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose version

##  Baixando o repositório git na máquina EC2

    git clone https://github.com/lucascoimbr/fiap-challenge.git



##  Instalando as dependências necessárias
    sudo apt update
    sudo apt install virtualenv
    sudo apt-get install nodejs-dev node-gyp
    sudo apt install npm 
    npm install no-kafka
    sudo apt install default-jdk
    sudo wget https://packages.confluent.io/archive/5.5/confluent-5.5.0-2.12.tar.gz
    tar xvzf confluent-5.5.0-2.12.tar.gz

    cd confluent-5.5.0/
    
    sudo vi /etc/profile

Pressione i  (insert mode do vi), e insira a linha abaixo no arquivo:

    export PATH=/home/ubuntu/confluent-5.5.0/bin:$PATH

Para salvar, saia do modo edição (esc) pressione :wq, para sair sem salvar, pressione :q!

    source /etc/profile
    echo $PATH
    /home/ubuntu/confluent-5.5.0/bin/confluent-hub install --no-prompt confluentinc/kafka-connect-datagen:0.1.0


###  Iniciando o confluent

    cd bin/
    confluent local start

Para verificar o status

    confluent local status

###  Acessar no browser

Como, no momento da criação da máquina EC2, foi adicionada uma regra de segurança de login TCP from anywhere pelo IPV4, basta utilizar o IPV4:9091 para acessar o Kafka

####  Criar um tópico 

    kafka-topics --create --topic test-topic --bootstrap-server localhost:9092

##### Verificar se o tópicofoi criado:

    kafka-topics --describe --topic kafka-python-topic --bootstrap-server localhost:9092

##### Mandar mensagens para o tópico (Producer)

    kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092

Para sair, basta apertar ctrl + C

##### Ler os eventos (Consumer)

    kafka-console-consumer --topic kafka-python-topic --from-beginning --bootstrap-server localhost:9092

#### Configurar producers (Python)

    virtualenv -p python3 .env3
    source .env3/bin/activate
    pip install kafka-python

Criar o tópico

    kafka-topics --create --topic kafka-python-topic --bootstrap-server localhost:9092

#### Configurar os advertised listeners

Precisa abrir a porta 9092 na aws

kafka-configs --alter --bootstrap-server localhost:9092 --entity-type brokers --entity-name 0 --add-config  advertised.listeners=PLAINTEXT://186.220.36.60:9092

kafka-configs --alter --bootstrap-server localhost:9092 --entity-type brokers --entity-name 0 --add-config  listeners=PLAINTEXT://0.0.0.0:9092

descrever listeners (mudar o entity-name entre 0 e 1)
kafka-configs --bootstrap-server localhost:9092 --entity-type brokers --entity-name 0 --describe advertised.listeners


echo "test"|kafka-console-producer --broker-list ec2-52-201-234-137.compute-1.amazonaws.com:9092 --topic test
