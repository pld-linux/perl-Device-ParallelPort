
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Device
%define	pnam	ParallelPort
Summary:	Device::ParallelPort
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
If you run your program with `perl -d:Trace program', this module will
print a message to standard error just before each line is executed.
This is is something like the shell's `-x' option.

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
