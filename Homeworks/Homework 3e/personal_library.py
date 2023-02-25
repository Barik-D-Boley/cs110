class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


def main():
    books_read = []

    print('Enter the title, author, and pages of each book.\nEnd with a blank title.')

    while True:
        title = input('Title: ')
        if title == '':
            break
        author = input('Author: ')
        pages = input('Pages: ')
        books_read.append(Book(title, author, int(pages)))

    author_report = input('Enter an author to report on.\nAuthor: ')
    author_books = 0
    author_pages = 0

    for i in range(len(books_read)):
        if books_read[i].author.lower() == author_report.lower():
            author_books += 1
            author_pages += books_read[i].pages

    print(f'You have read {author_books} books by {author_report}.')
    print(f'You have read {author_pages} pages by {author_report}.')


if __name__ == '__main__':
    main()