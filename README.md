# Welcome to Coding Exercise - Library problem

This is a coding exercise example.

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


## Requirements

* Python (https://www.python.org/)

* setuptools (http://pypi.python.org/pypi/setuptools)
```bash
    $> wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
```

* pip (https://pip.pypa.io/en/latest/installing.html)
```bash
    $> sudo easy_install pip
```

* virtualenvwrapper (http://virtualenvwrapper.readthedocs.org/)
```bash
    $> sudo pip install virtualenvwrapper
```


## Configure

virtualenv tool has become the de-facto standard mechanism for isolating Python 
environments. Install virtualenvwrapper for starting a new project. Run:
```bash
    $> mkvirtualenv library
```

Install requirements for this project:

* Enum
```bash
    $> pip install enum34
```

* Sphinx (http://sphinx-doc.org/index.html)
```bash
    $> pip install Sphinx
```

* Coverage.py (http://nedbatchelder.com/code/coverage/)
```bash
    $> pip install pytest-cov
```

Update requirements.txt. The following command list of all of the requirements 
for your project, which can later be used by the setup.py file to list your 
dependencies.


```bash
    $> pip freeze > requirements.txt
```


## Run

Print program options:
```bash
    $> bin/library.sh
```
