# CS386 Group Project (Group 7)

# budgettrackr
Budgettrackr is an open source tool enabling online shoppers to make an educated purchase on a given 
product by comparing listings across multiple sources. Budgettrackr allows users to view prices, 
descriptions, details, ratings, and amount of ratings to determine where they should purchase a product. 

# Getting Started
## Prerequisites
For python dependencies: 
```
# install pip (python pkg manager)
$ sudo apt install python3-pip

# verify install
$ pip --version

# install dependencies from requirements.txt
$ pip install -r requirements.txt
```
For docker installation you can follow your own installation guide or the one 
provided from [docker](https://docs.docker.com/engine/install/)(this is 
for ubuntu).

Linux-based users:
```
# use apt to install docker
$ sudo apt install docker.io
```

## Installing
The installation process is fairly minimal. It is a matter of having a server 
of some kind (we recommend a Linux-based server such as Ubuntu), installing 
the prerequisites correctly, and running the dockerfile for the project. This will
enable any user to run their own instance of budgettrackr also encouraging them to
make contributions to the project. 
```
# simply clone the repo
$ git clone git@github.com:SWE-team7/budgettrackr.git

# enter the budgettrack directory
$ cd budgettrack

# remove intermediate containers and assign name to container
$ sudo docker build --rm -t budgettrackr-dckr .
# run the application using the dockerfile
$ docker build -t budgettrackr-dckr .
```

## Built With
> * [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - library for scraping web data
> * [requests](https://pypi.org/project/requests/) - library for handling HTTP requests
> * [jinja2](https://pypi.org/project/Jinja2/) - formatting for console output
> * [Python HTTP-Server](https://docs.python.org/3/library/http.server.html) - publishing HTML to localhost
> * [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Integrating Python with HTML elements
See [requirements.txt](https://github.com/SWE-team7/budgettrackr/blob/main/requirements.txt). 

## Running the Tests
TODO

## Deployment
Budgettrackr is currently hosted on a Raspberry Pi 4 running Ubuntu LTS 22.04 
running in a Docker container. Our website is made with Flask 

# Contributing
Please refer to [CONTRIBUTING.md](https://github.com/SWE-team7/budgettrackr/blob/main/CONTRIBUTING.md) on how
to contribute to this project. 

# Versioning
We are using SemVer for our releases. Check out the [tags](https://github.com/SWE-team7/budgettrackr/tags) to see versions.

# Authors
Contributors:
> * Akiel Aries - *Data Mining, Back-End, Documentation, Integration* - [akielaries](https://github.com/akielaries)
> * Braedon Behnke - *Documentation, Planning* - [B-Man420](https://github.com/B-Man420)
> * Kyler Conant - *Documentation, Testing* - [kylerc150](https://github.com/kylerc150)
> * Brock Heinz - *Documentation* - [BrockHeinz](https://github.com/BrockHeinz)
> * Brandon Mack - *Front-End, SysAdmin* - [infinity3arc3](https://github.com/infinity3arc3)

See the list of contributors [here](https://github.com/SWE-team7/budgettrackr/blob/main/CONTRIBUTORS.md)

# License
Budgettracker adopts the MIT License, see [here](https://github.com/SWE-team7/budgettrackr/blob/main/LICENSE) for details. 

# Acknowledgements
> * budgettrackr contributors
> * Professor Marco Gerosa
