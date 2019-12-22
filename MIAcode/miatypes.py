"""
typing for mia, used in video generation
"""
import logging
import os
from typing import NamedTuple, List
from uuid import uuid4
from datetime import datetime
from pprint import pformat

class MiaScript():
    """
    this is a class to fix the classes of miascript 
    dict that we pass around during the video processing
    """
    def __init__(self):
        self.script_id = uuid4()
        self.creation_date = datetime.now()

    def _debug(self):
        logging.info(pformat(self.__dict__))

    def has_output_video(self) -> (bool, str):
        """
        returns (True/False, reason)
        """
        if not hasattr(self, 'video_filename'):
            return (False, 'video has not been generated')
        if not os.path.isfile(self.video_filename):
            return (False, 'video has been generated but \
                    is not present anymore (e.g. deleted)')
        return (True, 'video is present')


    #-------- SET METHODS -------------------------------------

    def set_original_video_name(self, original_video_name: str):
        """
        video name in EN
        """
        self.original_video_name = original_video_name

    def set_original_video_link(self, video_link: str):
        """
        video name in EN
        """
        self.video_link = video_link

    def set_video_name(self, video_name: str):
        """
        this is like "Emprendimiento", the name that goes in the thumbnail
        """
        self.video_name = video_name

    def set_video_long_name(self, video_long_name: str):
        """
        this is like "Que es el Emprendimiento?", is the video title
        """
        self.video_long_name = video_long_name

    def set_video_text_filename(self, video_text_filename: str):
        """
        location of the text
        """
        self.video_text_filename = video_text_filename

    def set_audio_filename(self, audio_filename: str):
        """
        """
        self.audio_filename = audio_filename

    def set_video_filename(self, video_filename: str):
        """
        """
        self.video_filename = video_filename

    def set_video_description(self, video_description: str):
        """
        """
        self.video_description = video_description

    def set_images_filename(self, images_filename: List[str]):
        """
        """
        self.images_filename = images_filename

    def set_upload_outcome(self, upload_outcome: bool):
        """
        False: fail
        True: success
        """
        self.upload_outcome = upload_outcome

def miafilter(
        miascripts: List[MiaScript], 
        attribute: str = 'video_name') -> List[MiaScript]:
    """
    filter miascripts on a given attribute (to kill videos
    that didn't pass the operator
    """
    def check_attribute(script: MiaScript):
        if not hasattr(script, attribute):
            return False
        if getattr(script, attribute) is None:
            return False
        return True

    original_length = len(miascripts)
    miascripts = list(filter(check_attribute, miascripts))
    filtered_length = len(miascripts)

    logging.warning("Filtered MiaScripts from {} to {} (on {})".format(
        original_length,
        filtered_length,
        attribute))
    return miascripts
