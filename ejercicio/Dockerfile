FROM python:3.11.7
WORKDIR /ejercicio
COPY requirements.text .
RUN ! pip install --no-cache-dir -r requirements.text
COPY . .
EXPOSE 8000
CMD ["python", "app_model.py", "--host", "0.0.0.0", "--port", "8000"]