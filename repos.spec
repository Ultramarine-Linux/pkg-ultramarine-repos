%global _disable_source_fetch 0
%global _dist_version %{?fedora}

Name: ultramarine-repos
Version: %{_dist_version}
Release: 0.71
License: MIT
Summary: Repositories for Ultramarine Linux
Requires: %{name}-common = %{version}-%{release}
Recommends: %{name}-extras = %{version}-%{release}
Suggests: %{name}-extras-jam = %{version}-%{release}
Provides: ultramarine-repos(%{_dist_version}) = %{_dist_version}
%description
Metapackage for Ultramarine Linux repositories

%package common
Summary: Common repository for Ultramarine Linux
Requires: fedora-repos(%{version})
Source100: ultramarine.repo
Source101: ultramarine-updates.repo
%description common
Common repository file for Ultramarine Linux

%package extras
Summary: Additional repositories for Ultramarine Linux
Requires: distribution-gpg-keys
Requires: flatpak
Source200: https://flathub.org/repo/flathub.flatpakrepo

# Don't own the rpmfusion repositories, let it be overridden by the real packages

#Source201: rpmfusion-free.repo
#Source202: rpmfusion-free-updates.repo
#Source203: rpmfusion-nonfree.repo
#Source204: rpmfusion-nonfree-updates.repo
Source205: docker-ce.repo
Source206: vscodium.repo
Source209: akmods-secureboot.repo
%description extras
Additional repository files for Ultramarine Linux that provides access to popular software that are not shipped by default:
    - Flathub's Flatpak repo (enabled by default)
    - RPMFusion Free (all patented codecs filtered out)
    - RPMFusion Nonfree (disabled by default)
    - Repositories for secureboot support for 'akmod' kernel modules (enabled by default)
    - Docker CE (disabled by default)
    - VSCodium (enabled by default)

%package extras-jam
Summary: Additional packages for Audio Production
Source300: fedorajam-plus.repo
%description extras-jam
PatrickL's extra Copr repositories for audio production. Includes:
    - yabridge (Yet Another [plugin] Bridge) by Robbert https://github.com/robbert-vdh/yabridge --> enabled by default
    - cappyishihara's Wine-TkG patch
    - libcurl-gnutls for some plugins with issues (Matt Tytel Vital, for example.)  --> enabled by default

%prep

%build

%install
# DNF repos
mkdir -p %{buildroot}/%{_sysconfdir}/yum.repos.d/

#common
cp -avx %{SOURCE100} %{buildroot}/%{_sysconfdir}/yum.repos.d/
cp -avx %{SOURCE101} %{buildroot}/%{_sysconfdir}/yum.repos.d/
#extras
cp -avx %{SOURCE205} %{buildroot}/%{_sysconfdir}/yum.repos.d/
cp -avx %{SOURCE206} %{buildroot}/%{_sysconfdir}/yum.repos.d/
cp -avx %{SOURCE209} %{buildroot}/%{_sysconfdir}/yum.repos.d/

#extras-jam
cp -avx %{SOURCE300} %{buildroot}/%{_sysconfdir}/yum.repos.d/

# Flatpak remotes
mkdir -p %{buildroot}/%{_sysconfdir}/flatpak/remotes.d
cp -avx %{SOURCE200} %{buildroot}/%{_sysconfdir}/flatpak/remotes.d/

%files

%files common
%{_sysconfdir}/yum.repos.d/ultramarine.repo
%{_sysconfdir}/yum.repos.d/ultramarine-updates.repo
%files extras
%{_sysconfdir}/flatpak/remotes.d/flathub.flatpakrepo
%{_sysconfdir}/yum.repos.d/akmods-secureboot.repo
%{_sysconfdir}/yum.repos.d/docker-ce.repo
%{_sysconfdir}/yum.repos.d/vscodium.repo
#%%{_sysconfdir}/yum.repos.d/rpmfusion-free.repo
#%%{_sysconfdir}/yum.repos.d/rpmfusion-free-updates.repo
#%%{_sysconfdir}/yum.repos.d/rpmfusion-nonfree.repo
#%%{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-updates.repo

%files extras-jam
%{_sysconfdir}/yum.repos.d/fedorajam-plus.repo
