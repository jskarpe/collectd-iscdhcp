#!/usr/bin/env python

import collectd
import subprocess
import os
import json


def configure(conf):
        collectd.info('Configured with')


def read(data=None):
    vl = collectd.Values(type='gauge')
    vl.plugin = 'iscdhcp'

    out = subprocess.Popen(['dhcpd-pools', '-c', '/etc/dhcp/dhcpd.conf', '-f', 'j'], stdout=subprocess.PIPE).communicate()[0]
    j = json.loads(out)

    s = j['summary']
    vl.plugin_instance = 'All networks'
    vl.dispatch(type='count', type_instance='total',
                values=[s['defined']])
    vl.dispatch(type='count', type_instance='used',
                values=[s['used']])
    vl.dispatch(type='count', type_instance='free',
                values=[s['free']])
    used_percent = 100 * float(s['used']) / float(s['defined'])
    vl.dispatch(type='percent', type_instance='used_percent',
                values=[used_percent])
    free_percent = 100 * float(s['free']) / float(s['defined'])
    vl.dispatch(type='percent', type_instance='free_percent',
                values=[free_percent])

    for subnet in j['subnets']:
        vl.plugin_instance = subnet['range']
        vl.dispatch(type='count', type_instance='total',
                    values=[subnet['defined']])
        vl.dispatch(type='count', type_instance='used',
                    values=[subnet['used']])
        vl.dispatch(type='count', type_instance='free',
                    values=[subnet['free']])
        used_percent = 100 * float(subnet['used'])/float(subnet['defined'])
        vl.dispatch(type='percent', type_instance='used_percent',
                    values=[used_percent])
        free_percent = 100 * float(subnet['free']) / float(subnet['defined'])
        vl.dispatch(type='percent', type_instance='free_percent',
                    values=[free_percent])

    for sharednetwork in j['shared-networks']:
        vl.plugin_instance = sharednetwork['location']
        vl.dispatch(type='count', type_instance='total',
                    values=[sharednetwork['defined']])
        vl.dispatch(type='count', type_instance='used',
                    values=[sharednetwork['used']])
        vl.dispatch(type='count', type_instance='free',
                    values=[sharednetwork['free']])
        used_percent = 100 * float(sharednetwork['used'])/float(sharednetwork['defined'])
        vl.dispatch(type='percent', type_instance='used_percent',
                    values=[used_percent])
        free_percent = 100 * float(sharednetwork['free']) / float(sharednetwork['defined'])
        vl.dispatch(type='percent', type_instance='free_percent',
                    values=[free_percent])

collectd.register_config(configure)
collectd.register_read(read)
