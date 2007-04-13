#
# Conditional build:
%bcond_with	privacy		# more privacy
#
Summary:	Tk Jabber client
Summary(pl.UTF-8):	Klient Jabbera oparty o Tk
Name:		tkabber
Version:	0.10.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://files.jabber.ru/tkabber/%{name}-%{version}.tar.gz
# Source0-md5:	f14c77d2d0cf30bc3a7ca298688f847e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-privacy.patch
URL:		http://tkabber.jabber.ru/
BuildRequires:	sed >= 4.0
Requires:	tcl >= 8.3.4-7
Requires:	tcl-tls >= 1.4.1
Requires:	tcllib >= 1.2
Requires:	tclsasl
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
- tclgpgme, for end-to-end message encryption and signing
- tkXwin, for auto-away

%description -l pl.UTF-8
Tkabber udostępnia interfejs Tcl/Tk dla komunikatora Jabber.

Mimo że jest to dosyć nowy program, Tkabber ma duże możliwości,
obejmujące:
- emotikony,
- przesyłanie plików,
- wcielenia,
- przeglądanie
i wiele, wiele więcej.

Do pełnej funkcjonalności mogą być potrzebne dodatkowe pakiety:
- tk-Img do obsługi większej liczby formatów plików,
- tcl-tls do szyfrowanych połączeń z serwerem,
- tclgpgme do podpisywania i szyfrowania wiadomości,
- tkXwin do auto-away.

%prep
%setup -q
%{?with_privacy:%patch0 -p1}

sed -i -e 's#ifaceck##g' Makefile

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
%doc ChangeLog AUTHORS README examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
