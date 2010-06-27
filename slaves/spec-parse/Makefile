# -*- makefile -*-

# This is a simple makefile which lives in a buildmaster/buildslave
# directory (next to the buildbot.tac file). It allows you to start/stop the
# master or slave by doing 'make start' or 'make stop'.

# The 'reconfig' target will tell a buildmaster to reload its config file.

start:
	twistd --no_save -y buildbot.tac

stop:
	if [ -e twistd.pid ]; \
	then kill `cat twistd.pid`; \
	else echo "Nothing to stop."; \
	fi

reconfig:
	if [ -e twistd.pid ]; \
	then kill -HUP `cat twistd.pid`; \
	else echo "Nothing to reconfig."; \
	fi

log:
	if [ -e twistd.log ]; \
	then tail -f twistd.log; \
	else echo "Nothing to tail."; \
	fi

ipfw:
	sudo ipfw pipe 1 config bw 450Kbit delay 60ms
	sudo ipfw pipe 2 config bw 1400Kbit delay 30ms
	sudo ipfw pipe 3 config bw 8000Kbit delay 10ms

normal: ipfw \
;	sudo ipfw flush -f

slow: normal \
;	sudo ipfw add 100 pipe 1 all from localhost to localhost

medium: normal \
;	sudo ipfw add 200 pipe 2 all from localhost to localhost

fast: normal \
;	sudo ipfw add 300 pipe 3 all from localhost to localhost

vnc: \
;	vncserver :1 \
||	echo ... but who cares

test: vnc \
;	pushd ../../talos \
;	DISPLAY=localhost:1 python run_tests.py --noisy spec-parse.config \
;	popd

show: \
;	sudo ipfw show
