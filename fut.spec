Summary:	Fusion Transpiler
Summary(pl.UTF-8):	Konwerter języka Fusion
Name:		fut
Version:	3.2.7
Release:	1
License:	GPL v3+
Group:		Development/Languages
#Source0Download: https://github.com/fusionlanguage/fut/releases
Source0:	https://github.com/fusionlanguage/fut/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	09b0299bd8ebddea58f09e906ff474ae
URL:		https://github.com/fusionlanguage/fut
# C++20 with <format>
BuildRequires:	libstdc++-devel >= 6:13.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fusion Transpiler transpiles the Fusion programming language to C,
C++, C#, D, Java, JavaScript, Python, Swift, TypeScript and OpenCL C.

%description -l pl.UTF-8
Fusion Transpiler przekształca język programowania Fusion na języki C,
C++, C#, D, Java, JavaScript, Python, Swift, TypeScript i OpenCL C.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags} %{rpmcppflags} %{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/{editors,getting-started,history,reference}.md
%attr(755,root,root) %{_bindir}/fut
