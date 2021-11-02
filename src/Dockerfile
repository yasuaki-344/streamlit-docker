FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8501

ENTRYPOINT [ "streamlit", "run", "app.py" ]
