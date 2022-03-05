mkdir docker-compose
docker build . -t kafka
docker run -it kafka

# docker run -it -v $PWD:/app debenture bash