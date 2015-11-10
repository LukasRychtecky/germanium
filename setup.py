from setuptools import setup, find_packages

setup(
    name='germanium',
    version='0.2.10',
    description='Helpful methods for Python Selenium and REST testing',
    author='Lukas Rychtecky, Lubos Matl',
    author_email='lukas.rychtecky@gmail.com, matllubos@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'django>=1.6',
        'django-selenium>=0.9.6',
        'PyVirtualDisplay>=0.1.2',
        'selenium>=2.37.2',
        'nose>=1.3.4',
        'django-nose>=1.3'
    ],
    include_package_data=True,
    zip_safe=False,
)
