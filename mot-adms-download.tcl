#!/usr/bin/tclsh

# PROJECT     : Free Electronic Lab
# AUTHOR      : Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org>
# DESCRIPTION : Download script for mot-adms
# DATE        : Thu Aug 19 19:21:21 CEST 2010

set pkgname "mot-adms"

file delete -force $pkgname
file mkdir $pkgname

if { [ catch { exec svn co https://mot-adms.svn.sourceforge.net/svnroot/mot-adms/trunk/adms $pkgname } errmsg ] } {
    # Error thrown - package not found.
    puts "FEL - ERROR: $pkgname could not be checkout"
    puts "$errmsg\n\tExiting !"
    exit -1
}



if { [ catch { exec tar czvf  /home/chitlesh/rpmbuild/SOURCES/$pkgname.tar.gz $pkgname } errmsg ] } {
    # Error thrown - package not found.
    puts "FEL - ERROR: $pkgname could not be tarballed"
    puts "$errmsg\n\tExiting !"
    exit -1
}

file delete -force $pkgname

