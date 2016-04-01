# pylint: disable=missing-docstring
# Copyright (c) 2016 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup, find_packages

setup(
    name='demiurge',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'awacs',
        'boto3',
        'click',
        'connexion',
        'fauxfactory',
        'Flask-HTTPAuth',
        'troposphere',
        ],
    author='Maciej Strzelecki',
    author_email='maciej.strzelecki@intel.com',
    license='Apache License, Version 2.0',
    entry_points={
        'console_scripts': [
            'demiurge = demiurge.cli:cli',
            ],
        },
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 colorcolumn=100
