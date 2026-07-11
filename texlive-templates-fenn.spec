%global tl_name templates-fenn
%global tl_revision 79121

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Templates for TeX usage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/templates/fenn
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-fenn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/templates-fenn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of templates for using LaTeX packages that the author uses,
comprising: scrlttr2.tex: a letter, written with scrlttr2.cls from the
KOMA-Script bundle dinbrief.tex: a letter according to the German (DIN)
standards, written with dinbrief.cls kbrief.tex: a brief memo
('Kurzbrief') to accompany enclosures, as used in German offices, again
based on dinbrief vermerk.tex: a general form for taking down notes on
events in the office; and diabetes.tex: a diary for the basis-bolus
insulin therapy of diabetes mellitus, using scrartcl.cls from the KOMA-
Script bundle

