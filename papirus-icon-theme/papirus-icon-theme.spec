Name:           papirus-icon-theme
Version:        20231101
Release:        %autorelease
Summary:        Free and open source SVG icon theme based on Paper Icon Set

# Some icons are based on Paper Icon Theme, CC-BY-SA
# The rest is GPLv3
License:        GPLv3 and CC-BY-SA
URL:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make

%description
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE colorscheme support, Folder Color support, and others.

Papirus icon theme is available in six variants:

 - Papirus (for Arc / Arc Darker)
 - Papirus Dark (for Arc Dark)
 - Papirus Light (light theme with Breeze colors)
 - ePapirus (for elementary OS and Pantheon Desktop)
 - ePapirus-Dark (for elementary OS and Pantheon Desktop)

%prep
%autosetup

%install
%make_install

export THEMES="ePapirus ePapirus-Dark Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch %{buildroot}/%{_datadir}/icons/$t/icon-theme.cache
done

%post
export THEMES="ePapirus ePapirus-Dark Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
    export THEMES="ePapirus ePapirus-Dark Papirus Papirus-Dark Papirus-Light"
    for t in $THEMES; do
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    done
fi

%posttrans
export THEMES="ePapirus ePapirus-Dark Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done

%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_datadir}/icons/Papirus-Dark
%dir %{_datadir}/icons/Papirus-Light
%dir %{_datadir}/icons/Papirus
%dir %{_datadir}/icons/ePapirus-Dark
%dir %{_datadir}/icons/ePapirus
%ghost %{_datadir}/icons/Papirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Light/icon-theme.cache
%ghost %{_datadir}/icons/Papirus/icon-theme.cache
%ghost %{_datadir}/icons/ePapirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/ePapirus/icon-theme.cache
%{_datadir}/icons/Papirus-Dark/*x*
%{_datadir}/icons/Papirus-Dark/symbolic
%{_datadir}/icons/Papirus-Light/*x*
%{_datadir}/icons/Papirus-Light/symbolic
%{_datadir}/icons/Papirus/*x*
%{_datadir}/icons/Papirus/symbolic
%{_datadir}/icons/ePapirus-Dark/*x*
%{_datadir}/icons/ePapirus-Dark/symbolic
%{_datadir}/icons/ePapirus/*x*
%{_datadir}/icons/ePapirus/symbolic

%changelog
%autochangelog
