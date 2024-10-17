%define name	mp1e
%define version	1.9.9
%define snapshot 20060612
%define rel	5
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
URL: https://sourceforge.net/projects/zapping/
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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.9-0.20060612.5mdv2011.0
+ Revision: 620398
- the mass rebuild of 2010.0 packages

* Sun Jul 12 2009 Anssi Hannula <anssi@mandriva.org> 1.9.9-0.20060612.4mdv2010.0
+ Revision: 395405
- use autoreconf (autoconf no longer enough)
- fix build with recent autotools (recent-autoconf.patch)

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.9.9-0.20060612.3mdv2009.0
+ Revision: 136607
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.9.9-0.20060612.3mdv2008.1
+ Revision: 130229
- kill re-definition of %%buildroot on Pixel's request

* Sat Jul 14 2007 Anssi Hannula <anssi@mandriva.org> 1.9.9-0.20060612.3mdv2008.0
+ Revision: 51967
- annual rebuild
- adapt for autoconf of new era
- Import mp1e



* Wed Jun 14 2006 Anssi Hannula <anssi@mandriva.org> 1.9.9-0.20060612.2mdv2007.0
- builds only on x86

* Mon Jun 12 2006 Anssi Hannula <anssi@mandriva.org> 1.9.9-0.20060612.1mdv2007.0
- CVS snapshot
- fix URL
- untar and rediff the aiw patch

* Wed Sep 10 2003 Austin Acton <aacton@yorku.ca> 1.9.3-2mdk
- from Spencer Anderson <sdander@oberon.ark.com> :
  - patch for better handling with km (Nikolai Zhubr)
  - more docs

* Wed Aug 20 2003 Austin Acton <aacton@yorku.ca> 1.9.3-1mdk
- from Spencer Anderson <sdander@oberon.ark.com> :
  - initial Mandrake release
- add URL, add buildrequires, fix group, parallel make
