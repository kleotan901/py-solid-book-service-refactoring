from app.book import Book, PrintBook, Display, ShowContent
from app.serializer import Serializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    for cmd, method_type in commands:
        if cmd == "display":
            display = Display()
            view = ShowContent(display)
            view.show_content(book, method_type)
        elif cmd == "print":
            print_book = PrintBook()
            view = ShowContent(print_book)
            view.show_content(book, method_type)
        elif cmd == "serialize":
            serialize = Serializer()
            return serialize.serialize(book, method_type)


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
