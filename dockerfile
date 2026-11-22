FROM python:3.14

WORKDIR -app

COPY greeting.py .

CMD ["python","greeting.py"]