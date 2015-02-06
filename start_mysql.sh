#! /bin/bash
export DYLD_LIBRARY_PATH=/usr/local/mysql/lib:$DYLD_LIBRARY_PATH
cd /usr/local/mysql
./bin/mysqld_safe
