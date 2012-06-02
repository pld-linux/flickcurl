
Summary:	Flickcurl is a C library for the Flickr API
Summary(pl.UTF-8):	Flickcurl is a C library for the Flickr API
Name:		flickcurl
Version:	1.22
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz
# Source0-md5:	33106156f9a9e538b5787f92db717f5d
URL:		http://dajobe.org
BuildRequires:	curl-devel
BuildRequires:	libraptor-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package devel
Summary:	Flickcurl development files
Summary(pl.UTF-8):	Pliki programistyczne Flickcurl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the include files used to develop using
Flickcurl APIs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkow służące do programowania z użyciem
API Flickcurl.

%package static
Summary:	The Flickcurl static libraries
Summary(pl.UTF-8):	Statyczne biblioteki Flickcurl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the Flickcurl static libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki Flickcurl.

%package tools
Summary:	The Flickcurl utility tools
Summary(pl.UTF-8):	Programy narzędziowe do biblioteki Flickcurl
Group:		Libraries

%description tools
This package contains the Flickcurl utility tools.

%description tools -l pl.UTF-8
Ten pakiet zawiera programy narzędziowe do biblioteki Flickcurl.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libflickcurl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflickcurl.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root)  %{_bindir}/flickcurl-config
%{_libdir}/libflickcurl.la
%{_libdir}/libflickcurl.so
%{_pkgconfigdir}/flickcurl.pc
%{_includedir}/flickcurl.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libflickcurl.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root)  %{_bindir}/flickcurl
%attr(755,root,root)  %{_bindir}/flickrdf
%{_mandir}/man1/flickcurl.1.*
%{_mandir}/man1/flickcurl-config.1.*
%{_mandir}/man1/flickrdf.1.*
