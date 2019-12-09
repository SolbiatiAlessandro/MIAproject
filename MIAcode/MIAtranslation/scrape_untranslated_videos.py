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

def scrape_untranslated_videos(**kwargs) -> List[Tuple[str, str]]:
    """
    returns [[video_name_EN, video_link]]
    """

    BATCH_SIZE  = int(Variable.get("youtube_translation_encyclopedia_BATCH_SIZE"))
    BATCH_START = int(Variable.get("youtube_translation_encyclopedia_BATCH_START"))
    logging.info(BATCH_SIZE)
    logging.info(BATCH_START)

    # hack on how to get out of the async loop, scraper is an awaitable
    untranslated_videos: List[scraper.Title] = asyncio.get_event_loop().run_until_complete(
            scraper.main(
                batch_size=BATCH_SIZE,
                batch_start=BATCH_START
                )
            )

    # TODO: this probably is not persistent when you quit the session
    # updating batch start
    BATCH_START += BATCH_SIZE
    Variable.set("youtube_translation_encyclopedia_BATCH_START", 
            BATCH_START)

    return untranslated_videos
