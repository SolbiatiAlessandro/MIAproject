"""
this is the module that generates the actual .mp4 file
"""
from typing import Dict

def generate_video_from_mp4(miascript: Dict) -> Dict:
    """
    given a `miascript` dictionary with at least:
    - miascript.audio_filename
    - miascript.imges

    generates a video
    """
    assert miascript.audio_filename
    assert miascript.images

    miascript.video_filename = "Not Implemented"
    return miascript
