## START: Set by rpmautospec
## (rpmautospec version 0.7.3)
## RPMAUTOSPEC: autorelease, autochangelog
%define autorelease(e:s:pb:n) %{?-p:0.}%{lua:
    release_number = 1;
    base_release_number = tonumber(rpm.expand("%{?-b*}%{!?-b:1}"));
    print(release_number + base_release_number - 1);
}%{?-e:.%{-e*}}%{?-s:.%{-s*}}%{!?-n:%{?dist}}
## END: Set by rpmautospec

Name:           hyprland
Version:        0.48.1
Release:        0.1.1
Summary:        Dynamic tiling Wayland compositor that doesn't sacrifice on its looks

# hyprland: BSD-3-Clause
# ./subprojects/udis86: BSD-2-Clause
# ./protocols/kde-server-decoration.xml: LGPL-2.1-or-later
# ./protocols/wayland-drm.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-data-control-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-foreign-toplevel-management-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-gamma-control-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-layer-shell-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
# ./protocols/wlr-output-management-unstable-v1.xml: HPND-sell-variant and/or ntp_disclaimer
License:        BSD-3-Clause AND BSD-2-Clause AND LGPL-2.1-or-later AND HPND-sell-variant
URL:            https://github.com/hyprwm/Hyprland
Source:         %{url}/releases/download/v%{version}/source-v%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glaze-static
BuildRequires:  meson

BuildRequires:  pkgconfig(aquamarine)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprcursor)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(hyprland-protocols) >= 0.6.2
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libliftoff)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-dri3)
BuildRequires:  pkgconfig(xcb-errors)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-present)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)

# udis86 is packaged in Fedora, but the copy bundled here is actually a
# modified fork.
Provides:       bundled(udis86) = 1.7.2^1.git5336633

Requires:       xorg-x11-server-Xwayland%{?_isa}
Requires:       xdg-desktop-portal%{?_isa}
Requires:       hyprcursor%{?_isa} >= 0.1.12
Requires:       hyprutils%{?_isa} >= 0.5.0

# Used in the default configuration
Recommends:     kitty
Recommends:     wofi
Recommends:     playerctl
Recommends:     brightnessctl
# Lack of graphical drivers may hurt the common use case
Recommends:     mesa-dri-drivers
# Logind needs polkit to create a graphical session
Recommends:     polkit

Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)

%description
Hyprland is a dynamic tiling Wayland compositor that doesn't sacrifice
on its looks. It supports multiple layouts, fancy effects, has a
very flexible IPC model allowing for a lot of customization, a powerful
plugin system and more.

%package        devel
Summary:        Meta package to install dependencies for hyprpm
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake
Requires:       cpio
Requires:       gcc-c++
Requires:       meson
Requires:       ninja-build
Requires:       pkgconfig(aquamarine)
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(hwdata)
Requires:       pkgconfig(hyprcursor)
Requires:       pkgconfig(hyprlang)
Requires:       pkgconfig(hyprutils)
Requires:       pkgconfig(hyprwayland-scanner)
Requires:       pkgconfig(libdisplay-info)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(libliftoff)
Requires:       pkgconfig(libseat)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(pango)
Requires:       pkgconfig(pangocairo)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(tomlplusplus)
Requires:       pkgconfig(uuid)
Requires:       pkgconfig(wayland-client)
Requires:       pkgconfig(wayland-protocols)
Requires:       pkgconfig(wayland-server)
Requires:       pkgconfig(xcb-composite)
Requires:       pkgconfig(xcb-dri3)
Requires:       pkgconfig(xcb-errors)
Requires:       pkgconfig(xcb-ewmh)
Requires:       pkgconfig(xcb-icccm)
Requires:       pkgconfig(xcb-present)
Requires:       pkgconfig(xcb-render)
Requires:       pkgconfig(xcb-renderutil)
Requires:       pkgconfig(xcb-res)
Requires:       pkgconfig(xcb-shm)
Requires:       pkgconfig(xcb-util)
Requires:       pkgconfig(xcb-xfixes)
Requires:       pkgconfig(xcb-xinput)
Requires:       pkgconfig(xcb)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xkbcommon)
Requires:       pkgconfig(xwayland)
Recommends:     git-core

%description    devel
%{summary}.


%prep
%autosetup -n %{name}-source -p1
rm -rf subprojects/{tracy,hyprland-protocols}
# don't run generateVersion.sh, release tarballs have pregenerated version.h
sed -i '/scripts\/generateVersion.sh/d' meson.build

cp -p subprojects/udis86/LICENSE LICENSE-udis86


%build
%meson
%meson_build


%install
%meson_install
rm %{buildroot}%{_datadir}/wayland-sessions/hyprland-uwsm.desktop
rm -rf %{buildroot}%{_includedir}/%{name}
rm -rf %{buildroot}%{_datadir}/pkgconfig/%{name}.pc


%files
%license LICENSE LICENSE-udis86
%{_bindir}/hyprctl
%{_bindir}/Hyprland
%{_bindir}/hyprland
%{_bindir}/hyprpm
%{_datadir}/hypr/
%{_datadir}/wayland-sessions/%{name}.desktop
%{_datadir}/xdg-desktop-portal/%{name}-portals.conf
%{_mandir}/man1/hyprctl.1*
%{_mandir}/man1/Hyprland.1*
%{bash_completions_dir}/hypr*
%{fish_completions_dir}/hypr*.fish
%{zsh_completions_dir}/_hypr*

