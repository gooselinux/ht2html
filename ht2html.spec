Name:		ht2html
Version:	2.0
Release:	10.1%{?dist}
URL:		http://ht2html.sourceforge.net
Source0:	http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}
Source2:	%{name}-LICENSE
License:	Python
Group:		System Environment/Libraries
Summary:	The www.python.org Web site generator
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch
BuildRequires:  python
Requires:  python

%description
The www.python.org Web site generator.

%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} ./LICENSE

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}

install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 calcroot.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 755 ht2html.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 BAWGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 Banner.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 HTParser.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 IPC8Generator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 JPyGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 JPyLocalGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 LinkFixer.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 PDOGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 SelfGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 Sidebar.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 Skeleton.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 StandardGenerator.py $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README LICENSE doc/*.{html,png}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.py
%{_datadir}/%{name}/*.pyc
%{_datadir}/%{name}/*.pyo
%{_bindir}/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.0-10.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0-8
- Rebuild for Python 2.6

* Tue Sep 16 2008 Matt Domsch <mdomsch@fedoraproject.org> - 2.0-7
- BR python, fixes FTBFS BZ#440916

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.0-6
- fix license tag

* Wed Sep 06 2006 Igor Foox <ifoox@redhat.com> 2.0-5
- Remove ghosting of pyo files as per new Fedora Guidelines.

* Tue Jul 25 2006 Igor Foox <ifoox@redhat.com> 2.0-4
- Fix Requires from Python to python.

* Mon Jul 24 2006 Igor Foox <ifoox@redhat.com> 2.0-3
- Remove comment to reference license and include a copy as another source file.
- Add Requires for Python.
- Add dist tag.

* Mon Jul 24 2006 Igor Foox <ifoox@redhat.com> 2.0-2
- Include comment to reference ML thread about licensing.

* Mon Jun 26 2006 Igor Foox <ifoox@redhat.com> 2.0-1
- Changed release number to numeric (1)
- Fixed license to 'Python Software Foundation License'

* Fri Jun 23 2006 Igor Foox <ifoox@redhat.com> 2.0-1jpp_2fc
- Removed BuildRequires of python-devel
- Removed Vendor and Distribution tags
- Changed Source0 to be a URL, and also changed to the file provided by 
upstream
- Changed license to Python License
- Split %%files section into seperate entries for .pyo .pyc and .py files,
%%ghosting the .pyo files

* Thu Jun 1 2006 Igor Foox <ifoox@rehdat.com> 2.0-1jpp_1fc
- Changed buildroot to what Extras expects

* Mon Nov 22 2004 Fernando Nasser <fnasser@redhat.com> 2.0-1jpp
- Import of 2.0-4mdk spec file from
  Guillaume Rousse <g.rousse@linux-mandrake.com>
  David Walluck <walluck@linux-mandrake.com>
