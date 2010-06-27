Before doing anything else, execute the command `make setup` from this
directory.  This will fetch the standalone talos suite and upgrade the
buildbot master database.

After that, you should be able to issue `make start` in both this
directory and the slaves/spec-parse subdirectory to start the buildbot
harness.  Visit http://localhost:8012 to access the web interface.

Miscellaneous dependencies are listed below.  Apologies for the
note-to-self quality of this list; email me at mozilla@benjamn.com if
you have questions.

vncserver
  - used by slaves/spec-parse/Makefile

ipfw3:
  - http://info.iet.unipi.it/~luigi/dummynet/
  - http://info.iet.unipi.it/~luigi/dummynet/README
  - slaves/spec-parse/Makefile
  - edit /etc/sudoers to allow buildbot slave user to invoke `sudo ipfw`

buildot:
  - http://hg.mozilla.org/build/buildbot/file/e14dab7788ad/README#l51

startup:
  - /etc/init.d/spec-parse
  - spec-parse.init.d.example
