%define rname magicolor5440dl

Summary:	Cups Driver for KONICA MINOLTA magicolor 5440 DL
Name:		cups-drivers-%{rname}
Version:	1.2.1
Release:	%mkrel 13
License:	GPL
Group:		System/Printing
URL:		http://printer.konicaminolta.net/
Source0:	magicolor5440DL-%{version}.tar.gz
Patch0:		magicolor2430DL-shared_system_libs.diff
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	jbig-devel
BuildRequires:	lcms-devel
Requires:	cups
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains KONICA MINOLTA CUPS LavaFlow stream(PCL-like) filter
rastertokm5440dl and the PPD file. The filter converts CUPS raster data to
KONICA MINOLTA LavaFlow stream.

This package contains CUPS drivers (PPD) for the following printers:

 o KONICA MINOLTA magicolor 5440 DL printer

%prep

%setup -q -n magicolor5440DL-%{version}
%patch0 -p0

# Fix copy of CUPS headers in kmlf.h
perl -p -i -e 's:\bcups_strlcpy:_cups_strlcpy:g' src/kmlf.h

# Remove asterisks from group names in PPD file
gzip -dc src/km_en.ppd.gz | perl -p -e 's/(Group:\s+)\*/$1/g' | gzip > src/km_en.tmp.ppd.gz && mv -f src/km_en.tmp.ppd.gz src/km_en.ppd.gz

# Determine the directory for the CUPS filters using the correct method
perl -p -i -e 's:(CUPS_SERVERBIN=)"\$libdir/cups":$1`cups-config --serverbin`:' configure*

%build
rm -f configure
libtoolize --force --copy; aclocal; automake --add-missing --copy --foreign; autoconf

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_prefix}/lib/cups/filter/rastertokm5440dl
%{_datadir}/KONICA_MINOLTA/mc5440DL
%attr(0644,root,root) %{_datadir}/cups/model/KONICA_MINOLTA/km5440dl.ppd*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-13mdv2011.0
+ Revision: 663444
- mass rebuild

* Sun Jan 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-12mdv2011.0
+ Revision: 627568
- don't force the usage of automake1.7

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-11mdv2011.0
+ Revision: 603876
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-10mdv2010.1
+ Revision: 518848
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-9mdv2010.0
+ Revision: 413292
- rebuild

* Sat Jan 31 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-8mdv2009.1
+ Revision: 335841
- rebuilt against new jbigkit major

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-7mdv2009.1
+ Revision: 318076
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-6mdv2009.0
+ Revision: 220547
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-5mdv2008.1
+ Revision: 149154
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdv2008.0
+ Revision: 75333
- fix deps (pixel)

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 1.2.1-3mdv2008.0
+ Revision: 69001
- fix description

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdv2008.0
+ Revision: 64154
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdv2008.0
+ Revision: 62520
- Import cups-drivers-magicolor5440dl



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdv2008.0
- initial Mandriva package
