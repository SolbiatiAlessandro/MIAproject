"""
some ideas here

- GoogleTranlsate APIs
"""
from typing import List, Tuple
import logging

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

    translated_video_scripts_filenames = [
            'translated_scripts_1.miascript',
            'translated_scripts_2.miascript',
            ]
    return translated_video_scripts_filenames
