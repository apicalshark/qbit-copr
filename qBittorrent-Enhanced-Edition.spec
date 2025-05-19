Name:    qBittorrent-Enhanced-Edition
Summary: qBittorrent Enhanced, based on qBittorrent 
Epoch:   1
Version: 5.1.0.10
Release: 2%{?dist}
License: GPL-2.0-or-later
URL:     https://github.com/c0re100/qBittorrent-Enhanced-Edition

Source0: %{url}/archive/refs/tags/release-%{version}.tar.gz


ExcludeArch:   %{ix86}
Conflicts:     qbittorrent
Conflicts:     qbittorrent-nox

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gnupg2
BuildRequires: ninja-build
BuildRequires: systemd
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: libxkbcommon-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-linguist
BuildRequires: rb_libtorrent-devel >= 1.2.12
BuildRequires: desktop-file-utils
BuildRequires: boost-devel >= 1.60
BuildRequires: libappstream-glib
BuildRequires: openssl-devel-engine
BuildRequires: zlib-ng-compat-static

Requires: python3
Recommends: (qgnomeplatform-qt6%{?_isa} if gnome-shell)
Recommends: (qgnomeplatform-qt6%{?_isa} if cinnamon)
Requires:   qt6-qtsvg%{?_isa}

%description
A Bittorrent client using rb_libtorrent and a Qt6 Graphical User Interface.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%package nox
Summary: A Headless Bittorrent Client

%description nox
A Headless Bittorrent client using rb_libtorrent.
It aims to be as fast as possible and to provide multi-OS, unicode support.

%prep
%autosetup -n qBittorrent-Enhanced-Edition-release-%{version}

%build
mkdir build-nox
pushd build-nox
%cmake \
 -DSYSTEMD=ON \
 -Wno-dev \
 -GNinja \
 -DQT6=ON \
 -DGUI=OFF \
 ..
%cmake_build
popd

# Build gui version
mkdir build
pushd build
%cmake \
 -Wno-dev \
 -DQT6=ON \
 -GNinja \
 ..
%cmake_build
popd

%install
# install headless version
pushd build-nox
%cmake_install
popd

# install gui version
pushd build
%cmake_install
popd

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml

%files
%license COPYING
%doc README.md AUTHORS Changelog
%{_bindir}/qbittorrent
%{_metainfodir}/org.qbittorrent.qBittorrent.metainfo.xml
%{_datadir}/applications/org.qbittorrent.qBittorrent.desktop
%{_datadir}/icons/hicolor/*/apps/qbittorrent.*
%{_datadir}/icons/hicolor/*/status/qbittorrent-tray*
%{_mandir}/man1/qbittorrent.1*
%{_mandir}/ru/man1/qbittorrent.1*

%files nox
%license COPYING
%doc README.md AUTHORS Changelog
%{_bindir}/qbittorrent-nox
%{_unitdir}/qbittorrent-nox@.service
%{_mandir}/man1/qbittorrent-nox.1*
%{_mandir}/ru/man1/qbittorrent-nox.1*

%changelog
%autochangelog
