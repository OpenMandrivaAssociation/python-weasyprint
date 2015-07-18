%global pypi_name weasyprint
%global pypi_oname WeasyPrint

%define python3 1

Name:           python-weasyprint
Version:        0.19.2
Release:        %mkrel 5
Group:          Development/Python
Summary:        WeasyPrint converts web documents to PDF

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/c/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
Patch0:         WeasyPrint-0.19.2-fix-python3-build.patch

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python)
BuildRequires:  python-setuptools

Requires:       %{pypi_name}

%description
WeasyPrint converts web documents to PDF

%package -n %{pypi_name}
Summary:        WeasyPrint converts web documents to PDF
Group:          Development/Python

%description -n %{pypi_name}
WeasyPrint converts web documents to PDF

%if %python3
%package -n python3-%{pypi_name}
Summary:        WeasyPrint converts web documents to PDF
Group:          Development/Python

Requires:       %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
WeasyPrint converts web documents to PDF
%endif

%prep
%setup -q -n %{pypi_oname}-%{version}

%apply_patches

%if %python3
cp -a . %{py3dir}
%endif

%build
%{__python} setup.py build

%if %python3
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%install
%if %python3
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif

%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/WeasyPrint-%version-py?.?.egg-info

%files -n %{pypi_name}
%_bindir/*

%if %python3
%files -n python3-%{pypi_name}
%{python3_sitelib}/%{pypi_name}*
%{python3_sitelib}/WeasyPrint-%version-py?.?.egg-info
%endif


%changelog
* Wed Oct 15 2014 umeabot <umeabot> 0.19.2-5.mga5
+ Revision: 750747
- Second Mageia 5 Mass Rebuild

* Sat Sep 27 2014 tv <tv> 0.19.2-4.mga5
+ Revision: 729966
- rebuild for missing pythoneggs deps

* Tue Sep 16 2014 umeabot <umeabot> 0.19.2-3.mga5
+ Revision: 688413
- Mageia 5 Mass Rebuild

* Mon Jun 02 2014 philippem <philippem> 0.19.2-2.mga5
+ Revision: 630659
- fix files list

  + pterjan <pterjan>
    - Rebuild for new Python

* Thu Oct 31 2013 neoclust <neoclust> 0.19.2-1.mga4
+ Revision: 548104
- imported package python-weasyprint

