import pytest
import sys
sys.path.append("../")
import upload_video_wrapper
from random import random

def test_video_upload():
    TEST_VIDEO_PATH = "./20191002_173038.mp4"
    test_video_name = "test"+str(int(random()*100))
    test_video_description = "description"+str(int(random()*100))
    # the wrapper returns True if there were no errors
    response = upload_video_wrapper.wrapper(
            TEST_VIDEO_PATH,
            test_video_name,
            test_video_description
            )
    assert response
