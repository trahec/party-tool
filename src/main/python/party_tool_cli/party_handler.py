# -*- coding: utf-8 -*-
from jinja2 import Environment, PackageLoader, select_autoescape, StrictUndefined


class PartyHandler():

    def __init__(self):
        self.env = Environment(
            loader=PackageLoader('party_tool_cli', 'party_templates'),
            autoescape=select_autoescape(['html', 'xml', 'yaml']),
            undefined=StrictUndefined
        )

    def create_party(self, config={}):

        if config['custom_party_dir'] is None:
            # load default party
            loaded_template = self.env.get_template("default_party.j2")
            rendered_template = loaded_template.render(**config)
            return rendered_template


