FROM python:3
COPY . /workdir
WORKDIR /workdir
RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    mutmut==2.* \
    pylint \
    pytest \
    pytest-cov \
    rope
CMD make
