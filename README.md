usage: AutoWordList.py [-h] [-s [# of sites]] [-d [search depth]] [keywords ...]

AutoWordList uses Google to create a "smart" wordlist that can help speed up bruteforcing. The generated list is designed to be used in conjuction
with a standard wordlist to create an effective Combinator attack with Hashcat. AutoWordList searches Google for the inputted words, scrapes the
top websites that come up, and creates a wordlist using the most common words found on each site.
