import requests
import domain_extract


def check(url, test=False):
    if not (url.startswith("http://") or url.startswith("https://")):
        return False
    try:
        domain = domain_extract.domain(url)
        if not domain or not "." in domain:
            return False, 2
    except:
        return False
    if test:
        try:
            is_ok = requests.get(url).ok
            if is_ok:
                return True
            else:
                return False
        except:
            return False
    return True
