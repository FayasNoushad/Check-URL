import requests


def check(url, test=False):
    if url.startswith("http://") or url startswith("https://"):
        return False 
    try:
        domain = domain_extract.domain(url)
        if not domain or not "." in domain:
            return False
    except:
        return False 
    if test:
        try:
            requests.get(url)
        except:
            return False
    return True
