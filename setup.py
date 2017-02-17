#!/usr/bin/env python
from setuptools import setup


setup(name='collectd-iscdhcp',
      version='0.0.7',
      description='CollectD plugin for ISC DHCP',
      author='Jon Skarpeteig',
      author_email='jon.skarpeteig@gmail.com',
      url='https://github.com/Yuav/collectd-iscdhcp',
      packages=[
        'collectd_iscdhcp',
      ],
      scripts=['bin/dhcpd-pools'],
      package_dir={'collectd_iscdhcp': 'collectd_iscdhcp'},
      keywords=['collectd-iscdhcp', 'collectd', 'isc', 'dhcp', 'metrics'],
      include_package_data=True,
      install_requires=[
          'collectd'
      ],
      )
