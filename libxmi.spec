%define	name	libxmi
%define	version	1.2
%define release 	7

%define fakename xmi

%define major 0
%define libname %mklibname %{fakename} %major
%define libnamedev %mklibname %{fakename} %major -d


Summary: Libxmi for library rasterizing 2-D vector graphics
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: System/Libraries
URL: http://www.gnu.org/software/libxmi/
Source: ftp://ftp.gnu.org/pub/gnu/libxmi/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot


%description
GNU libxmi is a C/C++ function library for rasterizing 2-D vector 
graphics. It can draw 2-D graphical primitives, including wide 
polygonal lines and circular and elliptical arcs, into a 
user-supplied matrix of pixels. Sophisticated line styles, such 
as multicolored dashing patterns, can be specified. There is also 
support for filling and texturing polygons.

%package -n %{libname}
Summary: Libxmi for library rasterizing 2-D vector graphics
Group: Development/Other
Provides: %{name} = %{version}

%description -n %{libname}
GNU libxmi is a C/C++ function library for rasterizing 2-D vector 
graphics. It can draw 2-D graphical primitives, including wide 
polygonal lines and circular and elliptical arcs, into a 
user-supplied matrix of pixels. Sophisticated line styles, such 
as multicolored dashing patterns, can be specified. There is also 
support for filling and texturing polygons.

%package -n %{libnamedev}
Summary: Libxmi for library rasterizing 2-D vector graphics
Group: Development/Other
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}

%description -n %{libnamedev}
libxmi devel files


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 

%build
autoreconf -fi
%configure

%make

%install

%makeinstall




%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname} 
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/*
%{_infodir}/*




%changelog
* Mon Apr 30 2012 Crispin Boylan <crisb@mandriva.org> 1.2-6
+ Revision: 794533
- Remove mkrel

* Sun Apr 29 2012 Crispin Boylan <crisb@mandriva.org> 1.2-5
+ Revision: 794444
- Rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2009.0
+ Revision: 250735
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.2-1mdv2008.1
+ Revision: 136571
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

