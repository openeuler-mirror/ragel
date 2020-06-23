%bcond_with bootstrap

Name:           ragel
Version:        7.0.0.12
Release:        1
Summary:        Finite state machine compiler

# aapl/ is the LGPLv2+
License:        MIT and LGPLv2+
URL:            http://www.colm.net/open-source/%{name}/
Source0:        https://www.colm.net/files/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
%if %{with bootstrap}
BuildRequires:  kelbt
BuildRequires:  ragel
%endif
BuildRequires:  colm-devel

# Unfortunately, upstream doesn't exist and not possible to find version
Provides:       bundled(aapl)

%description
Ragel compiles executable finite state machines from regular languages.
Ragel targets C, C++ and ASM. Ragel state machines can not only recognize
byte sequences as regular expression machines do, but can also execute code
at arbitrary points in the recognition of a regular language. Code embedding
is done using inline operators that do not disrupt the regular language syntax.

%package devel
Summary:        Development libraries header files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup
# Do not pollute with docs
sed -i -e "/dist_doc_DATA/d" Makefile.am

%build
autoreconf -vfi
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -type f -name '*.la' -print -delete
install -p -m 0644 -D %{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%ldconfig_scriptlets

%files
%license COPYING
%doc CREDITS ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_mandir}/man1/%{name}.1*
%{_libdir}/libfsm.so.*
%{_libdir}/libragel.so.*
%{_datarootdir}/%{name}.lm
%dir %{_datadir}/vim
%dir %{_datadir}/vim/vimfiles
%dir %{_datadir}/vim/vimfiles/syntax
%{_datadir}/vim/vimfiles/syntax/%{name}.vim

%files devel
%{_libdir}/libfsm.so
%{_libdir}/libragel.so
%{_includedir}/%{name}/

%changelog
* Mon Jun 22 2020 Yikun Jiang <yikunkero@gmail.com> - 7.0.0.12-1
- Package init
