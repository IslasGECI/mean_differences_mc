FROM python:3.7
COPY . /workdir
WORKDIR /workdir
RUN pip install \
    autopep8 \
    black \
    codecov \
    flake8 \
    mutmut \
    pandas \
    pylint \
    pylint-fail-under \
    pytest-cov \
    pytest==5.0.1 
CMD make