%global forgeurl https://gitlab.freedesktop.org/wlroots/wlr-protocols
%global commit 2b8d43325b7012cc3f9b55c08d26e50e42beac7d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           wlr-protocols
Version:        1^git%{shortcommit}
Release:        1
Summary:        Wayland protocols designed for use in wlroots (and other compositors)
License:        MIT
URL:            https://gitlab.freedesktop.org/wlroots/wlr-protocols
Source0:        %{url}/-/archive/%{commit}/%{name}-%{commit}.tar.bz2

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  pkgconfig(wayland-scanner)

%description
Wayland protocols designed for use in wlroots (and other compositors).

%package        devel
Summary:        Wayland protocols designed for use in wlroots (and other compositors)

%description    devel
Wayland protocols designed for use in wlroots (and other compositors).

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%make_build
%install
%make_install

%files devel
%{_datadir}/pkgconfig/wlr-protocols.pc
%{_datadir}/wlr-protocols/
