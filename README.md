# Python package example

This GitHub repository demonstrates how to create a Python package with a project structure that follows best practices,
including tox testing. The repository contains sample code, tests, and configuration files to help you get started.
Additionally, this package can be used as a private package that is installable directly from a GitHub repository.

This repository features a Flask application that showcases how to execute shell commands and retrieve their output. 
Although the application is straightforward and designed for demonstration purposes, the primary focus is on presenting best practices for structuring Python packages.

## Installation
It is possible to install a package directly from a GitHub repository without having to upload it to PyPI.

If the repository is public, you can install it using the command:

```
pip install git+https://github.com/<repository_owner>/<repository_name>.git
```

However, if you need to keep your code private - as is often the case - you can install it using the command:
```
pip install git+https://<username>:<access_token>@github.com/<repository_owner>/<repository_name>.git
```

Simply replace <username> with your GitHub username and <access_token> with a personal access token generated on GitHub 
with appropriate permissions to access the repository. Then, replace <repository_owner> with the username or 
organization that owns the repository and <repository_name> with the name of the repository itself.

## Development
```
# Clone the repository
git clone https://github.com/nnovovic/python_package.git

# Navigate to the project
cd python_package

# Install package in "editable" mode
pip install -e .

# Install tox
pip install tox

# Run tests with tox
tox
```