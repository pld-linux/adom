Summary:	Very popular rogue-like adventure game
Summary(pl):	Bardzo popularna tekstowa gra przygodowa
Name:		adom
Version:	099g15
Release:	3
Group:		Games
Group(pl):	Gry
Copyright:	postcardware
Source0:	http://www.adom.de/adom/download/linux/%{name}-%{version}-elf.tar.gz
URL:		http://www.adom.de/
ExclusiveArch:  %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ADOM stands for Ancient Domains of Mystery. ADOM is a so-called
rogue-like game. This means that it is a single-user game which allows
you to play the role of an intrepid adventurer exploring a large
dungeon with some specific goal in mind. The graphics in the game are
based on simple text characters and the game is controlled with a
large number of keyboard commands.

%description -l pl
ADOM to skrót od "Ancient Domains of Mystery". ADOM to tak zwana gra
rogue-podobna. To znaczy, ¿e jest to gra dla jednej osoby, która
pozwala na wcielenie siê w postaæ poszukiwacza przygód przeszukuj±cego
olbrzymie podziemia próbuj±c wype³niæ pewn± misjê. Grafika w grze jest
oparta na prostym trybie tekstowym, a sama gra jest kontrolowana przy
u¿yciu du¿ej ilo¶ci poleceñ z klawiatury.

%prep
%setup -q -n adom

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install adom $RPM_BUILD_ROOT%{_bindir}

gzip -9nf adomfaq.txt manual.doc readme.1st

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/adom
