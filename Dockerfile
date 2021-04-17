FROM frolvlad/alpine-python-machinelearning
WORKDIR /project
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python","wsgi.py"]
