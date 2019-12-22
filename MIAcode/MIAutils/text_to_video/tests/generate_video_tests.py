from generate_video_utils import generate_video_from_mp4, generate_image_filename, _videoclip
from miatypes import MiaScript
import pytest

@pytest.mark.skip(reason="expensive test")
def test_full_video():
    miascript = MiaScript()
    miascript.set_video_name("Emprendimiento")
    miascript.set_video_long_name("Que es el Emprendimiento?")
    miascript.set_audio_filename("./tts/Audio Files/test_audio_filename.mp3")
    #miascript.set_images_filename(["./static/example_img_1.png", "./static/example_img_2.png"])
    generate_video_from_mp4(miascript)
    assert miascript.video_filename == "Que es el Emprendimiento?.mp4"

def videoclip_no_audio(video_filename, text_title):
    video = _videoclip(generate_image_filename(), text_title).set_duration(30)
    video.write_videofile(
            video_filename,
            fps=1, 
            audio_bitrate="1000k", 
            bitrate="4000k")

def test_videoclip_no_audio_short():
    video_filename = "test_videoclip_no_audio_short.mp4"
    videoclip_no_audio(video_filename, "Short")
    assert True

def test_videoclip_no_audio_medium():
    video_filename = "test_videoclip_no_audio_medium.mp4"
    videoclip_no_audio(video_filename, "Medium Title")
    assert True

def test_videoclip_no_audio_long():
    video_filename = "test_videoclip_no_audio_long.mp4"
    videoclip_no_audio(video_filename, "Long Long Long Title")
    assert True
