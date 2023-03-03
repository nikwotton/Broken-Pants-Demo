python_requirements(
    name="requirements37",
    source="requirements-37.txt",
    resolve="37python"
)

python_requirements(
    name="requirements38",
    source="requirements-38.txt",
    resolve="38python"
)

# TODO: Idea to think through
# are resolves still needed? If python_tests has to define its constraints, can multiple tests with different constraints be in the same resolve?
# python_requirements is the issue - can't do constraints on that....right?

python_sources(name="source", sources=["my_file.py"], resolve=parametrize("37python", "38python"), interpreter_constraints=["==3.8.15", "==3.10.8"])

python_tests(name="tests37", resolve="37python", interpreter_constraints=["==3.10.8"])
python_tests(name="tests38", resolve="38python", interpreter_constraints=["==3.8.15"])
