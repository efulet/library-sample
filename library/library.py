"""
You run a successful software consulting business, and you've just gotten a visit 
from Earl, who runs the local library. He's looking for software that will help 
him manage his very peculiar checkout process.

"Organizing books is hard," says Earl. "I gave up on it years ago. Nowadays when 
you come into the library and ask for a book in a particular genre, I just give 
you the last book anybody checked in that belongs to that genre."

"You give people the last book that came in?" you ask.

"Yeah; it's easy that way, because I can just keep a pile of books near the front."

"But what do you do if they want a different book?"

"You can't get cable in this town, so most people aren't so picky. I do like to 
do some reading on my own inside the library, though, so I instituted a new 
process. When you check a book in, you give it a rating. Every once in a while
I want to know the book that was rated the highest in the genre by the last 
person to check it in."

After talking it through with Earl, you agree to implement the following interface:

  * checkOutBook: This function returns the book that was last checked in 
    inside a particular genre, and removes it from the Library's store.

  * checkInBook: This function allows the customer to return a book. That book 
    becomes the last one checked into the genre. It also takes a rating between 
    1 and 100 (inclusive) so that Earl can figure out which the best books are.

  * peekHighestRatedBook: This function returns the highest-rated book that is 
    currently checked into a given genre. It does not change its order in the 
    check-in and -out process.

Earl and you agree that you can manage storage in memory without worrying about 
persisting it to disk.

@created_at 2015-05-16
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import sys

from lib.library import Library, Book, Genre


def main(args):
    try:
        library = Library()
        
        # Create a fake books for running tests
        # Input for book: genre, title, author, rating
        # Available genre: NON_FICTION, GENERAL_FICTION, SCIENCE_FICTION, WESTERN
        book_1 = Book(Genre.NON_FICTION, "The Princess Bride", "William Goldman", 1)
        library.add_book(book_1)
        book_2 = Book(Genre.GENERAL_FICTION, "The Hunger Games", "Suzanne Collins", 1)
        library.add_book(book_2)
        book_3 = Book(Genre.SCIENCE_FICTION, "Divergent", "Veronica Roth", 1)
        library.add_book(book_3)
        book_4 = Book(Genre.WESTERN, "Pride and Prejudice", "Jane Austen", 1)
        library.add_book(book_4)
        book_5 = Book(Genre.NON_FICTION, "The Diary of a Young Girl", "Anne Frank", 1)
        library.add_book(book_5)
        library.print_library()
        
        print "-----------------------"
        print "Checkout Genre.NON_FICTION"
        book = library.checkout_book(Genre.NON_FICTION)
        print "book title: %s" % book.get_title()
        print "book rating: %s" % book.get_rating()
        print "book available: %s" % book.get_available()
        print "book get_checkin_timestamp: %s" % book.get_checkin_timestamp()
        
        print "-----------------------"
        print "Changing rating for book 1"
        library.checkin_book(book_1, 50)
        library.checkin_book(book_5, 80)
        library.print_library()
        
        print "-----------------------"
        print "The highest rated book in the specified genre"
        book = library.peek_highest_rated_book(Genre.NON_FICTION)
        print "book title: %s" % book.get_title()
        print "book rating: %s" % book.get_rating()
        print "book available: %s" % book.get_available()
        print "book get_checkin_timestamp: %s" % book.get_checkin_timestamp()
        
        return 0
    except Exception, err:
        logger.error(str(err), exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
