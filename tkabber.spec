Summary:	Tk Jabber client
Summary(pl):	Klient Jabbera oparty o Tk
Name:		tkabber
Version:	0.9.3beta
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jabber.ru/projects/tkabber/tkabber-0.9beta/%{name}-%{version}.tar.gz
URL:		http://www.jabber.ru/projects/tkabber/index_en.html
Requires:	tcl >= 8.3.4-7
Requires:	tk >= 8.3.3
Requires:	tcllib >= 1.2
Requires:	BWidget >= 1.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tkabber provides a Tcl/Tk interface to the Jabber instant messaging and
presence service. 

Although relatively new software, Tkabber is fully-featured. Its features
include:

- emoticons
- file transfers
- avatars
- browsing

and many, many more.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install PREFIX="%{_prefix}" DESTDIR="$RPM_BUILD_ROOT"

rm -rf $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS README.html examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
