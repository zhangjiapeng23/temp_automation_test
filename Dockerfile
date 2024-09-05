FROM python:3.10-slim

WORKDIR /test-agent

COPY requirements.txt requirements.txt
RUN pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/ &&\
    pip3 install -r requirements.txt

COPY . .

CMD [ "flask", "--app" , "easy_test:create", "run"]