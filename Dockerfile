FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /GemManageSystem
COPY requirements.txt /GemManageSystem/
RUN pip install -r requirements.txt
COPY . /GemManageSystem/
