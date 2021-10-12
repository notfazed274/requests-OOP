import requests
import json
from assertpy.assertpy import assert_that
from cerberus import Validator

# Documentación de esta API: "https://animechan.vercel.app/guide"
url_get_quotes = 'https://animechan.vercel.app/api/random'

class Test_animechan():

    def test_get_random_quotes(self):
        r = requests.get(url_get_quotes)
        response = json.loads(r.text)

        schema = {
            'anime': {'type': 'string'},
            'character': {'type': 'string'},
            'quote': {'type': 'string'}
        }

        #Schema validation
        validator = Validator()
        schema_validation = validator.validate(response, schema)

        #Assertions
        assert_that(schema_validation).is_true()
        assert_that(r.status_code).is_equal_to(200)
        assert_that(response).is_not_none()

        #Extraer un valor
        global anime_nombre
        anime_nombre = (response.get('anime'))
        print(anime_nombre)

        #Mostrar el response indentado
        print(json.dumps(response, indent=4))

    def test_get_quote_by_anime(self):
        r = requests.get(f'https://animechan.vercel.app/api/quotes/anime?title={anime_nombre}')
        response = json.loads(r.text)

        schema =  {
            'anime': {'type': 'string'},
            'character': {'type': 'string'},
            'quote': {'type': 'string'}
        }

        #Schema validation en una lista de dict
        for diccionario in response:
            validator = Validator(schema)
            schema_validation = validator.validate(diccionario)
            assert_that(schema_validation).is_true()
            assert_that(diccionario['anime']).contains(anime_nombre)
            assert_that(r.status_code).is_equal_to(200)

        #Extrar un value
        global personaje
        personaje = (response[0].get('character'))
        print(personaje)

        #Mostrar el response indentado
        print(json.dumps(response, indent=4))

    def test_get_quote_by_character(self):
        r = requests.get(f'https://animechan.vercel.app/api/quotes/character?name={personaje}')
        response = json.loads(r.text)

        schema = {
            'anime': {'type': 'string'},
            'character': {'type': 'string'},
            'quote': {'type': 'string'}
        }

        #Schema validation
        for diccionario in response:
            validator = Validator(schema)
            schema_validation = validator.validate(diccionario)
            assert_that(schema_validation).is_true()
            assert_that(diccionario['character']).contains(personaje)
            assert_that(r.status_code).is_equal_to(200)

        #Mostrar el response
        print(json.dumps(response, indent=4))