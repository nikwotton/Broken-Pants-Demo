python_requirements(
    name="reqs0",
)

python_sources(
    name="root",
)

resource(name="pyproject", source="pyproject.toml")
python_distribution(
    name="whl",
    dependencies=[
        ":pyproject",
        ":reqs0",
        ":root",
    ],
    provides=python_artifact(
        name="whl",
        version="2.21.0",# TODO
    ),
    # Example of setuptools config, other build backends may have other config.
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
    # Don't use setuptools with a generated setup.py.
    # You can also turn this off globally in pants.toml:
    #
    # [setup-py-generation]
    # generate_setup_default = false
    generate_setup = True,
    sdist = True
)

python_tests(
    name="tests0",
    dependencies=[":reqs0"]
)
