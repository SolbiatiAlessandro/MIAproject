"""
typing for mia, used in video generation
"""
from typing import NamedTuple, List
from uuid import uuid4
import logging
from pprint import pformat

class MiaScript():
    """
    this is a class to fix the classes of miascript 
    dict that we pass around during the video processing
    """
    def __init__(self):
        self.script_id = uuid4()

    def _debug(self):
        logging.info(pformat(self.__dict__))

    def set_video_name(self, video_name: str):
        """
        """
        self.video_name = video_name

    def set_video_text(self, video_text: str):
        """
        """
        self.video_text = video_text

    def set_audio_filename(self, audio_filename: str):
        """
        """
        self.audio_filename = audio_filename

    def set_video_filename(self, video_filename: str):
        """
        """
        self.video_filename = video_filename

    def set_images_filename(self, images_filename: List[str]):
        """
        """
        self.images_filename = images_filename
