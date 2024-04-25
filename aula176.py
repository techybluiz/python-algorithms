import json
import os
from pprint import pprint

NOME_ARQUIVO = 'aula177.json'
CAMINHO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

string_json = ''' {
    "title": "the Maze Runner",
    "original_tite": "Run or Die",
    "is_movie": true,
    "imdb_rating": 4.9,
    "year": 2014,
    "budget": null
}
'''
movie = json.loads(string_json)