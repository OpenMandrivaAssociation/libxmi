%define major 0
%define libname %mklibname xmi %{major}
%define libnamedev %mklibname xmi -d

Summary:	Libxmi for library rasterizing 2-D vector graphics
Name:		libxmi
Version:	1.2
Release:	10
License:	GPL
Group:		System/Libraries
URL:		http://www.gnu.org/software/libxmi/
Source0:	ftp://ftp.gnu.org/pub/gnu/libxmi/%{name}-%{version}.tar.bz2

%description
GNU libxmi is a C/C++ function library for rasterizing 2-D vector 
graphics. It can draw 2-D graphical primitives, including wide 
polygonal lines and circular and elliptical arcs, into a 
user-supplied matrix of pixels. Sophisticated line styles, such 
as multicolored dashing patterns, can be specified. There is also 
support for filling and texturing polygons.

%package -n %{libname}
Summary:	Libxmi for library rasterizing 2-D vector graphics
Group:		Development/Other
Provides:	%{name} = %{version}

%description -n %{libname}
GNU libxmi is a C/C++ function library for rasterizing 2-D vector 
graphics. It can draw 2-D graphical primitives, including wide 
polygonal lines and circular and elliptical arcs, into a 
user-supplied matrix of pixels. Sophisticated line styles, such 
as multicolored dashing patterns, can be specified. There is also 
support for filling and texturing polygons.

%package -n %{libnamedev}
Summary:	Libxmi for library rasterizing 2-D vector graphics
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Obsoletes:	%{mklibname xmi -d 0 } < 1.2-8

%description -n %{libnamedev}
libxmi devel files.


%prep

%setup -q 

%build
autoreconf -fi
%configure2_5x

%make

%install
%makeinstall_std

%files -n %{libname} 
%{_libdir}/*.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/*.so
%{_includedir}/*
%{_infodir}/*
