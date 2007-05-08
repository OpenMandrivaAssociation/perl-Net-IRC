%define	module	Net-IRC
%define	name	perl-%{module}
%define	version	0.75
%define	release %mkrel 3

Name:		%{name}
Summary:	%{module} module for perl
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{module}-%{version}.tar.bz2
Patch0:		%{name}-0.75-workwithlocalhost.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
Buildarch:	noarch

%description
%{module} perl module allows you to access IRC networks with perl.
It is used to program irc bot in perl or various software.

%prep
%setup -q -n %{module}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std}

%clean
%{__rm} -rf $RPM_BUILD_ROOT 

%files
%defattr(-,root,root)
%doc README Changes TODO 
%{perl_vendorlib}/Net
%{_mandir}/*/*

