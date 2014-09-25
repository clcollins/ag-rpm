%define nickname the_silver_searcher

Name:		ag
Version:	0.24.1
Release:	0
Summary:	Code searching tool

Group:		Applications/Utilities

License:        Apache 2.0
URL:            https://github.com/ggreer/the_silver_searcher
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:		https://github.com/ggreer/the_silver_searcher/archive/%{version}.tar.gz

BuildRequires:		pcre
BuildRequires:		pcre-devel
BuildRequires:		automake
BuildRequires:		ppl
BuildRequires:		cpp
BuildRequires:		mpfr
BuildRequires:		xz-devel
BuildRequires:		zlib
BuildRequires:		zlib-devel

%description
A code searching tool similar to ack, with a focus on speed.

%prep
%setup -q -n %{nickname}-%{version}

%build
%__aclocal
%__autoconf
%__autoheader
%__automake --add-missing
%configure
make

%install
%__sed -i 's|$(DESTDIR)|$(ROOT)$(DESTDIR)|g' Makefile
make ROOT="$RPM_BUILD_ROOT" install

%clean

%files
%{_bindir}/%{name}
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/%{nickname}/completions/%{name}.bashcomp.sh


%changelog
* Wed Sep 25 2014 Chris Collins <collins.christopher@gmail.com> - 0.24.1
- Initial 0.24.1 release

