%define 	_ver	%(echo %{version} | tr -d .)

Summary:	Very popular rogue-like adventure game
Summary(pl):	Bardzo popularna tekstowa gra przygodowa
Name:		adom
Version:	1.0.0
Release:	1
Epoch:		1
License:	postcardware
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Source0:	http://www.adom.de/adom/download/linux/%{name}-%{_ver}-elf.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.adom.de/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_scoredir	/var/games/adom

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
u¿yciu du¿ej liczby poleceñ z klawiatury.

%prep
%setup -q -n adom

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_scoredir},%{_sysconfdir},%{_applnkdir}/Games/Roguelike,%{_pixmapsdir}}

install adom $RPM_BUILD_ROOT%{_prefix}/games
touch $RPM_BUILD_ROOT%{_scoredir}/.HISCORE

cat > $RPM_BUILD_ROOT%{_sysconfdir}/adom_ds.cfg << EOF
%{_scoredir}
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Roguelike
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf adomfaq.txt manual.doc readme.1st

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_prefix}/games/adom
%attr(775,root,games) %dir %{_scoredir}
%attr(664,root,games) %config(noreplace) %verify(not md5 size mtime) %{_scoredir}/.HISCORE
%{_sysconfdir}/adom_ds.cfg

%{_applnkdir}/Games/Roguelike/*
%{_pixmapsdir}/*

%doc *.gz
