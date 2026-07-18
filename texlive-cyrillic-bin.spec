%global tl_name cyrillic-bin
%global tl_revision 62517
%global tl_bin_links rubibtex:%{_texmfdistdir}/scripts/texlive-extra/rubibtex.sh rumakeindex:%{_texmfdistdir}/scripts/texlive-extra/rumakeindex.sh

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Cyrillic bibtex and makeindex
Group:		Publishing
URL:		https://www.ctan.org/pkg/cyrillic-bin
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic-bin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cyrillic-bin.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cyrillic-bin.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
Cyrillic bibtex and makeindex

