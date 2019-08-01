#!/bin/sh
set -eu

docker run \
    -v `pwd`:/workspace \
    -it \
    --rm \
    --runtime=nvidia \
    yolov3:1.0 \
    bash -c "export PYTHONPATH=/opt/darknet && cd /workspace && python3 sample.py"
