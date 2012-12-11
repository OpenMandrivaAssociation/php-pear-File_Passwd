%define		_class		File
%define		_subclass	Passwd
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	1.1.7
Release:	%mkrel 6
Summary:	Manipulate password files
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/File_Passwd/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Provides methods to manipulate standard Unix, SMB server,
AuthUser (.htpasswd), AuthDigest (.htdigest) and CVS pserver password
files.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-6mdv2012.0
+ Revision: 741979
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-5
+ Revision: 679324
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.7-4mdv2011.0
+ Revision: 613661
- the mass rebuild of 2010.1 packages

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.7-3mdv2010.1
+ Revision: 478671
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.1.7-2mdv2010.0
+ Revision: 441074
- rebuild

* Sat Jan 24 2009 Funda Wang <fwang@mandriva.org> 1.1.7-1mdv2009.1
+ Revision: 333195
- update to new version 1.1.7

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-2mdv2009.0
+ Revision: 236841
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-1mdv2008.0
+ Revision: 15426
- 1.1.6


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-5mdv2007.0
+ Revision: 81588
- Import php-pear-File_Passwd

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-5mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-1mdk
- 1.1.5

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-1mdk
- initial Mandriva package (PLD import)

