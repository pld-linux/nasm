Summary:   nasm is a free assembler for the 80x86 series of microprocessors
Name:      nasm
Version:   0.97
Release:   2
URL:       http://www.cryogen.com/nasm/
Source:    ftp://sunsite.unc.edu/pub/Linux/devel/lang/assemblers/%{name}-%{version}.tar.gz
Copyright: Distributable and free for non-commercial use
Group:     Development
BuildRoot: /tmp/%{name}-%{version}-root

%description
NASM is an 80x86 assembler designed for portability and modularity. It
supports a range of object file formats including Linux a.out and ELF,
COFF, Microsoft 16-bit OBJ and Win32. It will also output plain binary
files. Its syntax is designed to be simple and easy to understand, similar
to Intel's but less complex. It supports Pentium, P6 and MMX opcodes, and
has macro capability. It includes a disassembler as well. 

Version 0.97 was entirely a bug fix release, since 0.96 had more bugs than
we could shake a large stick at.

%package doc
Summary: NASM - the netwide assembler, documentation
Group:   Development

%description doc
Documentation for nasm in various formats.

%prep
%setup -q
cp rdoff/README rdoff/README.rdoff

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS=-s ./configure --prefix=/usr
make all rdf

%install 
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,info,man/man1}
make prefix=$RPM_BUILD_ROOT/usr install install_rdf

install -m644 doc/nasm.info $RPM_BUILD_ROOT%{_infodir}
gzip -9nf $RPM_BUILD_ROOT%{_infodir}/nasm.info

strip $RPM_BUILD_ROOT/usr/bin/* ||

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes Licence Readme Wishlist misc rdoff/README.rdoff rdoff/rdoff.txt
%{_infodir}/nasm.info.gz
/usr/bin/*
%attr(-,root,man) %{_mandir}/*/*

%files doc
%defattr(-,root,root)
%doc doc/*.html doc/*.ps doc/*.txt

%changelog
* Sun Oct 18 1998 Arne Coucheron <arneco@online.no>
  [0.97-2]
- using %%{name} and %%{version} macros
- added -q parameter to %setup
- added URL tag and corrected Source tag
- using %defattr in files list
- rearranged the spec file a little

* Thu Jan 22 1998 Steven Krikstone <triden@cheney.net>
- upgraded to 0.97.
- stripped rdoff/* files

* Sun Nov 30 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- added %attr's
- added sanity check for RPM_BUILD_ROOT
- the prefix used in configure _must_ be the one the package resides
  _after_ installation, as it might be compiled into the binaries. fixed.

* Fri Nov 21 1997 Karsten Weiss <karsten@addx.au.s.shuttle.de>
- Upgraded to 0.96.
- Using configure now.
- Using BuildRoot now.
- Install info file. Other doc file formats omitted.
- Default output format is ELF.

* Wed Jun 4 1997 Karsten Weiss <karsten@addx.au.s.shuttle.de>
- Created this spec file based on the old 0.93-1.src.rpm.
- Included all doc files.
- Added verbose description.
- Makefile uses RPM_OPT_FLAGS.
- Compiles without debug info.
- Changed default object file format to ELF32 (i386)
