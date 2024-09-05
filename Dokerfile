FROM python:3.11.9-alpine

WORKDIR /test-agent

COPY requirements.txt requirements.txt
RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/ &&\
    pip3 install -r requirements.tx

COPY . .

CMD [ "flask", "--app" , "easy_test:create", "run"]