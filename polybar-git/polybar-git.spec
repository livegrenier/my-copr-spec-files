# Git submodules
#   * i3ipcpp
%global commit1         86ddf7102c6903ae0cc543071e2d375403fc0727
%global shortcommit1    %(c=%{commit1}; echo ${c:0:7})

#   * xpp
%global commit2         7a9960bbb912f0ed66929c978aaeb1c30acf4bfd
%global shortcommit2    %(c=%{commit2}; echo ${c:0:7})

%global url1    https://github.com/%{name}

Name:           polybar
Version:        3.7.1
Release:        1%{?dist}
Summary:        Fast and easy-to-use status bar

# BSD 2-clause "Simplified" License
# ---------------------------------
# lib/concurrentqueue/
#
# Expat License
# -------------
# lib/i3ipcpp/
# lib/xpp/
#
License:        MIT and BSD
URL:            https://polybar.github.io/
Source0:        %{url1}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Bundled libs
Source1:        %{url1}/i3ipcpp/archive/%{commit1}/i3ipcpp-%{shortcommit1}.tar.gz
Source2:        %{url1}/xpp/archive/%{commit2}/xpp-%{shortcommit2}.tar.gz

BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  i3-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  libnl3-devel
BuildRequires:  make
BuildRequires:  python3 >= 3.5
BuildRequires:  python3-sphinx
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp) >= 1.7.7
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libuv) >= 1.3
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb)

Provides:       bundled(i3ipcpp) = 0.7.1~git%{shortcommit1}
Provides:       bundled(xpp) = 1.4.0~git%{shortcommit2}

%description
Polybar aims to help users build beautiful and highly customizable status bars
for their desktop environment, without the need of having a black belt in shell
scripting.


%prep
%setup -q
%setup -q -D -T -a1
%setup -q -D -T -a2

mv i3ipcpp-%{commit1}/* lib/i3ipcpp
mv xpp-%{commit2}/*     lib/xpp


%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md SUPPORT.md
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/
%{_docdir}/%{name}/
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_sysconfdir}/%{name}/config.ini


%changelog
