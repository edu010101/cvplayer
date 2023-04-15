FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install libxcb-xinerama0

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN apt-get update
RUN pip install numpy==1.24.2

RUN apt-get update
RUN pip install setuptools==65.6.3 wheel==0.38.4

RUN pip3 install PyQt6==6.4.2 PyQt6-Qt6==6.4.2 PyQt6-sip==13.4.1

RUN pip3 install opencv-python-headless

RUN pip install pillow

RUN apt-get update
RUN apt install qt6-base-abi -y

RUN apt-get update
RUN apt install qt6-base-dev -y

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

RUN apt-get update
RUN apt-get install -y git

WORKDIR /home
RUN git clone https://github.com/edu010101/opencvplayer

WORKDIR /home/opencvplayer/opencvplayer

RUN pip3 install -e .

WORKDIR /home/opencvplayer

ENV DEBIAN_FRONTEND=noninteractive

RUN adduser --quiet --disabled-password qtuser && usermod -a -G audio qtuser

ENV LIBGL_ALWAYS_INDIRECT=1

COPY ./opencvplayer/test.py /home/opencvplayer/test.py
COPY ./opencvplayer/cut.mp4 /home/opencvplayer/cut.avi

ENTRYPOINT python3 test.py

#ENTRYPOINT bash
