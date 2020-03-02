from setuptools import find_namespace_packages, setup

with open("README.md") as f:
    readme = f.read()

extras_require = {
    "test": [
        "coverage>=4.5.1",
        "isort>=4.3.4",
        "pylama>=7.6.5",
        "pytest",
        "tox>=3.5.2",
    ],
    "dev": ["pre-commit"],
}

extras_require["dev"] = extras_require["dev"] + extras_require["test"]

setup(
    name="home.denoising_signal",
    version="0.0.1",
    description="Denoise audio/speech signal",
    long_description=readme,
    author="Julien WEBER",
    author_email="julien.weber@home.fr",
    url="https://github.com/Tijuweb/denoising_signal",
    license=license,
    packages=find_namespace_packages(include=["home.*"]),
    install_requires=["numpy","SoundFile","scipy","matplotlib"],
    extras_require=extras_require,
    python_requires=">=3.5.*, <4",
)
