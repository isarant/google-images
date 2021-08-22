from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt','r') as f:
    install_requires=f.read().splitlines()

setup(
    name='google_images',
    version='0.1.0',
    description='A tool to downloda images from google images',
    long_description=readme,
    author='Giannis Sarantopoulos',
    author_email='ioansarant@yahoo.gr',
    keywords='google, image, download',
    #url='',
    license=license,
    python_requires='>=3.6, <4',
    #packages=find_packages(exclude=('tests', 'docs')),
    packages=find_packages(where='src'), 
    package_dir={'': 'src'},
    include_package_data = True,
    install_requires=install_requires,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3 :: Only',
    ]
)