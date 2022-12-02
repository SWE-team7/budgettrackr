![html](https://github.com/SWE-team7/budgettrackr/actions/workflows/valid-html.yml/badge.svg)
![deps](https://github.com/SWE-team7/budgettrackr/actions/workflows/deps.yml/badge.svg)
![build](https://github.com/SWE-team7/budgettrackr/actions/workflows/build.yml/badge.svg)
![test](https://github.com/SWE-team7/budgettrackr/actions/workflows/unittest.yml/badge.svg)

# CS386 Group Project (Group 7)

# budgettrackr
Budgettrackr is an open source tool enabling online shoppers to make an educated purchase on a given 
product by comparing listings across multiple sources. Budgettrackr allows users to view prices, 
descriptions, details, ratings, and amount of ratings to determine where they should purchase a product. 

# Getting Started
## Prerequisites
When running this project with Docker, dependencies other than the container
application itself, will be taken care of. 
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
provided from [docker](https://docs.docker.com/engine/install/) (this is 
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
# build the docker container using the dockerfile
$ docker build -t budgettrackr-dckr .
# run the image using the built container
$ docker run -d -p 5000:5000 budgettrackr-dckr
# list containers
$ docker ps
```
And the container is now ready to see at `localhost:5000/`

Budgettrackr is currently deployed at http://192.129.136.171:5000

To remove the built container + images run:
```
# find the hash of the docker container
$ docker ps
# remove container
$ docker rm -f <container_hash>
# find image hash
$ docker images
# remove the image 
$ docker image rm -f <image_hash>
```

## Built With
> * [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) - library for scraping web data
> * [requests](https://pypi.org/project/requests/) - library for handling HTTP requests
> * [jinja2](https://pypi.org/project/Jinja2/) - formatting for console output
> * [Python HTTP-Server](https://docs.python.org/3/library/http.server.html) - publishing HTML to localhost
> * [Flask](https://flask.palletsprojects.com/en/2.2.x/) - Integrating Python with HTML elements

See [requirements.txt](https://github.com/SWE-team7/budgettrackr/blob/main/requirements.txt). 

## Running the Tests

### Repository Checks
Currently our tests our minimal and implemented on pushes to our main branch. 
Our tests check for current versions, dependency installations, code style, among other 
minor things. Unit tests checking against our code more in depth are in current development.

The following actions are ran against the project upon every push or pull request made to the `main` or `sandbox` branches.
> * [Proof HTML](https://github.com/SWE-team7/budgettrackr/blob/sandbox/.github/workflows/proof-html.yml): confirms
our HTML in the repo is valid.
> * [Setup Python Dependencies](https://github.com/SWE-team7/budgettrackr/blob/sandbox/.github/workflows/deps.yml): confirms the
dependencies of our project work correctly.
> * [Build](https://github.com/SWE-team7/budgettrackr/blob/sandbox/.github/workflows/build.yml): Confirms our project builds by 
running the Dockerfile of our project
is working. 
> * See the workflow actions in place [here](https://github.com/SWE-team7/budgettrackr/tree/sandbox/.github).

### Unit Tests
* Our unit tests are ran automatically when changes are made to the budgettrackr repository. 
To run the unit tests yourself, clone the repo and enter the repository's root directory, and
run every test with `python -m unittest tests/`
* All Python code is checked before pushed to a branch with autopep8.
    * `autopep8 --in-place --aggressive --aggressive <filename>`

## Deployment
Budgettrackr is currently hosted on a hostwinds server running Ubuntu SMP
running in a Docker container. Our website is made with Flask 

# Contributing
Please refer to [CONTRIBUTING.md](https://github.com/SWE-team7/budgettrackr/blob/main/CONTRIBUTING.md) on how
to contribute to this project. 

# Versioning
We are using SemVer for our releases. Check out the [tags](https://github.com/SWE-team7/budgettrackr/tags) to see versions.

# Authors
Contributors:
> * Akiel Aries - *Data Mining, Back-End, Documentation, Integration, Deployment, Deliverables* - [akielaries](https://github.com/akielaries)
> * Braedon Behnke - *Documentation, Planning, Deliverables* - [B-Man420](https://github.com/B-Man420)
> * Kyler Conant - *Documentation, Testing, Deliverables* - [kylerc150](https://github.com/kylerc150)
> * Brock Heinz - [BrockHeinz](https://github.com/BrockHeinz)
> * Brandon Mack - *Front-End, Deployment, SysOps, Deliverables* - [infinity3arc3](https://github.com/infinity3arc3)

See the list of contributors [here](https://github.com/SWE-team7/budgettrackr/blob/main/CONTRIBUTORS.md)

# License
Budgettracker adopts the MIT License, see [here](https://github.com/SWE-team7/budgettrackr/blob/main/LICENSE) for details. 

# Acknowledgements
> * budgettrackr contributors
> * Professor Marco Gerosa

