"""A wrapper for sms-slang-translator"""

from setuptools import setup


setup(
    name='slang',
    version='1.0.0',
    description='A wrapper for sms-slang-translator',
    # url='https://github.com/FraBle/python-duckling',
    author='Qiu Junda (Amaris)',
    author_email='qiu.junda@amaris.ai',
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: Stable',
        'Intended Audience :: Amaris',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='slangs acronyms parser parsing nlp',
    packages=['slang'],
    install_requires=[],
    package_dir={'slang': 'slang'},
    include_package_data=False,
    zip_safe=False
)
