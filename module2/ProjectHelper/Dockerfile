FROM python:3

ADD setup.py /

ADD README.md /

ADD MANIFEST.in /

ADD LICENSE /

ADD ProjectHelper /

RUN pip install -e .

CMD ["python3", "helper-folder"]