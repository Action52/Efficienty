FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
EXPOSE 8000
ADD . /code/
CMD ["python", "quickstart/seeds.py"]
CMD ["python", "manage.py", "runserver"]
