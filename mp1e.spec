%define name	mp1e
%define version	1.9.9
%define snapshot 20060612
%define rel	4
%define release 0.%snapshot.%rel

Name: %{name}
Version: %{version}
Release: %mkrel %{release}
Summary: Real Time Software MPEG-1 Video/Audio Encoder
License: GPL
Group: Video

# There are no mp1e standalone releases made currently, so we have to use
# snapshots from CVS of zapping project.
# The code is contained in rte/mp1e, but context.h, codec.h, rte.h, option.h
# and rtepriv.h have to be copied from rte/src to mp1e/rte for a standalone
# mp1e build.
Source: %{name}-%{snapshot}.tar.bz2
Source1: README-aiw
Patch1: mp1e-1.9.8-aiw.patch.bz2
Patch2: mp1e-recent-autoconf.patch

BuildRoot: %{_tmppath}/%{name}-buildroot
URL: http://sourceforge.net/projects/zapping/
BuildRequires: libalsa-devel libesound-devel libaudiofile-devel
ExclusiveArch: %ix86

%description
Real Time Software MPEG-1 Video/Audio Encoder.

%prep
%setup -q -n %name
%patch1 -p0 -b .aiw
%patch2 -p1
cp -a %SOURCE1 .

# configure wants to copy headers from ../src, but we have precopied them
perl -pi -e 's,context.h codec.h rte.h option.h rtepriv.h,,' configure.in

%build
autoreconf -if
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%doc ChangeLog README BUGS README-aiw AUTHORS COPYING INSTALL
%{_bindir}/%name
%{_mandir}/man1/*

