# party-tool

A command line tool, to help you party!

Had a funny dream and decided to throw this together.. literally no real need or use ;)

## Getting Started

### Prerequisites

* virtualenv installed `pip install virtualenv`
* python setup.py
* export PYTHONPATH=$(pyb print_module_path -Q | tail -n1)
* export PATH=$(pyb -Q print_scripts_path | tail -n1):$PATH

### Usage

Run the tool by providing a name for your party and see what appears!

```
Usage: party-tool create [OPTIONS]

Options:
  --name TEXT          Name of your party  [required]
  --custom-party TEXT  path to directory which contains files for a custom
                       party                    If you do not set this, you

                       will enjoy our default party!
  --help               Show this message and exit.
```

## Built With

* [click](http://click.pocoo.org/) - Command Line Parser
* [pybuilder](https://github.com/pybuilder/pybuilder) - Dependency Management
* [jinja2](http://jinja.pocoo.org) - Template Engine

## Authors

* **Christine Trahe** - *Initial work* - [ctrahe](https://github.com/trahec)

See also the list of [contributors]() *to be added*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
