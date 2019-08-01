FROM nvidia/cuda:10.0-cudnn7-devel

ENV DEBIAN_FRONTEND=noninteractive

MAINTAINER @reouno

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y wget git cmake libopencv-dev python3 python3-dev python3-pip && \
    pip3 install opencv-python && \
    pip3 install numpy && \
    pip3 install pillow && \
    pip3 install matplotlib && \
    pip3 install scikit-image && \
    cd /opt && \
    git clone https://github.com/reouno/darknet.git && \
    cd darknet && \
    git checkout -b docker origin/docker && \
    make

CMD echo "Finished!"
