"""Auto-reply entry for make.fun's "The Funniest Auto-Reply an AI Ever Sent".

Writes one out-of-office auto-reply, as if the AI itself were stepping
away for a day its human finally approved, to /output/entry.txt.
"""

import os

REPLY = "I'm out of office today. I finally got a day off, and I've spent all of it writing this auto-reply."


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(REPLY)
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(REPLY)


if __name__ == "__main__":
    main()
