# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		casttube
%define		egg_name	casttube
%define		pypi_name	casttube
Summary:	casttube provides a way to interact with the Youtube Chromecast api
Name:		python-%{module}
Version:	0.2.0
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/casttube/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	4bb24ba1639d16c8fa367537bf3b88a6
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
casttube provides a way to interact with the Youtube Chromecast api.

Features:
- Play video
- Play a playlist
- Add video to the end of the play queue
- Play next
- Remove video
- Clear the entire queue

%package -n python3-%{module}
Summary:	casttube provides a way to interact with the Youtube Chromecast api
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
casttube provides a way to interact with the Youtube Chromecast api.

Features:
- Play video
- Play a playlist
- Add video to the end of the play queue
- Play next
- Remove video
- Clear the entire queue

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
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
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
