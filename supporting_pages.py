from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

template_env =  Environment(loader=FileSystemLoader(searchpath="./"))
template = template_env.get_template("homepage.html")

with open ("articles.md") as markdown_file:
    article = markdown(markdown_file.read())

with open("config.json") as config_file:
    config = load(config_file)


with open("first.html","w") as output_file:
    output_file.write(
        template.render(
            title = config["title"],
            article = article
         )
    )



    