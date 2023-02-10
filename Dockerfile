FROM python:3.9-slim-bullseye

WORKDIR /usr/src/app

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD .env .
ADD main.py .
ADD jira_data_adapter.py .
ADD jira_api.py .
ADD template_demo.pptx .
CMD ["python", "./main.py"]