# https://github.com/plutoniumm/SvCRUD REFERENCE
FROM ubuntu:latest

# Update and install necessary packages & set locale
RUN apt-get update && apt-get install -y sudo locales curl unzip python3 && rm -rf /var/lib/apt/lists/* && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py | bash
RUN python3 get-pip.py
RUN rm get-pip.py | bash

# create user - docker
RUN adduser --disabled-password --gecos "" --shell /bin/bash docker
RUN usermod -g sudo docker
RUN passwd -d docker
RUN adduser docker sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# switch user to docker
USER docker

# install bun
RUN curl https://bun.sh/install | bash

RUN echo 'export BUN_INSTALL="$HOME/.bun"' >> ~/.bashrc
RUN echo 'export PATH="$BUN_INSTALL/bin:$PATH"' >> ~/.bashrc
RUN . ~/.bashrc

# create app folder and copy content to app folder
RUN sudo mkdir -p app
WORKDIR /app
COPY . ./

RUN pip3 install -r requirements.txt

RUN python3 ./server/server.py