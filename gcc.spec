# functions with printf format attribute but with special parser and also
# receiving non constant format strings
%define		Werror_cflags			%{nil}

# avoid failures when testing if compiler used to build gcc can generate
# shared objects (regardless of unresolved symbols)
%define		_disable_ld_no_undefined	1

# avoid build failure due to configure built with different autoconf version
%define		_disable_libtoolize		1

#-----------------------------------------------------------------------
%define		snapshot		-20110506
%define		system_compiler		1
%define		branch			4.6
%define		alternatives		/usr/sbin/update-alternatives
%define		multilib_64		x86_64
%define		remove_alternatives	0
%define		obsolete_devmajor	0
%define		provide_libmajor	0
%if %mdkversion <= 201100
  %if %{system_compiler}
    %define	remove_alternatives	1
    %define	obsolete_devmajor	1
  %endif
  %ifarch %{multilib_64}
    %define	provide_libmajor	1
  %endif
%endif
%define		gccdir			%{_libdir}/gcc/%{_target_platform}/%{version}
%define		libdir32		%{_prefix}/lib

#-----------------------------------------------------------------------
%define		gcc_major		1
%define		libgcc			%mklibname gcc %{gcc_major}
%define		stdcxx_major		6
%define		libstdcxx		%mklibname stdc++ %{stdcxx_major}
%define		libstdcxx_devel		%mklibname -d stdc++
%define		libstdcxx_static_devel	%mklibname -d -s stdc++
%define		gcj_major		12
%define		libgcj			%mklibname gcj %{gcj_major}
%define		libgcj_devel		%mklibname -d gcj
%define		libgcj_static_devel	%mklibname -d -s gcj
%define		gcj_bc_major		1
%define		libgcj_bc		%mklibname gcj_bc %{gcj_bc_major}
%define		gfortran_major		3
%define		libgfortran		%mklibname gfortran %{gfortran_major}
%define		libgfortran_devel	%mklibname -d gfortran
%define		libgfortran_static_devel %mklibname -d -s gfortran
%define		ffi_major		4
%define		libffi			%mklibname ffi %{ffi_major}
%define		libffi_devel		%mklibname -d ffi
%define		libffi_static_devel	%mklibname -d -s ffi
%define		gnat_major		1
%define		libgnat			%mklibname gnat %{gnat_major}
%define		libgnat_devel		%mklibname -d gnat
%define		libgnat_static_devel	%mklibname -d -s gnat
%define		go_major		0
%define		libgo			%mklibname go %{go_major}
%define		libgo_devel		%mklibname -d go
%define		libgo_static_devel	%mklibname -d -s go
%define		gomp_major		1
%define		libgomp			%mklibname gomp %{gomp_major}
%define		libgomp_devel		%mklibname -d gomp
%define		libgomp_static_devel	%mklibname -d -s gomp
%define		mudflap_major		0
%define		libmudflap		%mklibname mudflap %{mudflap_major}
%define		libmudflap_devel	%mklibname -d mudflap
%define		libmudflap_static_devel %mklibname -d -s mudflap
%define		objc_major		3
%define		libobjc			%mklibname objc %{objc_major}
%define		libobjc_devel		%mklibname -d objc
%define		libobjc_static_devel	 %mklibname -d -s objc
%define		quadmath_major		0
%define		libquadmath		%mklibname quadmath %{quadmath_major}
%define		libquadmath_devel	%mklibname -d quadmath
%define		libquadmath_static_devel %mklibname -d -s quadmath
%define		ssp_major		0
%define		libssp			%mklibname ssp %{ssp_major}
%define		libssp_devel		%mklibname -d ssp
%define		libssp_static_devel 	%mklibname -d -s ssp

#-----------------------------------------------------------------------
%define		build_ada		0
%ifarch %{ix86} x86_64
  %define	build_ada		%{system_compiler}
%endif
%define		build_check		0
%define		build_cloog		%{system_compiler}
%define		build_cxx		%{system_compiler}
%define		build_doc		%{system_compiler}
%define		build_ffi		%{system_compiler}
%define		build_fortran		%{system_compiler}
%define		build_gomp		%{system_compiler}
%define		build_quadmath		%{build_fortran}
%define		build_mudflap		%{system_compiler}
%define		build_go		0
%ifarch %{ix86} x86_64
  %define	build_go		%{system_compiler}
%endif
%define		build_java		%{system_compiler}
%define		build_lto		1
%define		build_objc		0
%define		build_objcxx		0
%ifarch %{ix86} x86_64
  %define	build_objc		%{system_compiler}
  %define	build_objcxx		%{system_compiler}
%endif
%define		build_pdf		%{build_doc}
%define		build_ssp		0
%define		build_plugin		%{system_compiler}
%define		build_melt		0
%ifarch x86_64
  %define	build_melt		%{build_plugin}
%endif

#-----------------------------------------------------------------------
Name:		gcc
Version:	4.6.0
Release:	9
Summary:	GNU Compiler Collection
License:	GPLv3+ and GPLv3+ with exceptions and GPLv2+ with exceptions and LGPLv2+ and BSD
Group:		Development/C
URL:		http://gcc.gnu.org/
# http://gcc.gnu.org/mirrors.html
# <<mirror>>/snapshots/LATEST-4.6/gcc-4.6-20110422.tar.bz2
Source0:	gcc-%{branch}%{snapshot}.tar.bz2
Source1:	md5.sum

Source2:	http://gcc-melt.org/melt-0.7-plugin-for-gcc-4.6.tgz
#3672c1569ea95a27e0df5ad597ee7301

Source3:	c89
Source4:	c99
%if %{system_compiler}
Requires:	gcc-cpp >= %{version}-%{release}
Requires:	libgcc >= %{version}-%{release}
Requires:	libgomp >= %{version}-%{release}
%endif
BuildRequires:	binutils >= 2.20.51.0.2
Requires:	binutils >= 2.20.51.0.2
BuildRequires:	elfutils-devel >= 0.147
%if %mdkversion <= 201100
Obsoletes:	manbo-mandriva-files-gcc
%endif

# Ensure https://qa.mandriva.com/show_bug.cgi?id=62943
# have been addressed if using an older version
Requires:	glibc-devel >= 2.13

BuildRequires:	dejagnu
BuildRequires:	bison
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	gdb
BuildRequires:	gettext
BuildRequires:	sharutils
BuildRequires:	texinfo
%if %{build_doc}
BuildRequires:	texi2html
%endif
%if %{build_pdf}
BuildRequires:	texlive
%endif
BuildRequires:	zlib-devel
%if %{build_cloog}
BuildRequires:	ppl-devel >= 0.11
BuildRequires:	pwl-devel >= 0.11
BuildRequires:	ppl_c-devel >= 0.11
BuildRequires:	cloog-ppl-devel >= 0.16.1
%endif
%if %{remove_alternatives}
Requires(pre):	update-alternatives
%endif
Obsoletes:	gcc-doc
%if %mdkversion <= 201100
# force same urpmi transaction
Conflicts:	libgomp1 = 4.5.2
Conflicts:	libgomp-devel = 4.5.2
Conflicts:	gcc-c++ = 4.5.2
Conflicts:	libstdc++-devel = 4.5.2
Conflicts:	libstdc++-static-devel = 4.5.2
Conflicts:	gcc-gnat = 4.5.2
Conflicts:	libgnat1 = 4.5.2
Conflicts:	gcc-gfortran = 4.5.2
Conflicts:	libgfortran3 = 4.5.2
Conflicts:	gcc-java = 4.5.2
Conflicts:	gcc-objc = 4.5.2
Conflicts:	gcc-objc++ = 4.5.2
%endif

Patch0:		gcc-4.6.0-uclibc-ldso-path.patch
Patch1:		gcc-4.6.0-java-nomulti.patch
Patch2:		gcc-4.6.0-make-pdf.patch
Patch3:		gcc-4.6.0-linux32.patch

%description
The gcc package contains the GNU Compiler Collection version 4.6.

%if %{remove_alternatives}
%pre
if [ -f %{_bindir}/gcc ]; then %{alternatives} --remove-all gcc; fi
%endif

