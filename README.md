perl-Authen-Simple-LDAP-rpm
===========================

rpm spec for CPAN perl-Authen-Simple-LDAP module

Target OS
---------

- CentOS 6, RHEL 6 or RHEL clones
- CentOS 7, RHEL 7 or RHEL clones

Install required rpm packagesi for build
-----------------------------------------

### CentOS 7 ###

- CentOS standard
  perl-Class-Data-Inheritable
  perl-Crypt-PasswdMD5
  perl-ExtUtils-MakeMaker
  perl-LDAP
  perl-Module-Implementation
  perl-Params-Validate
  perl-Test-Fatal
  perl-Test-Requires
  perl-Try-Tiny

- EPEL
  perl-Authen-Simple
  perl-Class-Accessor

- Download perl-Authen-Simple-LDAP module tar ball.
http://search.cpan.org/CPAN/authors/id/C/CH/CHANSEN/Authen-Simple-LDAP-0.3.tar.gz

Then, copy rpmbuild's SOURCE directory.

How to build
------------

~$ rpmbuild -ba rpm/SPECS/perl-Authen-Simple-LDAP.spec

