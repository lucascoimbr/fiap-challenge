# FIAP Challenge - Hospital Moinhos de Vento

## Configurar ambiente AWS EC2

Instalar máquina EC2 na AWS para utilizar ambiente Linux
Tutorial de como montar a máquina: https://www.youtube.com/watch?v=f3jaO-wmQtA
- Foi utilizada uma máquina Ubuntu 18.04 medium
- Como usar máquina EC2 com SSH
    - Baixar o arquivo .pem
    - Vá até o diretório em que se encontra o .pem
    - chmod 400 challangefiap1.pem
    -  ssh -i "challangefiap1.pem" ubuntu@ec2-35-175-145-34.compute-1.amazonaws.com

##  Baixando o repositório git na máquina EC2

    git clone https://github.com/lucascoimbr/fiap-challenge.git
##  Instalando o Docker, Docker Compose e Git
    sudo apt update
    sudo apt install virtualenv
    sudo apt install default-jdk
    sudo wget https://packages.confluent.io/archive/5.5/confluent-5.5.0-2.12.tar.gz
    tar xvzf confluent-5.5.0-2.12.tar.gz

    cd confluent-5.5.0/
    
    sudo vi /etc/profile

Pression i  (insert mode do vi), e insira a linha abaixo no arquivo:

    export PATH=/home/ubuntu/confluent-5.5.0/bin:$PATH

Para salvar, pressione :wq, para sair sem salvar, pressione :q!

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

    kafka-topics --create --topic quickstart-events --bootstrap-server localhost:9092

##### Verificar se o tópicofoi criado:

    kafka-topics --describe --topic quickstart-events --bootstrap-server localhost:9092

##### Mandar mensagens para o tópico (Producer)

    kafka-console-producer --topic quickstart-events --bootstrap-server localhost:9092

Para sair, basta apertar ctrl + C

##### Ler os eventos (Consumer)

    kafka-console-consumer --topic quickstart-events --from-beginning --bootstrap-server localhost:9092

#### Configurar producers (Python)

    virtualenv -p python3 .env3
    source .env3/bin/activate
    pip install kafka-python
