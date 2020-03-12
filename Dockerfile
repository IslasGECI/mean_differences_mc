FROM python:3.7
COPY . /workdir
WORKDIR /workdir
RUN pip install \
    autopep8 \
    codecov \
    mutmut \
    pandas \
    pytest-cov \
    pytest==5.0.1 
CMD make