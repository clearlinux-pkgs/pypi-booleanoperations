#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-booleanoperations
Version  : 0.9.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/57/d9/9eae7bc4ba3a38ab7426522fb08e12df54aec27595d7bcd1bc0670aec873/booleanOperations-0.9.0.zip
Source0  : https://files.pythonhosted.org/packages/57/d9/9eae7bc4ba3a38ab7426522fb08e12df54aec27595d7bcd1bc0670aec873/booleanOperations-0.9.0.zip
Summary  : Boolean operations on paths.
Group    : Development/Tools
License  : MIT
Requires: pypi-booleanoperations-license = %{version}-%{release}
Requires: pypi-booleanoperations-python = %{version}-%{release}
Requires: pypi-booleanoperations-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(pluggy)
BuildRequires : py-python
BuildRequires : pypi(fonttools)
BuildRequires : pypi(pyclipper)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pytest
BuildRequires : tox
BuildRequires : pypi(virtualenv)

%description
BooleanOperations
        =================
        
        Boolean operations on paths which uses a super fast `polygon clipper

%package license
Summary: license components for the pypi-booleanoperations package.
Group: Default

%description license
license components for the pypi-booleanoperations package.


%package python
Summary: python components for the pypi-booleanoperations package.
Group: Default
Requires: pypi-booleanoperations-python3 = %{version}-%{release}

%description python
python components for the pypi-booleanoperations package.


%package python3
Summary: python3 components for the pypi-booleanoperations package.
Group: Default
Requires: python3-core
Provides: pypi(booleanoperations)
Requires: pypi(fonttools)
Requires: pypi(pyclipper)

%description python3
python3 components for the pypi-booleanoperations package.


%prep
%setup -q -n booleanOperations-0.9.0
cd %{_builddir}/booleanOperations-0.9.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640194711
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-booleanoperations
cp %{_builddir}/booleanOperations-0.9.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-booleanoperations/3bdf95815fd839c7dc1d192732ac14bb012d9eef
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-booleanoperations/3bdf95815fd839c7dc1d192732ac14bb012d9eef

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
