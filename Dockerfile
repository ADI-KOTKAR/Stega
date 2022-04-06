FROM python:3.10.4-alpine3.15
MAINTAINER Aditya Kotkar "adityakotkar75@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]
