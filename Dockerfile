FROM	python:3.8-alpine

COPY    requirements.txt /tmp

RUN	apk add --no-cache tzdata && \
        pip install --no-cache-dir -r /tmp/requirements.txt

RUN	adduser -D user -h /user

COPY	*.py /
RUN	python -OO -m compileall && \
	python -OO -m compileall /*.py

ENV     PYTHONPATH /
ENV	PYTHONUNBUFFERED 1
ENV	DBUS_SESSION_BUS_ADDRESS /dev/null

WORKDIR	/user

USER	user
ENTRYPOINT ["/usr/local/bin/python3", "/tellme.py"]
