class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_name(self, name):
        tmp = name.replace("-", " ")
        return tmp.capitalize()


    def _stringify_dependencies(self, dependencies):
        output = ""

        for item in dependencies:
            # <=, >= ja == loppuvat '=' merkkiin,
            # joten täytyy vain löytää viimeinen '='
            # ja vähentää indeksi yhdellä
            output = output + f"\n- {item[:item.rindex('=')-1]}"

        return output

    def _stringify_list(self, items, tag):
        output = ""

        for item in items:
            output = output + f"\n- {item[tag]}"

        return output


    def __str__(self):
        return (
            f"Name: {self._stringify_name(self.name)}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors: {self._stringify_list(self.authors, "name")}"
            f"\n\nDependencies:"
            f"\n- python"
            f"{self._stringify_dependencies(self.dependencies)}"
            f"\n\nDevelopment dependencies: {self._stringify_dependencies(self.dev_dependencies)}"
        )
