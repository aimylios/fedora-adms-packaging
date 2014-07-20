# This package is part of the Free Electronic Lab.

Name:           mot-adms
Version:        2.3.2
Release:        2%{?dist}
Summary:        An electrical compact device models converter

Group:          Applications/Engineering
License:        LGPLv2+
URL:            http://mot-adms.sourceforge.net/

Source0:        http://sourceforge.net/projects/mot-adms/files/adms-source/2.3/adms-%{version}.tar.gz

# Remove useless perl-GD dependency
Patch0:         mot-adms-remove-BR-perl-GD.patch
Patch1:         mot-adms-format-security.patch

BuildRequires:  flex bison perl-XML-LibXML
BuildRequires:  automake autoconf libtool

%description
ADMS is a code generator that converts electrical compact
device models specified in high-level description language
into ready-to-compile C code for the API of spice simulators.
Based on transformations specified in XML language, ADMS
transforms Verilog-AMS code into other target languages.

%prep
%setup -q -n adms-%{version}

%patch0 -p1 -b .perlGD
%patch1 -p1 -b .format-security
mv README.md README

%build
autoreconf -vif
%configure \
    --disable-static \
    --enable-maintainer-mode \
    --libdir=%{_libdir}/%{name}

# not parallel build safe
make
# %{?_smp_mflags}


%install
make INSTALL="%{_bindir}/install -p" install DESTDIR=%{buildroot}

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO README ChangeLog
%{_bindir}/admsXml
%{_libdir}/%{name}
%{_mandir}/man1/admsXml.1.gz
%{_mandir}/man1/admsCheck.1.gz

%changelog
* Sun Jul 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.2-2
- Remove libtool archive files

* Sun Jul 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.3.2-1
- Update to 2.3.2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-7.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-6.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-5.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-4.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-3.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.9-2.svn1186
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Aug 19 2010 Chitlesh GOORAH <chitlesh [AT] fedoraproject DOT org> - 2.2.9-1.svn1186
- Setup for ngspice and qucs support

* Sun Feb 22 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2.2.9-1
- New package
