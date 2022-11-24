# https://github.com/oven-sh/bun/issues/211
# FROM alpine:3.14
FROM debian:stable-slim as get
ENV PYTHONUNBUFFERED=1
RUN apt-get install -y python
# INSTALL BUN
WORKDIR /bun

RUN apt-get update
RUN apt-get install curl unzip -y
RUN curl --fail --location --progress-bar --output "/bun/bun.zip" "https://github.com/oven-sh/bun/releases/download/bun-v0.2.2/bun-linux-x64.zip"
RUN unzip -d /bun -q -o "/bun/bun.zip"
RUN mv /bun/bun-linux-x64/bun /usr/local/bin/bun
RUN chmod 777 /usr/local/bin/bun

FROM debian:stable-slim
COPY --from=get /usr/local/bin/bun /bin/bun

WORKDIR /app
RUN addgroup --gid 101 --system appuser && adduser --uid 101 --system appuser
RUN chown -R 101:101 /app && chmod -R g+w /app
USER appuser
COPY . ./
# INSTALL REQUIEMNTS
# RUN
# RUN pip3 install -r requirements.txt
CMD bun run server.js