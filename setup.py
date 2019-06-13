from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='ccypher',
      version='0.1',
      description='Graphic user interface to encrypt or decrypt text.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Filters',
        ],
      keywords='ccypher cypher encrypt decrypt text casear caesarcypher',
      url='https://github.com/iwkerr/ccypher.git',
      author='IK',
      author_email='iwkerr48@gmail.com',
      license='MIT',
      packages=['ccypher'],
      install_requires=[
          'pyperclip', 'tkinter',
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      scripts=['bin/ccypher'],
      zip_safe=False)
