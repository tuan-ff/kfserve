# Copyright 2020 kubeflow.org.
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

import setuptools

TESTS_REQUIRES = [
    'pytest',
    'pytest-tornasync',
    'mypy'
]

setuptools.setup(
    name='kfserving',
    version='0.4.0',
    author="Kubeflow Authors",
    author_email='ellisbigelow@google.com, hejinchi@cn.ibm.com',
    license="Apache License Version 2.0",
    url="https://github.com/kubeflow/kfserving/python/kfserving",
    description="KFServing Python SDK",
    long_description="Python SDK for KFServing Server and Client.",
    python_requires='>=3.6',
    packages=[
        'kfserving',
        'kfserving.api',
        'kfserving.constants',
        'kfserving.models',
        'kfserving.handlers',
        'kfserving.utils',
    ],
    package_data={'': ['requirements.txt']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'certifi>=15.05.14',
        'six==1.15',
        'python_dateutil>=2.5.3',
        'setuptools>=21.0.0',
        'urllib3>=1.15.1',
        'kubernetes==10.0.1',
        'tornado>=6.0.0',
        'argparse>=1.4.0',
        'minio>=4.0.9',
        'google-cloud-storage>=1.31.0',
        'adal>=1.2.2',
        'table_logger>=0.3.5',
        'numpy>=1.17.3',
        'azure-storage-blob>=12.0.0',
    ],
    tests_require=TESTS_REQUIRES,
    extras_require={'test': TESTS_REQUIRES}
)