%if %{system_compiler}
%post
  %_install_info gcc.info
  %_install_info gccint.info
  %_install_info gccinstall.info

%preun
  %_remove_install_info gcc.info
  %_remove_install_info gccint.info
  %_remove_install_info gccinstall.info
%endif

%files
%defattr(-,root,root)
%if %{system_compiler}
%{_bindir}/cc
%{_bindir}/c89
%{_bindir}/c99
%{_bindir}/gcc
%{_bindir}/gcov
%{_bindir}/%{_target_platform}-gcc
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*
%{_mandir}/man7/*
%{_localedir}/*/LC_MESSAGES/gcc.mo
%{_infodir}/gcc.info*
%{_infodir}/gccint.info*
%{_infodir}/gccinstall.info*
%{_libdir}/libgcc_s.so
#%{_libdir}/libiberty.a
  %ifarch %{multilib_64}
%{libdir32}/libgcc_s.so
#%{libdir32}/libiberty.a
  %endif
%endif
%{_bindir}/gcc-%{version}
%{_bindir}/%{_target_platform}-gcc-%{version}
%dir %{gccdir}
%{gccdir}/cc1
%{gccdir}/collect2
%{gccdir}/*.o
%{gccdir}/libgcc*.a
%{gccdir}/libgcov.a
%if %{build_lto}
%{gccdir}/lto*
%{gccdir}/liblto*
%endif
%dir %{gccdir}/include
%{gccdir}/include/*.h
%if %{build_java}
%exclude %{gccdir}/include/jawt*.h
%exclude %{gccdir}/include/jni*.h
%exclude %{gccdir}/include/jvm*.h
%endif
%{gccdir}/install-tools
%if %{build_quadmath}
%exclude %{gccdir}/include/quadmath*.h
%endif
%if %{build_gomp}
%exclude %{gccdir}/include/omp*.h
%endif
%if %{build_mudflap}
%exclude %{gccdir}/include/mf-runtime.h
%endif
%ifarch %{multilib_64}
%dir %{gccdir}/32
%{gccdir}/32/*.o
%{gccdir}/32/libgcc*.a
%{gccdir}/32/libgcov.a
%endif
%if %{build_doc}
%doc %{_docdir}/gcc
%endif
%if %{build_check}
%doc test_summary.log
%endif

#-----------------------------------------------------------------------
%package	-n %{libgcc}
Summary:	GNU C library
Group:		System/Libraries
Provides:	libgcc = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgcc%{gcc_major} < %{version}-%{release}
Provides:	libgcc%{gcc_major} = %{version}-%{release}
%endif
%if %mdkversion <= 201100
Obsoletes:	libgcc3.0 < %{version}-%{release}
Obsoletes:	libgcc3.2 < %{version}-%{release}
Obsoletes:	libgcc4.5 < %{version}-%{release}
%endif

%description	-n %{libgcc}
The %{libgcc_name} package contains GCC shared libraries for gcc %{branch}

%files		-n %{libgcc}
%defattr(-,root,root)
%{_libdir}/libgcc_s.so.*
%ifarch %{multilib_64}
%{libdir32}/libgcc_s.so.*
%endif

########################################################################
%if %{build_plugin}
#-----------------------------------------------------------------------
%package	plugin-devel
Summary:	Headers to build gcc plugins
Group:		Development/C
Obsoletes:	gcc-plugins <= 4.5.2
Requires:	%{name} = %{version}-%{release}

%description	plugin-devel
This package contains header files and other support files
for compiling GCC plugins.  The GCC plugin ABI is currently
not stable, so plugins must be rebuilt any time GCC is updated.

%files		plugin-devel
%defattr(-,root,root,-)
%dir %{gccdir}/plugin
%{gccdir}/plugin/include
%if %{build_melt}
%exclude %{gccdir}/plugin/include/gimple-pretty-print.h
%exclude %{gccdir}/plugin/include/tree-pretty-print.h
%exclude %{gccdir}/plugin/include/realmpfr.h
%exclude %{gccdir}/plugin/include/melt*.h
%endif
#-----------------------------------------------------------------------
# build_plugin
%endif

########################################################################
%if %{build_melt}
#-----------------------------------------------------------------------
%package	plugin-melt
Summary:	Middle End Lisp Translator GCC plugin
Group:		Development/C
Requires:	gcc-plugin-devel = %{version}-%{release}
BuildRequires:	gcc-plugin-devel
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description	plugin-melt
GCC MELT is a GCC plugin providing a lispy domain specific
language to easily code GCC extensions in.

GCC MELT should interest any important software project
(coded in C, C++, Ada, Fortran, ...), compiled with GCC,
since it facilitates the development of customized GCC
extensions for:

* specific warnings or typechecks
* specific optimizations
* coding rules validation
* source code navigation or processing, in particular aspect
  oriented programming, retro-engineering or refactoring tasks
* Any processing taking advantage of powerful GCC internal
  representations of your source code.

%post		plugin-melt
  %_install_info meltplugin.info
  %_install_info meltpluginapi.info

%preun		plugin-melt
  %_remove_install_info meltplugin.info
  %_remove_install_info meltpluginapi.info

%files		plugin-melt
%defattr(-,root,root,-)
%{gccdir}/plugin/include/gimple-pretty-print.h
%{gccdir}/plugin/include/tree-pretty-print.h
%{gccdir}/plugin/include/realmpfr.h
%{gccdir}/plugin/include/melt*.h
%{gccdir}/plugin/libexec
%{gccdir}/plugin/melt*
%if %{system_compiler}
%{_infodir}/meltplugin*
%doc %{_docdir}/gcc-plugin-melt
%endif
#-----------------------------------------------------------------------
# build_melt
%endif

########################################################################
%if %{system_compiler}
#-----------------------------------------------------------------------
%package	cpp
Summary:	The C Preprocessor
Group:		Development/C
Provides:	cpp = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
%if %{remove_alternatives}
Requires(pre):	update-alternatives
%endif
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description	cpp
Cpp is the GNU C-Compatible Compiler Preprocessor.
Cpp is a macro processor which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define macros, abbreviations for longer
constructs.

The C preprocessor provides four separate functionalities:

* Inclusion of header files. These are files of declarations that can be
  substituted into your program.
* Macro expansion. You can define 'macros,' which are abbreviations for 
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation. Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control. If you use a program to combine or rearrange source files
  into an intermediate file which is then compiled, you can use line
  control to inform the compiler about where each source line originated.

%if %{remove_alternatives}
%pre		cpp
if [ -f %{_bindir}/cpp ]; then %{alternatives} --remove-all cpp; fi
%endif

%post		cpp
  %_install_info cpp.info

%preun		cpp
  %_remove_install_info cpp.info

%files		cpp
%defattr(-,root,root)
/lib/cpp
%{_bindir}/cpp
%{_mandir}/man1/cpp.1*
%{_infodir}/cpp*
%if %{build_doc}
%doc %{_docdir}/gcc-cpp
%endif
%{_localedir}/*/LC_MESSAGES/cpplib.mo
#-----------------------------------------------------------------------
# system_compiler
%endif

########################################################################
%if %{build_cxx}
#-----------------------------------------------------------------------
%package	c++
Summary:	C++ support for gcc
Group:		Development/C++
Requires:	%{name} = %{version}-%{release}
%if %{system_compiler}
Requires:	%{libstdcxx_devel} = %{version}
%endif
%if %{remove_alternatives}
Requires(pre):	update-alternatives
%endif
%if %mdkversion <= 201100
Obsoletes:	manbo-mandriva-files-g++
%endif

%description	c++
This package adds C++ support to the GNU Compiler Collection.
It includes support for most of the current C++ specification,
including templates and exception handling.

%if %{remove_alternatives}
%pre		c++
if [ -f %{_bindir}/c++ ]; then %{alternatives} --remove-all c++; fi
if [ -f %{_bindir}/g++ ]; then %{alternatives} --remove-all g++; fi
%endif

