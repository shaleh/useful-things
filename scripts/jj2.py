import os
import sys

from jinja2 import Environment, FileSystemLoader
import yaml

if __name__ == "__main__":
    template_file = sys.argv[1]
    vars_file = sys.argv[2]

    with open(vars_file) as fp:
        variables = yaml.load(fp)

    print(variables)

    j2_env = Environment(trim_blocks=True)

    with open(template_file) as fp:
        template_data = fp.read()
        print(j2_env.from_string(template_data).render(variables))
