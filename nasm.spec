Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Name:		nasm
Version:	0.98
Release:	2
Copyright:	GPL
URL:		http://www.cryogen.com/nasm/
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.bz2
Group:		Development
BuildRoot:	/tmp/%{name}-%{version}-root

%description
NASM is an 80x86 assembler designed for portability and modularity. It
supports a range of object file formats including Linux a.out and ELF,
COFF, Microsoft 16-bit OBJ and Win32. It will also output plain binary
files. Its syntax is designed to be simple and easy to understand, similar
to Intel's but less complex. It supports Pentium, P6 and MMX opcodes, and
has macro capability. It includes a disassembler as well. 

Version 0.97 was entirely a bug fix release, since 0.96 had more bugs than
we could shake a large stick at.

%prep
%setup -q
cp rdoff/README rdoff/README.rdoff

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	--prefix=%{_prefix}
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
/sbin/install-info %{_infodir}/nasm.info.gz /etc/info-dir

%preun
if [ "$1" = "0" ]; then
	/sbin/install-info --delete %{_infodir}/nasm.info.gz /etc/info-dir
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%{_infodir}/nasm.info*gz
%{_mandir}/man?/*

%changelog
* Fri Jun  4 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.98-2]
- based on spec from RH contrib,
- rewrited to PLD coding style,
- added {un}registering info pages for nasm.
