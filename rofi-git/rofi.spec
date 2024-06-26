Name:    rofi
Version: 1.7.5
Release: 1%{?dist}
Summary: A window switcher, application launcher and dmenu replacement

# lexer/theme-parser.[ch]:
# These files are generated from lexer/theme-parser.y and licensed with GPLv3+
# with Bison exception.
# As the source file is licensed with MIT, according to the Bison exception,
# the shipped files are considered to be MIT-licensed.
# See also
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/C4VVT54Z4WFGJPPD5X54ILKRF6X2IFLZ/
License: MIT
URL:     https://github.com/davatorium/%{name}
Source0: %{URL}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig
BuildRequires: gcc-c++
BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: flex
BuildRequires: graphviz
BuildRequires: make
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-xcb)
BuildRequires: pkgconfig(check) >= 0.11.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(libstartup-notification-1.0)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-xinerama)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)

# https://github.com/sardemff7/libgwater
Provides: bundled(libgwater)
# https://github.com/sardemff7/libnkutils
Provides: bundled(libnkutils)

Requires:      %{name}-themes = %{version}-%{release}
Requires:      hicolor-icon-theme

%description
Rofi is a dmenu replacement. Rofi, like dmenu, will provide the user with a
textual list of options where one or more can be selected. This can either be,
running an application, selecting a window or options provided by an external
script.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        devel-doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    devel-doc
The %{name}-devel-doc package contains documentation files for developing
applications that use %{name}.

%package        themes
Summary:        Themes for %{name}
BuildArch:      noarch

%description    themes
The %{name}-themes package contains themes for %{name}.

%prep
%autosetup -p1

%build
%configure
%make_build

make doxy
find doc/html/html -name "*.map" -delete
find doc/html/html -name "*.md5" -delete

%install
%make_install

%check
make check || (cat ./test-suite.log; false)
desktop-file-validate %{buildroot}%{_datadir}/applications/rofi*.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_datadir}/applications/rofi.desktop
%{_datadir}/applications/rofi-theme-selector.desktop
%{_datadir}/icons/hicolor/apps/rofi.svg
%{_mandir}/man1/rofi*
%{_mandir}/man5/rofi*

%files themes
%license COPYING
%{_datarootdir}/rofi

%files devel
%{_includedir}/rofi
%{_libdir}/pkgconfig/rofi.pc

%files devel-doc
%license COPYING
%doc doc/html/html/*

%changelog
