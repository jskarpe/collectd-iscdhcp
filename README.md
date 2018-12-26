# collectd-iscdhcp

`collectd-iscdhcp` is a `collectd-python` plugin for pushing statistics
from the [dhcpd-pools](http://dhcpd-pools.sourceforge.net/) utility to
collectd.

## Installation

Requires `collectd-python` package. On Ubuntu 16.04,

    $ apt-get install collectd-python
    $ pip install collectd-iscdhcp

The configuration file (iscdhcp.conf) should be either placed in a
path that is included within collectd.conf, for e.g. if it there is a
line in collectd.conf such as -
``` Include "/etc/collectd/conf.d/*.conf" ```
then iscdhcp.conf should be placed in the managed_config folder.

Example configuration file    

# iscdhcp.conf
LoadPlugin python
<Plugin python>
    ModulePath "/usr/local/lib/python2.7/dist-packages"
    Interactive False
    Import "collectd_iscdhcp.collectd_plugin"
</Plugin>
