FROM python:3.11-slim

WORKDIR /app

# install deps first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app
COPY app.py .

# stdout immediately (important for logging)
# ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]