"""
this is the generate_translated_videos operator
we use utils from MIAutils.text_to_video

- where to find TTS? can we use WaveNet? : kind of, we use Tacotron + LCPnet
- what images to use? : in the beinning we don't use images, just slide with text
- how to generate video in python? : we use moviepy
"""
from typing import List, Tuple
import logging

def generate_translated_videos(**kwargs) -> List[str]:
    """
    generate .mp4 files from scripts
    """
    task_instance = kwargs['ti']
    miascripts: List[MiaScript] = task_instance.xcom_pull(
            key=None, 
            task_ids='translate_scripts') 
    logging.info("retrieved translated_videos_scripts_filenames from xcom_pull")
    miascripts[0]._debug()
    miascripts[-1]._debug()

    ## TODO (OANA)
    # given the translated name and script
    # generate a video to be uploaded on youtube 
    # and save it in a local path

    generated_video_path = [
            'translated_video_1.mp4',
            'translated_video_2.mp4',
            ]
    return generated_video_path