%files devel


%changelog
* Sun Mar 30 2025 ploxold - 0.48.1-0.1
- Update to 0.48.1

* Sun Mar 23 2025 ploxold - 0.48.0-0.1
- Update to 0.48.0

* Sun Feb 02 2025 ploxold - 0.47.2-0.1
- Update to 0.47.2

* Thu Jan 30 2025 ploxold - 0.47.1-0.1
- Update to 0.47.1

* Mon Jan 27 2025 ploxold - 0.47.0-0.1
- Update to 0.47.0

* Tue Jan 07 2025 ploxold - 0.46.2-0.5
- Update to 0.46.2

## START: Generated by rpmautospec
* Fri Nov 22 2024 Jannik MÃ¼ller <nightishaman@fedoraproject.org> - 0.45.2-1
- Update to 0.45.2

* Mon Nov 18 2024 Jannik MÃ¼ller <nightishaman@fedoraproject.org> - 0.45.1-1
- Update to 0.45.1

* Sat Nov 09 2024 Pavel Solovev <daron439@gmail.com> - 0.45.0-1
- Update to 0.45.0

* Wed Oct 09 2024 Pavel Solovev <daron439@gmail.com> - 0.44.1-1
- Update to 0.44.1

* Sun Oct 06 2024 Pavel Solovev <daron439@gmail.com> - 0.44.0-1
- Update to 0.44.0

* Sun Sep 08 2024 Pavel Solovev <daron439@gmail.com> - 0.43.0-1
- Update to 0.43.0

* Mon Sep 02 2024 Pavel Solovev <daron439@gmail.com> - 0.42.0-2
- aquamarine rebuild

* Wed Aug 07 2024 Pavel Solovev <daron439@gmail.com> - 0.42.0-1
- Update to 0.42.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.41.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Pavel Solovev <daron439@gmail.com> - 0.41.2-3
- hyprutils rebuild

* Wed Jul 03 2024 Pavel Solovev <daron439@gmail.com> - 0.41.2-2
- libdisplay-info rebuild

* Tue Jun 25 2024 Pavel Solovev <daron439@gmail.com> - 0.41.2-1
- Update to 0.41.2

* Thu Jun 13 2024 Pavel Solovev <daron439@gmail.com> - 0.41.1-1
- Update to 0.41.1

* Mon Jun 10 2024 Pavel Solovev <daron439@gmail.com> - 0.41.0-1
- Update to 0.41.0

* Tue Jun 04 2024 Pavel Solovev <daron439@gmail.com> - 0.40.0-2
- add deps for hyprpm

* Sat Jun 01 2024 Pavel Solovev <daron439@gmail.com> - 0.40.0-1
- Update to 0.40.0

* Sat Apr 27 2024 Pavel Solovev <daron439@gmail.com> - 0.39.1-2
- minor spec tweaking

* Tue Apr 16 2024 Pavel Solovev <daron439@gmail.com> - 0.39.1-1
- Update to 0.39.1

* Sun Apr 14 2024 Pavel Solovev <daron439@gmail.com> - 0.39.0-1
- Update to 0.39.0

* Sun Apr 07 2024 Pavel Solovev <daron439@gmail.com> - 0.38.1-1
- Update to 0.38.1 (rhbz#2273790)

* Mon Apr 01 2024 Pavel Solovev <daron439@gmail.com> - 0.38.0-1
- Update to 0.38.0

* Mon Mar 18 2024 Pavel Solovev <daron439@gmail.com> - 0.37.1-1
- Update to 0.37.1

* Mon Mar 11 2024 Pavel Solovev <daron439@gmail.com> - 0.36.0-3
- hyprlang rebuild

* Mon Mar 04 2024 Pavel Solovev <daron439@gmail.com> - 0.36.0-2
- Add missing dep

* Wed Feb 28 2024 Pavel Solovev <daron439@gmail.com> - 0.36.0-1
- Update to 0.36.0

* Mon Feb 05 2024 Pavel Solovev <daron439@gmail.com> - 0.35.0-1
- Update to 0.35.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.34.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Pavel Solovev <daron439@gmail.com> - 0.34.0-3
- Disable werror in wlroots

* Wed Jan 17 2024 Pavel Solovev <daron439@gmail.com> - 0.34.0-2
- prevent partial update

* Mon Jan 15 2024 Pavel Solovev <daron439@gmail.com> - 0.34.0-1
- Update to 0.34.0

* Mon Nov 20 2023 Pavel Solovev <daron439@gmail.com> - 0.32.3-2
- add dependencies for the devel package

* Sat Nov 11 2023 Pavel Solovev <daron439@gmail.com> - 0.32.3-1
- Update to 0.32.3

* Sat Nov 11 2023 Pavel Solovev <daron439@gmail.com> - 0.32.2-1
- Update to 0.32.2

* Sat Nov 11 2023 Pavel Solovev <daron439@gmail.com> - 0.32.1-1
- Update to 0.32.1

* Tue Nov 07 2023 Pavel Solovev <daron439@gmail.com> - 0.32.0-1
- Update to 0.32.0

* Sun Nov 05 2023 Pavel Solovev <daron439@gmail.com> - 0.31.0-1
- Initial import (rhbz#2244377)
## END: Generated by rpmautospec