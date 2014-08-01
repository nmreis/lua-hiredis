Name:		lua-hiredis
Version:	scm
Release:	1%{?dist}
Summary:	Bindings for hiredis Redis-client library

License:	MIT
URL:		https://github.com/agladysh/lua-hiredis
Source0:	%{name}-%{version}.tar.gz

BuildRequires: lua52-devel
Requires: lua52

%description
The lua-hiredis module is pretty stable. It is heavily used in production under high load by the author and team. 
There are still some things to do (see TODO file) in the feature completeness field, this is why the module is not 1.0 yet. 
But all the features necessary for regular usage are here.

%prep
%setup -q

%build
#make %{?_smp_mflags}
bash make.sh

%install
mkdir -p %{buildroot}/%{_libdir}/lua/5.2
cp hiredis.so %{buildroot}/%{_libdir}/lua/5.2


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%{_libdir}/lua/5.2/hiredis.so


%changelog
* Tue Jul 29 2014 FSCloud Release Engineering <nreis@wavecom.pt> - 0.4.4
- First version
