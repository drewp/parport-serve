from setuptools import setup, find_packages

setup(name='parport_serve',
      version='1.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      scripts=['parport-serve'],
      install_requires=['twisted', 'BitVector', 'parallel'],
      )
