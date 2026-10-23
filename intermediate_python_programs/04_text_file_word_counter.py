
from pathlib import Path
import re


def analyze_text(text):
    words = re.findall(r"\b[\w'-]+\b", text)
    sentences = re.findall(r"[.!?]+(?=\s|$)", text)

    return {
        "characters": len(text),
        "characters_without_spaces": sum(
            not character.isspace() for character in text
        ),
        "words": len(words),
        "lines": len(text.splitlines()),
        "sentences": len(sentences),
    }


def main():
    print("=" * 40)
    print("        TEXT FILE WORD COUNTER")
    print("=" * 40)

    file_name = input("Enter the text file path: ").strip().strip('"')
    file_path = Path(file_name)

    try:
        text = file_path.read_text(encoding="utf-8")
        result = analyze_text(text)

        print("\nTEXT ANALYSIS REPORT")
        print("-" * 40)

        for label, count in result.items():
            formatted_label = label.replace("_", " ").title()
            print(f"{formatted_label:<30}: {count}")

        print("-" * 40)

    except FileNotFoundError:
        print("Error: The specified file was not found.")

    except PermissionError:
        print("Error: You don't have permission to read this file.")

    except UnicodeDecodeError:
        print("Error: The file could not be read as UTF-8 text.")

    except OSError as error:
        print(f"File error: {error}")


if __name__ == "__main__":
    main()
