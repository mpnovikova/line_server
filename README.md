This project contains two different implementations of the LineServer problem:
* LineService uses caching mechanism to facilitate support of the large files and many concurrent users;
      This version worked just a tiny bit worce for small files with cache size being equal or larger than
      a size of a file loaded. This version started performing better (better availabily and concurrency) 
      than a basic version starting at ~300Mb. Unline basic version server continue to work while processing
      500Mb, 700Mb and 1Gb files. For generating large files I used 
      [Fake Apache Log Generator](https://github.com/kiritbasu/Fake-Apache-Log-Generator)
* LineServiceBasic is the naive implementation which places the entire file into memory upon reading. This 
      implementation was performing better for me on smaller files such as odyssey.txt ~ 600kB. However with 
      large enough files ~1Gb the server just wouldn't start because it was running out of memory 


# Prerequisites

* [Python 3.8](https://www.python.org/downloads/)
* [PyEnv](https://github.com/pyenv/pyenv)
* [git](https://git-scm.com/downloads)
* [flask](http://flask.pocoo.org/)


# Installation

To install requirements in a virtual environment begin by running 

    $ ./install.sh

# Running
To start this application, run 

    $ ./run.sh
     * Running on http://127.0.0.1:5000/
     
# Access
 
    GET http://127.0.0.1:5000/lines/<line_id> 


# Deinstallation

To install requirements in a virtual environment begin by running 

    $ ./uninstall.sh

Then remove the project folder