from setuptools import setup, find_packages

setup(
    name="jokerai",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Clinical analysis dependencies
        'numpy>=1.21',
        'pytest>=7.0'
    ],
    # Forensic metadata
    author="Arkham Clinical Research",
    description="Pathological cognition simulation framework",
    license="GPL-3.0 (Gotham Public License)",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Psychology :: Psychopathology"
    ]
)
