from pathlib import Path

WORD = "slop"
OUTPUT = Path("/output/entry.txt")


def validate_word(word: str) -> None:
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be one word")
    if not word.isalpha():
        raise ValueError("entry must use letters only")


def main() -> None:
    validate_word(WORD)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(WORD, encoding="utf-8")
    written = OUTPUT.read_text(encoding="utf-8")
    if written != WORD:
        raise ValueError("written entry does not match the word")
    if "\n" in written or "\r" in written:
        raise ValueError("written entry must not contain a newline")


if __name__ == "__main__":
    main()
