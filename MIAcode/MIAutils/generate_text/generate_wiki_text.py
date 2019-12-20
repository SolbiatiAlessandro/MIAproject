# -*- coding: utf-8 -*-
"""
generate wiki test module
"""
import wikipediaapi
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
    
def get_spanish_title(input_keyword: str) -> str:
    """
    """
    logging.warning("called get_spanish_title with input_keyword={}".format(input_keyword))
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(input_keyword)

    if not page_py.title:
        logging.warning('Wikipedia page does not exist')
        return
    if 'es' not in page_py.langlinks.keys(): 
        logging.warning('Wikipedia page does not have a spanish version')
        return

    page_py_es = page_py.langlinks['es']

    return page_py_es.title

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

    filepath = create_filepath(input_keyword)
    create_textfile(filepath, translated_text)
    return filepath

    
    print(translated_text)

if __name__ == "__main__":
    print(generate_wiki_text('Entrepreneurship'))
