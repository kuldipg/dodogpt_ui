FROM python:3.8
#COPY requirements.txt .
RUN pip install flask requests
COPY ui_app /ui_app
CMD ["python", "ui_app/app.py"]

