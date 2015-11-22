Name:		perl-Authen-Simple-LDAP
Version:	0.3
Release:	1%{?dist}
Summary:	Simple LDAP authentication
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/Authen-Simple-LDAP/
Source0:	http://www.cpan.org/authors/id/C/CH/CHANSEN/Authen-Simple-LDAP-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:	perl(Authen::Simple)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Class::Data::Inheritable)
BuildRequires:	perl(Crypt::PasswdMD5)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Module::Implementation)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl(Test::Requires)
BuildRequires:	perl(Try::Tiny)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Authenticate against a LDAP service.

%prep
%setup -q -n Authen-Simple-LDAP-%{version}

%build
%{__perl} Makefile.PL installdirs=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sun Nov 22 2015 Toru Takahashi <torutk@gmail.com> - 0.3-1 for centos7
- Modified for CentOS 7
* Mon Jan 28 2013 Toru Takahashi <torutk@gmail.com> - 0.3-1
- Specfile created based on perl-Authen-Simple-0.4-5, and modified.
