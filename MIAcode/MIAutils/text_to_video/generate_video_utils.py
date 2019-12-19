"""
this is the module that generates the actual .mp4 file
"""
from typing import Dict
from moviepy.editor import AudioFileClip, clips_array, concatenate_videoclips
from moviepy.video.VideoClip import ImageClip
import sys
sys.path.append("../../")
from miatypes import MiaScript
import logging

def generate_video_filename(video_name: str) -> str:
    """
    standardise video output name
    """
    return video_name + ".mp4"

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
    
    assert miascript.images_filename, "you need images to create video"
    clip_duration = total_duration / len(miascript.images_filename)
    image_clips = [ImageClip(image_filename)\
                .set_duration(clip_duration)\
                .fadein(.5)\
                .fadeout(.5)
                for image_filename in miascript.images_filename[::-1]]

    video = concatenate_videoclips(image_clips)\
            .set_audio(audio)\
            .set_duration(total_duration - 1)

    assert miascript.video_name, "you need a video_name to save video"
    video_filename  = generate_video_filename(miascript.video_name)
    
    logging.info("writing video to {}".format(video_filename))
    # parameters are at random
    video.write_videofile(
            video_filename, 
            fps=10, 
            audio_bitrate="1000k", 
            bitrate="4000k")

    miascript.set_video_filename(video_filename)
