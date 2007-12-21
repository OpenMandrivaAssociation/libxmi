%define	name	libxmi
%define	version	1.2
%define	release	%mkrel 1

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
  
%configure

%make

%install

%makeinstall

%find_lang %name

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%post -n %{libnamedev}
%_install_info %{name}.info

%postun -n %{libnamedev}
%_remove_install_info %{name}.info


%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname} -f %name.lang
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/*
%{_infodir}/*


