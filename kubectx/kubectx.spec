Name:           kubectx
Version:        0.9.5
Release:        1%{?dist}
Summary:        The Kubernetes context manager

License: Apache License 2.0
URL: https://github.com/ahmetb/kubectx
Source0: https://github.com/ahmetb/kubectx/archive/refs/tags/v%{version}.tar.gz

Requires: bash

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/*

%gopkgfiles

%changelog