%files		c++
%defattr(-,root,root)
%if %{system_compiler}
%{_bindir}/c++
%{_bindir}/g++
%{_mandir}/man1/g++.1*
%endif
%{_bindir}/c++-%{version}
%{_bindir}/g++-%{version}
%{_bindir}/%{_target_platform}-g++-%{version}
%{gccdir}/cc1plus

#-----------------------------------------------------------------------
%package	-n %{libstdcxx}
Summary:	GNU Standard C++ library
Group:		System/Libraries
Provides:	libstdc++ = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libstdc++%{stdcxx_major} < %{version}-%{release}
Provides:	libstdc++%{stdcxx_major} = %{version}-%{release}
%endif
%if %{build_doc}
BuildRequires:	doxygen
BuildRequires:	graphviz
%endif

%description	-n %{libstdcxx}
The libstdc++ package contains a rewritten standard compliant
GCC Standard C++ Library.

%files		-n %{libstdcxx}
%defattr(-,root,root)
%{_libdir}/libstdc++.so.*
%ifarch %{multilib_64}
%{libdir32}/libstdc++.so.*
%endif
%if %{system_compiler}
%{_localedir}/*/LC_MESSAGES/libstdc++.mo
%endif
%if %{build_doc}
%doc %{_docdir}/libstdc++
%endif

#-----------------------------------------------------------------------
%package	-n %{libstdcxx_devel}
Summary:	Header files and libraries for C++ development
Group:		Development/C++
Requires:	%{libstdcxx} = %{version}-%{release}
Provides:	libstdc++-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libstdc++-devel < %{version}-%{release}
%endif
%if %{obsolete_devmajor}
Obsoletes:	libstdc++4.5-devel
Obsoletes:	libstdc++%{stdcxx_major}-devel
%endif

%description	-n %{libstdcxx_devel}
This is the GNU implementation of the standard C++ libraries.  This
package includes the header files and libraries needed for C++
development. This includes rewritten implementation of STL.

%files		-n %{libstdcxx_devel}
%defattr(-,root,root)
%{_includedir}/c++/%{version}
%{_libdir}/libstdc++.la
%{_libdir}/libstdc++.so
%ifarch %{multilib_64}
%{libdir32}/libstdc++.la
%{libdir32}/libstdc++.so
%endif
%{py_puresitedir}/libstdcxx

#-----------------------------------------------------------------------
%package	-n %{libstdcxx_static_devel}
Summary:	Static libraries for the GNU standard C++ library
Group:		Development/C++
Requires:	%{libstdcxx_devel} = %{version}-%{release}
Provides:	libstdc++-static-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libstdc++-static-devel < %{version}-%{release}
%endif
%if %{obsolete_devmajor}
Obsoletes:	libstdc++4.5-static-devel
Obsoletes:	libstdc++%{stdcxx_major}-static-devel
%endif

%description	-n %{libstdcxx_static_devel}
Static libraries for the GNU standard C++ library.

%files		-n %{libstdcxx_static_devel}
%defattr(-,root,root)
%{_libdir}/libstdc++.a
%{_libdir}/libsupc++.a
%{_libdir}/libsupc++.la
%ifarch %{multilib_64}
%{libdir32}/libstdc++.a
%{libdir32}/libsupc++.a
%{libdir32}/libsupc++.la
%endif
#-----------------------------------------------------------------------
# build_cxx
%endif

########################################################################
%if %{build_ada}
#-----------------------------------------------------------------------
%package	gnat
Summary:	Ada 95 support for gcc
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libgnat_devel} = %{version}-%{release}
# no bootstrap support
BuildRequires:	gcc-gnat >= 3.1, libgnat >= 3.1

%description	gnat
GNAT is a GNU Ada 95 front-end to GCC. This package includes development
tools, the documents and Ada 95 compiler.

%post		gnat
for info in _rm ugn -stype; do
    %_install_info gnat${info}.info
done

%preun		gnat
for info in _rm ugn -stype; do
    %_remove_install_info gnat${info}.info
done

%files		gnat
%defattr(-,root,root)
%{_bindir}/gnat*
%exclude %{_bindir}/gnative2ascii
%{gccdir}/gnat1
%{_infodir}/gnat*
%if %{build_doc}
%doc %{_docdir}/gcc-gnat
%endif

#-----------------------------------------------------------------------
%package	-n %{libgnat}
Summary:	GNU Ada 95 runtime libraries
Group:		System/Libraries
Provides:	libgnat = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgnat%{gnat_major} < %{version}-%{release}
Provides:	libgnat%{gnat_major} = %{version}-%{release}
%endif
Obsoletes:	gnat-runtime

%description	-n %{libgnat}
GNAT is a GNU Ada 95 front-end to GCC. This package includes shared
libraries, which are required to run programs compiled with the GNAT.

%files		-n %{libgnat}
%defattr(-,root,root)
%{_libdir}/libgnat-%{branch}.so.*
%{_libdir}/libgnarl-%{branch}.so.*
%ifarch %{multilib_64}
%{libdir32}/libgnat-%{branch}.so.*
%{libdir32}/libgnarl-%{branch}.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libgnat_devel}
Summary:	GNU Ada 95 libraries
Group:		Development/Other
Requires:	%{libgnat} = %{version}-%{release}
Provides:	libgnat-devel = %{version}-%{release}

%description	-n %{libgnat_devel}
GNAT is a GNU Ada 95 front-end to GCC. This package includes shared
libraries, which are required to compile with the GNAT.

%files		-n %{libgnat_devel}
%defattr(-,root,root)
%{_libdir}/libgnat*.so
%{_libdir}/libgnarl*.so
%{gccdir}/adalib
%{gccdir}/adainclude
%exclude %{gccdir}/adalib/lib*.a
%ifarch %{multilib_64}
%{libdir32}/libgnat*.so
%{libdir32}/libgnarl*.so
%{gccdir}/32/adalib
%{gccdir}/32/adainclude
%exclude %{gccdir}/32/adalib/lib*.a
%endif

#-----------------------------------------------------------------------
%package	-n %{libgnat_static_devel}
Summary:	GNU Ada 95 static libraries
Group:		Development/Other
Requires:	%{libgnat_devel} = %{version}-%{release}
Provides:	libgnat-static-devel = %{version}-%{release}

%description	-n %{libgnat_static_devel}
GNAT is a GNU Ada 95 front-end to GCC. This package includes static
libraries.

%files		-n %{libgnat_static_devel}
%defattr(-,root,root)
%{gccdir}/adalib/lib*.a
%ifarch %{multilib_64}
%{gccdir}/32/adalib/lib*.a
%endif
#-----------------------------------------------------------------------
# build ada
%endif

########################################################################
%if %{build_fortran}
#-----------------------------------------------------------------------
%package	gfortran
Summary:	Fortran 95 support for gcc
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libgfortran_devel} = %{version}-%{release}
BuildRequires:	gmp-devel, mpfr-devel, libmpc-devel
%if %{system_compiler}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif
%if %mdkversion <= 201100
Obsoletes:	manbo-mandriva-files-gfortran
%endif

%description	gfortran
The gcc-gfortran package provides support for compiling Fortran
programs with the GNU Compiler Collection.

%if %{system_compiler}
%post		gfortran
  %_install_info gfortran.info

%preun	gfortran
  %_remove_install_info gfortran.info
%endif

%files		gfortran
%defattr(-,root,root)
%if %{system_compiler}
%{_bindir}/gfortran
%{_infodir}/gfortran.info*
%{_mandir}/man1/gfortran.1*
%endif
%{_bindir}/gfortran-%{version}
%{_bindir}/%{_target_platform}-gfortran-%{version}
%{gccdir}/f951
%{gccdir}/finclude
%{gccdir}/libgfortranbegin.*
%ifarch %{multilib_64}
%{gccdir}/32/libgfortranbegin.*
%endif
%if %{build_doc}
%doc %{_docdir}/gcc-gfortran
%endif

#-----------------------------------------------------------------------
%package	-n %{libgfortran}
Summary:	Fortran 95 runtime libraries
Group:		System/Libraries
Provides:	libgfortran = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgfortran%{gfortran_major} < %{version}-%{release}
Provides:	libgfortran%{gfortran_major} = %{version}-%{release}
%endif
%if %mdkversion <= 201100
Obsoletes:	libgfortran4.5 < %{version}-%{release}
%endif
%if %{build_quadmath}
Requires:	%{libquadmath} = %{version}-%{release}
%endif

%description	-n %{libgfortran}
This package contains Fortran 95 shared library which is needed to run
Fortran 95 dynamically linked programs.

%files		-n %{libgfortran}
%defattr(-,root,root)
%{_libdir}/libgfortran.so.*
%ifarch %{multilib_64}
%{libdir32}/libgfortran.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libgfortran_devel}
Summary:	Fortran 95 libraries
Group:		System/Libraries
Requires:	%{libgfortran} = %{version}-%{release}
Provides:	libgfortran-devel = %{version}-%{release}
%if %{build_quadmath}
Requires:	%{libquadmath_devel} = %{version}-%{release}
%endif

%description	-n %{libgfortran_devel}
This package contains Fortran 95 shared library which is needed to
compile Fortran 95 programs.

%files		-n %{libgfortran_devel}
%defattr(-,root,root)
%{_libdir}/libgfortran.la
%{_libdir}/libgfortran.so
%{_libdir}/libgfortran.spec
%ifarch %{multilib_64}
%{libdir32}/libgfortran.la
%{libdir32}/libgfortran.so
%{libdir32}/libgfortran.spec
%endif

#-----------------------------------------------------------------------
%package	-n %{libgfortran_static_devel}
Summary:	Fortran 95 static libraries
Group:		System/Libraries
Requires:	%{libgfortran_devel} = %{version}-%{release}
Provides:	libgfortran-static-devel = %{version}-%{release}

%description	-n %{libgfortran_static_devel}
This package contains Fortran 95 static library which is needed to
compile Fortran 95 programs.

%files		-n %{libgfortran_static_devel}
%defattr(-,root,root)
%{_libdir}/libgfortran.a
%ifarch %{multilib_64}
%{libdir32}/libgfortran.a
%endif
#-----------------------------------------------------------------------
# build fortran
%endif

########################################################################
%if %{build_go}
#-----------------------------------------------------------------------
%package	go
Summary:	Go support for gcc
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libgo_devel} = %{version}-%{release}
%if %{system_compiler}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
%endif

%description	go
The gcc-go package provides support for compiling Go programs
with the GNU Compiler Collection.

%if %{system_compiler}
%post		go
  %_install_info gccgo.info

%preun	go
  %_remove_install_info gccgo.info
%endif

%files		go
%defattr(-,root,root)
%if %{system_compiler}
%{_bindir}/gccgo
%dir %{_libdir}/go
  %ifarch %{multilib_64}
%dir %{libdir32}/go
  %endif
%{_infodir}/gccgo.info*
%{_mandir}/man1/gccgo.1*
%endif
%{_bindir}/gccgo-%{version}
%{_bindir}/%{_target_platform}-gccgo-%{version}
%{gccdir}/go1
%{_libdir}/go/%{version}
%{_libdir}/libgobegin.a
%ifarch %{multilib_64}
%{libdir32}/go/%{version}
%{libdir32}/libgobegin.a
%endif
%if %{build_doc}
%doc %{_docdir}/gcc-go
%endif

#-----------------------------------------------------------------------
%package	-n %{libgo}
Summary:	Go runtime libraries
Group:		System/Libraries
Provides:	libgo = %{version}-%{release}

%description	-n %{libgo}
This package contains Go shared library which is needed to run
Go dynamically linked programs.

%files		-n %{libgo}
%defattr(-,root,root)
%{_libdir}/libgo.so.*
%ifarch %{multilib_64}
%{libdir32}/libgo.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libgo_devel}
Summary:	Go development libraries
Group:		Development/Other
Requires:	%{libgo} = %{version}-%{release}
Provides:	libgo-devel = %{version}-%{release}

%description	-n %{libgo_devel}
This package includes libraries and support files for compiling
Go programs.

%files		-n %{libgo_devel}
%defattr(-,root,root)
%{_libdir}/libgo.la
%{_libdir}/libgo.so
%ifarch %{multilib_64}
%{libdir32}/libgo.la
%{libdir32}/libgo.so
%endif

#-----------------------------------------------------------------------
%package	-n %{libgo_static_devel}
Summary:	Static Go libraries
Group:		Development/Other
Requires:	%{libgo_devel} = %{version}-%{release}
Provides:	libgo-static-devel = %{version}-%{release}

%description	-n %{libgo_static_devel}
This package contains static Go libraries.

%files		-n %{libgo_static_devel}
%defattr(-,root,root)
%defattr(-,root,root)
%{_libdir}/libgo.a
%ifarch %{multilib_64}
%{libdir32}/libgo.a
%endif
#-----------------------------------------------------------------------
# build go
%endif

########################################################################
%if %{build_java}
#-----------------------------------------------------------------------
%package	java
Summary:	Java support for GCC
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	%{libgcj_devel} = %{version}-%{release}
Requires:	eclipse-ecj
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
BuildRequires:	eclipse-ecj
BuildRequires:	jpackage-utils
BuildRequires:	unzip
BuildRequires:	zip
%if %mdkversion <= 201100
Obsoletes:	manbo-mandriva-files-java
%endif

%description	java
This package adds support for compiling Java(tm) programs and
bytecode into native code.

%post		java
  %_install_info gcj.info

%preun		java
  %_remove_install_info gcj.info

%files java
%defattr(-,root,root,-)
%{_bindir}/gcj
%{_bindir}/gjavah
%{_bindir}/gcjh
%{_bindir}/jcf-dump
%{_mandir}/man1/gcj.1*
%{_mandir}/man1/jcf-dump.1*
%{_mandir}/man1/gjavah.1*
%{_mandir}/man1/gcjh.1*
%{_infodir}/gcj.info*
%{_bindir}/gcj-%{version}
%{_bindir}/%{_target_platform}-gcj-%{version}
%{gccdir}/jc1
%{gccdir}/ecj1
%{gccdir}/jvgenmain
%if %{build_doc}
%doc %{_docdir}/gcc-java
%endif

#-----------------------------------------------------------------------
%package	-n %{libgcj}
Summary:	Java runtime library for gcc
Group:		System/Libraries
Provides:	gcj-tools = %{version}-%{release}
Provides:	libgcj = %{version}-%{release}
Provides:	%{libgcj_bc} = %{version}-%{release}
%if %{provide_libmajor}
Provides:	libgcj%{gcj_major} = %{version}-%{release}
%endif
%if %mdkversion <= 201100
Obsoletes:	libgcj_bc%{gcj_bc_major} < %{version}-%{release}
Provides:	libgcj_bc%{gcj_bc_major} = %{version}-%{release}
Provides:	libgcj%{gcj_major}-base = %{version}-%{release}
Provides:	%{libgcj}-base = %{version}-%{release}
Obsoletes:	gcc-libgcj
Obsoletes:	libgcj4.5 < %{version}-%{release}
Obsoletes:	gcj4.5-tools
Obsoletes:	gcj-tools <= 4.5.2
Obsoletes:	%{mklibname gcj 11}
Obsoletes:	%{mklibname gcj 11}-base
%endif
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires:	gtk2 >= 2.4.0
Requires:	glib2 >= 2.4.0
Requires:	libart_lgpl >= 2.1.0
Requires:	zip >= 2.1
BuildRequires:	antlr
BuildRequires:	gtk2-devel >= 2.4.0
BuildRequires:	glib2-devel >= 2.4.0
BuildRequires:	libart_lgpl-devel >= 2.1.0
BuildRequires:	alsa-lib-devel
BuildRequires:	libxtst-devel
BuildRequires:	libxt-devel
BuildRequires:	qt4-devel

%description	-n %{libgcj}
The Java(tm) runtime library. You will need this package to run your Java
programs compiled using the Java compiler from GNU Compiler Collection (gcj).

%post		-n %{libgcj}
  %_install_info cp-tools.info

%preun		-n %{libgcj}
  %_remove_install_info cp-tools.info

%files		-n %{libgcj}
%defattr(-,root,root,-)
%{_bindir}/aot-compile
%{_bindir}/jv-convert
%{_bindir}/gappletviewer
%{_bindir}/gc-analyze
%{_bindir}/gij
%{_bindir}/gjar
%{_bindir}/gjdoc
%{_bindir}/gnative2ascii
%{_bindir}/grmic
%{_bindir}/grmid
%{_bindir}/grmiregistry
%{_bindir}/gtnameserv
%{_bindir}/gkeytool
%{_bindir}/gorbd
%{_bindir}/gserialver
%{_bindir}/gcj-dbtool
%{_bindir}/gjarsigner
%{_bindir}/rebuild-gcj-db
%{_mandir}/man1/aot-compile.1*
%{_mandir}/man1/gappletviewer.1*
%{_mandir}/man1/gc-analyze.1*
%{_mandir}/man1/gjdoc.1*
%{_mandir}/man1/gnative2ascii.1*
%{_mandir}/man1/gjar.1*
%{_mandir}/man1/gjarsigner.1*
%{_mandir}/man1/jv-convert.1*
%{_mandir}/man1/gij.1*
%{_mandir}/man1/grmic.1*
%{_mandir}/man1/grmiregistry.1*
%{_mandir}/man1/gcj-dbtool.1*
%{_mandir}/man1/gkeytool.1*
%{_mandir}/man1/gorbd.1*
%{_mandir}/man1/grmid.1*
%{_mandir}/man1/gserialver.1*
%{_mandir}/man1/gtnameserv.1*
%{_mandir}/man1/rebuild-gcj-db.1*
%{_infodir}/cp-tools.info*
%{_javadir}/libgcj*.jar
%dir %{_libdir}/gcj-%{version}-12
%{_libdir}/gcj-%{version}-12/*.so
%attr(0644,root,root) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{_libdir}/gcj-%{version}-12/classmap.db
%{_libdir}/libgcj*.so.*
%{_libdir}/libgij.so.*
%{_libdir}/logging.properties
%{_libdir}/security
%if %{build_pdf}
%doc %{_docdir}/libjava
%endif

#-----------------------------------------------------------------------
%package	-n %{libgcj_devel}
Summary:	Libraries for Java development using GCC
Group:		Development/Java
Provides:	libgcj-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgcj-devel < %{version}-%{release}
%endif
Requires:	%{libgcj} = %{version}-%{release}
Requires:	zlib-devel
Requires:	awk

%description	-n %{libgcj_devel}
The Java(tm) static libraries and C header files. You will need this
package to compile your Java programs using the GCC Java compiler (gcj).

%files		-n %{libgcj_devel}
%defattr(-,root,root,-)
%{gccdir}/include/gcj
%{gccdir}/include/jawt*.h
%{gccdir}/include/jni*.h
%{gccdir}/include/jvm*.h
%{py_puresitedir}/libjava
%{_libdir}/pkgconfig/libgcj-%{branch}.pc
%{_libdir}/gcj-%{version}-12/*.la
%{_libdir}/libgcj*.spec
%{_libdir}/libgcj*.la
%{_libdir}/libgcj*.so
%{_libdir}/libgij.la
%{_libdir}/libgij.so

#-----------------------------------------------------------------------
%package	-n %{libgcj_static_devel}
Summary:	Static Libraries for Java development using GCC
Group:		Development/Other
Requires:	%{libgcj_devel} = %{version}-%{release}
Provides:	libgcj-static-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgcj-static-devel < %{version}-%{release}
%endif

%description	-n %{libgcj_static_devel}
Static Libraries for Java development using GCC.

%files		-n %{libgcj_static_devel}
%defattr(-,root,root)
%{_libdir}/libgcj*.a
%{_libdir}/libgij.a
%{_libdir}/gcj-%{version}-12/*.a

#-----------------------------------------------------------------------
%package	-n libgcj%{gcj_major}-src
Summary:	Java library sources
Group:		Development/Java
Provides:	libgcj-src = %{version}-%{release}
Requires:	%{libgcj} = %{version}-%{release}

%description	-n libgcj%{gcj_major}-src
The Java(tm) runtime library sources.

%files	-n libgcj%{gcj_major}-src
%defattr(-,root,root)
%{_javadir}/src-%{version}.zip
#-----------------------------------------------------------------------
# build java
%endif

########################################################################
%if %{build_objc}
#-----------------------------------------------------------------------
%package	objc
Summary:	Objective-C support for GCC
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}
Requires:	%{libobjc_devel} = %{version}-%{release}

%description	objc
gcc-objc provides Objective-C support for the GCC.
Mainly used on systems running NeXTSTEP, Objective-C is an
object-oriented derivative of the C language.

%files		objc
%defattr(-,root,root)
%{gccdir}/cc1obj

#-----------------------------------------------------------------------
%package	-n %{libobjc}
Summary:	Objective-C runtime
Group:		System/Libraries
Provides:	libobjc = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libobjc%{objc_major} < %{version}-%{release}
Provides:	libobjc%{objc_major} = %{version}-%{release}
%endif
%if %mdkversion <= 201100
Obsoletes:	libobjc3.0 < %{version}-%{release}
Obsoletes:	libobjc3.1 < %{version}-%{release}
%endif

%description	-n %{libobjc}
This package contains Objective-C shared library which is needed to run
Objective-C dynamically linked programs.

%files		-n %{libobjc}
%defattr(-,root,root)
%{_libdir}/libobjc.so.*
%ifarch %{multilib_64}
%{libdir32}/libobjc.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libobjc_devel}
Summary:	Objective-C development libraries
Group:		Development/Other
Requires:	%{libobjc} = %{version}-%{release}
Provides:	libobjc-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libobjc-devel < %{version}-%{release}
%endif

%description	-n %{libobjc_devel}
This package includes libraries and support files for compiling
Objective-C programs.

%files		-n %{libobjc_devel}
%defattr(-,root,root)
%{_libdir}/libobjc.la
%{_libdir}/libobjc.so
%{gccdir}/include/objc
%ifarch %{multilib_64}
%{libdir32}/libobjc.la
%{libdir32}/libobjc.so
%endif

#-----------------------------------------------------------------------
%package	-n %{libobjc_static_devel}
Summary:	Static Objective-C libraries
Group:		Development/Other
Requires:	%{libobjc_devel} = %{version}-%{release}
Provides:	libobjc-static-devel = %{version}-%{release}

%description	-n %{libobjc_static_devel}
This package contains static Objective-C libraries.

%files		-n %{libobjc_static_devel}
%defattr(-,root,root)
%{_libdir}/libobjc.a
%ifarch %{multilib_64}
%{libdir32}/libobjc.a
%endif
#-----------------------------------------------------------------------
# build objc
%endif

########################################################################
%if %{build_objcxx}
#-----------------------------------------------------------------------
%package	objc++
Summary:	Objective-C++ support for GCC
Group:		Development/Other
Requires:	gcc-objc = %{version}-%{release}

%description	objc++
gcc++-objc provides Objective-C++ support for the GCC.

%files		objc++
%defattr(-,root,root)
%{gccdir}/cc1objplus
#-----------------------------------------------------------------------
# build objcxx
%endif

########################################################################
%if %{build_ffi}
#-----------------------------------------------------------------------
%package	-n %{libffi}
Summary:	GCC support library for FFI
Group:		System/Libraries
Provides:	libffi = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libffi%{ffi_major} < %{version}-%{release}
Provides:	libffi%{ffi_major} = %{version}-%{release}
%endif

%description	-n %{libffi}
This package contains GCC shared support library which is needed
for FFI support.

%files		-n %{libffi}
%defattr(-,root,root)
%{_libdir}/libffi.so.*
%ifarch %{multilib_64}
%{libdir32}/libffi.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libffi_devel}
Summary:	GCC development for FFI
Group:		Development/C
Requires:	%{libffi} = %{version}-%{release}
Provides:	libffi-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libffi-devel < %{version}-%{release}
%endif
%if %{obsolete_devmajor}
Obsoletes:	libffi%{ffi_major}-devel < %{version}-%{release}
%endif
Requires:	%{name} = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description	-n %{libffi_devel}
This package contains GCC development which is needed
to compile FFI support.

%post		-n %{libffi_devel}
  %_install_info libffi.info

%preun		-n %{libffi_devel}
  %_remove_install_info libffi.info

%files		-n %{libffi_devel}
%defattr(-,root,root)
%{_libdir}/libffi.la
%{_libdir}/libffi.so
%ifarch %{multilib_64}
%{libdir32}/libffi.la
%{libdir32}/libffi.so
%endif
%if %{system_compiler}
%{_mandir}/man3/*.3*
%endif

#-----------------------------------------------------------------------
%package	-n %{libffi_static_devel}
Summary:	GCC FFI static library
Group:		Development/C
Requires:	%{libffi_devel} = %{version}-%{release}
Provides:	libffi-static-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libffi-static-devel < %{version}-%{release}
%endif

%description	-n %{libffi_static_devel}
This package contains GCC static libraries which are needed
to compile FFI support.

%files		-n %{libffi_static_devel}
%defattr(-,root,root)
%{_libdir}/libffi.a
%ifarch %{multilib_64}
%{libdir32}/libffi.a
%endif
#-----------------------------------------------------------------------
# build ffi
%endif

########################################################################
%if %{build_quadmath}
#-----------------------------------------------------------------------
%package	-n %{libquadmath}
Summary:	GCC __float128 shared support library
Group:		System/Libraries
%if %{provide_libmajor}
Obsoletes:	libquadmath%{quadmath_major} < %{version}-%{release}
Provides:	libquadmath%{quadmath_major} = %{version}-%{release}
%endif
Provides:	libquadmath = %{version}-%{release}

%description	-n %{libquadmath}
This package contains GCC shared support library which is needed
for __float128 math support and for Fortran REAL*16 support.

%files		-n %{libquadmath}
%defattr(-,root,root)
%{_libdir}/libquadmath.so.*
%ifarch %{multilib_64}
%{libdir32}/libquadmath.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libquadmath_devel}
Summary:	GCC __float128 support
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{libquadmath} = %{version}-%{release}
Provides:	libquadmath-devel = %{version}-%{release}
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description	-n %{libquadmath_devel}
This package contains support for building Fortran programs using
REAL*16 and programs using __float128 math.

%post		-n %{libquadmath_devel}
  %_install_info libquadmath.info

%preun		-n %{libquadmath_devel}
  %_remove_install_info libquadmath.info

%files		-n %{libquadmath_devel}
%defattr(-,root,root)
%{_libdir}/libquadmath.la
%{_libdir}/libquadmath.so
%ifarch %{multilib_64}
%{libdir32}/libquadmath.la
%{libdir32}/libquadmath.so
%endif
%if %{system_compiler}
%{_infodir}/libquadmath.info*
%endif
%{gccdir}/include/quadmath*.h
%if %{build_pdf}
%doc %{_docdir}/libquadmath
%endif

#-----------------------------------------------------------------------
%package	-n %{libquadmath_static_devel}
Summary:	Static libraries for __float128 support
Group:		Development/C
Requires:	%{libquadmath_devel} = %{version}-%{release}
Provides:	libquadmath-static-devel = %{version}-%{release}

%description	-n %{libquadmath_static_devel}
This package contains static libraries for building Fortran programs
using REAL*16 and programs using __float128 math.

%files		-n %{libquadmath_static_devel}
%defattr(-,root,root)
%{_libdir}/libquadmath.a
%ifarch %{multilib_64}
%{libdir32}/libquadmath.a
%endif
#-----------------------------------------------------------------------
# build quadmath
%endif

########################################################################
%if %{build_gomp}
#-----------------------------------------------------------------------
%package	-n %{libgomp}
Summary:	GCC OpenMP v3.0 shared support library
Group:		System/Libraries
Provides:	libgomp = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgomp%{gomp_major} < %{version}-%{release}
Provides:	libgomp%{gomp_major} = %{version}-%{release}
%endif

%description	-n %{libgomp}
This package contains GCC shared library which is needed
for OpenMP v3.0 support.

%files		-n %{libgomp}
%defattr(-,root,root)
%{_libdir}/libgomp.so.*
%ifarch %{multilib_64}
%{libdir32}/libgomp.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libgomp_devel}
Summary:	GCC OpenMP v3.0 development support
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{libgomp} = %{version}-%{release}
Provides:	libgomp-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgomp-devel < %{version}-%{release}
%endif
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info

%description	-n %{libgomp_devel}
This package contains GCC development which is needed
to compile OpenMP v3.0 support.

%post		-n %{libgomp_devel}
  %_install_info libgomp.info

%preun		-n %{libgomp_devel}
  %_remove_install_info libgomp.info

%files		-n %{libgomp_devel}
%defattr(-,root,root)
%{_libdir}/libgomp.la
%{_libdir}/libgomp.so
%{_libdir}/libgomp.spec
%ifarch %{multilib_64}
%{libdir32}/libgomp.la
%{libdir32}/libgomp.so
%{libdir32}/libgomp.spec
%endif
%if %{system_compiler}
%{_infodir}/libgomp.info*
%endif
%{gccdir}/include/omp*.h
%if %{build_pdf}
%doc %{_docdir}/libgomp
%endif

#-----------------------------------------------------------------------
%package	-n %{libgomp_static_devel}
Summary:	GCC OpenMP v3.0 static library
Group:		Development/C
Requires:	%{libgomp_devel} = %{version}-%{release}
Provides:	libgomp-static-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libgomp-static-devel < %{version}-%{release}
%endif

%description	-n %{libgomp_static_devel}
This package contains GCC static libraries which are needed
to compile OpenMP v3.0 support.

%files		-n %{libgomp_static_devel}
%defattr(-,root,root)
%{_libdir}/libgomp.a
%ifarch %{multilib_64}
%{libdir32}/libgomp.a
%endif
#-----------------------------------------------------------------------
# build gomp
%endif

########################################################################
%if %{build_mudflap}
#-----------------------------------------------------------------------
%package	-n %{libmudflap}
Summary:	GCC mudflap shared support libraries
Group:		System/Libraries
Provides:	libmudflap = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libmudflap%{mudflap_major} < %{version}-%{release}
Provides:	libmudflap%{mudflap_major} = %{version}-%{release}
%endif

%description	-n %{libmudflap}
This package contains GCC shared libraries which are needed
for mudflap support.

For front-ends that support it (C and C++), instrument all risky
pointer/array dereferencing operations, some standard library
string/heap functions, and some other associated constructs with
range/validity tests.  Modules so instrumented should be immune to
buffer overflows, invalid heap use, and some other classes of C/C++
programming errors.

%files		-n %{libmudflap}
%defattr(-,root,root)
%{_libdir}/libmudflap.so.*
%{_libdir}/libmudflapth.so.*
%ifarch %{multilib_64}
%{libdir32}/libmudflap.so.*
%{libdir32}/libmudflapth.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libmudflap_devel}
Summary:	GCC mudflap development support
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{libmudflap} = %{version}-%{release}
Provides:	libmudflap-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libmudflap-devel < %{version}-%{release}
%endif

%description	-n %{libmudflap_devel}
This package contains GCC libraries which are needed
to compile mudflap support.

%files		-n %{libmudflap_devel}
%defattr(-,root,root)
%{_libdir}/libmudflap.la
%{_libdir}/libmudflap.so
%{_libdir}/libmudflapth.la
%{_libdir}/libmudflapth.so
%ifarch %{multilib_64}
%{libdir32}/libmudflap.la
%{libdir32}/libmudflap.so
%{libdir32}/libmudflapth.la
%{libdir32}/libmudflapth.so
%endif
%{gccdir}/include/mf-runtime.h

#-----------------------------------------------------------------------
%package	-n %{libmudflap_static_devel}
Summary:	GCC mudflap static libraries
Group:		Development/C
Requires:	%{libmudflap_devel} = %{version}-%{release}
Provides:	libmudflap-static-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libmudflap-static-devel < %{version}-%{release}
%endif

%description	-n %{libmudflap_static_devel}
This package contains GCC static libraries which are needed
to compile mudflap support.

%files		-n %{libmudflap_static_devel}
%defattr(-,root,root)
%{_libdir}/libmudflap.a
%{_libdir}/libmudflapth.a
%ifarch %{multilib_64}
%{libdir32}/libmudflap.a
%{libdir32}/libmudflapth.a
%endif
#-----------------------------------------------------------------------
# build mudflap
%endif

########################################################################
%if %{build_ssp}
#-----------------------------------------------------------------------
%package	-n %{libssp}
Summary:	GCC SSP shared support library
Group:		System/Libraries
Provides:	libssp = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libssp%{ssp_major} < %{version}-%{release}
Provides:	libssp%{ssp_major} = %{version}-%{release}
%endif

%description	-n %{libssp}
%description -n %{libssp_name}
This package contains GCC shared support library which is needed
for SSP support.

%files		-n %{libssp}
%defattr(-,root,root)
%{_libdir}/libssp.so.*
%ifarch %{multilib_64}
%{libdir32}/libssp.so.*
%endif

#-----------------------------------------------------------------------
%package	-n %{libssp_devel}
Summary:	GCC SSP development support
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Requires:	%{libssp} = %{version}-%{release}
Provides:	libssp-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libssp-devel < %{version}-%{release}
%endif

%description	-n %{libssp_devel}
This package contains GCC libraries which are needed
to compile SSP support.

%files		-n %{libssp_devel}
%defattr(-,root,root)
%{_libdir}/libssp.la
%{_libdir}/libssp.so
%ifarch %{multilib_64}
%{libdir32}/libmssp.la
%{libdir32}/libmssp.so
%endif
%{gccdir}/include/ssp

#-----------------------------------------------------------------------
%package	-n %{libssp_static_devel}
Summary:	GCC SSP static libraries
Group:		Development/C
Requires:	%{libssp_devel} = %{version}-%{release}
Provides:	libssp-static-devel = %{version}-%{release}
%if %{provide_libmajor}
Obsoletes:	libssp-static-devel < %{version}-%{release}
%endif

%description	-n %{libssp_static_devel}
This package contains GCC static libraries which are needed
to compile SSP support.

%files		-n %{libssp_static_devel}
%defattr(-,root,root)
%{_libdir}/libssp_nonshared.a
%ifarch %{multilib_64}
%{libdir32}/libssp_nonshared.a
%endif
#-----------------------------------------------------------------------
# build ssp
%endif

########################################################################
%prep
%setup -q -n %{name}-%{branch}%{snapshot}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# do not pretend it is gcc-4.6.1 besides snapshot telling so
echo %{version} > gcc/BASE-VER

#-----------------------------------------------------------------------
%build
OPT_FLAGS=`echo %{optflags} |					\
	sed	-e 's/\(-Wp,\)\?-D_FORTIFY_SOURCE=[12]//g'	\
		-e 's/-m\(31\|32\|64\)//g'			\
		-e 's/-fstack-protector//g'			\
		-e 's/--param=ssp-buffer-size=4//'		\
		-e 's/-pipe//g'`
OPT_FLAGS=`echo "$OPT_FLAGS" | sed -e 's/[[:blank:]]\+/ /g'`

# FIXME debugedit
[ ! -z "$TMP" ] && export TMP=`echo $TMP | sed -e 's|/$||'`
[ ! -z "x$TMPDIR" ] && export TMPDIR=`echo $TMPDIR | sed -e 's|/$||'`

LANGUAGES=c
%if %{build_ada}
    LANGUAGES="$LANGUAGES,ada"
%endif
%if %{build_cxx}
    LANGUAGES="$LANGUAGES,c++"
%endif
%if %{build_fortran}
    LANGUAGES="$LANGUAGES,fortran"
%endif
%if %{build_go}
    LANGUAGES="$LANGUAGES,go"
%endif
%if %{build_java}
    LANGUAGES="$LANGUAGES,java"
%endif
%if %{build_lto}
    LANGUAGES="$LANGUAGES,lto"
%endif
%if %{build_objc}
    LANGUAGES="$LANGUAGES,objc"
%endif
%if %{build_objcxx}
    LANGUAGES="$LANGUAGES,obj-c++"
%endif

CC=%{__cc}							\
CFLAGS="$OPT_FLAGS"						\
CXXFLAGS="$OPT_FLAGS"						\
GCJFLAGS="$OPT_FLAGS"						\
TCFLAGS="$OPT_FLAGS"						\
XCFLAGS="$OPT_FLAGS"						\
%configure2_5x							\
%if !%{build_java}
	--disable-libgcj					\
%else
	--disable-libjava-multilib				\
	--with-java-home=%{java_home}				\
	--with-ecj-jar=%{_datadir}/java/eclipse-ecj.jar		\
	--enable-java-awt=qt,gtk				\
	--enable-gtk-cairo					\
%endif
%if !%{build_cloog}
	--without-cloog						\
	--without-ppl						\
%else
	--with-cloog						\
	--with-ppl						\
	--enable-cloog-backend=ppl				\
%endif
%if !%{build_ffi}
	--disable-libffi					\
%endif
%if !%{build_gomp}
	--disable-libgomp					\
%endif
%if !%{build_quadmath}
	--disable-libquadmath					\
  %if %{build_fortran}
	--disable-libquadmath-support				\
  %endif
%endif
%if !%{build_mudflap}
	--disable-libmudflap					\
%endif
%if !%{build_ssp}
	--disable-libssp					\
%endif
	--disable-libunwind-exceptions				\
	--disable-werror					\
	--enable-__cxa_atexit					\
%if %{system_compiler}
	--enable-bootstrap					\
%endif
	--enable-checking=release				\
	--enable-gnu-unique-object				\
	--enable-languages="$LANGUAGES"				\
	--enable-linker-build-id				\
%if !%{build_plugin}
	--disable-plugin					\
%else
	--enable-plugin						\
%endif
	--enable-shared						\
%if !%{system_compiler}
	--disable-static					\
%endif
	--enable-threads=posix					\
	--with-system-zlib					\
	--with-bugurl=https://qa.mandriva.com/			\
%ifarch %{ix86} x86_64
	--with-tune=generic					\
%endif
%ifarch %{ix86}
	--with-arch=i686					\
%endif
%ifarch x86_64
	--with-arch_32=i686					\
%endif
	--host=%{_target_platform}				\
	--target=%{_target_platform}

%if %{system_compiler}
GCJFLAGS="$OPT_FLAGS"						\
%make BOOT_CFLAGS="$OPT_FLAGS" profiledbootstrap
%else
%make
%endif

%if %{build_pdf}
%make pdf
%endif

%if %{build_doc}
    pushd host-%{_target_platform}/gcc
	%make html
	%if %{build_pdf}
	    %make pdf
	%endif
    popd
%endif

#-----------------------------------------------------------------------
%if %{build_check}
%check
echo ====================TESTING=========================
%{_bindir}/time %make -k check || true
echo "XXX check time above XXX"
contrib/test_summary > test_summary.log
echo ====================TESTING END=====================
%endif

#-----------------------------------------------------------------------
%install
%makeinstall_std

%if %{build_java}
    %make DESTDIR=%{buildroot} -C %{_target_platform}/libjava install-src.zip
%endif

# configure python dir option does not cover libstdc++ and needs to remove
# /usr prefix for libjava
mkdir -p %{buildroot}%{py_puresitedir}
if [ -d %{buildroot}%{_datadir}/%{name}-%{version}/python ]; then
    mv -f %{buildroot}%{_datadir}/%{name}-%{version}/python/*		\
	%{buildroot}%{py_puresitedir}
    rm -fr %{buildroot}%{_datadir}/%{name}-%{version}
    %if %{build_cxx}
    perl -pi -e 's|%{_datadir}/%{name}-%{version}/python|%{py_puresitedir}|;' \
	%{buildroot}%{py_puresitedir}/libstdcxx/lib*.py
    %endif
    %if %{build_java}
    perl -pi -e 's|%{_datadir}/%{name}-%{version}/python|%{py_puresitedir}|;' \
	%{buildroot}%{_bindir}/aot-compile
    %endif
fi

pushd %{buildroot}%{_bindir}
%if %{system_compiler}
    mkdir -p %{buildroot}/lib
    ln -sf %{_bindir}/cpp %{buildroot}/lib/cpp
    cp -fa %{SOURCE3} %{SOURCE4} %{buildroot}%{_bindir}
    ln -sf %{_target_platform}-%{name}-%{version} %{buildroot}%{_bindir}/cc
%else
    rm -f %{buildroot}%{_bindir}/cpp
%endif

    LANGUAGES="gcc g++ gcc gccgo gcj gfortran"
    for lang in $LANGUAGES; do
	if [ -f %{_target_platform}-$lang ]; then
	    mv -f %{_target_platform}-$lang{,-%{version}}
	    rm -f $lang
	    ln -sf %{_target_platform}-$lang-%{version} $lang-%{version}
	%if %{system_compiler}
		ln -sf %{_target_platform}-$lang-%{version} $lang
	elif [ -f %{_target_platform}-$lang-%{version} ]; then
		ln -sf %{_target_platform}-$lang-%{version} %{_target_platform}-$lang
	%endif
	fi
    done

%if %{build_cxx}
    rm -f c++ %{_target_platform}-c++{,-%{version}}
    ln -sf %{_target_platform}-g++-%{version} c++-%{version}
    %if %{system_compiler}
	ln -sf %{_target_platform}-g++-%{version} c++
    %endif
    %ifarch %{multilib_64}
	mv -f %{buildroot}%{_libdir}/libstdc++.so.6.0.16-gdb.py		\
		%{buildroot}%{py_puresitedir}/libstdcxx/lib64stdc++.so.6.0.16-gdb.py
	mv -f %{buildroot}%{libdir32}/libstdc++.so.6.0.16-gdb.py	\
		%{buildroot}%{py_puresitedir}/libstdcxx
    %else
	mv -f %{buildroot}%{_libdir}/libstdc++.so.6.0.16-gdb.py		\
		%{buildroot}%{py_puresitedir}/libstdcxx
    %endif
%endif
popd

%if %{build_ada}
    for lib in libgnarl libgnat; do
	rm -f	%{buildroot}%{_libdir}/$lib.so
	rm -f	%{buildroot}%{gccdir}/adalib/$lib.so
	mv -f	%{buildroot}%{gccdir}/adalib/$lib-%{branch}.so		\
		%{buildroot}%{_libdir}/$lib-%{branch}.so.1
	ln -sf	$lib-%{branch}.so.1 %{buildroot}%{_libdir}/$lib-%{branch}.so
	ln -sf	$lib-%{branch}.so.1 %{buildroot}%{_libdir}/$lib.so
    %ifarch %{multilib_64}
	rm -f %{buildroot}%{libdir32}/$lib.so
	rm -f	%{buildroot}%{gccdir}/32/adalib/$lib.so
	mv -f	%{buildroot}%{gccdir}/32/adalib/$lib-%{branch}.so	\
		%{buildroot}%{libdir32}/$lib-%{branch}.so.1
	ln -sf	$lib-%{branch}.so.1 %{buildroot}%{libdir32}/$lib-%{branch}.so
	ln -sf	$lib-%{branch}.so.1 %{buildroot}%{libdir32}/$lib.so
    %endif
    done
%endif

mv -f %{buildroot}%{gccdir}/include{-fixed,}/syslimits.h
mv -f %{buildroot}%{gccdir}/include{-fixed,}/limits.h
rm -fr %{buildroot}%{gccdir}/include-fixed
rm -fr %{buildroot}%{gccdir}/install-tools/include

%if !%{system_compiler}
    rm -fr %{buildroot}%{_infodir}
    rm -fr %{buildroot}%{_mandir}
    rm -fr %{buildroot}%{_localedir}
    rm -f %{buildroot}%{_bindir}/gcov
    rm -f %{buildroot}%{_libdir}/libgcc_s.so
    %ifarch %{multilib_64}
	rm -f %{buildroot}%{libdir32}/libgcc_s.so
    %endif
%endif
rm -f %{buildroot}%{_libdir}/libiberty.a
rm -f %{buildroot}%{libdir32}/libiberty.a

%if %{build_doc}
    %if %{build_cxx}
    mkdir -p %{buildroot}%{_docdir}/libstdc++
    cp -far libstdc++-v3/doc/html %{buildroot}%{_docdir}/libstdc++
    %endif
    pushd host-%{_target_platform}/gcc/HTML/%{name}-%{version}
	mkdir -p %{buildroot}%{_docdir}/gcc/html
	for doc in gcc gccinstall gccint; do
	    cp -far $doc %{buildroot}%{_docdir}/gcc/html
	done
	%if %{system_compiler}
	mkdir -p %{buildroot}%{_docdir}/gcc-cpp/html
	for doc in cpp cppinternals; do
	    cp -far $doc %{buildroot}%{_docdir}/gcc-cpp/html
	done
	%endif
	%if %{build_fortran}
	mkdir -p %{buildroot}%{_docdir}/gcc-gfortran/html
	cp -far gfortran %{buildroot}%{_docdir}/gcc-gfortran/html
	%endif
	%if %{build_go}
	mkdir -p %{buildroot}%{_docdir}/gcc-go/html
	cp -far go %{buildroot}%{_docdir}/gcc-go/html
	%endif
	%if %{build_java}
	mkdir -p %{buildroot}%{_docdir}/gcc-java/html
	cp -far java %{buildroot}%{_docdir}/gcc-java/html
	%endif
    popd
    %if %{build_pdf}
    pushd host-%{_target_platform}/gcc/doc
	for doc in gcc.pdf gccinstall.pdf gccint.pdf; do
	    install -m 0644 $doc %{buildroot}%{_docdir}/gcc/$doc
	done
	%if %{system_compiler}
	for doc in cpp.pdf cppinternals.pdf; do
	    install -m 0644 $doc %{buildroot}%{_docdir}/gcc-cpp/$doc
	done
	%endif
	%if %{build_ada}
	mkdir -p %{buildroot}%{_docdir}/gcc-gnat
	for doc in gnat_ugn.pdf gnat_rm.pdf gnat-style.pdf; do
	    install -m 0644 $doc %{buildroot}%{_docdir}/gcc-gnat/$doc
	done
	%endif
	%if %{build_fortran}
	for doc in gfc-internals.pdf gfortran.pdf; do
	    install -m 0644 $doc %{buildroot}%{_docdir}/gcc-gfortran/$doc
	done
	%endif
	%if %{build_go}
	install -m 0644 -D gccgo.pdf %{buildroot}%{_docdir}/gcc-go/gccgo.pdf
	%endif
	%if %{build_java}
	install -m 0644 -D gcj.pdf %{buildroot}%{_docdir}/gcc-java/gcj.pdf
	%endif
    popd
    pushd %{_target_platform}
	%if %{build_gomp}
	install -m 0644 -D libgomp/libgomp.pdf %{buildroot}%{_docdir}/libgomp/libgomp.pdf
	%endif
	%if %{build_quadmath}
	install -m 0644 -D libquadmath/libquadmath.pdf %{buildroot}%{_docdir}/libquadmath/libquadmath.pdf
	%endif
	%if %{build_java}
	install -m 0644 -D libjava/classpath/doc/cp-tools.pdf %{buildroot}%{_docdir}/libjava/cp-tools.pdf
	%endif
    popd
    %endif
%endif

%if %{build_melt}
    tar zxf %{SOURCE2}
    pushd melt-0.7-plugin-for-gcc-4.6
	DESTDIR=%{buildroot}/				\
	./build-melt-plugin.sh				\
	-S$PWD/..					\
	-B$PWD/../host-%{_target_platform}		\
	-M$PWD						\
	-Y$PWD/melt/generated/gt-melt-runtime-plugin.h
	%if %{system_compiler}
	install -m 0644 *.info %{buildroot}%{_infodir}
	mkdir -p %{buildroot}%{_docdir}/gcc-plugin-melt/html
	cp -fa *.html %{buildroot}%{_docdir}/gcc-plugin-melt/html
	%endif
    popd
%endif

#-----------------------------------------------------------------------
%clean
rm -fr %{buildroot}
