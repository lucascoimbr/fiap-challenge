FROM python:3.9

COPY . /ec2-user
WORKDIR /ec2-user

RUN sudo yum update -y
RUN sudo amazon-linux-extras install docker
RUN sudo service docker start
RUN sudo usermod -a -G docker ec2-user
RUN sudo yum install git -y
RUN git version
RUN sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
RUN sudo chmod +x /usr/local/bin/docker-compose
RUN docker-compose version

