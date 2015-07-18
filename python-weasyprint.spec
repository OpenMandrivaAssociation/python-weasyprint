%global pypi_name weasyprint
%global pypi_oname WeasyPrint
Name:           python-weasyprint
Version:        0.19.2
Release:        1
Group:          Development/Python
Summary:        WeasyPrint converts web documents to PDF

License:        MIT
URL:            http://pypi.python.org/pypi/%{pypi_name}
Source0:        http://pypi.python.org/packages/source/c/%{pypi_oname}/%{pypi_oname}-%{version}.tar.gz
Patch0:         WeasyPrint-0.19.2-fix-python3-build.patch

BuildArch:      noarch
 
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)

Requires:       %{pypi_name}

%rename		python3-weasyprint

%description
WeasyPrint converts web documents to PDF

%package -n %{pypi_name}
Summary:        WeasyPrint converts web documents to PDF
Group:          Development/Python

%description -n %{pypi_name}
WeasyPrint converts web documents to PDF

%package -n python2-%{pypi_name}
Summary:        WeasyPrint converts web documents to PDF
Group:          Development/Python

Requires:       %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pythonegg(setuptools)

%description -n python2-%{pypi_name}
WeasyPrint converts web documents to PDF

%prep
%setup -q -n %{pypi_oname}-%{version}

%apply_patches

pushd .. 
cp -rp %{pypi_oname}-%{version} %{py3dir}

%build
%{__python2} setup.py build

pushd %{py3dir}
%{__python3} setup.py build
popd

%install
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%{python_sitelib}/%{pypi_name}*
%{python_sitelib}/WeasyPrint-%version-py?.?.egg-info

%files -n %{pypi_name}
%_bindir/*

%files -n python2-%{pypi_name}
%{python2_sitelib}/%{pypi_name}*
%{python2_sitelib}/WeasyPrint-%version-py?.?.egg-info

