FROM python:3.10

WORKDIR /api_oportunidade

COPY . /api_oportunidade

RUN pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT ["python"]

# CMD ["run.py"]