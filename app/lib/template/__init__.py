import os
from settings import TEMPLATES_DIR

class Template:
    path:str = None
    context:dict = {}

    def __init__(self, path:str = None, context:dict = {}) -> None:
        self.path = path
        self.context = context

    def get(self) -> str:
        template_path:str = os.path.join(TEMPLATES_DIR, self.path)

        if(not os.path.exists(template_path)):
            return False
        
        with open(template_path, "r") as file:
            return file.read()

    def render(self, context:dict = {}) -> str:
        template_context:dict = context

        if not template_context:
            template_context = self.context

        if not isinstance(template_context, dict):
            template_context = {}

        template_string:str = self.get()

        if not template_string:
            return ""

        return template_string.format(**template_context)
            