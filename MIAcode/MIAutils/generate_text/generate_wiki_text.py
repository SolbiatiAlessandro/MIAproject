# -*- coding: utf-8 -*-
"""
generate wiki test module
"""
import wikipediaapi
from typing import Dict, Tuple, Optional
import logging
import os

def create_filepath(filename: str) -> str:
    """
    """
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "Text Files"
    filename = ("%s.txt" % filename)
    filepath = os.path.join(here, subdir, filename)
    logging.warning("create_filpath: {}".format(filepath))
    return filepath

def create_textfile(filepath: str, text: str) -> None:  
    """
    """
    f = open(filepath,"wb+")
    encoded_text = (text).encode("utf-8")
    f.write(encoded_text)
    f.close()

def get_spanish_description(input_keyword: str) -> str:
    """
    """
    logging.warning("called get_spanish_title with input_keyword={}".format(input_keyword))
    long_title = get_spanish_title(input_keyword)['youtube_long_title']
    return ('Hola amigos! en este video nos enteramos' + long_title) if long_title else ''
    
def get_spanish_title(input_keyword: str) -> Dict[str, Optional[str]]:
    """
    https://github.com/SolbiatiAlessandro/MIAproject/issues/4
    return {'youtube_short_title':.., 'youtube_long_title':..}
    """
    logging.warning("called get_spanish_title with input_keyword={}".format(input_keyword))
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(input_keyword)

    titles = {
            'youtube_short_title': None,
            'youtube_long_title': None,
            }

    if not page_py.title:
        logging.warning('Wikipedia page does not exist')
        return titles
    if 'es' not in page_py.langlinks.keys(): 
        logging.warning('Wikipedia page does not have a spanish version')
        return titles

    page_py_es = page_py.langlinks['es']

    titles['youtube_short_title'] = page_py_es.title
    titles['youtube_long_title']  = '¿Qué es ' + page_py_es.title + '? Significado y definición'
    return titles

def generate_wiki_text(input_keyword: str) -> None:
    """
    """
    logging.warning("called generate_wiki_text with input_keyword={}".format(input_keyword))
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(input_keyword)

    if not page_py.title:
        logging.warning('Wikipedia page does not exist')
        return
    if 'es' not in page_py.langlinks.keys(): 
        logging.warning('Wikipedia page does not have a spanish version')
        return

    page_py_es = page_py.langlinks['es']
    translated_text = page_py_es.summary

    if page_py_es.sections:
        translated_text += page_py_es.sections[0].text

    import re
    translated_text = re.sub(r'\[.*?\]', '', translated_text)

    intro = 'Hola amigos! Soy Mia y estoy muy feliz de verte de nuevo aquí. Descubramos juntos la definición de ' + page_py_es.title + '. '
    outro = '. Eso es todo por hoy. Gracias por mirar el video. Eres una persona genial! Te deseo un buen dia. Recuerda sonreír y disfrutar tu día. No olvides suscribirte para approvechar otros interesantes vídeos como este!'

    translated_text = intro + translated_text + outro
    filepath = create_filepath(input_keyword)
    create_textfile(filepath, translated_text)

    #print(translated_text)
    return filepath

if __name__ == "__main__":
    print(generate_wiki_text('Entrepreneurship'))
