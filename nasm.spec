Summary:	Nasm is a free assembler for the 80x86 series of microprocessors
Summary(es.UTF-8):	Ensamblador de red
Summary(ja.UTF-8):	Intel風の文法を持つポータブルな x86 アセンブラ
Summary(pl.UTF-8):	Nasm jest darmowym asemblerem dla procesorów z serii 80x86
Summary(pt_BR.UTF-8):	O "Netwide Assembler"
Summary(ru.UTF-8):	Netwide Assembler, переносимый x86 ассемблер с Intel-подобным синтаксисом
Summary(uk.UTF-8):	Netwide Assembler, переносимий x86 асемблер з Intel-подібним синтаксисом
Name:		nasm
Version:	2.16.03
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	2b8c72c52eee4f20085065e68ac83b55
URL:		https://www.nasm.us/
BuildRequires:	perl-base
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	nasm-doc < 0.98
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
przenośności i modularności. Obsługuje szeroką gamę plików
obiektowych, w tym linuksowe a.out i ELF, COFF, 16-bitowe OBJ
Microsoftu oraz Win32. Może także zapisywać zwykłe pliki binarne.
Składnia jest opracowana z myślą o prostocie i łatwości zrozumienia,
podobna do intelowskiej, ale mniej złożona. Zawiera obsługę instrukcji
procesórów Pentium i P6 oraz MMX, obsługuje też makra. Zawiera także
deassembler.

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

%prep
%setup -q

%build
%configure

%{__make} -j1 all

%{__make} -C doc html

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.md doc/html
%attr(755,root,root) %{_bindir}/nasm
%attr(755,root,root) %{_bindir}/ndisasm
%{_mandir}/man1/nasm.1*
%{_mandir}/man1/ndisasm.1*
