FROM python:3

RUN apt-get update && apt-get install libcam-pdf-perl cpanminus -y --no-install-recommends

RUN cpanm App::skos2jskos

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./load_data.py" ]
