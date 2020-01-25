#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Data
%define		pnam	Page-Pageset
Summary:	Data::Page::Pageset - change long page list to be shorter and well navigate
Name:		perl-Data-Page-Pageset
Version:	1.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	859bb3abdfa710ef38b1140274eae051
URL:		http://search.cpan.org/dist/Data-Page-Pageset/
BuildRequires:	perl-Data-Page
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pages number can be very high, and it is not comfortable to show user
from the first page to the last page list. Sometimes we need split the
page list into some sets to shorten the page list, the form is like:

1-6 7-12 13 14 15 16 17 18 19-24 25-30 31-36 37-41

the first two part indicats the two pagesets, and in current pageset,
we provide the normal page list from the first one to the last one,
and provide the rest pagesets to indicate the pages scope.

In this module, you can specify the pages_per_set or max_pagesets for
fine showing.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Data/Page
%{perl_vendorlib}/Data/Page/*.pm
%{perl_vendorlib}/Data/Page/Pageset
%{_mandir}/man3/*
