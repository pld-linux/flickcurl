Summary:	Flickcurl - C library for the Flickr API
Summary(pl.UTF-8):	Flickcurl - biblioteka C do API serwisu Flickr
Name:		flickcurl
Version:	1.26
Release:	1
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0
Group:		Libraries
Source0:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz
# Source0-md5:	7013a36656400dac398748a374c9104f
URL:		http://dajobe.org/
BuildRequires:	curl-devel >= 7.10.0
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libraptor2-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 1:2.6.8
BuildRequires:	pkgconfig
Requires:	curl >= 7.10.0
Requires:	libraptor2 >= 2.0.0
Requires:	libxml2 >= 1:2.6.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flickcurl is a C library for the Flickr API.

%description -l pl.UTF-8
Flickcurl to biblioteka C do API serwisu Flickr.

%package devel
Summary:	Flickcurl development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Flickcurl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	curl-devel >= 7.10.0
Requires:	libraptor2-devel >= 2.0.0
Requires:	libxml2-devel >= 1:2.6.8

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

%package apidocs
Summary:	API documentation for Flickcurl library
Summary(pl.UTF-8):	Dokumentacja API biblioteki Flickcurl
Group:		Documentation

%description apidocs
API documentation for Flickcurl library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki Flickcurl.

%package tools
Summary:	The Flickcurl utility tools
Summary(pl.UTF-8):	Programy narzędziowe do biblioteki Flickcurl
Group:		Applications/Network
Requires:	%{name} = %{version}-%{release}

%description tools
This package contains the Flickcurl utility tools.

%description tools -l pl.UTF-8
Ten pakiet zawiera programy narzędziowe do biblioteki Flickcurl.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libflickcurl.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE.html NEWS NOTICE README.html
%attr(755,root,root) %{_libdir}/libflickcurl.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libflickcurl.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flickcurl-config
%attr(755,root,root) %{_libdir}/libflickcurl.so
%{_includedir}/flickcurl.h
%{_pkgconfigdir}/flickcurl.pc
%{_mandir}/man1/flickcurl-config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libflickcurl.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/flickcurl

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/flickcurl
%attr(755,root,root) %{_bindir}/flickrdf
%{_mandir}/man1/flickcurl.1*
%{_mandir}/man1/flickrdf.1*
