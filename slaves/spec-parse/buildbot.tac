
import os

from twisted.application import service
from buildbot.slave.bot import BuildSlave

basedir = r'.'
rotateLength = 1000000
maxRotatedFiles = None

# if this is a relocatable tac file, get the directory containing the TAC
if basedir == '.':
    import os.path
    basedir = os.path.abspath(os.path.dirname(__file__))

application = service.Application('buildslave')
try:
  from twisted.python.logfile import LogFile
  from twisted.python.log import ILogObserver, FileLogObserver
  logfile = LogFile.fromFullPath(os.path.join(basedir, "twistd.log"), rotateLength=rotateLength,
                                 maxRotatedFiles=maxRotatedFiles)
  application.setComponent(ILogObserver, FileLogObserver(logfile).emit)
except ImportError:
  # probably not yet twisted 8.2.0 and beyond, can't set log yet
  pass

buildmaster_host = 'localhost'
port = 9900
slavename = 'spec-parse'
passwd = 'HowToMeetLadies5'
keepalive = 600
usepty = 0
umask = None
maxdelay = 300

s = BuildSlave(buildmaster_host, port, slavename, passwd, basedir,
               keepalive, usepty, umask=umask, maxdelay=maxdelay)
s.setServiceParent(application)

