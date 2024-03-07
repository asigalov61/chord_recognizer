from setuptools import setup, find_packages

setup(
    name='chords_recognizer',
    version='0.0.1',
    description='Working and installable chords_recognizer repo mirror copy',
    url='https://github.com/Yikai-Liao/chord_recognizer',
    author='Yikai Liao',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,  # This line includes data files specified in MANIFEST.in
    package_data={
    '': ['test_data'],  # Include all files under test_data directory
    },
    install_requires=[
        'mido',  # Add any other dependencies here
    ],
    zip_safe=False
)
