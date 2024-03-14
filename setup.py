from setuptools import setup, find_packages

NAME = "Orange3 Interactive Tree Builder"
DESCRIPTION = "HITL supported tree builder for Orange3"
VERSION = "0.0.2"
NAMESPACE_PACKAGES = ["orangehitl"]

PACKAGES = find_packages()


PACKAGE_DATA = {
    "orangehitl.main.widgets": ["icons/*"],
}

INSTALL_REQUIRES = [
    "Orange3",
]

ENTRY_POINTS = {
    "orange3.addon": [
        "interactive = orangehitl.interactive",
    ],
    "orange.widgets": [
        "Widgets = orangehitl.interactive.widgets",
    ],
}


if __name__ == "__main__":
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        packages=PACKAGES,
        package_data=PACKAGE_DATA,
        install_requires=INSTALL_REQUIRES,
        entry_points=ENTRY_POINTS,
        namespace_packages=NAMESPACE_PACKAGES,
        zip_safe=False,
    )
