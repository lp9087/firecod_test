FROM python:3.9.6-alpine

WORKDIR /usr/src/firecode

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/firecode/entrypoint.sh
RUN chmod +x /usr/src/firecode/entrypoint.sh

COPY . .

ENTRYPOINT ["sh", "/usr/src/firecode/entrypoint.sh"]