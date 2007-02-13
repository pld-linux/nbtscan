Summary:	A program for scanning networks for NetBIOS name information
Summary(pl.UTF-8):	Program do skanowania sieci pod kątem informacji o nazwach NetBIOS
Name:		nbtscan
Version:	1.5.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.inetcat.org/software/%{name}-%{version}.tar.gz
# Source0-md5:	85bb085077c380b82a6ff73e0de0c154
URL:		http://www.inetcat.org/software/nbtscan.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NBTscan is a program for scanning IP networks for NetBIOS name
information. It sends NetBIOS status query to each address in supplied
range and lists received information in human readable form. For each
responded host it lists IP address, NetBIOS computer name, logged-in
user name and MAC address (such as Ethernet).

%description -l pl.UTF-8
NBTscan to program do skanowania sieci IP pod kątem informacji o
nazwach NetBIOS. Wysyła zapytanie NetBIOS o stan do każdego adresu z
podanego adresu i wypisuje otrzymane informacje w postaci czytelnej
dla człowieka. Dla każdego hosta, który odpowiedział, wypisuje adres
IP, NetBIOS-ową nazwę komputera, nazwę zalogowanego użytkownika oraz
adres MAC.

%prep
%setup -q -n %{name}-1.5.1a

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D nbtscan $RPM_BUILD_ROOT%{_bindir}/nbtscan

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
