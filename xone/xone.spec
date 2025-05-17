%global debug_package %{nil}
%global commit c682b0cd4fd56d2d9639b64787034a375535eb4b

Name:     xone
Version:  0.3.0
Release:  9%{?dist}
Epoch:    1
Summary:  Linux kernel driver for Xbox One and Xbox Series X|S accessories 
License:  GPLv2
#URL:      https://github.com/medusalix/xone
URL:      https://github.com/dlundqvist/xone
Source0:  %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
Source1:  modules-load-d-%{name}.conf

BuildRequires:  systemd-rpm-macros

Provides:       %{name}-kmod-common = %{epoch}:%{version}-%{release}
Requires:       %{name}-kmod >= %{epoch}:%{version}

Conflicts:      xow <= 0.5
Obsoletes:      xow <= 0.5

%description
xone is a Linux kernel driver for Xbox One and Xbox Series X|S accessories.
It serves as a modern replacement for xpad, aiming to be compatible with
Microsoft's Game Input Protocol (GIP).

%package kmod
Summary:  Kernel module (kmod) for %{name}
Requires: kernel-devel

%description kmod
kmod package for %{name}

%prep
%autosetup -n %{name}-%{commit} 

%build
# Nothing to build

%install
install -D -m 0644 install/modprobe.conf %{buildroot}%{_modprobedir}/60-%{name}.conf
install -D -m 0644 %{SOURCE1} %{buildroot}%{_modulesloaddir}/%{name}.conf

%files
%license LICENSE
%{_modprobedir}/60-%{name}.conf
%{_modulesloaddir}/%{name}.conf

%changelog
%autochangelog