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
from airflow.models import Variable
from youtube_translation_encyclopedia import BATCH_VARIABLE_NAMES


def get_batch_variables():
    # TODO: this stuff is not documented, might want to write
    # docs and push to airflow/answer SOF questions
    return [Variable.get(variable_name).get_val() \
                    for variable_name in BATCH_VARIABLE_NAMES]

def update_batch_variables(
        batch_size, batch_start
        ):
    #TODO: probably this is not persistent
    Variable.get(BATCH_VARIABLE_NAMES[0]).set_val(batch_size)
    Variable.get(BATCH_VARIABLE_NAMES[1]).set_val(batch_start)

def scrape_untranslated_videos(**kwargs) -> List[Tuple[str, str]]:
    """
    returns [[video_name_EN, video_link]]
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
    return untranslated_videos
