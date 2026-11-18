def format_header() -> str:
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                text = input("Text: ")
                return f"{'#' * level} {text}\n"
        except ValueError:
            pass
        print("The level should be within the range of 1 to 6")


def format_list(ordered: bool) -> str:
    while True:
        try:
            rows = int(input("Number of rows: "))
            if rows > 0:
                break
        except ValueError:
            pass
        print("The number of rows should be greater than zero")

    items = []
    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        prefix = f"{i}." if ordered else "-"
        items.append(f"{prefix} {row_text}\n")
    return "".join(items)


def format_link() -> str:
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def print_help() -> None:
    print(
        "Available formatters: plain bold italic header link "
        "inline-code ordered-list unordered-list new-line"
    )
    print("Special commands: !help !done")


def main() -> None:
    formatters = {
        "plain": lambda: input("Text: "),
        "bold": lambda: f"**{input('Text: ')}**",
        "italic": lambda: f"*{input('Text: ')}*",
        "inline-code": lambda: f"`{input('Text: ')}`",
        "new-line": lambda: "\n",
        "header": format_header,
        "link": format_link,
        "ordered-list": lambda: format_list(ordered=True),
        "unordered-list": lambda: format_list(ordered=False),
    }

    markdown_result = ""

    while True:
        choice = input("Choose a formatter: ")

        if choice == "!help":
            print_help()
        elif choice == "!done":
            with open("output.md", "w", encoding="utf-8") as file:
                file.write(markdown_result)
            break
        elif choice in formatters:
            markdown_result += formatters[choice]()
            print(markdown_result)
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()