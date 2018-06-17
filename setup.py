from setuptools import setup

setup(
    name='masonite',
    packages=[
        'masonite',
        'masonite.auth',
        'masonite.facades',
        'masonite.providers',
        'masonite.commands',
        'masonite.drivers',
        'masonite.managers',
        'masonite.testsuite',
        'masonite.queues',
        'masonite.contracts',
        'masonite.helpers',
    ],
    version='2.0.3',
    install_requires=[
        'validator.py==1.2.5',
        'cryptography==2.2.2',
        'bcrypt==3.1.4',
        'requests==2.19.1',
        'tldextract==2.2.0',
        'Jinja2==2.10',
        'python-dotenv==0.8.2',
        'passlib==1.7.1',
        'whitenoise==3.3.1',
        'pytest==3.6.0',
        'orator==0.9.7',
        'masonite-entry>=0.0.0,<=0.9.99',
        'masonite-scheduler>=1.0.0,<=1.0.99',
        'pendulum==1.5.1',
        'cleo>=0.6,<=0.6.99',
        'tabulate==0.8.2',
        'watchdog==0.8.3',
        'waitress==1.1.0',
    ],
    description='The core for the Masonite framework',
    author='Joseph Mancuso',
    author_email='idmann509@gmail.com',
    url='https://github.com/MasoniteFramework/masonite',
    keywords=['python web framework', 'python3', 'masonite'],
    classifiers=[],
    include_package_data=True,
)
