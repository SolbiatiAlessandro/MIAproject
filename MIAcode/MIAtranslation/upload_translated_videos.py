"""
some ideas here

- will YouTube kill us?
- is there a public api? YES
"""
import logging
from miatypes import MiaScript
from typing import List
from MIAutils.google_wrapper.upload_video_wrapper \
        import wrapper as uploader
from random import random

def _test_operator(**kwargs):
    """
    external operator for testing uploading
    """
    TEST_VIDEO_PATH = "./test_video.mp4"
    test_video_name = "test"+str(int(random()*100))
    test_video_description = "description"+str(int(random()*100))

    test_miascript = MiaScript()
    test_miascript.set_video_description(test_video_description)
    test_miascript.set_video_long_name(test_video_name)
    test_miascript.set_video_filename(TEST_VIDEO_PATH)

    assert _operator([test_miascript]), "upload failed"

def _operator(miascripts: List[MiaScript]) -> None:
    """
    internal logic of the operator (extracted here so it cann
    be tested indipendently)
    """
    for i, miascript in enumerate(miascripts):
        logging.info("starting video upload for video {}/{}".format(
            i+1, len(miascripts)))
        miascript._debug()

        assert miascript.video_filename, "you need a video_filename to upload a video"
        assert miascript.video_long_name, "you need a video_long_name to set as a video name for uploading"
        if not hasattr(miascript, 'video_description'):
            logging.warning("NO DESCRIPTION SET!")
            miascript.set_video_description("Enjoy the video!")

        response = uploader(
                miascript.video_filename,
                miascript.video_long_name,
                miascript.video_description
                )
        logging.info("uploading finished with response:")
        logging.info(response)

def upload_translated_videos(**kwargs):
    """
    upload videos from local .mp4 files
    """
    task_instance = kwargs['ti']
    miascripts: List[MiaScript] = task_instance.xcom_pull(
            key=None, 
            task_ids='generate_translated_videos') 
    logging.info("retrieved miascripts from xcom_pull")
    miascripts[0]._debug()
    miascripts[-1]._debug()

    _operator(miascripts)
