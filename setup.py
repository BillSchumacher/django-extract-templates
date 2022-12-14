from os.path import exists
from setuptools import setup


setup(
    name='django-extract-templates',
    author="Bill Schumacher",
    author_email="34168009+BillSchumacher@users.noreply.github.com",
    entry_points={
        'console_scripts': [
            'extract_templates = extract_templates:run',
        ],
      },
    scripts=[
        'extract_templates.py',
    ],
    url="https://github.com/BillSchumacher/django-extract-templates",
    license="MIT",
    description="Extracts Django's built-in templates and statics.",
    long_description=open("README.md").read() if exists("README.md") else "",
    long_description_content_type='text/markdown',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
    ],
    version="0.1.1",
    zip_safe=False,
)