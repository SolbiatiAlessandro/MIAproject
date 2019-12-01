"""
some ideas here

- where to find TTS? can we use WaveNet?
- what images to use? think about creative part
- how to generate video in python?
"""
from typing import List, Tuple
import logging

def generate_translated_videos(**kwargs) -> List[str]:
    """
    generate .mp4 files from scripts
    """
    task_instance = kwargs['ti']
    translated_videos_scripts_filenames = task_instance.xcom_pull(
            key=None, 
            task_ids='translate_scripts') 
    logging.info("retrieved translated_videos_scripts_filenames from xcom_pull")
    logging.info(translated_videos_scripts_filenames)

    ## TODO (OANA)
    # given the translated name and script
    # generate a video to be uploaded on youtube 
    # and save it in a local path

    generated_video_path = [
            'translated_video_1.mp4',
            'translated_video_2.mp4',
            ]
    return generated_video_path
