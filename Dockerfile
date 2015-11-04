# -*- docker-image-name: "ashgillman/papers-by-year-plot" -*-
FROM debian:jessie
MAINTAINER Ashley Gillman "ashley.gillman@uqconnect.edu.au"

RUN apt-get update && apt-get install -qy \
    git \
    libyaml-dev \
    python \
    python3 \
    python3-matplotlib \
    python3-numpy \
    python3-pip
RUN pip3 install pyyaml

RUN apt-get install -qy python-beautifulsoup

RUN git clone https://github.com/ckreibich/scholar.py.git

ADD . /app

ENTRYPOINT ["python3", "/app/make-plot.py"]
