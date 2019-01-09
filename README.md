# Cookiecutter SAM for Python3.7 Lambda functions

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless App based on Serverless Application Model (SAM) and Python 3.7.

## Requirements

* AWS CLI with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Pipenv installed](https://github.com/pypa/pipenv)
    - `pip install pipenv`
* [Docker installed](https://www.docker.com/community-edition)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local)

Python 2.7 will no longer be supported after 2019. It is suggested to use the most current version of Python, Python3.7, for all new Lambda functions.


## Usage

This will set up a new SAM (Serverless Application Model) with Python3.7 as the environment version, located in the current directory, and using this repo as a template for the project structure.

Generate a new SAM based Serverless App:
```
sam init \
--runtime python3.7 \
--output-dir $PWD \
--location https://github.com/sewardgw/lambda-python37-template
```

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.


```bash
project_name [Name of the project]: my-sample-lambda
project_short_description [A short description of the project]: "Just a short description"
```

To keep with Python Pep8 naming conventions, it is suggested to keep the project name all lower case and to only user underscores, not hyphens or spaces, in the project name.

If you have already executed this before you will be prompted to download the file again, you can choose yes or no for this.
