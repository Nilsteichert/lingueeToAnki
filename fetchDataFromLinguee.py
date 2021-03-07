from bs4 import BeautifulSoup


def main():
    with open("index.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')


if __name__ == '__main__':
    main()

