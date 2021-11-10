FROM python:3.9

WORKDIR /Innowise_support

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY req.txt /Innowise_support

RUN pip install -r /Innowise_support/req.txt

COPY . /Innowise_support

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

