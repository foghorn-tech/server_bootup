#!/bin/sh
src_dir=./src
build_dir=./build
file_name=tunnel_login
dest_dir=/usr/sbin/$file_name
rm -r $build_dir && \
	rm -r $dest_dir && \
usermod -s /bin/true tunnel
