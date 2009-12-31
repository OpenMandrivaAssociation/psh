%define upstream_name    psh
%define upstream_version 1.8.1

Name:       %{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Containing translations for default locale
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Cwd)
BuildRequires: perl(File::Spec)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
*psh* is a Perl program which executes a read-eval loop with enough options
so that general behavior reasonably similar to more traditional shells like
'*sh*' or '*bash*' can be achieved, while still allowing arbitrary perl
expressions to be evaluated.

By default within *psh*, the Perl *-w* flag and ''use strict'' are not
employed so that the user is not bound by their stipulations. They can both
be turned on via a command-line flag; or setting '$^W = 1' will turn on
warnings, and calling ''use strict'' will (almost) do the usual thing if
called by the user (see LIMITATIONS, below).

Each line of input is read. *psh* knows a number of possible strategies for
evaluating the line, such as "send it to 'system()' if it starts with the
name of an executable visible in '$ENV{PATH}'". (See below for a complete
list.) Each strategy in turn (from a user-definable list) examines the
command line to see if it can apply, and the first matching strategy
evaluates the line. There is a *psh* configuration variable (see below)
which controls whether the perl value of the evaluation is saved and
printed after each command.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/psh
/usr/share/man/man1/psh.1.lzma
/usr/share/man/man1/pshcomplete.1.lzma
/usr/share/man/man1/pshconfig.1.lzma
/usr/share/man/man1/pshdevel.1.lzma

