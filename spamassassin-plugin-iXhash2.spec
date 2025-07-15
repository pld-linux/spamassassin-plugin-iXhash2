Summary:	SpamAssassin plugin to lookup e-mail checksums in blacklists
Name:		spamassassin-plugin-iXhash2
Version:	2.05
Release:	2
License:	Apache v2.0
Group:		Applications/Networking
Source0:	http://mailfud.org/iXhash2/iXhash2-%{version}.tar.gz
# Source0-md5:	3acd152c17207ae2454a35c29b41a258
Source1:	spamassassin-iXhash2.eml
Patch0:		spamassassin-iXhash2-2.05-conf.patch
URL:		http://mailfud.org/iXhash2/
BuildRequires:	perl-devel
Requires:	spamassassin >= 3.2
Provides:	spamassassin-iXhash = 1.5.5-2
Obsoletes:	spamassassin-iXhash < 1.5.5-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iXhash2 is an unofficial improved version of the iXhash spam filter
plugin for SpamAssassin, adding async DNS lookups for performance and
removing unneeded features but fully compatible with the iXhash 1.5.5
(http://www.ixhash.net/) implementation. It computes MD5 checksums of
fragments of the body of an e-mail and compares them to those of known
spam using DNS queries to a RBL-like name server. So it works similar
to the standard plugins that use the Pyzor, Razor and DCC software
packages from within SpamAssassin.

%prep
%setup -q -n iXhash2-%{version}
%patch -P0 -p1 -b .conf
cp -pf %{SOURCE1} iXhash2.eml

%build

%install
rm -rf $RPM_BUILD_ROOT

install -D -p iXhash2.cf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/iXhash2.cf
touch -c -r iXhash2.cf.conf $RPM_BUILD_ROOT%{_sysconfdir}/mail/spamassassin/iXhash2.cf
install -D -p iXhash2.pm $RPM_BUILD_ROOT%{perl_vendorlib}/Mail/SpamAssassin/Plugin/iXhash2.pm
install -d $RPM_BUILD_ROOT%{_mandir}/man3/
perldoc iXhash2.pm > $RPM_BUILD_ROOT%{_mandir}/man3/Mail::SpamAssassin::Plugin::iXhash2.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README iXhash2.eml
%config(noreplace) %{_sysconfdir}/mail/spamassassin/iXhash2.cf
%{perl_vendorlib}/Mail/SpamAssassin/Plugin/iXhash2.pm
%{_mandir}/man3/*.3pm*
