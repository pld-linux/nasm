Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Summary(pl):	Nasm jest darmowym asemblerem dla procesor�w z serii 80x86
Name:		nasm
Version:	0.98
Release:	9
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.bz2
Patch0:		%{name}-info.patch
Patch1:		%{name}-3DNow.patch
Patch2:		%{name}-boguself.patch
URL:		http://www.cryogen.com/nasm/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	texinfo
BuildRequires:	perl
Obsoletes:	nasm-doc

%description
NASM is an 80x86 assembler designed for portability and modularity. It
supports a range of object file formats including Linux a.out and ELF,
COFF, Microsoft 16-bit OBJ and Win32. It will also output plain binary
files. Its syntax is designed to be simple and easy to understand,
similar to Intel's but less complex. It supports Pentium, P6 and MMX
opcodes, and has macro capability. It includes a disassembler as well.

%description -l pl
NASM jest asemblerem dla procesor�w 80x86 skonstruowanym z my�l� o 
przeno�no�ci i modularno�ci. Zawiera szerok� gam� obs�ugi obiekt�w,
w tym Linuxowe a.out i ELF, COFF, 16-bitowe OBJ Microsoft'u oraz Win32.
Dostajemy czysty wynikowy plik binarny. Sk�adnia jest skonstruowana z 
my�l� o prostocie i �atwo�ci zrozumienia, podobna do Intel'owskiej,
ale mniej komleksowa. Zawiera obs�ug� procesor�w Pentium, P6 oraz
MMX opcode i ma macro capability. Zawiera tak�e deassembler.

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Summary(pl):	Tools'y do formatu binarnego RDOFF. Czasem u�ywane z NASM'em.
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Requires:	%{name} = %{version}

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%description -l pl rdoff
Tools'y do niezale�nego od systemu operacyjnego formatu binarnego RDOFF,
czasem u�ywane z Netwide Assembler (NASM). Te narz�dzia zawieraj� linker,
linker, library manager, loader oraz information dump.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%configure

%{__make} all rdf

(cd doc; make nasmdoc.texi; makeinfo nasmdoc.texi)

%install 
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

%{__make} INSTALLROOT=$RPM_BUILD_ROOT install install_rdf

install doc/nasm.info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf Changes Licence Readme Wishlist MODIFIED \
	rdoff/README rdoff/Changes

%post
%fix_info_dir

%postun
%fix_info_dir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/nasm
%attr(755,root,root) %{_bindir}/ndisasm
%{_infodir}/nasm.info*
%{_mandir}/man?/*

%files rdoff
%defattr(644,root,root,755)
%doc rdoff/README.gz rdoff/Changes.gz
%attr(755,root,root) %{_bindir}/ldrdf
%attr(755,root,root) %{_bindir}/rdf2bin
%attr(755,root,root) %{_bindir}/rdf2com
%attr(755,root,root) %{_bindir}/rdfdump
%attr(755,root,root) %{_bindir}/rdflib
%attr(755,root,root) %{_bindir}/rdx
