%define	upstream_name	 Net-IRC
%define upstream_version 0.79
Name:		perl-%{upstream_name}
Version:	0.79
Release:	1

Summary:	Perl interface to the Internet Relay Chat protocol
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/A/AP/APEIRON/Net-IRC-0.79.tar.gz
Patch0:		%{name}-0.75-workwithlocalhost.patch
Patch2:		%{name}-0.76-no-warning.patch

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} perl module allows you to access IRC networks with perl.
It is used to program irc bot in perl or various software.

%prep
%setup -q -n %{upstream_name}-%{version}
%patch -P0 -p1
%patch -P2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*


