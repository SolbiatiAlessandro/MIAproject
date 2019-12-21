from generate_video_utils import generate_video_from_mp4
from miatypes import MiaScript

def test_example():
    miascript = MiaScript()
    miascript.set_video_name("Emprendimiento")
    miascript.set_video_long_name("Que es el Emprendimiento?")
    miascript.set_audio_filename("./tts/Audio Files/test_audio_filename.mp3")
    #miascript.set_images_filename(["./static/example_img_1.png", "./static/example_img_2.png"])
    generate_video_from_mp4(miascript)
    assert miascript.video_filename == "Que es el Emprendimiento?.mp4"
