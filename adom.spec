%define 	_ver	%(echo %{version} | tr -d .)
Summary:	Very popular rogue-like adventure game
Summary(pl.UTF-8):   Bardzo popularna tekstowa gra przygodowa
Name:		adom
Version:	1.1.1
Release:	2
Epoch:		1
License:	Postcardware
Group:		Applications/Games
Source0:	http://www.adom.de/adom/download/linux/%{name}-%{_ver}-elf.tar.gz
# Source0-md5:	801484ba7c7c03b3b999365bc45db053
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.adom.de/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scoredir	/var/games/adom

%description
ADOM stands for Ancient Domains of Mystery. ADOM is a so-called
rogue-like game. This means that it is a single-user game which allows
you to play the role of an intrepid adventurer exploring a large
dungeon with some specific goal in mind. The graphics in the game are
based on simple text characters and the game is controlled with a
large number of keyboard commands.

%description -l pl.UTF-8
ADOM to skrót od "Ancient Domains of Mystery". ADOM to tak zwana gra
rogue-podobna. To znaczy, że jest to gra dla jednej osoby, która
pozwala na wcielenie się w postać poszukiwacza przygód przeszukującego
olbrzymie podziemia próbując wypełnić pewną misję. Grafika w grze jest
oparta na prostym trybie tekstowym, a sama gra jest kontrolowana przy
użyciu dużej liczby poleceń z klawiatury.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix}/games,%{_scoredir},%{_sysconfdir},%{_desktopdir},%{_pixmapsdir}}

install adom $RPM_BUILD_ROOT%{_prefix}/games
touch $RPM_BUILD_ROOT%{_scoredir}/.HISCORE

cat > $RPM_BUILD_ROOT%{_sysconfdir}/adom_ds.cfg << EOF
%{_scoredir}
EOF

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(2755,root,games) %{_prefix}/games/adom
%attr(775,root,games) %dir %{_scoredir}
%attr(664,root,games) %config(noreplace) %verify(not md5 mtime size) %{_scoredir}/.HISCORE
%{_sysconfdir}/adom_ds.cfg

%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

%doc adomfaq.txt manual.doc readme.1st
