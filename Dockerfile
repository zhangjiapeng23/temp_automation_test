FROM python:3.10-slim

WORKDIR /test-agent

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "flask", "--app" , "easy_test:create_app", "run"]