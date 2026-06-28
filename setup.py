from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="need-for-speed-copperbelt",
    version="1.0.0",
    author="Your Name",
    description="A fun street racing game with police chases",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kapapala577-ux/CAR-RACING-ZED-TOP-SPEED",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "racing-game=racing_game:main",
            "racing-game-gui=gui_app:main",
        ],
    },
)
