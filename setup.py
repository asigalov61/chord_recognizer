from setuptools import setup, find_packages
from glob import glob

setup(
    name='chords_recognizer',
    version='0.0.1',
    description='Working and installable chords_recognizer repo mirror copy',
    url='https://github.com/Yikai-Liao/chord_recognizer',
    author='Yikai Liao',
    author_email='your.email@example.com',
    license='MIT',
    packages=find_packages(),  # Automatically find all packages
    data_files=[
        ('target_directory', glob('test_data/*'))
    ],
    install_requires=[
        'mido',  # Add any other dependencies here
    ],
    zip_safe=False
)
