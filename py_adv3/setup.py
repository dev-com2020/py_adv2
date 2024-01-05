import setuptools

pyc = setuptools.Extension('pyc', sources=['pyc.c'])
setuptools.setup(
    name='Pyc',
    version='1.0',
    ext_modules=[pyc],
)

packages = setuptools.find_packages(exclude=['test', 'docs'])
entry_points = {
    'distutils.command': [
        'command_name = pakiet:Eggs',
    ],
    'console_scripts': [
        'eggs = pakiet:Eggs'
    ]
}
