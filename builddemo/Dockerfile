FROM ubuntu
RUN apt-get update \
    && apt-get -y install  python3-pip \
    && pip3 install flask \
    && pip3 install flask_cors \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install nodejs \
    && apt-get -y install npm \
    && npm config set registry http://registry.npm.taobao.org \
    && npm install npm -g \
    && npm install -g vue-cli
COPY flaskdemo /flaskdemo
COPY vuedemo /vuedemo
COPY start.sh /
EXPOSE 5000
EXPOSE 8080
CMD /bin/sh /start.sh
