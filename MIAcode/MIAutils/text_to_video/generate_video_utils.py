"""
this is the module that generates the actual .mp4 file 
""" 
from typing import Dict
from moviepy.editor import AudioFileClip, clips_array, concatenate_videoclips, TextClip, CompositeVideoClip, vfx
from moviepy.video.VideoClip import ImageClip, ColorClip
from moviepy.video.fx.mask_color import mask_color
import sys
sys.path.append("../../")
from miatypes import MiaScript
from random import random
from PIL import Image, ImageDraw, ImageFont
import textwrap
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

# this is the mask color that later is removed
# so that we can achieve transparency
MASK_COLOR = (0,0,0) 
FONT_PATH = "./static/Typo Draft Demo.otf"

def generate_text_png(
        filename='01.png', 
        text="Hello", 
        size=12, 
        color=(255,255,255), 
        bg=MASK_COLOR,
        w=800,
        h=800,
        margin=50,
        ):
    """
    this method generates static .png image with title text
    to be resued later by moviepy: we need to do this because
    the fx.color_mask filter works only with static images and
    not with clips, so cant' use TextClip
    """
    logging.info("generating text .png image for text = "+str(text))
    "Draw a text on an Image, saves it, show it"

    fnt = ImageFont.truetype(FONT_PATH, size)
    # create image
    image = Image.new(mode = "RGB", size = (w, h), color = bg)
    draw = ImageDraw.Draw(image)
    # draw text

    """ 
    currently decided not to wrap text in multiline
    this is the code to do it:

    # https://stackoverflow.com/questions/8257147/wrap-text-in-pil
    wrapped_text = textwrap.wrap(text, width=10)
    logging.info("wrapping text")
    for line in wrapped_text:
        logging.info(line)
        draw.text((margin, offset), line, font=fnt, fill=color)
        offset += fnt.getsize(line)[1]
    """

    # offset is same from left (margin), same from bottom
    offset = h - fnt.getsize(text)[1] - margin
    draw.text((margin, offset), text, font=fnt, fill=color)

    # save file
    image.save(filename)
    return True

def _get_text_size(text: str, w: float, margin: int) -> int:
    """
    we are using a monospaced font so we can automatically resize
    it to fit exactly the width of the image
    FONT_PATH = "/Users/alex/Downloads/typo-draft/Typo Draft Demo.otf"

    to change font: select a monospace font and figure out a good 
    h_w_proportion ratio below for the font
    """
    # character are rectangles with this proportion
    h_w_proportion = 0.73
    # margin + text_size * h_w_proportion * len(text) + margin == w
    text_size = (w - (2 * margin))/(len(text) * h_w_proportion)
    return int(text_size)
    
def _videoclip(
        image_filename: str,
        title_text: str
        ) -> CompositeVideoClip:
    """
    generate a videoclip with background image and a text title,
    text title is with transparent background and resizes automatically
    (see _
    """
    logging.info('generating videoclip')
    image = ImageClip(image_filename)
    w, h, margin = image.w, image.h, 50

    text_title_image_path = title_text+".png"
    text_size = _get_text_size(title_text, w, margin)

    assert generate_text_png(
        filename=text_title_image_path,
        text=title_text,
        size=text_size,
        color=(255,255,255), # font color: white
        bg=MASK_COLOR, # this bg color get cut by the mask later
        w=w,
        h=h
        ), "something broke in generating .png static image"
    
    text_title_image = ImageClip(text_title_image_path)
    # this applies the mask so that we can get text transparency
    masked_text_title_image = mask_color(text_title_image, color=MASK_COLOR)

    video = CompositeVideoClip([image, masked_text_title_image], use_bgclip=True)
    return video

def generate_video_from_mp4(miascript: MiaScript) -> None:
    """
    given a `miascript` dictionary with at least:
    - miascript.audio_filename
    - miascript.video_name, "you need a video_name to add in the thumbnail"
    - miascript.video_long_name, "you need a video_long_name to save video for video full title"

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
    video_filename  = generate_video_filename(miascript.video_long_name)
    text_title = miascript.video_name.upper()

    video = (_videoclip(image_filename, text_title)
                    .set_duration(total_duration)
                    .set_audio(audio))

    logging.info("writing video to {}".format(video_filename))
    # parameters are at random
    video.write_videofile(
            video_filename,
            fps=10, 
            audio_bitrate="1000k", 
            bitrate="4000k")

    miascript.set_video_filename(video_filename)
