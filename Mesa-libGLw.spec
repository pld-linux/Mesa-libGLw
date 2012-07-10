#
# Conditional build:
%bcond_without	motif		# Motif interface
%bcond_without	static_libs	# static library
#
Summary:	SGI OpenGL Xt widgets library
Summary(pl.UTF-8):	Biblioteka SGI widgetów Xt dla OpenGL-a
Name:		Mesa-libGLw
Version:	8.0.0
Release:	1
Epoch:		1
License:	SGI MIT-like
Group:		X11/Libraries
Source0:	ftp://ftp.freedesktop.org/pub/mesa/glw/glw-%{version}.tar.bz2
# Source0-md5:	b29b8b5481b8cbc839cb02c324bdabd9
URL:		http://www.mesa3d.org/
BuildRequires:	OpenGL-devel >= 1.2
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
%{?with_motif:BuildRequires:	motif-devel}
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXt-devel
Provides:	OpenGL-GLw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGI OpenGL Xt widgets library.

%description -l pl.UTF-8
Biblioteka SGI widgetów Xt dla OpenGL-a.

%package devel
Summary:	Header files for SGI libGLw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki SGI libGLw
License:	SGI MIT-like
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL-devel >= 1.2
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXt-devel
Provides:	OpenGL-GLw-devel

%description devel
Header files for SGI libGLw library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki SGI libGLw.

%package static
Summary:	Static SGI libGLw library
Summary(pl.UTF-8):	Statyczna biblioteka SGI libGLw
License:	SGI MIT-like
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Provides:	OpenGL-GLw-static

%description static
Static SGI libGLw library.

%description static -l pl.UTF-8
Statyczna biblioteka SGI libGLw.

%prep
%setup -q -n glw-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static} \
	%{?with_motif:--enable-motif}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# there is pkg-config support; also, traditionally libGLw didn't have .la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libGLw.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libGLw.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLw.so
%{_includedir}/GL/GLwDrawA.h
%{_includedir}/GL/GLwDrawAP.h
%if %{with motif}
%{_includedir}/GL/GLwMDrawA.h
%{_includedir}/GL/GLwMDrawAP.h
%endif
%{_pkgconfigdir}/glw.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libGLw.a
%endif
