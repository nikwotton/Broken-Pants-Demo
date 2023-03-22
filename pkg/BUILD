python_distribution(
    name="whl37",
    dependencies=["pkg/cmt:src@resolve=37"],
    provides=python_artifact(
        name="cmt37",
        author="Nikolai",
        version="0.0.1"
    ),
    # Example of setuptools config, other build backends may have other config.
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
    generate_setup=True,
    sdist=True,
)
python_requirement(
    name="reqs37",
    resolve="37",
    requirements=["numpy >=1.16.2,<1.20; python_version == '3.7'"]
)
