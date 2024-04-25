%global _vpath_srcdir ..

Name:		libayatana-indicator
Version:	0.9.0
Release:	1%{?dist}
Summary:	Shared functions for Ayatana indicators

License:	GPLv3
URL:		https://ayatanaindicators.github.io/
Source0:	https://github.com/AyatanaIndicators/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Fix install for proper debuginfo
Patch0:         0001-install-targets.patch

BuildRequires:  gcc
BuildRequires:	cmake
BuildRequires:  make
BuildRequires:	pkgconfig

BuildRequires:	gtk2-devel
BuildRequires:	gtk3-devel
BuildRequires:  ayatana-ido-devel


%description
A set of symbols and convenience functions that all Ayatana indicators are
likely to use.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:       libindicator-devel = 1:%{version}-%{release}
Obsoletes:      libindicator-devel < 1:%{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package gtk3
Summary:	GTK+3 build of %{name}

%description gtk3
A set of symbols and convenience functions that all Ayatana indicators
are likely to use. This is the GTK+ 3 build of %{name}, for use
by GTK+ 3 apps.


%package gtk3-devel
Summary:	Development files for %{name}-gtk3
Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}
Provides:       libindicator-gtk3-devel = 1:%{version}-%{release}
Obsoletes:      libindicator-gtk3-devel < 1:%{version}-%{release}

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.


%package gtk3-tools
Summary:	Shared functions for Ayatana indicators - GTK3 Tools
Requires:	%{name}-gtk3%{?_isa} = %{version}-%{release}

%description gtk3-tools
This package contains tools used by the %{name}-gtk3 package, the
Ayatana indicators system. This package contains the builds of the
tools for the GTK+3 build of %{name}.


%prep
%autosetup -p1


%build
rm -rf build-gtk2 build-gtk3
mkdir build-gtk2 build-gtk3

pushd build-gtk2
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%cmake -DFLAVOUR_GTK2=ON
%cmake_build
popd

pushd build-gtk3
export CFLAGS="%{optflags} -Wno-error=deprecated-declarations"
%cmake -DFLAVOUR_GTK3=ON
%cmake_build
popd


%install
pushd build-gtk2
%cmake_install
popd
(
	PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
	export PKG_CONFIG_PATH
	for var in \
		iconsdir \
		indicatordir \
		%{nil}
	do
		vardir=$(pkg-config --variable=${var} ayatana-indicator-0.4)
		mkdir -p %{buildroot}${vardir}
	done
)

pushd build-gtk3
%cmake_install
popd
(
	PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
	export PKG_CONFIG_PATH
	for var in \
		iconsdir \
		indicatordir \
		%{nil}
	do
		vardir=$(pkg-config --variable=${var} ayatana-indicator3-0.4)
		mkdir -p %{buildroot}${vardir}
	done
)

ln -s libayatana-indicator %{buildroot}%{_includedir}/libayatana-indicator-0.4/libindicator
ln -s libayatana-indicator %{buildroot}%{_includedir}/libayatana-indicator3-0.4/libindicator
ln -s ayatana-indicator-0.4.pc %{buildroot}%{_libdir}/pkgconfig/indicator-0.4.pc
ln -s ayatana-indicator3-0.4.pc %{buildroot}%{_libdir}/pkgconfig/indicator3-0.4.pc


%files
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libayatana-indicator.so.7*
%dir %{_datadir}/libayatana-indicator/
%dir %{_datadir}/libayatana-indicator/icons/
%{_libdir}/ayatana-indicators/

%files devel
%{_includedir}/libayatana-indicator-0.4/
%{_libdir}/libayatana-indicator.so
%{_libdir}/pkgconfig/ayatana-indicator-0.4.pc
%{_libdir}/pkgconfig/indicator-0.4.pc

%files gtk3
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libayatana-indicator3.so.7*
%dir %{_datadir}/libayatana-indicator/
%dir %{_datadir}/libayatana-indicator/icons/
%{_libdir}/ayatana-indicators3/

%files gtk3-devel
%{_includedir}/libayatana-indicator3-0.4/
%{_libdir}/libayatana-indicator3.so
%{_libdir}/pkgconfig/ayatana-indicator3-0.4.pc
%{_libdir}/pkgconfig/indicator3-0.4.pc

%files gtk3-tools
%{_libexecdir}/libayatana-indicator/ayatana-indicator-loader3
%{_datadir}/libayatana-indicator/80indicator-debugging

%changelog
