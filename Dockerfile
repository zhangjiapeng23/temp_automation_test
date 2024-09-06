FROM python:3.10-slim

WORKDIR /test-agent

COPY requirements.txt requirements.txt
RUN pip3 config set global.index-url https://pypi.mirrors.ustc.edu.cn/simple/ &&\
    pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "gunicorn", "-w", "1", "-b", ":5000", "easy_test:create_app()"]