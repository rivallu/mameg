app.pyFROM python:3.6-alpine
LABEL maintainer "Lucas Rival lucas.rival@gmail.com"
RUN mkdir /app
WORKDIR /app
ADD requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt
COPY static static
COPY templates templates
COPY app.py .
COPY mameg.csv .

ENTRYPOINT ["/usr/local/bin/python", "/app/app.py"]