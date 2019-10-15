FROM python:3.7-slim-buster

COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
COPY ./demo ./demo

USER appuser

CMD ["python"]