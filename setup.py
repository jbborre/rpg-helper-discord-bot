from setuptools import setup

setup(name='rpg-helper',
      version='1.0.0',
      description='Rpg Helper Bot For Discord',
      url='http://gitlab.com/jbborre/rpg-helper',
      author='Jonathan Borre',
      author_email='jbborre@gmail.com',
      license='MIT',
      packages=['rpg-helper'],
      install_requires=[
          'discord',
          'python-dotenv'
      ],
      zip_safe=False)