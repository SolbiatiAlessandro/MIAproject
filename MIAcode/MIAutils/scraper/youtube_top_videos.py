import asyncio
import pyppeteer
from pyppeteer import launch
from typing import List, Tuple
import logging

CHANNEL_HASH_MAP = {
        "the audiopedia": "UC6ZQ-SuhvQAeQIR5tHJGGmQ"
        }

SCROLL_DELAY = 1000

# video title, video link
Title = Tuple[str, str]

async def extract_titles(page: pyppeteer.page.Page) -> List[Title]: 
    """
    """
    titles_selector = "#video-title"
    await page.waitForSelector(titles_selector)

    titles = await page.evaluate('''titles_selector => {
        const anchors = Array.from(document.querySelectorAll(titles_selector));
        return anchors.map(anchor => {return [anchor.innerText, anchor.href]})
    }''', titles_selector)
    return titles

async def extract_titles_batch(page: pyppeteer.page.Page, 
        batch_start: int, 
        batch_size: int
        ) -> List[Title]:
    """
    batch_start: extract from the `batch_start`-th video
    
    does not implement caching, stupidly re-extract old videos,
    should implement smarter solution when we pass the 10^3 extraction size
    """
    batch: List[Title] = []
    scrolls: int = 0

    while (len(batch) < batch_start + batch_size):
        if scrolls >= 10 and scrolls % 10 == 0:
            logging.warning("| chromium is scrolling a lot, scrolls = {}".format(scrolls))
        batch = await extract_titles(page)
        logging.info(len(batch))
        await page.evaluate(
           "window.scrollTo(0, document.body.scrollHeight+1000000000)", 
           force_expr=True)
        await page.waitFor(SCROLL_DELAY)
        scrolls += 1

    batch = batch[batch_start:batch_start + batch_size]
    logging.info("extract_titles_batch: {} scrolls to extract {} titles".format(
        scrolls,
        batch_size))
    logging.info("example titles")
    logging.info(batch[0])
    logging.info(batch[-1])
    return batch

async def main(
        channel_name: str = "the audiopedia",
        batch_start: int = 0,
        batch_size: int = 100
        ) -> List[Title]:
    """
    extract batch_size Title (name, link) from youtube channel_name
    starting from batch_start
    """
    assert channel_name in CHANNEL_HASH_MAP, \
            "!!channel {} not implemented".format(channel_name)
    channel_hash = CHANNEL_HASH_MAP[channel_name]
    logging.info("starting headless chromium")
    browser = await launch(headless=True)
    page = await browser.newPage()
    url = "https://www.youtube.com/channel/{}/videos?view=0&sort=p&flow=list".format(
            channel_hash)
    await page.goto(url)
    titles = await extract_titles_batch(page, batch_start, batch_size)
    assert len(titles) == batch_size
    await browser.close()
    return titles

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    res = asyncio.get_event_loop().run_until_complete(main())
    print(res)

