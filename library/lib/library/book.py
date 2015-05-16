"""
Define the implementation for Book.

@created_at 2015-05-16
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


import datetime
import time


class Book:
    """Define a class for book implementation"""
    
    def __init__(self, genre, title, author, rating=1):
        """Parameterized constructor for Books.
        
        :param genre: the genre to which this book belongs
        :param title: the title of this book
        :param author: the author of this book
        :param rating: the rating of this book
        """
        if not genre:
            raise Exception("Missed genre parameter")
        
        self.genre = genre
        
        if not title:
            raise Exception("Missed title parameter")
        
        self.title = title
        
        if not author:
            raise Exception("Missed author parameter")
        
        self.author = author
        
        if not rating:
            raise Exception("Missed rating parameter")
        
        self.rating = rating
        
        # This are useful class variables to keep the book information up-to-date
        self.available = True
        self.checkin_timestamp = datetime.datetime.now().microsecond
    
    def get_genre(self):
        """Returns the genre to which the book belongs.
        
        :return: a Genre representing the genre
        """
        return self.genre
    
    def get_title(self):
        """"Returns the title of the book.
        
        :return: a String containing the title of the book in English
        """
        return self.title
    
    def get_author(self):
        """Returns the author of the book.
        
        :return: a String containing the name of the author of the book
        """
        return self.author
    
    def get_rating(self):
        """Returns the rating of the book.
        
        :return: an int containing that rating
        """
        return self.rating
    
    def get_available(self):
        """Return the if book is available
        
        :return: a True or False which means is available or not
        """
        return self.available
    
    def get_checkin_timestamp(self):
        """Return when was the last checkin time
        
        :return: a timestamp when the book was checkin
        """
        return self.checkin_timestamp
    
    def set_available(self, available):
        """Set the available
        
        :param available: a True or False which means is available or not
        """
        self.available = available
    
    def set_checkin_timestamp(self):
        """Set checkin_timestamp"""
        self.checkin_timestamp = datetime.datetime.now().microsecond
    
    def set_rating(self, rating):
        """Set the rating
        
        :param rating: the rating of this book
        """
        self.rating = rating
