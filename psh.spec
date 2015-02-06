%define	version			1.8.1

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32(.*)\\)'
%else
%define	_requires_exceptions	perl(Win32)
%endif

Name:		psh
Version:	%perl_convert_version %{version}
Release:	9
Summary:	Developping for Perl Shell
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{name}
Source0:	http://search.cpan.org/CPAN/authors/id/G/GR/GREGOR/%{name}-%{version}.tar.gz
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl-devel
BuildArch:	noarch

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
%setup -q -n %{name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/psh
%{_mandir}/man1/*

