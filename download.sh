#!/bin/bash

set -e

VERSION=4.2.2

wget https://github.com/zeromq/libzmq/releases/download/v$VERSION/zeromq-$VERSION.tar.gz
tar xvf zeromq-$VERSION.tar.gz

cd zeromq-$VERSION

