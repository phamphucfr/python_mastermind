FROM python:slim
WORKDIR /app_mastermind
COPY . /app_mastermind
RUN pip install -r requirements.txt
ENTRYPOINT [ "bash" ]
