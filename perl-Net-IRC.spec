%define	upstream_name	 Net-IRC
%define	upstream_version 0.76

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{name}-0.75-workwithlocalhost.patch
Patch1:		%{name}-0.76-add-missing-modules.patch
Patch2:		%{name}-0.76-no-warning.patch
Buildarch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} perl module allows you to access IRC networks with perl.
It is used to program irc bot in perl or various software.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc README Changes TODO 
%{perl_vendorlib}/Net
%{_mandir}/*/*
