"""
this is the module that generates the actual .mp4 file 
""" 
from typing import Dict
from moviepy.editor import AudioFileClip, clips_array, concatenate_videoclips, TextClip, CompositeVideoClip
from moviepy.video.VideoClip import ImageClip
import sys
sys.path.append("../../")
from miatypes import MiaScript
from random import random
import logging
import os

def generate_video_filename(video_name: str) -> str:
    """
    standardise video output name
    """
    return video_name + ".mp4"

def generate_image_filename() -> str:
    """
    randomised image, like ./static/_mia1.jpg
    """
    NUMBER_OF_IMAGES = 3
    random_suffix = int(random()*10%NUMBER_OF_IMAGES) + 1
    return os.path.join("static","_mia"+str(random_suffix)+".jpg")


def generate_video_from_mp4(miascript: MiaScript) -> None:
    """
    given a `miascript` dictionary with at least:
    - miascript.audio_filename
    - miascript.imges

    generates a video and set it on the MiaScript
    """
    logging.info("calling generate_video_from_mp4 for miascript:")
    miascript._debug()

    assert miascript.audio_filename, "you need audio to create video"
    audio = (AudioFileClip(miascript.audio_filename))
    total_duration = audio.duration

    assert miascript.video_name, "you need a video_name to add in the thumbnail"
    assert miascript.video_long_name, "you need a video_long_name to save video for video full title"
    image_filename = generate_image_filename()
    image = ImageClip(image_filename)
    w, h = image.w, image.h

    text_title = (
                TextClip(miascript.video_name.upper(), 
                    fontsize=100,
                    font="Georgia",
                    color="black",
                    bg_color="white",
                    method='caption',
                    )
                .set_position((0, 0.61), relative=True)
                .resize(width=w)
                .margin(15, 'grey')
                )

    video = (CompositeVideoClip([image, text_title])
                .set_duration(total_duration)
                .set_audio(audio))

    video_filename  = generate_video_filename(miascript.video_long_name)
    
    logging.info("writing video to {}".format(video_filename))
    # parameters are at random
    video.write_videofile(
            video_filename,
            fps=10, 
            audio_bitrate="1000k", 
            bitrate="4000k")

    miascript.set_video_filename(video_filename)
