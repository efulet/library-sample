"""
Define the implementation for Library interface and their class exceptions.

@created_at 2015-05-16
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import operator

from book import Book


class LibraryException(Exception):
    """Define an exception class for Library errors"""
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class OutOfBooksException(LibraryException):
    """Define an exception class for OutOfBooks errors"""
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


class IllegalRatingException(LibraryException):
    """Define an exception class for IllegalRating errors"""
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)


# Steps:
# 1. Define a list of books for creating our library
# 2. Implement methods
# 3. Indicate time and space complexity
# 4. Document any unusual edge cases or problems
class Library:
    """Define a class for the library implementation"""
    MIN_RATING = 1
    MAX_RATING = 100
    
    def __init__(self):
        self.books = {}
    
    def add_book(self, book):
        """Add a new book to the library. We dont have a db, so we create a 
        dictonary with books
        """
        if not book:
            raise LibraryException("Book is null or empty, please add a book")
        id = self.library_length() + 1
        
        # id: primary key of the book
        # store a tuple: book, available
        self.books[str(id)] = book
    
    def library_length(self):
        """Return length of the library"""
        return len(self.books)
    
    def print_library(self):
        """Just for checking object in books"""
        for id, book in self.books.items():
            print "--"
            print "book id: %s" % id
            print "book title: %s" % book.get_title()
            print "book rating: %s" % book.get_rating()
            print "book available: %s" % book.get_available()
            print "book get_checkin_timestamp: %s" % book.get_checkin_timestamp()
    
    # So the best case scenario: O(n), average and worst case O(nlogn)
    def checkout_book(self, genre):
        """Returns the book most recently checked in in this genre, and removes 
        it from the pool of available items.
        
        :param genre: the genre to which the book belongs
        :return: the Book object that has just been checked out
        :raises OutOfBooksException: if there are no books in that genre available
        """
        if not genre:
            raise LibraryException("Missed genre parameter")
        
        # It has to go for all books in the list, so it's O(n)
        genre_list = []
        for id, book in self.books.items():
            if book.get_genre() == genre and book.get_available():
                genre_list.append(book)
        
        # Check if there is books avaible for sorting
        if not genre_list:
            raise OutOfBooksException("There is no books in that genre available")
        
        # Sorting by the highest rated book.
        # Best case scenario: O(n), average and worst case O(nlogn)
        recent_book = sorted(genre_list, key=operator.attrgetter('checkin_timestamp'), reverse=True)[0]
        recent_book.set_available(False)
        
        return recent_book
    
    # So the average and worst case O(n)
    def checkin_book(self, returned_book, rating):
        """Returns the book to the library's availability pool, making it the 
        last checked-in book and rating the book in the process.
        
        :param returned_book: the Book that is being checked back in
        :param rating: an integer from 1 to 100 (inclusive) specifying the 
                       rating. The last person to rate the book overwrites any 
                       previous rating
        :raises IllegalRatingException: if a rating less than 1 or more than 100 
                                        is specified
        """
        if not returned_book:
            raise LibraryException("Book is null or empty, please add a book")
        
        if rating < self.MIN_RATING:
            raise IllegalRatingException("Rating less than " + self.MIN_RATING)
        
        if rating > self.MAX_RATING:
            raise IllegalRatingException("Rating greater than " + self.MAX_RATING)
        
        # I'm guessing that the title is unique, then I'm checking if the book is
        # on the dict.
        # This implementation take O(n), where n is the number of books into the 
        # library.
        # If the library is a db it should take less time guessing we have a 
        # code for locate the book in table
        for id, book in self.books.items():
            if book.get_title() == returned_book.get_title():
                book.set_rating(rating)
                book.set_available(True)
                book.set_checkin_timestamp()
                break
        
        # What happens if the returned book is not into the list?
    
    # So the best case scenario: O(n), average and worst case O(nlogn)
    def peek_highest_rated_book(self, genre):
        """Returns the highest rated book in the specified genre, but does not 
        remove it from availability.
        
        param genre: the genre for which we'd like to retrieve the highest-rated 
                     book
        :return: a Book that is the highest-rated book currently available in 
                 the genre
        :raises OutOfBooksException: if there are no books in that genre available
        """
        if not genre:
            raise LibraryException("Missed genre parameter")
        
        # It has to go for all books in the list, so it's O(n)
        genre_list = []
        for id, book in self.books.items():
            if book.get_genre() == genre and book.get_available():
                genre_list.append(book)
        
        # Check if there is books avaible for sorting
        if not genre_list:
            raise OutOfBooksException("There is no books in that genre available")
        
        # Sorting by the highest rated book.
        # Best case scenario: O(n), average and worst case O(nlogn)
        return sorted(genre_list, key=operator.attrgetter('rating'), reverse=True)[0]
