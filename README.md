# Github repo cloner

This project aims to provide a cloning repository ability inside an github organization.

## Getting Started

For now there is no installation script. You can clone the repository and take a look.

### Prerequisites

To install and run project you need to have pygithub==1.37 and Python 3.6.

### Installing

Make your own virtualenv:

```
cd ~/PythonVirtualEnvs
python3 -m venv cloner
source ~/PythonVirtualEnvs/pygithubrepocloner/bin/activate
```

Now you can execute clone.py script like so:
```
python3 clone.py --access_token XXXX --base_repository_name BaseRepo --new_repository_name NewRepo --organization_name OrganizationName
```

## License

This project is licensed under the MIT License.

## Contributing
Anyone who would like to contribute feel free to create PR.
