Name: boost-jam
Version: 3.1.3
Summary: Build tool
Release: 1
Source: %{name}-%{version}.tgz

License: GPL
Group: Development/Tools
URL: http://www.boost.org
Packager: Vladimir Prus <ghost@cs.msu.su>
BuildRoot: /var/tmp/%{name}-%{version}.root

%description
Boost Jam is a build tool based on FTJam, which in turn is based on 
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible 
with Perforce Jam.

Authors:
	Perforce Jam : Cristopher Seiwald
	FT Jam       : David Turner
	Boost Jam    : David Abrahams

%prep
%setup -n %{name}-%{version}

%build
LOCATE_TARGET=bin ./build.sh

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 755 bin/bjam $RPM_BUILD_ROOT%{_bindir}/bjam-%{version}
ln -sf bjam-%{version} $RPM_BUILD_ROOT%{_bindir}/bjam
ln -sf bjam-%{version} $RPM_BUILD_ROOT%{_bindir}/jam
install -m 644 $BOOST_JAM_DOCS $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

find $RPM_BUILD_ROOT -name CVS -type d -depth -exec rm -r {} \;

%files
%defattr(-,root,root)
%attr(755,root,root) /usr/bin/*
%doc %{_docdir}/%{name}-%{version}


%clean
rm -rf $RPM_BUILD_ROOT

