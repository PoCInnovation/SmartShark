FROM fedora

RUN dnf -y install wireshark

RUN dnf -y install python3.8

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN python3.8 get-pip.py

COPY . /app/

WORKDIR /app

RUN python3.8 --version
RUN python3.8 -c 'import struct;print( 8 * struct.calcsize("P"))'

RUN pip install --upgrade pip
RUN python3.8 -m pip install tensorflow
RUN python3.8 -m pip install Flask
RUN python3.8 -m pip install pandas
RUN python3.8 -m pip install sklearn
RUN python3.8 -m pip install Keras

EXPOSE 5000

ENTRYPOINT ["python3.8", "/app/__init__.py"]
