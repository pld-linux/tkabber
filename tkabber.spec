Summary:	Tk Jabber client
Summary(pl):	Klient Jabbera oparty o Tk
Name:		tkabber
Version:	0.9.5beta
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jabberstudio.org/projects/tkabber/releases/file/%{name}-%{version}.tar.gz
# Source0-md5:	13c62b75d6c80ebbbff5eb3e9f2aa668
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-defaults.patch
Icon:		tkabber.xpm
URL:		http://tkabber.jabber.ru/
Requires:	tcl >= 8.3.4-7
Requires:	tcllib >= 1.2
Requires:	tk >= 8.3.3
Requires:	tk-BWidget >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tkabber provides a Tcl/Tk interface to the Jabber instant messaging
and presence service. 

Although relatively new software, Tkabber is fully-featured. Its
features include:
- emoticons
- file transfers
- avatars
- browsing

and many, many more.

You may need additional packages for full funcionality:
- tk-Img, for more image file formats support
- tcl-tls, for encrypted connections to server
- tclgpgme, for end-to-end message encryption and signing
- tkXwin, for auto-away

%description -l pl
Tkabber udost�pnia interfejs Tcl/Tk dla komunikatora Jabber.

Mimo �e jest to dosy� nowy program, Tkabber ma du�e mo�liwo�ci,
obejmuj�ce:
- emotikony,
- przesy�anie plik�w,
- wcielenia,
- przegl�danie
i wiele, wiele wi�cej.

Do pe�nej funkcjonalno�ci mog� by� potrzebne dodatkowe pakiety:
- tk-Img do obs�ugi wi�kszej liczby format�w plik�w,
- tcl-tls do szyfrowanych po��cze� z serwerem,
- tclgpgme do podpisywania i szyfrowania wiadomo�ci,
- tkXwin do auto-away.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Communications,%{_pixmapsdir}}

%{__make} install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Communications
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README.html examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_applnkdir}/Network/Communications/*.desktop
%{_pixmapsdir}/*
