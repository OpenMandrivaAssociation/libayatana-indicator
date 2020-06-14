%define api		0.4
%define major		7
%define libname		%mklibname ayatana-indicator3_ %{major}
%define develname	%mklibname ayatana-indicator3 -d

Name:		libayatana-indicator
Version:	0.6.3
Release:	1
Summary:	Ayatana panel indicator applet libraries
License:	GPLv3
Group:		System/Libraries
URL:		https://ayatanaindicators.github.io/
Source0:	https://github.com/AyatanaIndicators/libayatana-indicator/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		libayatana-indicator-Wno-error-deprecated-declarations.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libayatana-ido3-0.4)

%description
This library contains information to build indicators to go into
the indicator applet.

#------------------------------------------------

%package	tools
Summary:	Tools for GTK+3 %{name}
Group:		System/Libraries

%description	tools
This package provides tools for GTK+3 %{name}.

#------------------------------------------------

%package -n	%{libname}
Summary:	Ayatana panel indicator applet library for GTK+3
Group:		System/Libraries

%description -n	%{libname}
This package provides the GTK+3 libraries required to build indicators
and to go into the indicator applet.

#------------------------------------------------

%package -n	%{develname}
Summary:	Development package for %{name}3 (GTK+3)
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	ayatana-indicator3-devel = %{version}-%{release}

%description -n	%{develname}
Header files for development with %{name}3 (GTK+3).

#------------------------------------------------

%prep
%autosetup -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-error=gnu-designator"
#export CC=gcc
#export CXX=g++

NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-static \
	--disable-tests	\
	--with-gtk=3
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

# This dummy indicator is fairly useless, it is not shipped in Ubuntu.
find %{buildroot} -name 'libdummy-indicator*' -delete

%files tools
%license COPYING
%doc AUTHORS ChangeLog
%{_userunitdir}/ayatana-indicators-pre.target
%{_libexecdir}/ayatana-indicator-loader3
%{_datadir}/%{name}/

%files -n %{libname}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/%{name}3.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/%{name}3-%{api}/
%{_libdir}/%{name}3.so
%{_libdir}/pkgconfig/ayatana-indicator3-%{api}.pc
