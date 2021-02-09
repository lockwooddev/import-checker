import ast


class SetupParserException(Exception):
    pass


class SetupParser:
    """
    A parser using ast to parse install_requires contents
    """

    def __init__(self, target_file):
        self.target_file = target_file

    def parse(self):
        with open(self.target_file) as f:
            content = f.read()

        code = ast.parse(content)

        # build map of all List type variable assignments
        # lookup will be done in case of variable reference in setup(install_requires=)
        assignments = {}
        for el in code.body:
            # list assignment
            if isinstance(el, ast.Assign) and isinstance(el.value, ast.List):
                values = [e.value for e in el.value.elts]
                assignments[el.targets[0].id] = values

        for el in code.body:
            # find setup() and parse arguments for 'install_requires' arg
            if isinstance(el, ast.Expr) and el.value.func.id == 'setup':
                for keyword in el.value.keywords:
                    if keyword.arg == 'install_requires':
                        # reference to variable
                        if isinstance(keyword.value, ast.Name):
                            return assignments[keyword.value.id]
                        # return list values directly in case of list
                        if isinstance(keyword.value, ast.List):
                            return [e.value for e in keyword.value.elts]

        raise SetupParserException(
            'no parseable install_requires found in {0}'.format(self.target_file)
        )
