Summary:	A program for scanning networks for NetBIOS name information.
Name:		nbtscan
Version:	1.5.1
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.inetcat.org/software/%{name}-%{version}.tar.gz
# Source0-md5:	85bb085077c380b82a6ff73e0de0c154
URL:		http://www.inetcat.org/software/nbtscan.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NBTscan is a program for scanning IP networks for NetBIOS name
information. It sends NetBIOS status query to each address in supplied
range and lists received information in human readable form. For each
responded host it lists IP address, NetBIOS computer name, logged-in
user name and MAC address (such as Ethernet).

%prep
%setup -q -n %{name}-1.5.1a

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make} CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D nbtscan $RPM_BUILD_ROOT/%{_bindir}/nbtscan

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
