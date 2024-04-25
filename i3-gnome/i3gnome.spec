%define debug_package %nil

Name:		i3-gnome
Version:	40.4
Release:	1%{?dist}
Summary:	Use i3 with GNOME Session integration.

License:	MIT
URL:		https://github.com/i3-gnome/%{name}
Source0:	%{url}/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make

Requires:	i3
Requires:	gnome-session
Requires:	gnome-settings-daemon

%description
Allows you to use i3wm with GNOME 3 Session infrastructure

%prep
%setup

%build
%make_build
%install
%make_install

%files
/usr/bin/i3-gnome
/usr/share/applications/i3-gnome.desktop
/usr/share/gnome-session/sessions/i3-gnome.session
/usr/share/xsessions/i3-gnome.desktop
/usr/bin/gnome-session-i3

%doc README.md
%license LICENSE

%changelog
* Sat Feb 19 2022 dave <livegrenier@gmail.com> - 40.4
- Initial version
