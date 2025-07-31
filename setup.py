from setuptools import setup, find_packages

setup(
    name='aniplot',
    version='0.1.0',
    author='Scott Payseur',
    author_email='scott.payseur.phd@example.com',
    description='A simple object-oriented animation plotting library for matplotlib',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/payseur/aniplot',  # Replace with your actual GitHub repo
    packages=find_packages(),
    install_requires=[
        'matplotlib>=3.0',
        'numpy>=1.18'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.7',
)
