FROM python:3.9
WORKDIR /app

ARG USER_ID=johndoe
ARG UUID=8877

COPY requirements.txt .
COPY src/ ./

RUN useradd -ms /bin/bash -u ${UUID} ${USER_ID} && \
    chown -R ${USER_ID} . && \
    chmod -R 0500 . &&\
    chmod 0700 .

USER ${USER_ID}

RUN pip install -r requirements.txt && \
    rm requirements.txt

ENTRYPOINT [ "python", "./main.py" ]
