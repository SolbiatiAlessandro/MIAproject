import pytest
from generate_wiki_text import generate_wiki_text, get_spanish_title
from title_to_keyword import title_to_keyword
import os

def generate_filenames_for_tests():
     here = os.path.dirname(os.path.realpath(__file__))
     filename = ("%s.txt" % filename)
     filepath = os.path.join(here, filename)

def test_generate_sp_script_files_from_en_video_titles():
    untranslated_videos = [('What does Entrepreneurship mean? Entrepreneurship definition - Entrepreneurship meaning - How to pronounce ENtrepreneurship', 'video_link1'), ('What is Python? What does Python mean? Python meaning - How to pronounce Python?', 'video_link2')]
    translated_video_scripts_filenames = []
    for title, link in untranslated_videos:
        keyword_from_title = title_to_keyword(title)
        video_script_name = generate_wiki_text(keyword_from_title)
        translated_video_scripts_filenames.append(video_script_name)

    assert len(translated_video_scripts_filenames) == 2

    #create filenames for tests
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = 'Text Files'
    keyword1 = 'entrepreneurship.txt'
    filename1 = os.path.join(here, subdir, keyword1)

    assert translated_video_scripts_filenames ==  [filename1, None]



def test_generate_sp_script_files_from_en_video_titles_no_wiki_pages():

    untranslated_videos = [('title1', 'video_link1'), ('title2', 'video_link2')]
    translated_video_scripts_filenames = []                                       
    for title, link in untranslated_videos:                            
    
        keyword_from_title = title_to_keyword(title)                              
        video_script_name = generate_wiki_text(keyword_from_title)                
        translated_video_scripts_filenames.append(video_script_name)              
                                                                                  
    assert len(translated_video_scripts_filenames) == 2                            
    assert translated_video_scripts_filenames == [None, None]

def test_get_spanish_title():
    keyword = 'Entrepreneurship'

    titles = get_spanish_title(keyword)
    expected_long_answer = '¿Qué es Emprendimiento? Significado y definición'
    assert titles['youtube_long_title'] == expected_long_answer
    expected_short_answer = 'Emprendimiento'
    assert titles['youtube_short_title'] == expected_short_answer
