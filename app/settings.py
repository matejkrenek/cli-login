import os

BASE_DIR = os.path.dirname(__file__)
RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
TEMPLATES_DIR = os.path.join(RESOURCES_DIR, "templates")
ATTACHMENTS_DIR = os.path.join(RESOURCES_DIR, "attachments")

EMAILER = {

}

class STATUS:
    warning =  "\033[93m"
    error =  "\033[91m"
    success = "\033[92m"
    info =  "\033[94m"
