from setuptools import setup
#-----> Este cod define como vamos a invocar a nuestra linea de comando

setup(
    name="pv",
    version="0.1",
    py_modules=["pv"],
    install_requires=[
        "Click",
        ],
    entry_points="""
        [console_scripts]
        pv=pv:cli
    """,
)
