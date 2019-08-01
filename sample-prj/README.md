# How to use yolov3 docker to detect objects

- need *cfg* directory copied from https://github.com/reouno/darknet/tree/docker/cfg
- need *data* directory copied from https://github.com/reouno/darknet/tree/docker/data
- need to download weight file that is in weights directory in this sample project
  - download links: https://github.com/AlexeyAB/darknet#pre-trained-models
- need to export `PYTHONPATH=/opt/darknet` in which directory the darknet module is installed

# sample source code

Please refer to "./sample.py"

# Run sample

just run `run.sh` after creating the docker image with `../build.sh`.
