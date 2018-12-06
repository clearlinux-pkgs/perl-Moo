#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Moo
Version  : 2.003004
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.003004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-2.003004.tar.gz
Summary  : 'Minimalist Object Orientation (with Moose compatibility)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Defer)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
NAME
Moo - Minimalist Object Orientation (with Moose compatibility)
SYNOPSIS
package Cat::Food;

%package dev
Summary: dev components for the perl-Moo package.
Group: Development
Provides: perl-Moo-devel = %{version}-%{release}

%description dev
dev components for the perl-Moo package.


%prep
%setup -q -n Moo-2.003004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

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
/usr/lib/perl5/vendor_perl/5.28.1Method/Generate/Accessor.pm
/usr/lib/perl5/vendor_perl/5.28.1Method/Generate/BuildAll.pm
/usr/lib/perl5/vendor_perl/5.28.1Method/Generate/Constructor.pm
/usr/lib/perl5/vendor_perl/5.28.1Method/Generate/DemolishAll.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/HandleMoose.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/HandleMoose/FakeMetaClass.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/HandleMoose/_TypeMap.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/Object.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/Role.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/_Utils.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/_mro.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/_strictures.pm
/usr/lib/perl5/vendor_perl/5.28.1Moo/sification.pm
/usr/lib/perl5/vendor_perl/5.28.1oo.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Moo.3
/usr/share/man/man3/Moo::Role.3
/usr/share/man/man3/oo.3
