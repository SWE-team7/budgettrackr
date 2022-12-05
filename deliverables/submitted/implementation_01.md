# 1. Introduction
Our system provides a quick service of searching a product of choice followed 
by displaying - What the product is, price of product, rating of product, and 
number of ratings posted on said product. 

Link to whole system: [SWE-team7/budgettrackr](https://github.com/SWE-team7/budgettrackr)

# 2. Implemented requirements
Requirement: As an online shopper, I want an easy-to-use tool so that I can get the 
best prices on the things I purchase.

Issue: Online Shopper · Issue #3 · SWE-team7/budgettrackr (github.com)

Pull request: This solves issue #03 (As an online shopper, I want an easy-to-use to… 
by kylerc150 · [Pull Request #18 · SWE-team7/budgettrackr](https://github.com/SWE-team7/budgettrackr/pull/18)

Implemented by: Kyler Conant

Approved by: Akiel Aries

Print Screen: 

![](https://github.com/SWE-team7/budgettrackr/blob/sandbox/imgs/issue03.png)

Requirement: As a McDonald's manager, I want new chairs for my restaurant so that customers 
will be happy in the establishment.

Issue: https://github.com/SWE-team7/budgettrackr/issues/11 

Pull Request: https://github.com/SWE-team7/budgettrackr/pull/19 

Implemented by: Braedon Behnke

Approved by: Brandon Mack

Print Screen: 

![](https://github.com/SWE-team7/budgettrackr/blob/sandbox/imgs/issue18.png)

# 3. Tests
Currently our tests are minimal and implemented on pushes to our main branch. Our tests check for 
current versions, dependency installations, code style, among other minor things. Unit tests checking 
against our code more in depth are in current development.

# 4. Adopted Technologies
* Python 3 - A programming language which is very malleable and easy to use. Many plugins and adaptable 
measures to streamline the process of development. Also can be run in HTML.
* HTML 5 - A programming language designed to construct websites. Seeing as the service we aim to provide 
will be browser-based, an essential tool.
* CSS - Style functionality for HTML. Allows for more grandiose designs when running an HTML file through 
a browser. Grid is especially useful for sectioning the various elements we wish to webscrape.
* Py-Script - An HTML plugin which allows Python scripting within a webpage as opposed to Javascript. Allows 
us to use the greater Python language for increased development efficiency and complexity.
* Ubuntu 20.04 Web Server -  Hosted by Hostwinds as a way for us to develop a docker container within a linux 
environment. Keeps our program running and will be essential come time to provide a domain.
* Beautiful Soup - A Python library which is used to scrape data from HTML and XML elements. Necessary to gather 
pricing information from websites. 
* Flask - Python library for handling Python<->HTML integration and manipulation. 

# 5. Learning/training
The strategies employed by the team were making sure we definitely plan. Our plan included understanding what 
exactly we needed to make this product in fruition. Another part of our plan was researching what we need to 
connect the website to the data mining code, seeing how to test our code in github, and also finding easier ways 
to make our product shine. First we divided our product to see what people are okay with and what that they are 
strongest at. As of right now we have a low level website built and some data mining code to get some product 
information that is searched by the user. We also have been developing minimal tests as of right now.

The adopted technologies are intertwined with our strategy because we are using Python 3 to code this project. 
We are using HTML and CSS to develop our website connecting to our data mining code. We are using py-script 
instead of java script so we allow more python connecting code. We are also using a Ubuntu 20.04 web server 
to show this website is deployed and our code is working. Beautiful soup is used to data mine and get the data 
we need to search a product.

# 6. Deployment
We are utilizing Hostwinds Ubuntu 20.04 SSD server with a docker container in order to deploy our website. Hostwinds 
is also hosting our domain of budgettrackr.xyz. This deployed version is currently not hosted on the given URL instead on
its IP address. This deployment currently is not publically available as our program isn’t ready, however, the framework has 
been created and will be available as soon as our py-script can move values from the web scrape into our HTML elements.

View our deployed version here: http://192.129.136.171:5000

Docker instance: 
![](https://github.com/SWE-team7/budgettrackr/blob/sandbox/imgs/deployment_docker.png)

# 7. Licensing 
We have decided to adopt the MIT License as it is a very simple and permissive license which only requires license 
and copyright notice in our repository in order to allow for our work to be distributed, modified, and privately used.
see [here](https://github.com/SWE-team7/budgettrackr/blob/main/LICENSE) for details. 

# 8. README
Code of Conduct Link:
https://github.com/SWE-team7/budgettrackr/blob/main/CODE_OF_CONDUCT.md 

Contributing Link:
https://github.com/SWE-team7/budgettrackr/blob/main/CONTRIBUTING.md 

License Link:
https://github.com/SWE-team7/budgettrackr/blob/main/LICENSE 

Readme Link:
https://github.com/SWE-team7/budgettrackr/blob/main/README.md

# 9. Look & Feel
As of this Implementation, there are only two web pages, with a main page and a singular product page. Currently, the
main page is a simple homepage with a centered title and singular descriptive sentence. Below these is a note in 
place of a list or search bar which states that the image below links to the main centerpiece of development, the 
product page. The website will be using a dark purple color for the background and a bleached yellow accent to act 
as a more colorful dark mode.

![](https://github.com/SWE-team7/budgettrackr/blob/sandbox/imgs/look.png)

![](https://github.com/SWE-team7/budgettrackr/blob/sandbox/imgs/feel.png)

# 10. Lessons learned
The major problem we had with this iteration was preparation. We believed that the process of scraping and 
pasting text and other html data into another html page would be a simple process. Our first major hurdle was 
the fact that any activity Amazon (our number 1 target) when attempting to web scrape info was intercepted as 
bot activity and subsequently shut down. In order to get around this, Akiel had to find a way to spoof the 
machine into accepting him as a business account, thus he was no longer flagged as a bot. From here, beautiful 
soup took care of a lot of the Python binding, which was not a huge issue. Brandon then took over in designing 
the website using HTML and creating Py-Script variables which should have ideally fit into elements properly. 
A major issue arose here in that Brandon didn’t know how to spoof so testing was limited. Furthermore, we are 
still sorting out a major issue of the information not fitting so nicely into the HTML document as using class 
elements as a variable to pass into an HTML element. Our final major issue was the web server, which was not 
the correct kind and was only able to be rectified close to the deadline, thus full working deployment was out 
of reach.
For our next iteration, we need to meet a bit more frequently to iron out our team's issues ASAP. Also, get 
the other members involved in coding and implementation instead of two members passing the ball back-and-forth
intermittently. We also can’t assume that the next steps in achieving a viable product will fall into place 
like dominos after this first major hurdle and take our time fleshing out Implementation 2.

# 11. Demo
[See here](https://drive.google.com/file/d/1f1qwXQJSMBi49KCFnnM_SdSAW6DeAoJi/view?usp=sharing)
