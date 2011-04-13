Summary:	A small implementation of AVL trees
Summary(pl.UTF-8):	Mała implementacja drzew AVL
Name:		libavl
Version:	0.3.5
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://alioth.debian.org/~jblache/forked-daapd/%{name}_%{version}.tar.gz
# Source0-md5:	882c68ea7f71876ca110f3b84d7ab12d
URL:		http://blog.technologeek.org/category/hacks/forked-daapd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AVLTree is a small implementation of AVL trees for the C programming
language.

%description -l pl.UTF-8
AVLTree jest niewielką implementacją drzew AVL dla języka C.

%package devel
Summary:	Header files for libavl
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki libavl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libavl.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki libavl.

%prep
%setup -q -n avl-%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT%{_prefix} \
	$RPM_BUILD_ROOT%{_includedir} \
	$RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	libdir=%{_libdir} \
	includedir=%{_includedir} \
	LDCONFIG=true \
        LIBRARIES="*.so*"

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libavl.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libavl.so
%{_includedir}/*.h
