
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	ParallelPort
Summary:	Device::ParallelPort - Parallel Port Driver for Perl
Name:		perl-Device-ParallelPort
Version:	1.00
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6d2345b31f9c3871230ba384c62c2d00
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A parallel port driver module. This module provides an API to all 
parallel ports, by providing the ability to write any number of drivers
modules are available for linux (both directly and via parport), i
win32 and a simple script version.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Device/ParallelPort.pm
%dir %{perl_vendorlib}/Device/ParallelPort
%dir %{perl_vendorlib}/Device/ParallelPort/drv
%{perl_vendorlib}/Device/ParallelPort/*.pm
%{perl_vendorlib}/Device/ParallelPort/drv/*.pm
%{_mandir}/man3/*
