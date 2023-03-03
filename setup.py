from setuptools import setup, find_packages

setup(
    name='mailer_wildfluss',
    version='0.0.1',
    author="Yakov Wildfluss",
    author_email='yakov@wildfluss.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/wildfluss/mailer',
)
