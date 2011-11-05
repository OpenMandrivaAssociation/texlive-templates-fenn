# revision 15878
# category Package
# catalog-ctan /info/templates/fenn
# catalog-date 2009-08-28 15:51:43 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-templates-fenn
Version:	20090828
Release:	1
Summary:	Templates for TeX usage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/templates/fenn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-fenn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-fenn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A set of templates for using LaTeX packages that the author
uses, comprising: - scrlttr2.tex: a letter, written with
scrlttr2.cls from the KOMA-Script bundle; - dinbrief.tex: a
letter according to the German (DIN) standards, written with
dinbrief.cls; - kbrief.tex: a brief memo ('Kurzbrief') to
accompany enclosures, as used in German offices, again based on
dinbrief; - vermerk.tex: a general form for taking down notes
on events in the office; and - diabetes.tex: a diary for the
basis-bolus insulin therapy of diabetes mellitus, using
scrartcl.cls from the KOMA-Script bundle.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/templates-fenn/diabetes.tex
%doc %{_texmfdistdir}/doc/latex/templates-fenn/dinbrief.tex
%doc %{_texmfdistdir}/doc/latex/templates-fenn/kbrief.tex
%doc %{_texmfdistdir}/doc/latex/templates-fenn/scrlttr2.tex
%doc %{_texmfdistdir}/doc/latex/templates-fenn/scrlttr2en.tex
%doc %{_texmfdistdir}/doc/latex/templates-fenn/templates-fenn-de.txt
%doc %{_texmfdistdir}/doc/latex/templates-fenn/templates-fenn-en.txt
%doc %{_texmfdistdir}/doc/latex/templates-fenn/vermerk.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
