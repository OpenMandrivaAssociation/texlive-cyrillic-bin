Name:		texlive-cyrillic-bin
Version:	62517
Release:	2
Summary:	Cyrillic bibtex and makeindex
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic-bin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic-bin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-cyrillic-bin.bin = %{EVRD}

%description
TeXLive cyrillic-bin package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/rubibtex
%{_bindir}/rumakeindex
%{_texmfdistdir}/scripts/texlive-extra/rubibtex.sh
%{_texmfdistdir}/scripts/texlive-extra/rumakeindex.sh
%doc %{_mandir}/man1/rubibtex.1*
%doc %{_texmfdistdir}/doc/man/man1/rubibtex.man1.pdf
%doc %{_mandir}/man1/rumakeindex.1*
%doc %{_texmfdistdir}/doc/man/man1/rumakeindex.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/texlive/rubibtex.sh rubibtex
ln -sf %{_texmfdistdir}/scripts/texlive/rumakeindex.sh rumakeindex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
