%define debug_package %nil
%if %{_use_internal_dependency_generator}
%define __noautoprov 'libstdc++(.*)'
%define __noautoreq 'libstdc++(.*)|(.*)GLIBC_PRIVATE(.*)'
%endif

Summary:	SopCast client
Name:		sp-auth
Version:	3.2.6
Release:	4
License:	Freeware
Group:		Video
Url:		https://code.google.com/p/sopcast-player/
Source0:	http://sopcast-player.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:	libstdcpp5.tgz
ExclusiveArch:	%{ix86}

%description
Command line version of SopCast client.

%prep
%setup -q -n %{name} -a 1

%build
# Nothing

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
install -m 0755 sp-sc-auth %{buildroot}%{_libdir}/%{name}/
install -m 0755 usr/lib/libstdc++.so.5.0.1 %{buildroot}%{_libdir}/%{name}/

pushd %{buildroot}%{_libdir}/%{name}
ln -s libstdc++.so.5.0.1 libstdc++.so.5
popd

# Wrapper
mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/sp-sc-auth << EOF
#!/bin/bash

pushd %{_libdir}/%{name}
LD_PRELOAD=./libstdc++.so.5 ./sp-sc-auth \$@
popd
EOF

chmod 0755 %{buildroot}%{_bindir}/sp-sc-auth

%files
%{_bindir}/sp-sc-auth
%{_libdir}/%{name}

