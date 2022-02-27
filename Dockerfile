FROM python:3.9-alpine
COPY app.py /flask/app.py
ENV FLASK_APP=/flask/app.py
RUN pip install flask
EXPOSE 5000/tcp
CMD python -m flask run --host=0.0.0.0


