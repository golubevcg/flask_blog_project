FROM python:3.9-buster

ENV PYTHONBUFFERED=1

WORKDIR /var/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /etc/entrypoint.sh
RUN chmod +x /etc/entrypoint.sh

COPY . .

ENTRYPOINT ["/etc/entrypoint.sh"]

CMD python app.py