%define debug_package %nil
%define base_name i3

Name:       i3-gaps
Version:	4.20.1
Release:	7%{?dist}
Summary:	i3 with more features
License:	BSD
URL:        https://github.com/Airblader/%{base_name}
Source0:    https://github.com/Airblader/%{base_name}/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: asciidoc
BuildRequires: bison
BuildRequires: flex
BuildRequires: libev-devel
BuildRequires: libX11-devel
BuildRequires: libxcb-devel
BuildRequires: libXcursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbfile-devel
BuildRequires: pango-devel
BuildRequires: pcre-devel
BuildRequires: perl-devel
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Data::Dumper::Names)
BuildRequires: startup-notification-devel
BuildRequires: xcb-proto
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xmlto
BuildRequires: yajl-devel
BuildRequires: git
BuildRequires: pkgconfig(xcb-xrm)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(cairo-xcb)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       xorg-x11-fonts-misc

Conflicts:      otherproviders(i3)
Provides:       i3 = %{version}

%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

%prep
%autosetup -n %{base_name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc RELEASE-NOTES-%{version}
%license LICENSE
%{_bindir}/%{base_name}*
%{_includedir}/%{base_name}/
%dir %{_sysconfdir}/%{base_name}/
%config(noreplace) %{_sysconfdir}/%{base_name}/config
%config(noreplace) %{_sysconfdir}/%{base_name}/config.keycodes
%{_datadir}/xsessions/%{base_name}.desktop
%{_datadir}/xsessions/%{base_name}-with-shmlog.desktop
%{_datadir}/applications/%{base_name}.desktop
%exclude %{_docdir}/%{base_name}/

%changelog
