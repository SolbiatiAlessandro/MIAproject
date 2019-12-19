"""
this is the module that generates the actual .mp4 file
"""
from typing import Dict
from moviepy.editor import AudioFileClip
import sys
sys.path.append("../../")
from miatypes import MiaScript
import logging

def generate_video_from_mp4(miascript: MiaScript) -> MiaScript:
    """
    given a `miascript` dictionary with at least:
    - miascript.audio_filename
    - miascript.imges

    generates a video
    """
    assert miascript.video_name
    assert miascript.audio_filename
    assert miascript.images_filename
    logging.info("calling generate_video_from_mp4 for miascript:")
    miascript._debug()
    miascript.set_video_filename("Not Implemented")
