Name:           hyprsunset
Version:        0.2.0
Release:        0.1.1
Summary:        An application to enable a blue-light filter on Hyprland
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/hyprsunset
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
Requires:       hyprland%{?_isa} >= 0.48.0
%description
%{summary}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install
install -m0644 -Dt %{buildroot}%{_userunitdir}/ %{buildroot}%{_libdir}/systemd/user/%{name}.service
rm %{buildroot}%{_libdir}/systemd/user/%{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun %{name}.service

%changelog
* Mon Mar 24 2025 ploxold - 0.2.0-0.1
- Update to 0.2.0

* Sun Jan 19 2025 ploxold - 0.1.0-1.5
- Add patch

* Tue Oct 08 2024 Pavel Solovev <daron439@gmail.com> - 0.1.0-1
- Version 0.1.0