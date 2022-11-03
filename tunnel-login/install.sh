#!/bin/sh
src_dir=./src
build_dir=./build
file_name=tunnel_login
dest_dir=/usr/sbin/$file_name
rm -rf $build_dir && \
	mkdir -p $file_name $build_dir && \
	echo "unsigned char pycode[] = {$(xxd -i - < $src_dir/${file_name}.py), 0x0};
	size_t pycode_len = sizeof(pycode);" > $build_dir/pyscript.h && \
	g++ $src_dir/python.cpp -I$build_dir -o $build_dir/$file_name && \
	chown -R root:tunnel $build_dir/ && \
	chmod 750 $build_dir/$file_name && \
	chmod u+s $build_dir/$file_name && \
	rm -rf $dest_dir && \
	cp -p -r $build_dir $dest_dir && \
usermod -s $dest_dir/$file_name tunnel
