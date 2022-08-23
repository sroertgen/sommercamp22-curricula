# TODO prefixes aus einer Datei auslesen
# TODO Triples auslesen und concatten

from SPARQLWrapper import SPARQLWrapper, POST, DIGEST
from rdflib import Graph
from pathlib import Path

# def readTTL(filename):
#     prefixes = []
#     triples = []
#     with open(filename, "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             if "prefix" in line[0:6].lower():
#                 print(f"found prefix: {line}")
#                 prefixes.append(line)
#             elif "\n" not in line[0:2]:
#                 print(f"found triple: {line}")
#                 triples.append(line)
#             else:
#                 print("empty row, skipping...")

#         prefixes = " ".join(prefixes)
#         triples =  " ".join(triples)

#     return prefixes, triples


# def readFiles(file_list):
#     prefixes_all = []
#     triples_all = []

#     for item in file_list:
#         prefixes, triples = readTTL(item)
#         prefixes_all.append(prefixes)
#         triples_all.append(triples)

#     prefixes_all = " ".join(prefixes_all)
#     triples_all = " ".join(triples_all)

#     return prefixes_all, triples_all


# file_list = [
#     "curr-model.ttl",
#     "data.ttl",
#     "curr-inferencing.ttl"
# ]

# prefixes, triples = readFiles(file_list)
def insert_data(_ids: list[str]):
    prefixes = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    prefix ex: <http://example.org/>
    """

    triples = []
    exact_matches = list(_ids)
    print(exact_matches)
    for _id in exact_matches:
        triples.append(f"<{exact_matches[0]}> skos:exactMatch <{_id}> ")

    triples_str = ". ".join(triples) + "."
    print(triples_str)
    query = (
        # f"CREATE GRAPH <http://model.com>"
        f"{prefixes}"
        # f"INSERT DATA {{ GRAPH <http://model.com> {{ {triples} }} }} "
        f"INSERT DATA {{ {triples_str} }}"
    )

    print(query)
    sparql = SPARQLWrapper("http://localhost:3030/inference/update")

    sparql.setHTTPAuth(DIGEST)
# sparql.setCredentials("admin", "admin")
    sparql.setMethod(POST)


    sparql.setQuery(query)

    results = sparql.query()
    print(results.response.read())
    return True
