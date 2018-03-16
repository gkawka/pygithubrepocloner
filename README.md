# Github repo cloner

This project aims to provide a cloning repository ability inside a GitHub organization.

## Getting Started

For now, there is no installation script. You can clone the repository and take a look.

### Prerequisites

To install and run the project you need to have pygithub==1.37 and Python 3.6.

### Example
You can execute clone.py script like so:
```
python3 clone.py --access_token XXXX --base_repository_name BaseRepo --new_repository_name NewRepo --organization_name OrganizationName
```

## License

This project is licensed under the GNU General Public License.

## Contributing
Feel free to create Pull Requests if you want to contribute. You can add more clone strategies by inheriting from `AbstractStrategy` and adding it to `Cloner` using `add_strategy` method.
