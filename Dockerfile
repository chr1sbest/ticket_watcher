FROM lambci/lambda:python3.6
MAINTAINER hello@chrisbest.com
ENV APP_DIR /var/task
USER root
WORKDIR $APP_DIR

COPY requirements.txt .
COPY bin ./bin
COPY lib ./lib
COPY . .

RUN mkdir -p $APP_DIR/lib
RUN pip3 install -r requirements.txt -t /var/task/lib
