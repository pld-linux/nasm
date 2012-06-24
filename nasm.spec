Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Summary(es):	Ensamblador de red
Summary(ja):	Intel����ʸˡ����ĥݡ����֥�� x86 ������֥�
Summary(pl):	Nasm jest darmowym asemblerem dla procesor�w z serii 80x86
Summary(pt_BR):	O "Netwide Assembler"
Summary(ru):	Netwide Assembler, ����������� x86 ��������� � Intel-�������� �����������
Summary(uk):	Netwide Assembler, ����������� x86 �������� � Intel-��Ħ���� �����������
Name:		nasm
Version:	0.98.37
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	dbb9c410bfcf5cd0ccf6f71963d66abc
Patch0:		%{name}-boguself2.patch
Patch1:		%{name}-cpp_macros.patch
Patch2:		%{name}-info.patch
URL:		http://nasm.2y.net/
BuildRequires:	autoconf
BuildRequires:	perl
BuildRequires:	texinfo
Obsoletes:	nasm-doc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NASM is an 80x86 assembler designed for portability and modularity. It
supports a range of object file formats including Linux a.out and ELF,
COFF, Microsoft 16-bit OBJ and Win32. It will also output plain binary
files. Its syntax is designed to be simple and easy to understand,
similar to Intel's but less complex. It supports Pentium, P6 and MMX
opcodes, and has macro capability. It includes a disassembler as well.

%description -l es
Ensamblador de red.

%description -l pl
NASM jest asemblerem dla procesor�w 80x86 skonstruowanym z my�l� o
przeno�no�ci i modularno�ci. Zawiera szerok� gam� obs�ugi obiekt�w, w
tym Linuxowe a.out i ELF, COFF, 16-bitowe OBJ Microsoft'u oraz Win32.
Dostajemy czysty wynikowy plik binarny. Sk�adnia jest skonstruowana z
my�l� o prostocie i �atwo�ci zrozumienia, podobna do Intel'owskiej,
ale mniej komleksowa. Zawiera obs�ug� procesor�w Pentium, P6 oraz MMX
opcode i ma macro capability. Zawiera tak�e deassembler.

%description -l pt_BR
Este � o NASM, o "Netwide Assembler". o NASM � um assembler para a
familia x86 de processadores. Atualmente, ele sabe gerar bin�rios
puros, a.out, COFF, ELF, Microsoft Win32 e 16 bits DOS, OS/2, as86, e
um formato "caseiro" chamado RDF.

%description -l ru
NASM - ��� Netwide Assembler, ��������� ����������� ��������� ���
����� ���������������� Intel 80x86. ���������� � �������� ������������
����������� ��������� ���������� � ���������.

%description -l uk
NASM - �� Netwide Assembler, צ����� ����������� �������� ��� ��Ҧ�
ͦ����������Ҧ� Intel 80x86. ����������դ � ��������� �����æ�Φ
����̦���˦ �����Φ�� �������æ� �� ���������.

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Summary(pl):	Narz�dzia do formatu binarnego RDOFF, czasem u�ywane z NASM-em
Summary(ru):	����������� ��� ��������� ������� RDOFF
Summary(uk):	����������� ��� ¦������� ������� RDOFF
Group:		Development/Tools
Requires:	%{name} = %{version}

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%description rdoff -l pl
Narz�dzia do niezale�nego od systemu operacyjnego formatu binarnego
RDOFF, czasem u�ywane z Netwide Assembler (NASM). Te narz�dzia
zawieraj� linker, library manager, loader oraz information dump.

%description rdoff -l ru
����������� ��� ������������ �� ������������ ������� ��������� �������
RDOFF, ������� ������ ���������� � NASM. ��� ����������� ��������
�������� ������, ������������ ��������, ��������� � ��������� ������
���������������� �����.

%description rdoff -l uk
����������� ��� ����������� צ� �����æ��ϧ ������� ¦������� �������
RDOFF, ������ ���Ħ �������������� � NASM. � ����������� ���������
�������� ��'��˦�, ¦�̦������� ��������, ������������ �� ��������
����ަ �������æ����� �����.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure

%{__make} all rdf

cd doc
%{__make} nasmdoc.texi
makeinfo nasmdoc.texi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

%{__make} install install_rdf \
	INSTALLROOT=$RPM_BUILD_ROOT

install doc/nasm.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README TODO
%attr(755,root,root) %{_bindir}/nasm
%attr(755,root,root) %{_bindir}/ndisasm
%{_infodir}/nasm.info*
%{_mandir}/man?/*

%files rdoff
%defattr(644,root,root,755)
%doc rdoff/README
%attr(755,root,root) %{_bindir}/ldrdf
%attr(755,root,root) %{_bindir}/rdf2bin
%attr(755,root,root) %{_bindir}/rdf2com
%attr(755,root,root) %{_bindir}/rdf2ihx
%attr(755,root,root) %{_bindir}/rdfdump
%attr(755,root,root) %{_bindir}/rdflib
%attr(755,root,root) %{_bindir}/rdx
