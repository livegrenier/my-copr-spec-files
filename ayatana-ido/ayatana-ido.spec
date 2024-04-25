
Name:		ayatana-ido
Version:	0.9.0
Release:	1%{?dist}
Summary:	Ayatana Indicator Display Objects library

License:	GPLv3
URL:		https://ayatanaindicators.github.io/
Source0:	https://github.com/AyatanaIndicators/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-install-targets.patch

BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:  make
BuildRequires:  gobject-introspection-devel
BuildRequires:	gtk3-devel
BuildRequires:  vala


%description
Ayatana IDO provides custom GTK menu widgets for Ayatana System Indicators.


%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1
#sed -i -e '/set.*CMAKE_BUILD_TYPE/d' CMakeLists.txt


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc AUTHORS COPYING NEWS ChangeLog
%{_libdir}/libayatana-ido3-0.4.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/AyatanaIdo3-0.4.typelib

%files devel
%{_includedir}/libayatana-ido3-0.4/
%{_libdir}/libayatana-ido3-0.4.so
%{_libdir}/pkgconfig/libayatana-ido3-0.4.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/AyatanaIdo3-0.4.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/AyatanaIdo3-0.4.*


%changelog
