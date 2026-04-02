import re
import sys


def main():
    s = input("HTML: ").strip()
    print(parse(s))


# expect a string as input, extract the youtube url and return the video id, otherwise return None
# return the short youtube url.


# example input: <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
def parse(s):
    matches = re.search(r"<iframe.*?src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)\".*?>", s, re.IGNORECASE)
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
