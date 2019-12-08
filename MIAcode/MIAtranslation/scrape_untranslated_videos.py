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

def scrape_untranslated_videos(**kwargs) -> List[Tuple[str, str]]:
    """
    returns [[video_name_EN, video_link]]
    """

    # TODO: figure out how to pass arguments from DAG to operator
    DEFAULT_BATCH_SIZE = 100

    untranslated_videos: List[scraper.Title] = asyncio.get_event_loop().run_until_complete(scraper.main(batch_size=DEFAULT_BATCH_SIZE))

    return untranslated_videos
