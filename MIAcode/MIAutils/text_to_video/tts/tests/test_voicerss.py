import voicerss_tts

#python -m pytest tests/test_voicerss.py

def test_basic():
    voicerss_tts.generate_mp3('C:\\Users\\ASUS\\MIAProject\\MIAcode\\MIAutils\\generate_text\\Text Files\\Entrepreneurship.txt', 'test_audio_filename')
    assert True