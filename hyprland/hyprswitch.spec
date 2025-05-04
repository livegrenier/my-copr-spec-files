Name:           hyprswitch
Version:        3.3.2
Release:        %autorelease
Summary:        A CLI/GUI that allows switching between windows in Hyprland

License:        MIT
URL:            https://github.com/H3rmt/hyprswitch
# Replace this with your vendored tarball name
Source:         %{name}-%{version}.tar.gz

BuildRequires:  rust
BuildRequires:  rust-packaging
BuildRequires:  cargo
ExclusiveArch:  %{rust_arches}

%description
%{summary}

%prep
%autosetup -n %{name}-%{version}

# Set Cargo to use vendored dependencies
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
# Prevent network access during build
%cargo_build --offline

%install
%cargo_install

%files
%license LICENSE
%doc README.md
%{_bindir}/hyprswitch

%changelog
%autochangelog
