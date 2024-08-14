from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader("html"))  # Load html folder
