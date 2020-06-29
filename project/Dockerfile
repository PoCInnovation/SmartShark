FROM fedora

RUN dnf -y install wireshark

RUN dnf -y install python3
RUN dnf -y install pip

COPY . /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "/app/__init__.py"]