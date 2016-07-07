# Multitouch device related problems
# Author: Ara Pulido <ara@ubuntu.com>
# (C) 2010 Canonical Ltd.
# License: GPL v2 or later.

from glob import glob
from subprocess import Popen, PIPE
import sys
import apport.hookutils
import time
import os

# See linux/input.h
ABS_MT_POSITION_X = 0x35

# scan-for-mt-devices written by Marc Tardif, 
# based on a script by Henrik Rydberg
class Input(object):

    def __init__(self, path):
        self.path = path

    @property
    def device(self):
        base = os.path.basename(self.path)
        return os.path.join("/dev", "input", base)

    @property
    def name(self):
        path = os.path.join(self.path, "device", "name")
        return read_line(path)

    def get_capabilities(self):
        path = os.path.join(self.path, "device", "capabilities", "abs")
        line = read_line(path)
        capabilities = []
        long_bit = getconf("LONG_BIT")
        for i, word in enumerate(line.split(" ")):
            word = int(word, 16)
            subcapabilities = [bool(word & 1<<i) for i in range(long_bit)]
            capabilities[:0] = subcapabilities

        return capabilities

    def has_capability(self, capability):
        capabilities = self.get_capabilities()
        return len(capabilities) > capability and capabilities[capability]


def getconf(var):
    output = Popen(["getconf", var], stdout=PIPE).communicate()[0]
    return int(output)

def get_inputs(path):
    event_glob = os.path.join(path, "event*")
    for event_path in glob(event_glob):
        yield Input(event_path)

def read_line(path):
    f = open(path)
    try:
        return f.readline().strip()
    finally:
        f.close()

def scan_for_mt_devices(report):

    capability = ABS_MT_POSITION_X
    input = "/sys/class/input"

    inputs = get_inputs(input)
    inputs = [i for i in inputs if i.has_capability(capability)]

    report['MtDevices'] = ''

    if inputs:
        for input in inputs:
            report['MtDevices'] += "%s: %s\n" % (input.name, input.device)

        return 0
    else:
        report['MtDevices'] += "No capable devices found..."
        return 1

##################################

description = 'Multitouch device problem'
RELATED_PACKAGES = ['xserver-xorg', 'xserver-xorg-video-intel', 'xserver-xorg-video-ati', 'libmtdev1', 'libutouch-grail1', 'libutouch-geis1']


def add_info(report, ui):

    report.setdefault('Tags', '')
    report['Tags'] += ' hci touch'

    # Capture hardware
    apport.hookutils.attach_hardware(report)
    report['PciDisplay'] = apport.hookutils.pci_devices(apport.hookutils.PCI_DISPLAY)
    
    # Attach the results of scan mt devices
    scan_for_mt_devices(report)

    # Only collect the following data if X11 is available
    if os.environ.get('DISPLAY'):
        # For resolution/multi-head bugs
        report['Xrandr'] = apport.hookutils.command_output(['xrandr', '--verbose'])
        apport.hookutils.attach_file_if_exists(report,
                              os.path.expanduser('~/.config/monitors.xml'),
                              'monitors.xml')

    # Attach the Xorg logs and config    
    apport.hookutils.attach_file_if_exists(report, '/etc/X11/xorg.conf', 'XorgConf')
    apport.hookutils.attach_file(report, '/var/log/Xorg.0.log', 'XorgLog')
    apport.hookutils.attach_file_if_exists(report, '/var/log/Xorg.0.log.old', 'XorgLogOld')
    apport.hookutils.attach_file_if_exists(report, '/var/log/gdm/:0.log', 'GdmLog')
    apport.hookutils.attach_file_if_exists(report, '/var/log/gdm/:0.log.1', 'GdmLogOld')


    # Attach the output of xinput
    report['XInput'] = apport.hookutils.command_output(['xinput', 'input'])

    # Attach the output of lsinput
    report['LsInput'] = apport.hookutils.root_command_output(["lsinput"])

    # Attach descriptors
    attach_descriptors(report)

    apport.hookutils.attach_related_packages(report, RELATED_PACKAGES)

def attach_descriptors(report):
    path = '/sys/kernel/debug/hid/*/rdesc'
    for desc in glob(path):
        name = desc.split('/')[5]
        name = name.replace(":", "").replace(".", "")
        report[name] = apport.hookutils.root_command_output(["cat", desc])


