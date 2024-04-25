%global _vpath_srcdir ..

Name:		libayatana-appindicator
Version:	0.5.90
Release:	1%{?dist}
Summary:	Ayatana Application Indicators library

License:	GPLv3
URL:		https://ayatanaindicators.github.io/
Source0:	https://github.com/AyatanaIndicators/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-install-targets.patch

BuildRequires:  gcc
BuildRequires:	cmake
BuildRequires:  make
BuildRequires:	gtk-doc

BuildRequires:	gtk2-devel
BuildRequires:	gtk3-devel
BuildRequires:  libayatana-indicator-devel
BuildRequires:  libayatana-indicator-gtk3-devel
BuildRequires:  libdbusmenu-gtk2-devel
BuildRequires:  libdbusmenu-gtk3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  vala


%description
A library to allow applications to export a menu into the an Application
Indicators aware menu bar. Based on KSNI it also works in KDE and will
fallback to generic Systray support if none of those are available.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:       libappindicator-devel = 1:%{version}-%{release}
Obsoletes:      libappindicator-devel < 1:%{version}-%{release}

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
Provides:       libappindicator-gtk3-devel = 1:%{version}-%{release}
Obsoletes:      libappindicator-gtk3-devel < 1:%{version}-%{release}

%description gtk3-devel
The %{name}-gtk3-devel package contains libraries and header files for
developing applications that use %{name}-gtk3.


%prep
%autosetup -p1


%build
rm -rf build-gtk2 build-gtk3
mkdir build-gtk2 build-gtk3

pushd build-gtk2
%cmake -DFLAVOUR_GTK2=ON -DENABLE_GTKDOC=ON -DENABLE_BINDINGS_MONO=OFF
%cmake_build
popd

pushd build-gtk3
%cmake -DFLAVOUR_GTK3=ON -DENABLE_GTKDOC=ON -DENABLE_BINDINGS_MONO=OFF
%cmake_build
popd


%install
pushd build-gtk2
%cmake_install
popd

pushd build-gtk3
%cmake_install
popd

ln -s libayatana-appindicator %{buildroot}%{_includedir}/libayatana-appindicator-0.1/libappindicator
ln -s libayatana-appindicator %{buildroot}%{_includedir}/libayatana-appindicator3-0.1/libappindicator
ln -s ayatana-appindicator-0.1.pc %{buildroot}%{_libdir}/pkgconfig/appindicator-0.1.pc
ln -s ayatana-appindicator3-0.1.pc %{buildroot}%{_libdir}/pkgconfig/appindicator3-0.1.pc

%files
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libayatana-appindicator.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/AyatanaAppIndicator-0.1.typelib

%files devel
%{_includedir}/libayatana-appindicator-0.1/
%{_libdir}/libayatana-appindicator.so
%{_libdir}/pkgconfig/ayatana-appindicator-0.1.pc
%{_libdir}/pkgconfig/appindicator-0.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/AyatanaAppIndicator-0.1.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}

%files gtk3
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libayatana-appindicator3.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/AyatanaAppIndicator3-0.1.typelib

%files gtk3-devel
%{_includedir}/libayatana-appindicator3-0.1/
%{_libdir}/libayatana-appindicator3.so
%{_libdir}/pkgconfig/ayatana-appindicator3-0.1.pc
%{_libdir}/pkgconfig/appindicator3-0.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/AyatanaAppIndicator3-0.1.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}3
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/ayatana-appindicator3-0.1.*


%changelog
