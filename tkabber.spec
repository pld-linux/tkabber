Summary:	Tk Jabber client
Summary(pl):	Klient Jabbera oparty o Tk
Name:		tkabber
Version:	0.9.7
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jabberstudio.org/projects/tkabber/releases/file/%{name}-%{version}.tar.gz
# Source0-md5:	41a0f24239415edb8e3d2cd86e532f38
Source1:	%{name}.desktop
Source2:	%{name}.png
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
Tkabber udostêpnia interfejs Tcl/Tk dla komunikatora Jabber.

Mimo ¿e jest to dosyæ nowy program, Tkabber ma du¿e mo¿liwo¶ci,
obejmuj±ce:
- emotikony,
- przesy³anie plików,
- wcielenia,
- przegl±danie
i wiele, wiele wiêcej.

Do pe³nej funkcjonalno¶ci mog± byæ potrzebne dodatkowe pakiety:
- tk-Img do obs³ugi wiêkszej liczby formatów plików,
- tcl-tls do szyfrowanych po³±czeñ z serwerem,
- tclgpgme do podpisywania i szyfrowania wiadomo¶ci,
- tkXwin do auto-away.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	PREFIX="%{_prefix}" \
	DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README.html examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
