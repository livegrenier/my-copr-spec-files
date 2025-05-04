Name:           hyprswitch
Version:        3.3.2
Release:        %autorelease
Summary:        A CLI/GUI that allows switching between windows in Hyprland

License:        MIT
URL:            https://github.com/H3rmt/hyprswitch
Source:         %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
ExclusiveArch:  %{rust_arches}

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

%build
%cargo_build

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprswitch

%changelog
%autochangelog
