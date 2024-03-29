# - NOTE
# - in english the word is "promille"
Summary:	promile-qt counts rate of alcohol in function of time from consumption
Summary(pl.UTF-8):	promile-qt oblicza liczbe promili alkoholu w zależności od czasu po jego spożyciu
Name:		promile-qt
Version:	0.8.0
Release:	3
License:	GPL v3
Group:		X11/Applications
Source0:	http://piro.wikidot.com/local--files/promile-qt/%{name}-%{version}-src.tar.bz2
# Source0-md5:	8e44db476a6109ddc2c1059de6dae5c9
URL:		http://piro.wikidot.com/promile-qt
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build >= 4.3.3-3
BuildRequires:	qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
promile-qt counts rate of alcohol in function of time from consumption.

WARNING: This program doesn't have English interface.

%description -l pl.UTF-8
Program oblicza liczbę promili alkoholu w zależności od czasu po jego
spożyciu.

%prep
%setup -q

%build
qmake-qt4 -project
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install promile-qt-0 $RPM_BUILD_ROOT%{_bindir}/promile-qt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog TODO 
%attr(755,root,root) %{_bindir}/*
