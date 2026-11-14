FROM python:3.13-slim

WORKDIR /app/

COPY frontend frontend

ENV PYTHONPATH=/app/frontend

RUN pip install --no-cache-dir uv 

WORKDIR /app/frontend/src/frontend

RUN uv sync --no-dev

CMD [ "uv" , "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
