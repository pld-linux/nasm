Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Summary(es):	Ensamblador de red
Summary(ja):	Intel風の文法を持つポータブルな x86 アセンブラ
Summary(pl):	Nasm jest darmowym asemblerem dla procesor�w z serii 80x86
Summary(pt_BR):	O "Netwide Assembler"
Summary(ru):	Netwide Assembler, 佚凖力喇踊� x86 喪單預姪� � Intel-佻掴体挈 喇淋阻喇嗜�
Summary(uk):	Netwide Assembler, 佚凖力喇揺� x86 喪斗駄賭 � Intel-佻彫体浜 喇淋阻喇嗜�
Name:		nasm
Version:	0.98.38
Release:	1
License:	LGPL v2.1
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	9f682490c132b070d54e395cb6ee145e
Patch0:		%{name}-boguself2.patch
Patch1:		%{name}-cpp_macros.patch
Patch2:		%{name}-info.patch
URL:		http://nasm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	perl-base
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
tym linuksowe a.out i ELF, COFF, 16-bitowe OBJ Microsoftu oraz Win32.
Dostajemy czysty wynikowy plik binarny. Sk�adnia jest skonstruowana z
my�l� o prostocie i �atwo�ci zrozumienia, podobna do intelowskiej, ale 
mniej kompleksowa. Zawiera obs�ug� procesor�w Pentium, P6 oraz MMX
opcode i ma macro capability. Zawiera tak�e deassembler.

%description -l pt_BR
Este � o NASM, o "Netwide Assembler". o NASM � um assembler para a
familia x86 de processadores. Atualmente, ele sabe gerar bin�rios
puros, a.out, COFF, ELF, Microsoft Win32 e 16 bits DOS, OS/2, as86, e
um formato "caseiro" chamado RDF.

%description -l ru
NASM - 榑� Netwide Assembler, 嘛和歪隣� 佚凖力喇踊� 喪單預姪� 通�
單夘� 揺牧椀厦壇嗷碗�� Intel 80x86. 蚌佻蒙旁都 � 腕力徇詫 墟祖秒貧領拇
蚓堙模徨防� 洋斗藁彬� 瀕嘖簒肪品 � 喇淋阻喇�.

%description -l uk
NASM - 壇 Netwide Assembler, 廢蒙良� 佚凖力喇揺� 喪斗駄賭 通� 單勁�
勇牧椀厦壇嗜勁� Intel 80x86. �彬碗瓶塹徼� � 腕力徇詫� 墟祖秒κ陸
粁堙巳徨慄� 洋斗藁λ� ξ嘖簒肪κ 堊 喇淋阻喇�.

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Summary(pl):	Narz�dzia do formatu binarnego RDOFF, czasem u�ywane z NASM-em
Summary(ru):	蚓嘖簒妖淋� 通� 舵料厠惑� 届厖壮� RDOFF
Summary(uk):	粁嘖簒妖淋� 通� 側料厠惑� 届厖壮� RDOFF
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
蚓嘖簒妖淋� 通� 療攸徂喇溶馬 �� 椀賭礎貧領亙 喇嘖斗� 舵料厠惑� 届厖壮�
RDOFF, 墨塹燮� 瀕惑珍 瓶佻蒙旁脊 � NASM. �塢 瀕嘖簒妖淋� 徊明涸脊
凖珍穆碗 嘛凉妬, 舵駄貧堙淮拱 妖療綴賭, 攸拝孳淺� � 侑惑卅様� 忸珍淺
瀕届厖礎貧領力馬 珍熔�.

%description rdoff -l uk
粁嘖簒妖淋� 通� 療攸姪嵶惑� 廢� 椀賭礎κ力� 喇嘖斗� 側料厠惑� 届厖壮�
RDOFF, 墨墟品 ξ歪� 徂墨夘嘖�徼脊� � NASM. 礒 ξ嘖簒妖淋� 徊明涸脊�
凖珍穆碗 旌'凉胞�, 側駄ο堙淮品 妖療綴賭, 攸彖淋爽孥挿 堊 侑惑卅葉
徂珍洟 ξ届厖礎κ力馬 珍熔�.

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
