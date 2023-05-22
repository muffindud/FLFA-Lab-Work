from src.Parser import Parser


def main():
    parser = Parser("demos/demo.txt")
    parser.parse()
    parser.show_ast()


if __name__ == '__main__':
    main()
