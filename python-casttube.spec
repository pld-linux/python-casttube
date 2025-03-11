#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		casttube
%define		egg_name	casttube
%define		pypi_name	casttube
Summary:	casttube - a way to interact with the Youtube Chromecast API
Summary(pl.UTF-8):	casttube - sposób interakcji z API Youtube Chromecast
Name:		python-%{module}
Version:	0.2.1
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/casttube/
Source0:	https://files.pythonhosted.org/packages/source/c/casttube/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	37f86084a36e0dbd72d45b0452b4b676
URL:		https://pypi.org/project/casttube/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
casttube provides a way to interact with the Youtube Chromecast API.

Features:
- Play video
- Play a playlist
- Add video to the end of the play queue
- Play next
- Remove video
- Clear the entire queue

%description -l pl.UTF-8
casttube udostępnia sposób interakcji z API Youtube Chromecast.

Możliwości:
- odtwarzanie filmów
- odtwarzanie z listy
- dodawanie filmów na końcu kolejki odtwarzania
- odtwarzanie następnego filmu
- usuwanie filmu
- czyszczenie całej kolejki

%package -n python3-%{module}
Summary:	casttube - a way to interact with the Youtube Chromecast API
Summary(pl.UTF-8):	casttube - sposób interakcji z API Youtube Chromecast
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
casttube provides a way to interact with the Youtube Chromecast API.

Features:
- Play video
- Play a playlist
- Add video to the end of the play queue
- Play next
- Remove video
- Clear the entire queue

%description -n python3-%{module} -l pl.UTF-8
casttube udostępnia sposób interakcji z API Youtube Chromecast.

Możliwości:
- odtwarzanie filmów
- odtwarzanie z listy
- dodawanie filmów na końcu kolejki odtwarzania
- odtwarzanie następnego filmu
- usuwanie filmu
- czyszczenie całej kolejki

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
