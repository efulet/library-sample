"""
Define the implementation for Genre.

Enums have been added to Python 3.4 as described in PEP 435. It has also been 
backported to 3.3, 3.2, 3.1, 2.7, 2.6, 2.5, and 2.4 on pypi.

Please install:
$> pip install enum34

@created_at 2015-05-16
@author Exequiel Fuentes Lettura <efulet@gmail.com>
"""


from enum import Enum


class Genre(Enum):
    """Genres to which books can belong. You're probably noticing that this 
    library has a limited selection. You're right."""
    
    NON_FICTION = 1
    GENERAL_FICTION = 2
    SCIENCE_FICTION = 3
    WESTERN = 4
