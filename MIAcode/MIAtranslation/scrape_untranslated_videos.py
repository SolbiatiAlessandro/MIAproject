"""
some ideas here

- go in top videos of Audiopedia
- go in top videos of The Audiopedia
- go in top videos of wikipedia tts
"""
from typing import List, Tuple

def scrape_untranslated_videos(**kwargs) -> List[Tuple[str, str]]:
    """
    returns [[video_name_EN, video_link]]
    """

    ## TODO (ALEX) : generate video_name and video_link
    # figure out here how to generate video names and links
    # scraping from youtube

    untranslated_videos = [
            ('test_video_english_name_1','test_video_url_1'),
            ('test_video_english_name_2','test_video_url_2'),
            ]
    return untranslated_videos
