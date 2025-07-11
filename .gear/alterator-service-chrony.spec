%define _unpackaged_files_terminate_build 1
%define service service-chrony
Name: alterator-service-chrony
Version: 0.1
Release: alt1

Summary: Service for managment chrony
License: GPLv3
Group: System/Configuration/Other
URL: https://gitlab.basealt.space/alt/alterator-service-chrony

BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator

Requires: alterator-module-executor
Requires: alterator-interface-service
Requires: alterator-entry

%description
Service for deploy chrony.

%prep
%setup

%install
mkdir -p %buildroot%_alterator_datadir/service

install -p -D -m755 %service %buildroot%_bindir/%service
install -p -D -m644 %service.backend %buildroot%_alterator_datadir/backends/%service.backend
install -p -D -m644 %service.service %buildroot%_alterator_datadir/service/%service.service

%files
%_alterator_datadir/backends/%service.backend
%_alterator_datadir/service/%service.service
%_bindir/%service

%changelog
* Tue Jan 28 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.1-alt1
- Initial commit