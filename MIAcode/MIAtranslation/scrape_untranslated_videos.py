"""
some ideas here

- go in top videos of Audiopedia
- go in top videos of The Audiopedia
- go in top videos of wikipedia tts
"""
import sys
sys.path.append("../")
import MIAutils.scraper.youtube_top_videos as scraper
from typing import List, Tuple
import asyncio
import logging
from airflow.models import Variable
from airflow.models.crypto import get_fernet, InvalidFernetToken
from miatypes import MiaScript

BATCH_VARIABLE_NAMES = [
    "youtube_translation_encyclopedia_BATCH_SIZE",
    "youtube_translation_encyclopedia_BATCH_START"
]

def get_batch_variables():
    # TODO: this stuff is not documented, might want to write
    # docs and push to airflow/answer SOF questions
    res = [int(Variable.get(variable_name)) \
                for variable_name in BATCH_VARIABLE_NAMES]
    return res


def update_batch_variables(
        batch_size, batch_start
        ):
    Variable.set(BATCH_VARIABLE_NAMES[0], batch_size)
    Variable.set(BATCH_VARIABLE_NAMES[1], batch_start)

def scrape_untranslated_videos(**kwargs) -> List[MiaScript]:
    """
    returns a list of MiaScript with original_video_name 
    and original_video_link populated
    """

    batch_size, batch_start = get_batch_variables()

    # hack on how to get out of the async loop, scraper is an awaitable
    untranslated_videos: List[scraper.Title] = asyncio.get_event_loop().run_until_complete(
            scraper.main(
                batch_size=batch_size,
                batch_start=batch_start
                )
            )

    update_batch_variables(batch_size, batch_start + batch_size)

    miascripts = []

    # generate miascripts
    for (video_name, video_link) in untranslated_videos:
        miascript = MiaScript()
        miascript.set_original_video_name(video_name)
        miascript.set_original_video_link(video_link)
        miascripts.append(miascript)

    return miascripts
