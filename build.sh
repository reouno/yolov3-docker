#!/bin/sh
set -eux

sudo nvidia-docker build -t yolov3:1.0 .
