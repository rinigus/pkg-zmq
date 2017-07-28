Summary: The ZeroMQ lightweight messaging kernel
Name: libzmq
Version: 4.2.2
Release: 1%{?dist}
License: LGPL
Group: Libraries/Network
URL: zeromq.org

#Source: https://github.com/zeromq/libzmq/releases/download/v4.2.2/zeromq-4.2.2.tar.gz
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc libtool

%description
The ZeroMQ lightweight messaging kernel is a library which extends the standard socket interfaces with features traditionally provided by specialised messaging middleware products. ZeroMQ sockets provide an abstraction of asynchronous message queues, multiple messaging patterns, message filtering (subscriptions), seamless access to multiple transport protocols and more.

%package devel
Summary: ZeroMQ development headers
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package provides headers for development


%package tools
Summary: ZeroMQ tools
Group: Libraries/Network
Requires: %{name} = %{version}

%description tools
The package provides command line tools to test basic operations of ZeroMQ

%prep
%setup -q -n %{name}-%{version}/libzmq

%build
%{__make} clean || true

./autogen.sh

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure --enable-static

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%pre

%post -n libzmq -p /sbin/ldconfig

%postun -n libzmq -p /sbin/ldconfig

%files
%files
%defattr(-, root, root, 0755)
%{_libdir}/libzmq.so*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/zmq.h
%{_includedir}/zmq_utils.h
%{_libdir}/libzmq.a
%{_libdir}/libzmq.la
%{_libdir}/pkgconfig/libzmq.pc
#%{_mandir}/man3/*
#%{_mandir}/man7/*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/curve_keygen

%changelog
* Mon May 15 2017 rinigus <rinigus.git@gmail.com> - 4.2.2-1
- initial packaging release for SFOS
