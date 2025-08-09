from setuptools import setup

setup(
    name="png-expand",
    version="1.0.0",
    description="Simple PNG image expander - add padding around PNG images",
    py_modules=["png_expand"],
    python_requires=">=3.7",
    install_requires=["Pillow>=9.0.0"],
    entry_points={
        "console_scripts": [
            "png-expand=png_expand:main",
        ],
    },
)