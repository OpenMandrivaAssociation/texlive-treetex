# revision 28176
# category Package
# catalog-ctan /macros/plain/contrib/treetex
# catalog-date 2012-01-20 11:26:32 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-treetex
Version:	20190228
Release:	1
Summary:	Draw trees
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/treetex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/treetex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/treetex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Macros to draw trees, within TeX (or LaTeX). The algorithm used
is discussed in an accompanying paper (written using LaTeX
2.09).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/treetex/classes.tex
%{_texmfdistdir}/tex/plain/treetex/l_pic.tex
%{_texmfdistdir}/tex/plain/treetex/treetex.tex
%doc %{_texmfdistdir}/doc/plain/treetex/epodd.tex
%doc %{_texmfdistdir}/doc/plain/treetex/readme
%doc %{_texmfdistdir}/doc/plain/treetex/tree_doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
