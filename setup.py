from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='echostatenetwork',
      version='0.1',
      description='tasks and objectives for neural networks in Python 3',
      author='Nathaniel Rodriguez',
      packages=['benchmarks'],
      url='https://github.com/Nathaniel-Rodriguez/benchmarks.git',
      install_requires=[
          'numpy'
      ],
      include_package_data=True)
