import re
from typing import Optional

def title_to_keyword(input_yt_title: str) -> Optional[str]:
    #input_yt_title
    #import pdb;pdb.set_trace()
    re_match_pattern1 = re.search('(?<=is )(.*)(?=\? What)', input_yt_title)
    re_match_pattern2 = re.search('(?<=does )(.*)(?= mean\?)', input_yt_title)
    
    if re_match_pattern1:
        re_match = re_match_pattern1
    elif re_match_pattern2:
        re_match = re_match_pattern2
    else:
        return

    keyword = re_match.group(0)
    no_spaces_keyword = keyword.replace(' ', '_')
    return no_spaces_keyword

if __name__ == '__main__':
    example = "What does CRINGE mean? CRINGE definition - CRINGE meaning - How to pronounce CRINGE"
    example2 = "What is HUMIDITY? What does HUMIDITY mean? HUMIDITY meaning - How to pronounce HUMIDITY?"
    print(title_to_keyword(example))
