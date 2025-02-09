FROM python:3.8-alpine
RUN apk update && apk add bash && apk add lsblk
SHELL ["/bin/bash", "-c"]
RUN mkdir /app
ADD . /app
WORKDIR /app
CMD ["python3", "app.py"]
