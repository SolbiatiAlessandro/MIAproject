"""
this is the generate_translated_videos operator
we use utils from MIAutils.text_to_video

- where to find TTS? can we use WaveNet? : kind of, we could use Tacotron + LCPnet 
but it breaks. so now we use an api service (voicerss.org)
- what images to use? : in the beinning we don't use images, just slide with text
- how to generate video in python? : we use moviepy
"""
from typing import List, Tuple
import logging
from MIAutils.text_to_video.generate_video_utils import \
        generate_video_from_mp4
from MIAutils.text_to_video.tts.voicerss_tts import \
        generate_mp3
from miatypes import MiaScript, miafilter


def generate_translated_videos(**kwargs) -> List[MiaScript]:
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

    for i, miascript in enumerate(miascripts):
        logging.info("starting video generation for video {}/{}".format(
            i, len(miascripts)))

        ## TODO (OANA)
        # add here your file that add .mp3 file
        # and that does this (inside or outside your function)
        assert(miascript.video_text_filename, "Trying to generate the audio, the path of the text file was not found")
        filepath_audio = generate_mp3(miascript.video_text_filename, miascript.title)
        miascript.set_audio_filename("./spanish_example.mp3")

        # in my case is doing it inside
        generate_video_from_mp4(miascript)

    return miafilter(miascripts, 'video_filename')
