Name:		texlive-templates-fenn
Version:	15878
Release:	1
Summary:	Templates for TeX usage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/templates/fenn
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-fenn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-fenn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
