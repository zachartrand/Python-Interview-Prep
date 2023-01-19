#!/usr/bin/env python3
"""
A Sorted Tale

You recently began employment at “A Sorted Tale”, an independent 
bookshop. Every morning, the owner decides to sort the books in a new way.

Some of his favorite methods include:

    By author name

    By title

    By number of characters in the title

    By the reverse of the author’s name

Throughout the day, patrons of the bookshop remove books from the 
shelf. Given the strange ordering of the store, they do not always get 
the books placed back in exactly the correct location.

The owner wants you to research methods of fixing the book ordering 
throughout the day and sorting the books in the morning. It is 
currently taking too long!

From Pass The Technical Interview With Python on CodeCademy:
    
    https://www.codecademy.com/paths/pass-the-technical-interview-with-python/tracks/sorting-algorithms-python/modules/radix-sort-python/projects/sorted-tale
"""

import sorts
import utils


def main():
    bookshelf = utils.load_books("books_small.csv")
    bookshelf_v1 = bookshelf[:]
    bookshelf_v2 = bookshelf[:]
    long_bookshelf = utils.load_books("books_large.csv")

    for book in bookshelf:
        print(book["title"])
    print()

    sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
    print()

    for book in sort1:
        print(book["title"])
    print()

    for book in bookshelf_v1:
        print(book["author"])
    print()

    sort2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
    print()

    for book in bookshelf_v1:
        print(book["author"])
    print()


    for book in bookshelf_v2:
        print(book["author"])
    print()

    print("Quicksorting by author ascending:")
    sorts.quicksort(bookshelf_v2, by_author_ascending)
    print("Done!")
    for book in bookshelf_v2:
        print(book["author"])
    print()

    print("Sorting long bookshelf...")
    # sort4 = sorts.bubble_sort(long_bookshelf, by_total_length)
    sorts.quicksort(long_bookshelf, by_total_length)
    print("Done!")


def by_title_ascending(book1, book2):
    if book1["title_lower"] > book2["title_lower"]:
        return True

    return False


def by_author_ascending(book1, book2):
    if book1["author_lower"] > book2["author_lower"]:
        return True

    return False


def by_total_length(book1, book2):
    len1 = len(book1["author_lower"]) + len(book1["title_lower"])
    len2 = len(book2["author_lower"]) + len(book2["title_lower"])
    if len1 > len2:
        return True

    return False


if __name__ == "__main__":
    main()