%global _disable_source_fetch 0
%global _dist_version %{?fedora}

Name: ultramarine-repos
Version: %{_dist_version}
Release: 0.3
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

%package cyber
Summary: Repository for the Cyber Desktop
Source400: cyber-desktop.repo
%description cyber
Repository file for the Cyber Desktop

%package cutefish
Summary: Repository for the Cutefish Desktop
Source500: cutefish-desktop.repo
%description cutefish
Repository file for the Cutefish Desktop


%prep

%build

%install
# DNF repos
mkdir -p %{buildroot}/%{_sysconfdir}/yum.repos.d/

#common
cp -avx %{SOURCE100} %{buildroot}/%{_sysconfdir}/yum.repos.d/

#extras
cp -avx %{SOURCE205} %{buildroot}/%{_sysconfdir}/yum.repos.d/
cp -avx %{SOURCE206} %{buildroot}/%{_sysconfdir}/yum.repos.d/
cp -avx %{SOURCE209} %{buildroot}/%{_sysconfdir}/yum.repos.d/

#extras-jam
cp -avx %{SOURCE300} %{buildroot}/%{_sysconfdir}/yum.repos.d/

#cyber
cp -avx %{SOURCE400} %{buildroot}/%{_sysconfdir}/yum.repos.d/

#cutefish
cp -avx %{SOURCE500} %{buildroot}/%{_sysconfdir}/yum.repos.d/

# Flatpak remotes
mkdir -p %{buildroot}/%{_sysconfdir}/flatpak/remotes.d
cp -avx %{SOURCE200} %{buildroot}/%{_sysconfdir}/flatpak/remotes.d/

%post
# rpmfusion-free.repo
cat <<'EOF' >%{_sysconfdir}/yum.repos.d/rpmfusion-free.repo
[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=14d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
excludepkgs=*freeworld* ffmpeg-libs gstreamer1-libav gstreamer1-plugins-ugly libaacs* libdca* libde265* libdvbcsa* libfame* libftl* libheif* libmms* libmpeg3* libndi* libquicktime* librtmp* libshairport* live555* medialibrary* mjpegtools-libs mythffmpeg vo-amrwbenc* x264* x265* xine-lib* xvidcore*

[rpmfusion-free-debuginfo]
name=RPM Fusion for Fedora $releasever - Free - Debug
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/debug/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-debug-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever

[rpmfusion-free-source]
name=RPM Fusion for Fedora $releasever - Free - Source
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/source/SRPMS/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
EOF

# rpmfusion-free-updates.repo
cat <<'EOF' >%{_sysconfdir}/yum.repos.d/rpmfusion-free-updates.repo
[rpmfusion-free-updates]
name=RPM Fusion for Fedora $releasever - Free - Updates
#baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-updates-released-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
excludepkgs=*freeworld* ffmpeg-libs gstreamer1-libav gstreamer1-plugins-ugly libaacs* libdca* libde265* libdvbcsa* libfame* libftl* libheif* libmms* libmpeg3* libndi* libquicktime* librtmp* libshairport* live555* medialibrary* mjpegtools-libs mythffmpeg vo-amrwbenc* x264* x265* xine-lib* xvidcore*

[rpmfusion-free-updates-debuginfo]
name=RPM Fusion for Fedora $releasever - Free - Updates Debug
#baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch/debug/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-updates-released-debug-$releasever&arch=$basearch
enabled=0
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever

[rpmfusion-free-updates-source]
name=RPM Fusion for Fedora $releasever - Free - Updates Source
#baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/SRPMS/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-updates-released-source-$releasever&arch=$basearch
enabled=0
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
EOF

# rpmfusion-nonfree.repo
cat <<'EOF' >%{_sysconfdir}/yum.repos.d/rpmfusion-nonfree.repo
[rpmfusion-nonfree]
name=RPM Fusion for Fedora $releasever - Nonfree
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-$releasever&arch=$basearch
enabled=0
enabled_metadata=1
metadata_expire=14d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-debuginfo]
name=RPM Fusion for Fedora $releasever - Nonfree - Debug
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/debug/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-debug-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Source
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/source/SRPMS/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-source-$releasever&arch=$basearch
enabled=0
metadata_expire=7d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever
EOF

# rpmfusion-nonfree-updates.repo
cat <<'EOF' >%{_sysconfdir}/yum.repos.d/rpmfusion-nonfree-updates.repo
[rpmfusion-nonfree-updates]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-updates-released-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-updates-debuginfo]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates Debug
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch/debug/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-updates-released-debug-$releasever&arch=$basearch
enabled=0
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-updates-source]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates Source
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/SRPMS/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-updates-released-source-$releasever&arch=$basearch
enabled=0
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever
EOF

%files

%files common
%{_sysconfdir}/yum.repos.d/ultramarine.repo

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

%files cyber
%{_sysconfdir}/yum.repos.d/cyber-desktop.repo

%files cutefish
%{_sysconfdir}/yum.repos.d/cutefish-desktop.repo
