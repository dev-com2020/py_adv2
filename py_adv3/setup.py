import setuptools

pyc = setuptools.Extension('pyc', sources=['pyc.c'])
setuptools.setup(
    name='Pyc',
    version='1.0',
    ext_modules=[pyc],
)