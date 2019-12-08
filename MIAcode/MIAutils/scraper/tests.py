import pytest
from youtube_top_videos import main

@pytest.mark.asyncio
async def test_youtube_top_videos_one_scroll():
    titles = await main(
            channel_name="the audiopedia",
            batch_size=20)
    assert len(titles) == 20

@pytest.mark.asyncio
async def test_youtube_top_videos_more_scrolls():
    # 2 scrolls
    prev_titles = await main(batch_size=50)
    assert len(prev_titles) == 50

    # 2 scrolls + start
    next_titles = await main(batch_start=49, batch_size=50)
    assert len(next_titles) == 50
    assert next_titles[0][0] == prev_titles[-1][0]
    assert next_titles[0][1] == prev_titles[-1][1]
