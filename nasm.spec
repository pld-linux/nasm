Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Name:		nasm
Version:	0.98
Release:	3
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
URL:		http://www.cryogen.com/nasm/
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.bz2
Patch:		nasm-info.patch
Prereq:		/usr/sbin/fix-info-dir
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NASM is an 80x86 assembler designed for portability and modularity. It
supports a range of object file formats including Linux a.out and ELF,
COFF, Microsoft 16-bit OBJ and Win32. It will also output plain binary
files. Its syntax is designed to be simple and easy to understand, similar
to Intel's but less complex. It supports Pentium, P6 and MMX opcodes, and
has macro capability. It includes a disassembler as well. 

%prep
%setup -q
%patch -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure

make all rdf

(cd doc; make nasmdoc.texi; makeinfo nasmdoc.texi)

%install 
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}
make INSTALLROOT=$RPM_BUILD_ROOT install install_rdf

install doc/nasm.info* $RPM_BUILD_ROOT%{_infodir}
gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man?/*} \
	Changes Licence Readme Wishlist MODIFIED

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/nasm.info*gz
%{_mandir}/man?/*
