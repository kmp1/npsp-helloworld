from setuptools import setup

dependencies = [
    'numpy',
    'scipy',
    'Flask',
    'nose',
]

project_name = 'statstest01'
project_version = '0.7'
python_version = 'py2.7'

setup(
    name=project_name,
    version=project_version,
    author="Simon Parry",
    description=("A numpy/scipy hello-world example program"),
    license="UNKNOWN",
    install_requires=dependencies,
    classifiers=[
        "Development Status :: 2 - Beta",
    ],
    zip_safe=False,
)
