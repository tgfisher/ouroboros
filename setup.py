try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup
    from distutils.util import convert_path
    from pkgutil import walk_packages

    def find_packages(
        path=".",
    ):
        """
        A simple version of find_packages from setuptools.
        If setup tools import fails this will do the trick.
        """

        def _find_packages_iter(path):
            """
            Each dir at the level of setup.py is a potential top-level package.
            This function will drill down and yeild packages and subpackages. It is
            a simple version of setuptools.find_packages.
            """
            for _, dirs, _files in os.walk(path, followlinks=True):
                potential_toplevel_package = dirs[
                    :
                ]  # packages are directories with __init__.py files inside
                for ptp in potential_toplevel_package:
                    ptp_path = os.path.join(path, ptp)
                    # check toplevel is package
                    if os.path.isfile(os.path.join(ptp_path, "__init__.py")):
                        yield ptp
                        # dive in
                        for _file_finder, subpackage_name, is_package in walk_packages(
                            [ptp_path], ptp + "."
                        ):
                            if is_package:
                                yield subpackage_name

        return list(_find_packages_iter(convert_path(path)))


config = {
    "name": "ouroboros",
    "version": "0.1",
    "description": "This package is a 'template' and shows you what a package contains.",
    "author": "Grace, Gabe, Linnie and Tucker",
    "author_email": "wouldn't you like to know",
    "url": "https://github.com/tgfisher/ouroboros",
    "download_url": "https://github.com/tgfisher/ouroboros.git",
    "install_requires": ["numpy", "matplotlib"],
    "extras_require": {
        "dev": [
            "black", # linting
            "jupytext", # manage jupyter md and py files 
            "pillow", # python imaging library
        ],
    }, # pip install -e .[dev] OR pip install -e ".[dev]" (.[dev] in "" if you get an error)
    "packages": find_packages(),
    # manualy specify packages like this # "packages": [
    # manualy specify packages like this #     "ouroboros","ouroboros.new_package",
    # manualy specify packages like this # ],
    "scripts": ["./bin/template_hello_worlds.py"],
}

setup(**config)
