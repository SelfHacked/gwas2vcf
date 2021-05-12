FROM python:3.8

MAINTAINER "Matt Lyon" matt.lyon@bristol.ac.uk

# copy flask app to container
COPY . /app
WORKDIR /app

# install python dependencies
RUN pip install Cython
# install gwas2vcf library
RUN pip install .

# launch app
CMD ["gwas2vcf"]