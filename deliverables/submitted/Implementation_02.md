# 1. Introduction

Our program will lead you to a website that will compare prices among different
websites with competitive prices. This will help you easily find any product with 
one click of a button. Once this button is clicked you will be able to compare 
prices across all big vendors. Giving the ease of search and taking time back to 
a whole other level!

Our program's main features are a selenium bot search to help scrape a web page 
and giving us information necessary to compare against other websites. A connection 
between docker and the bot to give us a website display. We have our search bar 
that will take in a search value and display exactly what we are looking for. Added 
to that we should be able to see graphs of prices going up and down within the year. 

Link: [SWE-team7/budgettrackr: Educated Purchasing Tool](https://github.com/SWE-team7/budgettrackr)

#2. Implemented Requirements

Requirement: Working website HTML that is easy to use, takes all inputs, and is more 
professionally designed.
Issue: 25. Overhaul Website HTML pages
Pull request: https://github.com/SWE-team7/budgettrackr/pull/26 
Implemented by: Brandon Mack
Approved by: Akiel Aries

Requirement: Selenium Bot which successfully scrapes from Amazon
Issue: 32. Needs working scraper bot
Pull request: https://github.com/SWE-team7/budgettrackr/pull/24 
Implemented by: Kyler Conant
Approved by: Akiel Aries

Requirement: Implementing docker, tests, and other toolsets
Issue: N/A
Pull request: https://github.com/SWE-team7/budgettrackr/pull/30 
Implemented by: Akiel Aries
Approved by: Kyler Conant

Requirement: Unit Tests
Issue: N/A
Pull request: https://github.com/SWE-team7/budgettrackr/pull/28 
Implemented by: Akiel Aries
Approved by: Akiel Aries

Requirement: Reformatting Sandbox
Issue: N/A
Pull request: https://github.com/SWE-team7/budgettrackr/pull/31 
Implemented by: Akiel Aries
Approved by: Akiel Aries

Requirement: Progress on dynamic search bar and tying it to the web scraping bot.
Issue: 27. Implement Search Bar
Pull request: https://github.com/SWE-team7/budgettrackr/pull/29 
Implemented by: Braedon Behnke
Approved by: Akiel Aries

# 3. Tests

Tests for budgettrackr are performed using Python’s unittest framework. The use 
of github actions is also seen within our repo by running a dockerfile that 
takes care of performing our unit tests execution then allowing our build to 
execute allowing for a 2 in 1 test. Running the tests manually within our project 
can be done using python3 -m unittest tests/. 
https://github.com/SWE-team7/budgettrackr/tree/main/tests

Github action that confirms our project Dockerfile builds. Within the Dockerfile 
we install our dependencies as specified in the requirements.txt files, run the 
unittests specified in the tests/ directory, and finally build our Flask-based 
application by running the main.py driver file. This tests/test_scrape.py files 
tests the functionality of our product class seen in the src/scrape.py files 
ensuring testable values are parsed correctly:
https://github.com/SWE-team7/budgettrackr/blob/sandbox/tests/test_scrape.py (tests 
this class https://github.com/SWE-team7/budgettrackr/blob/main/src/scrape.py)

# 4. Demo

Selenium Bot Running Example: 
[Download Here](https://github.com/SWE-team7/budgettrackr/blob/D6/imgs/Selenium.mp4)

# 5. Code Quality

Our best method for creating and maintaining high-quality code was to follow the 
PEP 8 style guide for Python to give us our code conventions.  This helped us in 
making sure that we were all able to understand the code written in our project, 
regardless of who produced it.  We also used a General Usage Rubric from another 
course to further help with creating good code, such as usage of self-documenting 
variables, not repeating any constants in our code, limiting the number of characters 
we can have on a single line of code, etc.

PEP 8 Style Guide: https://peps.python.org/pep-0008/ 

[Hocking Deep Learning in Python General Usage Rubric](https://docs.google.com/document/d/1UAxnf2QSebCQYKQiqmfyfOunsqIVD-2-OAoi-DG9F8s/edit#heading=h.pekgvy78tviz)

# 6. Lessons Learned

The biggest lesson learned when implementing our search bar feature was to make sure 
contributing members had a firm understanding both of how each individual file worked 
as well as how to make each part of the code properly interact with each other as the home 
page needed to take an input, then pass it on to the product page which would take the input 
and pass it as an argument to the Selenium Bot used to scrape the required information, 
which would be returned to the product page and printed.  This did not result in a major 
issue when implementing, as we were able to quickly consult other members about how the code 
worked and how to implement features when we were unsure of what to do, though it would have 
been a much more difficult task had we not been able to communicate properly.

One thing we would do differently as a group if we were to continue this project or restart 
our work on the project would be to better familiarize ourselves with the frameworks we will 
be using and to begin implementation of features earlier in the process as some of our 
planned features turned out to be more complex and difficult to implement than first 
anticipated.

