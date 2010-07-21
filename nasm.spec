Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Summary(es.UTF-8):	Ensamblador de red
Summary(ja.UTF-8):	Intel風の文法を持つポータブルな x86 アセンブラ
Summary(pl.UTF-8):	Nasm jest darmowym asemblerem dla procesorów z serii 80x86
Summary(pt_BR.UTF-8):	O "Netwide Assembler"
Summary(ru.UTF-8):	Netwide Assembler, переносимый x86 ассемблер с Intel-подобным синтаксисом
Summary(uk.UTF-8):	Netwide Assembler, переносимий x86 асемблер з Intel-подібним синтаксисом
Name:		nasm
Version:	2.08.02
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	2b0dfe9266491c14c4025f57c9cfd0f1
Patch0:		%{name}-info.patch
URL:		http://www.nasm.us/
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

%description -l es.UTF-8
Ensamblador de red.

%description -l pl.UTF-8
NASM jest asemblerem dla procesorów 80x86 skonstruowanym z myślą o
przenośności i modularności. Zawiera szeroką gamę obsługi obiektów, w
tym linuksowe a.out i ELF, COFF, 16-bitowe OBJ Microsoftu oraz Win32.
Dostajemy czysty wynikowy plik binarny. Składnia jest skonstruowana z
myślą o prostocie i łatwości zrozumienia, podobna do intelowskiej, ale 
mniej kompleksowa. Zawiera obsługę procesorów Pentium, P6 oraz MMX
opcode i ma macro capability. Zawiera także deassembler.

%description -l pt_BR.UTF-8
Este é o NASM, o "Netwide Assembler". o NASM é um assembler para a
familia x86 de processadores. Atualmente, ele sabe gerar binários
puros, a.out, COFF, ELF, Microsoft Win32 e 16 bits DOS, OS/2, as86, e
um formato "caseiro" chamado RDF.

%description -l ru.UTF-8
NASM - это Netwide Assembler, свободный переносимый ассемблер для
серии микропроцессоров Intel 80x86. Использует в основном традиционные
Интеловские мнемонику инструкций и синтаксис.

%description -l uk.UTF-8
NASM - це Netwide Assembler, вільний переносимий асемблер для серії
мікропроцесорів Intel 80x86. Використовує в основному традиційні
Інтелівські мнемоніку інструкцій та синтаксис.

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Summary(pl.UTF-8):	Narzędzia do formatu binarnego RDOFF, czasem używane z NASM-em
Summary(ru.UTF-8):	Инструменты для бинарного формата RDOFF
Summary(uk.UTF-8):	Інструменти для бінарного формату RDOFF
Group:		Development/Tools
Requires:	%{name} = %{version}-%{release}

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM). These tools
include linker, library manager, loader, and information dump.

%description rdoff -l pl.UTF-8
Narzędzia do niezależnego od systemu operacyjnego formatu binarnego
RDOFF, czasem używane z Netwide Assembler (NASM). Te narzędzia
zawierają linker, library manager, loader oraz information dump.

%description rdoff -l ru.UTF-8
Инструменты для независимого от операционной системы бинарного формата
RDOFF, который иногда используют с NASM. Эти инструменты включают
редактор связей, библиотечный менеджер, загрузчик и программу выдачи
информационнного дампа.

%description rdoff -l uk.UTF-8
Інструменти для незалежного від операційної системи бінарного формату
RDOFF, котрий іноді використовують з NASM. Ці інструменти включають
редактор зв'язків, бібліотечний менеджер, завантажувач та програму
видачі інформаційного дампу.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make} -j1 all rdf

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

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
%attr(755,root,root) %{_bindir}/rdf2ith
%attr(755,root,root) %{_bindir}/rdf2srec
%attr(755,root,root) %{_bindir}/rdfdump
%attr(755,root,root) %{_bindir}/rdflib
%attr(755,root,root) %{_bindir}/rdx
