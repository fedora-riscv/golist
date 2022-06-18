# Generated by go2rpm
%bcond_without check

# https://pagure.io/golist
%global goipath         pagure.io/golist
%global forgeurl        https://pagure.io/golist
Version:                0.10.1

%gometa

%global common_description %{expand:
A tool to analyse the properties of a Go (Golang) codebase.}

%global godocs          NEWS.md README.md
%global golicenses      LICENSE

Name:           golist
Release:        9%{?dist}
Summary:        A tool to analyse the properties of a Go (Golang) codebase

# Upstream license specification: BSD-3-Clause
License:        BSD
URL:            %{gourl}
#Source0:        #{gosource}  # Not supported by current forge macros.
Source0:        https://pagure.io/golist/archive/v%{version}/golist-%{version}.tar.gz

BuildRequires:  golang(github.com/urfave/cli)

# Before split of /usr/bin/golist.
# Remove in Fedora 34.
Conflicts: go-compilers-golang-compiler < 1-34

%description
%{common_description}


%prep
%goprep


%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done


%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/


%if %{with check}
%check
%gocheck
%endif


%files
%doc README.md NEWS.md
%license LICENSE
%{_bindir}/*


%changelog
* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.10.1-9
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Maxwell G <gotmax@e.email> - 0.10.1-7
- Rebuild for new go version. Related: rhbz#2033978

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 16:03:20 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10.1-1
- Update to latest version
- Rewrite for latest Go macros

* Mon May 27 01:19:35 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.10.0-1
- Initial package
