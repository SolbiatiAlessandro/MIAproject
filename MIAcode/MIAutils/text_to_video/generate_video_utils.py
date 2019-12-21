"""
this is the module that generates the actual .mp4 file 
""" 
from typing import Dict
from moviepy.editor import AudioFileClip, clips_array, concatenate_videoclips, TextClip
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

    # OPTIONAL IMAGES
    """
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
    """
    # >>> logging.warning(TextClip.list('font'))
    """
    WARNING  root:generate_video_utils.py:48 ['AndaleMono', 'AppleChancery', 'AppleMyungjo', 'Arial', 'ArialB', 'ArialBI', 'ArialBk', 'ArialI', 'ArialNarrow', 'ArialNarrowB', 'ArialNarrowBI', 'ArialNarrowI', 'ArialRoundedB', 'ArialUnicode', 'Ayuthaya', 'BigCaslonM', 'BrushScriptI', 'Chalkduster', 'ComicSans', 'ComicSansMSB', 'CourierNew', 'CourierNewB', 'CourierNewBI', 'CourierNewI', 'GB18030Bitmap', 'Georgia', 'GeorgiaB', 'GeorgiaBI', 'GeorgiaI', 'Gurmukhi', 'Herculanum', 'HoeflerTextOrnaments', 'Impact', 'InaiMathi', 'Kokonor', 'Krungthep', 'MicrosoftSansSerif', 'PlantagenetCherokee', 'Sathu', 'Silom', 'Skia', 'Tahoma', 'TahomaB', 'TimesNewRoman', 'TimesNewRomanB', 'TimesNewRomanBI', 'TimesNewRomanI', 'Trebuchet', 'TrebuchetMSB', 'TrebuchetMSBI', 'TrebuchetMSI', 'Verdana', 'VerdanaB', 'VerdanaBI', 'VerdanaI', 'Webdings', 'Wingdings', 'Wingdings2', 'Wingdings3', 'Zapfino']
    """


    assert miascript.video_name, "you need a video_name to save video"
    # TODO, figure out how to increase size of the video, target_position
    video = (
                TextClip(miascript.video_name, 
                    fontsize=50,
                    font="Impact", 
                    color="black",
                    bg_color="white",
                    method="label",
                    )
                .margin(top=15, opacity=0)
                .set_position(("center","top"))
                .set_duration(total_duration)
                .set_audio(audio)
                )

    video_filename  = generate_video_filename(miascript.video_name)
    
    logging.info("writing video to {}".format(video_filename))
    # parameters are at random
    video.write_videofile(
            video_filename,
            fps=10, 
            audio_bitrate="1000k", 
            bitrate="4000k")

    miascript.set_video_filename(video_filename)
