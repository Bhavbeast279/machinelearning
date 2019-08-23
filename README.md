# Templates for Machine Learning and Computer Vision Projects

This week-long program introduces a number of projects related to computer vision and machine learning using Python and JavaScript. 

This repository will be updated as week progresses.

Inital setup is

```
pipenv install
```

This will install all requirements for the projects in a new Python virtual environment.

Then activate the virtual environment with

```
pipenv shell
```

## Installation on a new computer

We are using Python 3.7.4, P5.js, VS Code, Git for Windows, and Github Desktop. The repository contains a number of template files that include p5.js and other dependencies. Python dependencies are managed with Pipenv.

Download links:
* [Python 3.7.4](https://www.python.org/downloads/)
* [VS Code](https://code.visualstudio.com/Download)
* [Git for Windows](https://gitforwindows.org/)
* [Github Desktop](https://desktop.github.com/)

## Installation Steps:

**Python 3.7**

Install Python 3.7 64 bit version. Make sure to add the Python installation directory to the system Path during installation.

**Windows Prerequisites for face_recognition and dlib**
* Install [CMake](https://cmake.org/download) and add to the system path.
* Install Visual Studio
* Select "Desktop development with C++" during installation

**Mac Prerequisites**
```
pip install cmake
```

**VS Code**

Select default shell. Ctrl-Shift-P, select default shell, choose bash. Open a terminal and run these commands:

Install pipenv

``` 
pip install pipenv 
```

Clone this git repository

``` 
git clone https://github.com/holyokecodes/ML-CV-Templates.git 
```

Change to the new directory

``` 
cd ML-CV-Templates 
```

Make a New Github Repo on Github.com

Setup Origin and Upstream
```
git remote remove origin
git remote add origin YOUR_GITHUB_REPO_URL.git

git remote add upstream https://github.com/holyokecodes/ML-CV-Templates.git
```

Install dependencies

``` 
pipenv install 
```

Activate Python virtual environment

``` 
pipenv shell 
```

Install NLTK data
```
python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
exit()
```
