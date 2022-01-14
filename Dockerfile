FROM python:3.9-slim

WORKDIR /usr/src/firecode

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt install -y netcat

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/firecode/entrypoint.sh
RUN chmod +x /usr/src/firecode/entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/firecode/entrypoint.sh"]