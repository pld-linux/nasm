Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Name:		nasm
Version:	0.98
Release:	4
License:	GPL
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
URL:		http://www.cryogen.com/nasm/
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.bz2
Patch0:		nasm-info.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	nasm-doc

%description
NASM is an 80x86 assembler designed for portability and modularity. It
supports a range of object file formats including Linux a.out and ELF,
COFF, Microsoft 16-bit OBJ and Win32. It will also output plain binary
files. Its syntax is designed to be simple and easy to understand,
similar to Intel's but less complex. It supports Pentium, P6 and MMX
opcodes, and has macro capability. It includes a disassembler as well.

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Requires:	%{name} = %{version}

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%prep
%setup -q
%patch -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure

%{__make} all rdf

(cd doc; make nasmdoc.texi; makeinfo nasmdoc.texi)

%install 
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}
%{__make} INSTALLROOT=$RPM_BUILD_ROOT install install_rdf

install doc/nasm.info* $RPM_BUILD_ROOT%{_infodir}
gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man?/*} \
	Changes Licence Readme Wishlist MODIFIED \
	rdoff/README rdoff/Changes

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/nasm
%attr(755,root,root) %{_bindir}/ndisasm
%{_infodir}/nasm.info*gz
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
