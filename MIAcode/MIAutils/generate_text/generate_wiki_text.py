# -*- coding: utf-8 -*-
import wikipediaapi
import os

def create_filepath(filename: str) -> str:
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "Text Files"
    filename = ("%s.txt" % filename)
    filepath = os.path.join(here, subdir, filename)
    return filepath

def create_textfile(filepath: str, text: str) -> None:  
    f = open(filepath,"wb+")
    encoded_text = (text).encode("utf-8")
    f.write(encoded_text)
    f.close()

def generate_wiki_text(input_keyword: str) -> None:
    # here the function return None in case 
    # there is not a wiki page or a wiki page
    # in Spanish for the specified keyword
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page('Entrepreneurship')

    if not page_py:
        return
    if 'es' not in page_py.langlinks.keys():
            return

    page_py_es = page_py.langlinks['es']
    translated_text = page_py_es.summary

    if page_py_es.sections:
        translated_text += page_py_es.sections[0].text

    filepath = create_filepath(input_keyword)
    create_textfile(filepath, translated_text)
    
    print(translated_text)

if __name__ == "__main__":
    generate_wiki_text('Entrepreneurship')