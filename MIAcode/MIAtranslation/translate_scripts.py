"""
some ideas here

- GoogleTranlsate APIs
"""
from typing import List, Tuple
import logging
import sys
sys.path.append("../")
from MIAutils.generate_text.generate_wiki_text import generate_wiki_text
from MIAutils.generate_text.generate_wiki_text import get_spanish_title
from MIAutils.generate_text.title_to_keyword import title_to_keyword 
from miatypes import MiaScript, miafilter

def translate_scripts(**kwargs) -> List[MiaScript]:
    """
    generate files with translated scripts and return a list of filenames
    """

    task_instance = kwargs['ti']
    miascripts: List[MiaScript] = task_instance.xcom_pull(
            key=None, 
            task_ids='scrape_untranslated_videos') 
    logging.info("retrieved untranslated_videos from xcom_pull")
    miascripts[0]._debug()
    miascripts[-1]._debug()

    for miascript in miascripts:
        EN_title = miascript.original_video_name
        keyword_from_title = title_to_keyword(EN_title)
        video_script_name = generate_wiki_text(keyword_from_title)

        ES_title = get_spanish_title(keyword_from_title)
        # TODO (oana)
        # fix title: put the long title here
        ES_long_title = "Que es " + ES_title

        miascript.set_video_name(ES_title) # this is 'Emprendimiento'
        miascript.set_video_long_name(ES_long_title) # this is 'Que es Emprendimiento?'
        miascript.set_video_text_filename(video_script_name)

    miascripts[0]._debug()
    miascripts[-1]._debug()
    return miafilter(miascripts, 'video_name')
