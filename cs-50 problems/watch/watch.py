import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"^<iframe.+src=\"(https?://(?:www\.)?youtube\.com/embed/[a-zA-Z0-9]+)\".+</iframe>$", s):
        address = (
            matches.group(1)
            .replace("youtube.com/embed", "youtu.be")
            .replace("www.", "")
        )
        if "https" not in address:
            address = address.replace("http", "https")

        return address


if __name__ == "__main__":
    main()
