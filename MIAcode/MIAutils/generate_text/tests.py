import pytest
from generate_wiki_text import generate_wiki_text
from title_to_keyword import title_to_keyword

def test_generate_sp_script_files_from_en_video_titles():
    untranslated_videos = [('What does Entrepreneurship mean? Entrepreneurship definition - Entrepreneurship meaning - How to pronounce ENtrepreneurship', 'video_link1'), ('What is Python? What does Python mean? Python meaning - How to pronounce Python?', 'video_link2')]
    translated_video_scripts_filenames = []
    for title, link in untranslated_videos:
        keyword_from_title = title_to_keyword(title)
        video_script_name = generate_wiki_text(keyword_from_title)
        translated_video_scripts_filenames.append(video_script_name)

    assert len(translated_video_scripts_filenames) == 2
    assert translated_video_scripts_filenames ==  ['C:\\Users\\ASUS\\MIAProject\\MIAcode\\MIAutils\\generate_text\\Text Files\\Entrepreneurship.txt', None]



def test_generate_sp_script_files_from_en_video_titles_no_wiki_pages():
    untranslated_videos = [('title1', 'video_link1'), ('title2', 'video_link2')]
    translated_video_scripts_filenames = []                                       
    for title, link in untranslated_videos:                            
        keyword_from_title = title_to_keyword(title)                              
        video_script_name = generate_wiki_text(keyword_from_title)                
        translated_video_scripts_filenames.append(video_script_name)              
                                                                                  
    assert len(translated_video_scripts_filenames) == 2                            
    assert translated_video_scripts_filenames == [None, None]
