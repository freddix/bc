Summary:	GNU's bc (a numeric processing language) and dc (a calculator)
Name:		bc
Version:	1.06
Release:	33
License:	GPL
Group:		Applications/Math
Source0:	ftp://ftp.gnu.org/pub/gnu/bc/%{name}-%{version}.tar.gz
# Source0-md5:	d44b5dddebd8a7a7309aea6c36fda117
Patch1:		%{name}-readline.patch
Patch2:		%{name}-flex.patch
Patch3:		%{name}-save_adr.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The bc package includes bc and dc. Bc is an arbitrary precision
numeric processing arithmetic language. Dc is an interactive arbitrary
precision stack based calculator, which can be used as a text mode
calculator. Install the bc package if you need its number handling
capabilities or if you would like to use its text mode calculator.

%prep
%setup -q
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-readline
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*

