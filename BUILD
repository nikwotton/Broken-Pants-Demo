python_requirements(
    name="requirements37",
    source="requirements-37.txt"
)

python_requirements(
    name="requirements38",
    source="requirements-38.txt"
)

# TODO: Idea to think through
# are resolves still needed? If python_tests has to define its constraints, can multiple tests with different constraints be in the same resolve?
# python_requirements is the issue - can't do constraints on that....right?
# Need the resolves, exclusively because pants won't parse the environment markers in the requirements files.

python_sources(name="source", sources=["my_file.py"], dependencies=[":requirements37", ":requirements38"], interpreter_constraints=["==3.8.15", "==3.10.8"])

python_tests(name="tests37", interpreter_constraints=["==3.10.8"])
python_tests(name="tests38", interpreter_constraints=["==3.8.15"])
