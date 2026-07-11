%global tl_name treetex
%global tl_revision 28176

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Draw trees
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/treetex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/treetex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/treetex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Macros to draw trees, within TeX (or LaTeX). The algorithm used is
discussed in an accompanying paper (written using LaTeX 2.09).

