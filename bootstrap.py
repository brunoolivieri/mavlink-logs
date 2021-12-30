
def mavtogpx_filepath():
    """Get mavtogpx script path."""
    return util.reltopdir("modules/mavlink/pymavlink/tools/mavtogpx.py")


def convert_gpx():
    """Convert any tlog files to GPX and KML."""
    mavlog = glob.glob(buildlogs_path("*.tlog"))
    passed = True
    for m in mavlog:
        util.run_cmd(mavtogpx_filepath() + " --nofixcheck " + m)
        gpx = m + '.gpx'
        kml = m + '.kml'
        try:
            util.run_cmd('gpsbabel -i gpx -f %s '
                         '-o kml,units=m,floating=1,extrude=1 -F %s' %
                         (gpx, kml))
        except subprocess.CalledProcessError:
            passed = False
        try:
            util.run_cmd('zip %s.kmz %s.kml' % (m, m))
        except subprocess.CalledProcessError:
            passed = False
        util.run_cmd("mavflightview.py --imagefile=%s.png %s" % (m, m))
    return passed
