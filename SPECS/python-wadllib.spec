%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

Name:		python-wadllib	
Version:	1.2.0
Release:	1.ius%{?dist}
Summary:	A Python library for navigating WADL files

Group:		Applicatons/System
License:	GPLv3
URL:		https://launchpad.net/wadllib
Source0:	http://launchpad.net/wadllib/trunk/%{version}/+download/wadllib-%{version}.tar.gz
Patch0:		remove_install_requires.diff

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

BuildRequires:	python, python-setuptools
Requires:	python, python-simplejson, python-elementtree, python-lazr.uri

%description
The Web Application Description Language is an XML vocabulary for describing the capabilities of HTTP resources. 
wadllib can be used in conjunction with an HTTP library to navigate and manipulate those resources.

%prep
%setup -q -n wadllib-%{version}
%patch0 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README.txt
%{python_sitelib}/wadllib-%{version}-py%{pyver}.egg-info/
%{python_sitelib}/wadllib/

%changelog
* Fri Jun 10 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.2.0-1.ius
- Initial spec
