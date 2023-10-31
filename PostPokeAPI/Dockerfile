FROM alpine:3.18.4
LABEL descripcion="Get mediante Post a una API"
RUN apk upgrade --no-cache
RUN apk add python3
RUN apk add py3-pip
COPY ./ConsumoPost /opt/app/ConsumoPost
WORKDIR /opt/app/ConsumoPost
RUN pip install -r requirements.txt
CMD uvicorn ServeAPI:app --reload --host 0.0.0.0 --port 8000