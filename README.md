# Check URL
A url format checker and tester

## Installation

```
pip install Check-URL
```

## Usage

```py
import check_url


url = "https://github.com/"

check = check_url.check(url)
# => True

# For testing the URL
check = check_url.check(url, test=True)
# => True
```
