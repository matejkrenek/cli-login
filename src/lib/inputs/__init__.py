from settings import STATUS
import re
import calendar 

print(calendar)

class Input():
    class Formats:
        email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    errors = {
        "bad_format": "Špatný formát"
    }

    def __init__(self):
        pass
    
    def Text(self, label, required = False):
        value = None

        if required:
            while value is None or value == "":

                if value == "":
                    print(STATUS.error + f"Toto pole je povinné" + "\033[0m")

                value = input(f'{label}')
        else: 
            value = input(f'{label}')

        return value

    def Email(self, label, required = False):
        value = None
        error = None

        if required:
            while value is None or value == "":

                if value == "":
                    print(STATUS.error + f"Toto pole je povinné" + "\033[0m")

                value = input(f'{label}')
        else: 
            value = input(f'{label}')

        if(not re.fullmatch(self.Formats.email, value)):
            error = "bad_format"
        
        if error:
            print(STATUS.error + f"{self.errors[error]}" + "\033[0m")
            return self.EmailList(label, True, separator = ",")

        return value

    def EmailList(self, label, required = False, separator = ","):
        value = None
        error = None

        if required:
            while value is None or value == "":

                if value == "":
                    print(STATUS.error + f"Toto pole je povinné" + "\033[0m")

                value = input(f'{label}')
        else: 
            value = input(f'{label}')

        value = value.replace(" ", "").split(separator)

        for val in value:
            if(not re.fullmatch(self.Formats.email, val)):
                error = "bad_format"

        if error:
            print(STATUS.error + f"{self.errors[error]}" + "\033[0m")
            return self.EmailList(label, True, separator = ",")

        return value

    def Path(self, label, required = False):
        value = None

        if required:
            while value is None or value == "":

                if value == "":
                    print(STATUS.error + f"Toto pole je povinné" + "\033[0m")

                value = input(f'{label}')
        else: 
            value = input(f'{label}')
        
        return value

    def PathList(self, label, required = False):
        value = None

        if required:
            while value is None or value == "":

                if value == "":
                    print(STATUS.error + f"Toto pole je povinné" + "\033[0m")

                value = input(f'{label}')
        else: 
            value = input(f'{label}')
        
        return value

            
    
