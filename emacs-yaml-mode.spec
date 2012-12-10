%define		rname yaml-mode

Summary:	Major mode for editing YAML file
Name:		emacs-%{rname}
Version:	0.0.4
Release:	%mkrel 2
Epoch:		1
Source0:	%{rname}-%{version}.tar.gz
URL:		http://github.com/yoshiki/yaml-mode/tree/master
License:	GPLv3+
Group:		Editors
BuildRoot:	%_tmppath/%{name}-%{release}-buildroot
Requires:	emacs >= 22.0
BuildRequires:	emacs >= 22.0, texinfo
BuildArch:    	noarch	

%description 
YAML mode is a major Emacs mode for editing YAML.

%prep
%setup -q -n yoshiki-yaml-mode-bce5aa195f30734b2f559ee36065e6c96b36986e/

%build
emacs -batch -q -no-site-file -f batch-byte-compile %{rname}.el 

%install
%__rm -rf %{buildroot}

%__install -m 755 -d %{buildroot}%{_datadir}/emacs/site-lisp
%__install -m 644 %{rname}.el* %{buildroot}%{_datadir}/emacs/site-lisp/

%__install -m 755 -d %{buildroot}%{_sysconfdir}/emacs/site-start.d
cat > %buildroot%_sysconfdir/emacs/site-start.d/%{name}.el << EOF
;; -*- Mode: Emacs-Lisp -*-
; 
; Redistribution of this file is permitted under the terms of the GNU 
; Public License (GPL)
;

(autoload '%{rname} "%{rname}" nil t)
(setq auto-mode-alist (append '(("\\\\.yml?\\\\'" . %{rname})) auto-mode-alist))

(add-hook 'yaml-mode-hook
      '(lambda ()
        (define-key yaml-mode-map "\C-m" 'newline-and-indent)))

EOF

%post
%_install_info %rname

%postun
%_remove_install_info %rname

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%config(noreplace) /etc/emacs/site-start.d/%{name}.el
%_datadir/*/site-lisp/*el*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.0.4-2mdv2011.0
+ Revision: 618056
- the mass rebuild of 2010.0 packages

* Mon Jun 08 2009 Jerome Martin <jmartin@mandriva.org> 1:0.0.4-1mdv2010.0
+ Revision: 383955
- create emacs-yaml-mode

