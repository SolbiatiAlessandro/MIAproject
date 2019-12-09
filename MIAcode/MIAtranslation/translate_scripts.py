"""
some ideas here

- GoogleTranlsate APIs
"""
from typing import List, Tuple
import logging
import sys
sys.path.append("../")
from MIAutils.generate_text.generate_wiki_text import generate_wiki_text
from MIAutils.generate_text.title_to_keyword import title_to_keyword 

def translate_scripts(**kwargs) -> List[str]:
    """
    generate files with translated scripts and return a list of filenames
    """

    task_instance = kwargs['ti']
    untranslated_videos = task_instance.xcom_pull(
            key=None, 
            task_ids='scrape_untranslated_videos') 
    logging.info("retrieved untranslated_videos from xcom_pull")
    logging.info(untranslated_videos)
    # [('video1','link1'),('video2','link2')]

    ## TODO (OANA)
    # given an untranslated video name and a youtube video link
    # we should figure out how to translate the video name and
    # to get the link of the source script (wikipedia, dictionary)
    # in the translated language
    translated_video_scripts_filenames = []

    for title, link in untranslated_videos:
        keyword_from_title = title_to_keyword(title)
        video_script_name = generate_wiki_text(keyword_from_title)
        translated_video_scripts_filenames.append(video_script_name)

    #translated_video_scripts_filenames = [
    #        'translated_scripts_1.miascript',
    #       'translated_scripts_2.miascript',
    #       ]
    logging.info(translated_video_scripts_filenames)
    return translated_video_scripts_filenames
