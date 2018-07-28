Name:           mot-adms
Version:        2.3.6
Release:        1%{?dist}
Summary:        An electrical compact device models converter

License:        GPLv3
URL:            https://sourceforge.net/projects/mot-adms/

Source:         https://sourceforge.net/projects/mot-adms/files/adms-source/2.3/adms-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-XML-LibXML

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
%setup -q -n adms-%{version}

%build
sh bootstrap.sh
%configure --enable-maintainer-mode
%make_build

%install
%make_install

%files
%{_bindir}/adms*
%{_includedir}/adms/*
%{_libdir}/libadms*.so*
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_mandir}/man1/adms*
%doc AUTHORS ChangeLog README.md
%license COPYING

%changelog
* Sun Jul 29 2018 Aimylios <aimylios@xxx.xx> - 2.3.6-1
- Initial release based on 2.3.4-7.fc29
