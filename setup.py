from setuptools import setup, find_packages

setup(
    name="demo-jformat",
    version="0.0.1",
    description="Reformats files to stdout",
    install_requires = ["click", "colorama"],
    entry_points="""
    [console_scripts]
    jformat=jformat.main:main
    """,
    author="Shuran Xu",
    author_email="xushuran2012@gmail.com",
    packages=find_packages(),
)
