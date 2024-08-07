#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Moo
Version  : 2.005005
Release  : 33
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.005005.tar.gz
Summary  : 'Minimalist Object Orientation (with Moose compatibility)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Moo-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Defer)
BuildRequires : perl(Sub::Quote)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
Moo - Minimalist Object Orientation (with Moose compatibility)
SYNOPSIS
package Cat::Food;

%package dev
Summary: dev components for the perl-Moo package.
Group: Development
Provides: perl-Moo-devel = %{version}-%{release}
Requires: perl-Moo = %{version}-%{release}

%description dev
dev components for the perl-Moo package.


%package perl
Summary: perl components for the perl-Moo package.
Group: Default
Requires: perl-Moo = %{version}-%{release}

%description perl
perl components for the perl-Moo package.


%prep
%setup -q -n Moo-2.005005
cd %{_builddir}/Moo-2.005005

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Moo.3
/usr/share/man/man3/Moo::Role.3
/usr/share/man/man3/oo.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
