# pkg-zmq
RPM packaging of ZeroMQ for Sailfish

To get the sources, run `download.sh`

To build and install:

```
export SFARCH=armv7hl
mb2 -t SailfishOS-$SFARCH -s ../rpm/zmq.spec build
sb2 -t SailfishOS-$SFARCH -m sdk-install -R rpm -i <INSERT-PATH>/libzmq*$SFARCH.rpm
```

