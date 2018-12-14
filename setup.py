#!/usr/bin/env python
from setuptools import setup


setup(name='collectd-iscdhcp',
      version='0.1.1',
      description='CollectD plugin for ISC DHCP',
      author='Jose Manuel Agudo',
      author_email='jagudo@gmail.com',
      url='https://github.com/jmagudo/collectd-iscdhcp',
      packages=[
        'collectd_iscdhcp',
      ],
      package_dir={'collectd_iscdhcp': 'collectd_iscdhcp'},
      keywords=['collectd-iscdhcp', 'collectd', 'isc', 'dhcp', 'metrics'],
      include_package_data=True,
      install_requires=[
          'collectd'
      ],
      )
