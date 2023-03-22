python_distribution(
    name="whl",
    dependencies=["pkg/cmt:src@resolve=37", "pkg/cmt:src@resolve=310"],
    provides=python_artifact(
        name="cmt",
        author="Nikolai",
        version="0.0.1"
    ),
    # Example of setuptools config, other build backends may have other config.
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
    generate_setup=True,
    sdist=True,
)
python_requirements(name="reqs37", source="requirements-37.txt", resolve="37")

python_requirements(name="reqs310", source="requirements-310.txt", resolve="310")
