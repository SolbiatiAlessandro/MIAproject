from miatypes import MiaScript, miafilter

def test_miafilter():
    length = 4
    scripts = [MiaScript() for _ in range(length)]
    for script in scripts:
        script.set_images_filename(['asd','edf'])
    assert len(miafilter(scripts, 'images_filename')) == length
    assert len(miafilter(scripts, 'video_filename')) == 0
    scripts[0].set_audio_filename('asdasd')
    assert len(miafilter(scripts, 'audio_filename')) == 1



