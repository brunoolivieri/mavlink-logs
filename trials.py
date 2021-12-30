#!/usr/bin/env python3
"""
Heavily based on ArduPilot automatic test suite.

"""

import glob
import optparse
import os
import re
import shutil
import subprocess
import sys
import time
import traceback

from pymavlink import mavutil
from pymavlink.generator import mavtemplate



def cmd_as_shell(cmd):
    return (" ".join(['"%s"' % x for x in cmd]))

def run_cmd(cmd, directory=".", show=True, output=False, checkfail=True):
    """Run a shell command."""
    shell = False
    if not isinstance(cmd, list):
        cmd = [cmd]
        shell = True
    if show:
        print("Running: (%s) in (%s)" % (cmd_as_shell(cmd), directory,))
    if output:
        return subprocess.Popen(cmd, shell=shell, stdout=subprocess.PIPE, cwd=directory).communicate()[0]
    elif checkfail:
        return subprocess.check_call(cmd, shell=shell, cwd=directory)
    else:
        return subprocess.call(cmd, shell=shell, cwd=directory)

def mavtogpx_filepath():
    """Get mavtogpx script path."""
    #return util.reltopdir("../ardupilot/modules/mavlink/pymavlink/tools/mavtogpx.py")
    return "../ardupilot/modules/mavlink/pymavlink/tools/mavtogpx.py"

def convert_tlog_files():
    """Convert any tlog files to GPX,  KML, KMZ and PNG."""
    mavlog = glob.glob("./sample-tlogs/*.tlog")
    passed = True
    for m in mavlog:
        run_cmd(mavtogpx_filepath() + " --nofixcheck " + m)
        gpx = m + '.gpx'
        kml = m + '.kml'
        try:
            run_cmd('gpsbabel -i gpx -f %s '
                         '-o kml,units=m,floating=1,extrude=1 -F %s' %
                         (gpx, kml))
        except subprocess.CalledProcessError:
            passed = False
        try:
            run_cmd('zip %s.kmz %s.kml' % (m, m))
        except subprocess.CalledProcessError:
            passed = False
        run_cmd("../MAVProxy/MAVProxy/tools/mavflightview.py --imagefile=%s.png %s" % (m, m))
    return passed


def convert_bin_files():
    # remember do add --no-flightmode-legend

    return passed

print("Starting")
convert_tlog_files()
#convert_bin_files():
