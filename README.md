# Cookiecutter SAM for Python3.7 Lambda functions

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless App based on Serverless Application Model (SAM) and Python 3.6.

It is important to note that you should not try to `git clone` this project but use `cookiecutter` CLI instead as ``{{cookiecutter.project_slug}}`` will be rendered based on your input and therefore all variables and files will be rendered properly.

## Requirements

* AWS CLI with Administrator permission
* [Python 3 installed](https://www.python.org/downloads/)
* [Pipenv installed](https://github.com/pypa/pipenv)
    - `pip install pipenv`
* [Docker installed](https://www.docker.com/community-edition)
* [SAM Local installed](https://github.com/awslabs/aws-sam-local)

Python 2.7 will no longer be supported after 2019. It is suggested to use the most current version of Python, Python3.7, for all new Lambda functions.

# Cloning this repo

Once the dependencies are downloaded this repo can be cloned for a new project. To clone this project run the following command.

```bash
sam init \
--runtime python3.7 \
--output-dir $PWD \
--name sampleLambda \
--location git+ssh://git@github.com/aws-samples/cookiecutter-aws-sam-python.git
```

This will set up a new SAM (Serverless Application Model) with Python3.7 as the environment version, located in the current directory, and using this repo as a template for the project structure.


## Usage

Generate a new SAM based Serverless App:
`
sam init \                      
--runtime python3.7 \
--output-dir $PWD \
--name sampleLambda \
--location git+https://github.com/sewardgw/lambda-python37-template
`

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.
