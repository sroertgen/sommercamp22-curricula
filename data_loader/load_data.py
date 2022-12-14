import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# upload to named graph
# url = "http://localhost:3030/inference/data?graph=urn:x-arq:DefaultGraph/"
# upload to default graph
url = "http://fuseki:3030/inference/data"

data = [
    "data/reasoning-skos-exactMatch.ttl",
    "data/wlo-fachportal.ttl",
    "data/b-w-mathe-6.ttl",
    "data/bayern-mathe-6.ttl",
    "data/rlp-mathe-7-8.ttl",
    "data/rlp-bio-7-8.ttl"
]

for _file in data:
    multipart_data = MultipartEncoder(
        fields={'file': (_file, open(_file, 'rb'), 'text/plain')})
    headers = {'Content-Type': multipart_data.content_type}

    r = requests.post(url, data=multipart_data, headers=headers)
    print(r.text)
