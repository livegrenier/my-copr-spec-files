## START: Set by rpmautospec
## (rpmautospec version 0.7.3)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

Name:           hyprland-qt-support
Version:        0.1.0
Release:        0.8
Summary:        Extra qt support libraries for the hyprland ecosystem

License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprland-qt-support
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  pkgconfig(hyprlang)

%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake_qt6 -DCMAKE_INSTALL_LIBDIR=lib64
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_qt6_libdir}/libhyprland-quick-style.so
%{_qt6_libdir}/libhyprland-quick-style-impl.so
%{_qt6_qmldir}/org/hyprland/style/

%changelog
* Mon Jan 13 2025 ploxold - 0.1.0-0.5
- Initial import