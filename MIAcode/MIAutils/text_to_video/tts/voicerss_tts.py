import http.client, urllib
import json
import logging
import os

VOICERSS_KEY = "voicerss_key.json"

def speech(settings):
    __validate(settings)
    return __request(settings)

def __validate(settings):
    if not settings: raise RuntimeError('The settings are undefined')
    if 'key' not in settings or not settings['key']: raise RuntimeError('The API key is undefined')
    if 'src' not in settings or not settings['src']: raise RuntimeError('The text is undefined')
    if 'hl' not in settings or not settings['hl']: raise RuntimeError('The language is undefined')

def __request(settings):
    result = {'error': None, 'response': None}

    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
    params = urllib.parse.urlencode(__buildRequest(settings))
    
    if 'ssl' in settings and settings['ssl']:
        conn = http.client.HTTPSConnection('api.voicerss.org:443')
    else:
        conn = http.client.HTTPConnection('api.voicerss.org:80')
        
    conn.request('POST', '/', params, headers)
    
    response = conn.getresponse()
    content = response.read()
    
    if response.status != 200:
        result['error'] = response.reason
    elif content.find(bytes('ERROR', 'utf8')) == 0:
        result['error'] = content
    else:
        result['response'] = content
        
    conn.close()

    return result

def __buildRequest(settings):
    params = {'key': '', 'src': '', 'hl': '', 'r': '', 'c': '', 'f': '', 'ssml': '', 'b64': ''}
    
    if 'key' in settings: params['key'] = settings['key']
    if 'src' in settings: params['src'] = settings['src']
    if 'hl' in settings: params['hl'] = settings['hl']
    if 'r' in settings: params['r'] = settings['r']
    if 'c' in settings: params['c'] = settings['c']
    if 'f' in settings: params['f'] = settings['f']
    if 'ssml' in settings: params['ssml'] = settings['ssml']
    if 'b64' in settings: params['b64'] = settings['b64']
    
    return params

def get_key():
    logging.warning("Reading KEY for Voicerss")
    secret = json.load(open(VOICERSS_KEY,"r"))
    logging.warning(secret['key'])
    return secret['key']

def get_text_from_file(filepath: str) -> str:
    with open(filepath, "rb+") as f:
        input_text = f.read()
    return input_text

def create_filepath(filename: str) -> str:
    """
    """
    here = os.path.dirname(os.path.realpath(__file__))
    subdir = "Audio Files"
    filename = ("%s.mp3" % filename)
    filepath = os.path.join(here, subdir, filename)
    logging.warning("create_filpath: {}".format(filepath))
    return filepath

def generate_mp3_helper(input_text: str, output_filepath: str) -> None:
    settings = {'key': get_key(), 'src': input_text, 'hl': 'es-es', 'r': '0', 'c': 'mp3', 'f': '44khz_16bit_stereo', 'ssml': 'false', 'b64': 'false'}
    result = speech(settings)
    # import pickle as pkl
    # pkl.dump(result, open("voicerss.pkl","wb"))
    # result = pkl.load(open("voicerss.pkl","rb"))
    with open(output_filepath, "wb+") as f:
        f.write(result['response'])

def generate_mp3(input_filepath: str, output_filename: str) -> str:
    input_text = get_text_from_file(input_filepath)

    output_filepath = create_filepath(output_filename)

    generate_mp3_helper(input_text, output_filepath)

    return output_filepath

