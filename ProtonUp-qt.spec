Name:		protonup-qt
Version:	2.11.1
Release:	1.git%{?dist}
Summary:	Install and manage Proton-GE and Luxtorpeda for Steam and Wine-GE for Lutris
License:	GPL3
URL:		https://davidotek.github.io/protonup-qt
Source0:	https://github.com/DavidoTek/ProtonUp-Qt/archive/refs/tags/v%{version}.tar.gz
Source1:	net.davidotek.pupgui2.sh

BuildRequires: python3
BuildRequires:  python3-devel
Requires: python-evdev
Requires: python3-pyxdg
Requires: python3-requests
Requires: python3-zstandard
Requires: python3-steam
Requires: python3-vdf
Requires: python3-pip
Requires: qt6-qttools

%description
Proton-GE and Wine-GE updater.

%prep
%setup -n ProtonUp-Qt-%{version}

%build
mkdir -p $RPM_BUILD_ROOT%{python3_sitearch}/
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -Rf pupgui2 -t $RPM_BUILD_ROOT%{python3_sitearch}/
cp -r share $RPM_BUILD_ROOT/usr/
cp %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/net.davidotek.pupgui2
chmod 755 $RPM_BUILD_ROOT%{_bindir}/net.davidotek.pupgui2
ln -s /usr/bin/net.davidotek.pupgui2 $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{python3_sitearch}/pupgui2/
%{_bindir}/net.davidotek.pupgui2
%{_bindir}/protonup-qt
%{_datadir}/*

%changelog
%autochangelog