Name:		python-weasyprint
Version:	68.0
Release:	1
Summary:	The Awesome Document Factory
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/weasyprint/
Source0:	weasyprint-68.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(pydyf)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(tinyhtml5)
BuildRequires:	python%{pyver}dist(tinycss2)
BuildRequires:	python%{pyver}dist(cssselect2)
BuildRequires:	python%{pyver}dist(pyphen)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pango)
BuildArch:	noarch
%description
The Awesome Document Factory.

%files
%{py_sitedir}/*
%{_bindir}/*
