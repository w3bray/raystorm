from distutils.core import setup

setup(
    name="raystorm",
    py_modules=["raystorm"],
    entry_points={"console_scripts": ["raystorm=raystorm:main"]},
    version="0.2.6",
    description="Low bandwidth DoS tool. Raystorm rewrite in Python.",
    author="w3b_ray",
    author_email="jejajnejejs@gmail.com",
    url="https://github.com/w3bray/raystorm",
    keywords=["dos", "http", "raystorm"],
    license="MIT",
)