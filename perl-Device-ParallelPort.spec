#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Device
%define		pnam	ParallelPort
Summary:	Device::ParallelPort - parallel port driver for Perl
Summary(pl.UTF-8):	Device::ParallelPort - sterownik portu równoległego dla Perla
Name:		perl-Device-ParallelPort
Version:	1.00
Release:	2
# same as perl (?)
# LICENSE says it is LGPL or Artistic
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d2345b31f9c3871230ba384c62c2d00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A parallel port driver module. This module provides an API to all
parallel ports, by providing the ability to write any number of
drivers. Modules are available for Linux (both directly and via
parport), Win32 and a simple script version.

%description -l pl.UTF-8
Moduł sterownika portu równoległego. Ten moduł dostarcza API do
wszystkich portów równoległych, dając możliwość pisania dowolnej
liczby sterowników. Dostępne są moduły dla Linuksa (zarówno działający
bezpośrednio jak i przez parport), Win32 oraz prosta wersja skryptowa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Device/ParallelPort.pm
%dir %{perl_vendorlib}/Device/ParallelPort
%dir %{perl_vendorlib}/Device/ParallelPort/drv
%{perl_vendorlib}/Device/ParallelPort/*.pm
%{perl_vendorlib}/Device/ParallelPort/drv/*.pm
%{_mandir}/man3/*
