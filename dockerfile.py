FROM python:3.8-slim-buster
COPY main3.py main3.py
CMD ["python3", "-u", "main3.py"] 
