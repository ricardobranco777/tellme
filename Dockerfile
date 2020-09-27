FROM	python:3.8-alpine

COPY    requirements.txt /tmp

RUN	apk add --no-cache tzdata && \
        pip install --no-cache-dir -r /tmp/requirements.txt

RUN	adduser -D user -h /user

COPY	tellme /
RUN	python -OO -m compileall && \
	python -OO -m compileall /*.py

COPY	SUSE_Trust_Root.crt /usr/local/share/ca-certificates/
RUN	update-ca-certificates

ENV     PYTHONPATH /
ENV	PYTHONUNBUFFERED 1

WORKDIR	/user

USER	user
ENTRYPOINT ["/usr/local/bin/python3", "/tellme"]
