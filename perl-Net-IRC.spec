%define	upstream_name	 Net-IRC
%define upstream_version 0.79

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl interface to the Internet Relay Chat protocol
License:	GPL
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{name}-0.75-workwithlocalhost.patch
Patch2:		%{name}-0.76-no-warning.patch

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} perl module allows you to access IRC networks with perl.
It is used to program irc bot in perl or various software.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1
%patch2 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Net
%{_mandir}/*/*


%changelog
* Mon Dec 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.790.0-1mdv2010.1
+ Revision: 483043
- update to 0.79

* Thu Dec 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.780.0-1mdv2010.1
+ Revision: 482136
- update to 0.78

* Mon Dec 21 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.770.0-1mdv2010.1
+ Revision: 480752
- update to 0.77

* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.760.0-2mdv2010.0
+ Revision: 449271
- ship missing modules

* Thu Sep 24 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.760.0-1mdv2010.0
+ Revision: 448395
- update to 0.76

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.750.0-1mdv2010.0
+ Revision: 407816
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.75-5mdv2009.0
+ Revision: 241785
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.75-3mdv2008.0
+ Revision: 25273
- rebuild


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.75-2mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Thu Jun 03 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.75-1mdk
- 0.75
- regenerate P0

* Sun May 09 2004 Michael Scherer <misc@mandrake.org> 0.74-2mdk 
- add patch0 to refix issues of bug #3715

* Thu Apr 22 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.74-1mdk
- 0.74

* Mon Aug 18 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.70-1mdk
- initial mdk release

