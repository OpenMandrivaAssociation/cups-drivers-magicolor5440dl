%define rname magicolor5440dl

Summary:	Cups Driver for KONICA MINOLTA magicolor 5440 DL
Name:		cups-drivers-%{rname}
Version:	1.2.1
Release:	29
License:	GPLv2
Group:		System/Printing
Url:		https://printer.konicaminolta.net/
Source0:	magicolor5440DL-%{version}.tar.gz
Patch0:		magicolor5440DL-shared_system_libs.diff
Patch1:		magicolor5440DL-1.2.1-automake-1.13.patch
Patch2:		magicolor5440DL-1.2.1-cups-2.2.patch
Patch3:		magicolor5440DL-lcms2.patch
BuildRequires:	cups-devel
BuildRequires:	jbig-devel
BuildRequires:	pkgconfig(lcms2)
Requires:	cups

%description
This package contains KONICA MINOLTA CUPS LavaFlow stream(PCL-like) filter
rastertokm5440dl and the PPD file. The filter converts CUPS raster data to
KONICA MINOLTA LavaFlow stream.

This package contains CUPS drivers (PPD) for the following printers:

 o KONICA MINOLTA magicolor 5440 DL printer

%prep
%setup -qn magicolor5440DL-%{version}
%patch0 -p0
%patch1 -p1 -b .automake-1_13
%patch2 -p1 -b .cups2_2
%patch3 -p1 -b .lcms2

# Fix copy of CUPS headers in kmlf.h
perl -pi -e 's:\bcups_strlcpy:_cups_strlcpy:g' src/kmlf.h

# Remove asterisks from group names in PPD file
gzip -dc src/km_en.ppd.gz | perl -p -e 's/(Group:\s+)\*/$1/g' | gzip > src/km_en.tmp.ppd.gz && mv -f src/km_en.tmp.ppd.gz src/km_en.ppd.gz

# Determine the directory for the CUPS filters using the correct method
perl -pi -e 's:(CUPS_SERVERBIN=)"\$libdir/cups":$1`cups-config --serverbin`:' configure*

rm -f configure
autoreconf -fi

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS COPYING ChangeLog
%{_prefix}/lib/cups/filter/rastertokm5440dl
%{_datadir}/KONICA_MINOLTA/mc5440DL
%{_datadir}/cups/model/KONICA_MINOLTA/km5440dl.ppd*
