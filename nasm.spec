Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Summary(pl):	Nasm jest darmowym asemblerem dla procesorów z serii 80x86
Name:		nasm
Version:	0.98.32
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://telia.dl.sourceforge.net/sourceforge/nasm/%{name}-%{version}.tar.bz2
Patch0:		%{name}-boguself2.patch
Patch1:		%{name}-cpp_macros.patch
URL:		http://nasm.2y.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
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
NASM jest asemblerem dla procesorów 80x86 skonstruowanym z my¶l± o
przeno¶no¶ci i modularno¶ci. Zawiera szerok± gamê obs³ugi obiektów, w
tym Linuxowe a.out i ELF, COFF, 16-bitowe OBJ Microsoft'u oraz Win32.
Dostajemy czysty wynikowy plik binarny. Sk³adnia jest skonstruowana z
my¶l± o prostocie i ³atwo¶ci zrozumienia, podobna do Intel'owskiej,
ale mniej komleksowa. Zawiera obs³ugê procesorów Pentium, P6 oraz MMX
opcode i ma macro capability. Zawiera tak¿e deassembler.

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Summary(pl):	Narzêdzia do formatu binarnego RDOFF, czasem u¿ywane z NASM-em
Group:		Development/Tools
Requires:	%{name} = %{version}

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%description rdoff -l pl
Narzêdzia do niezale¿nego od systemu operacyjnego formatu binarnego
RDOFF, czasem u¿ywane z Netwide Assembler (NASM). Te narzêdzia
zawieraj± linker, library manager, loader oraz information dump.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure

%{__make} all rdf

(cd doc; make nasmdoc.texi; makeinfo nasmdoc.texi)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

%{__make} INSTALLROOT=$RPM_BUILD_ROOT install install_rdf

install doc/nasm.info* $RPM_BUILD_ROOT%{_infodir}

gzip -9nf ChangeLog AUTHORS README TODO  \
	rdoff/README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/nasm
%attr(755,root,root) %{_bindir}/ndisasm
%{_infodir}/nasm.info*
%{_mandir}/man?/*

%files rdoff
%defattr(644,root,root,755)
%doc rdoff/*.gz
%attr(755,root,root) %{_bindir}/ldrdf
%attr(755,root,root) %{_bindir}/rdf2bin
%attr(755,root,root) %{_bindir}/rdf2com
%attr(755,root,root) %{_bindir}/rdfdump
%attr(755,root,root) %{_bindir}/rdflib
%attr(755,root,root) %{_bindir}/rdx
