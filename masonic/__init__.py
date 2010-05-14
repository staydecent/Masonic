import os
import re
import markdown
import yaml

from mako.template import Template

class Build(object):

    def __init__(self, source, destination, layouts):
        """Build pages from source+layouts into destination"""
        for root, dirs, files in os.walk(source):
            for name in files:
                content = open( os.path.join(root, name) ).read()
                # Iterate yaml front matter
                for config in yaml.load_all(content):
                    if type(config) is dict:
                        layout = Template(filename=os.path.join(layouts, config['layout']+".html"))
                        pieces = re.split("---\n", content) # expect [blank, yaml, content]
                        html = markdown.markdown(pieces[2])
                        # Save page
                        page = open(os.path.join(destination, name), 'w')
                        page.write(layout.render(data=config, content=html))
                        page.close()


    def utilpages(self):
        """
        Generated utility pages:
            Tags, list of content pages with same tag.
        """
        print "Nada"


    def deploy(self):
        print "Deployed!"