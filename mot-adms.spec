# This package is part of the Free Electronic Lab.

Name:           mot-adms
Version:        2.2.9
Release:        3.svn1186%{?dist}
Summary:        An electrical compact device models converter

Group:          Applications/Engineering
License:        LGPLv2+
URL:            http://mot-adms.sourceforge.net/

#Source0:        http://downloads.sourceforge.net/sourceforge/%{_name}/%{name}-%{version}.tar.gz
Source0:        mot-adms.tar.gz
# The above source file can be download with this Tcl script
Source1:        mot-adms-download.tcl

# Remove useless perl-GD dependency
Patch0:         mot-adms-remove-BR-perl-GD.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  flex bison perl-XML-LibXML automake libtool

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
%setup -q -n %name

%patch0 -p1 -b .perlGD

# minor cleanups and preparations
rm -rf auxconf && mkdir auxconf
%{__autoheader}
%{__libtoolize} --force --copy
%{__aclocal}
touch ChangeLog
%{__automake} --add-missing -c
%{__autoconf}

%build
%configure \
    --disable-static \
    --enable-maintainer-mode \
    --libdir=%{_libdir}/%{name}
# not parallel build safe
make
# %{?_smp_mflags}


%install
rm -rf %{buildroot}
make INSTALL="%{_bindir}/install -p" install DESTDIR=%{buildroot}

#find  %{buildroot}/%{_libdir} -name "*.la" -exec rm -f {} \;
#find  %{buildroot}/%{_libdir} -name "*.a"  -exec rm -f {} \;

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc ABOUT-NLS AUTHORS COPYING TODO README NEWS
%{_bindir}/admsXml
%{_libdir}/%{name}
%{_mandir}/man1/admsXml.1.gz


%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-3.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 2.2.9-1.svn1186
- Setup for ngspice and qucs support

* Sun Feb 22 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.9-1
- New package
