import re
from urlextract import URLExtract
from settings import REMOVE_URLS_WL_DATA as WHITELIST
extractor = URLExtract()


def remove_urls(text, limit_not_remove = 140, placeholder = '***'):
    if len(text) < limit_not_remove:
        return text

    urls = extractor.find_urls(text)
    for url in urls:
        allowed = False
        for ex in WHITELIST:
            if url.find(ex) != -1:
                allowed = True
                break
        if allowed is False:
            text = text.replace(url, placeholder)

    # @test => @ test
    text = re.sub(r'(@)([\d\w]*)', r'\1 \2', text)

    return text
