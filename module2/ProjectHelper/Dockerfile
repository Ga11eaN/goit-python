FROM python:3
WORKDIR app
RUN pip install pipenv
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install
COPY . .
CMD python main.py