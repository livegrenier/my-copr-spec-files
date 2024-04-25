# Rust doesn't create data for a -debuginfo package
%global debug_package %{nil}

Name:           icedtea-web
Version:        1.8.8
Release:        0%{?dist}.12
Summary:        Additional Java components for OpenJDK - Java browser plug-in and Web Start implementation

License:    LGPLv2+ and GPLv2 with exceptions
URL:        https://github.com/AdoptOpenJDK/IcedTea-Web
Source0:    https://github.com/AdoptOpenJDK/IcedTea-Web/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch0:     patchOutDunce.patch
# https://access.redhat.com/documentation/en-us/openjdk/11/pdf/using_alt-java/openjdk-11-using_alt-java-en-us.pdf
Patch1:     altjava.patch
Patch2:     disable-applet-support.diff
Patch3:     java11-compatibility.diff
Patch4:     icedtea-web-1.8.8-javadoc.patch
Patch5:     icedtea-web-1.8.8-bash-completion.patch
Patch6:     icedtea-web-1.8.8-applet-docs.patch

BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     bash-completion
BuildRequires:     cargo
BuildRequires:     desktop-file-utils
#BuildRequires:     glib2-devel
BuildRequires:     java-11-openjdk-devel
BuildRequires:     javapackages-local
BuildRequires:     javapackages-tools
BuildRequires:     libappstream-glib
BuildRequires:     tagsoup
BuildRequires:     zip

## For functionality and the OpenJDK dirs
Requires:          java-11-openjdk
#Requires:          javapackages-tools
#Recommends:        bash-completion
#maven fragments
#Requires(post):    javapackages-tools
#Requires(postun):  javapackages-tools

# When itw builds against it, it have to be also in runtime
Requires:          tagsoup

# Post requires alternatives to install tool alternatives.
Requires(post):    %{_sbindir}/alternatives
# jnlp protocols support
Requires(post):    GConf2
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun):  %{_sbindir}/alternatives
# jnlp protocols support
Requires(postun):  GConf2

# Cover third party repositories
Obsoletes:         javaws < 1.8.8-1
Provides:          javaws = %{version}-%{release}
Provides:          javaws%{?_isa} = %{version}-%{release}

%description
The IcedTea-Web project provides a an implementation of Java Web Start
(originally based on the Netx project) and a settings tool to
manage deployment settings for the aforementioned plugin and Web Start
implementations. 

%package javadoc
Summary:    API documentation for IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.

%package devel
Summary:    pure sources for debugging IcedTea-Web
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch

%description devel
This package contains ziped sources of the IcedTea-Web project.

%prep
%setup -q -n IcedTea-Web-%{name}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
rm -rf netx/sun netx/net/sourceforge/jnlp/{NetxPanel.java,runtime/RhinoBasedPacEvaluator.java,util/WindowsDesktopEntry.java}
%patch5 -p1
%patch6 -p1

%build
autoreconf --force --install
%configure \
  --with-pkgversion=fedora-%{release}-%{_arch} \
  --docdir=%{_datadir}/javadoc/%{name} \
  --with-jdk-home=%{_jvmdir}/java-11-openjdk \
  --with-jre-home=%{_jvmdir}/jre-11-openjdk \
  --program-suffix=.itweb \
  --disable-native-plugin \
  --disable-pluginjar \
  --with-itw-libs=DISTRIBUTION \
  --with-modularjdk-file=%{_sysconfdir}/java/%{name} \
  --enable-shell-launchers
%make_build

%install
%make_install

# bash-completion is unfortunately not handled by 'make install'
#install -D -p -m 0644 completion/javaws.bash $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/javaws
#install -D -p -m 0644 completion/itweb-settings.bash $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/itweb-settings
#install -D -p -m 0644 completion/policyeditor.bash $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/policyeditor

# Move javaws man page to a more specific name
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/javaws.1 $RPM_BUILD_ROOT%{_mandir}/man1/javaws.itweb.1
mv -f $RPM_BUILD_ROOT%{_mandir}/man1/policyeditor.1 $RPM_BUILD_ROOT%{_mandir}/man1/policyeditor.itweb.1

# Install desktop files
#install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications policyeditor.desktop

# install MetaInfo file for firefox
install -D -p -m 0644 metadata/%{name}.metainfo.xml $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml
#DESTDIR=%{buildroot} appstream-util install metadata/%{name}.metainfo.xml
# install MetaInfo file for javaws
install -D -p -m 0644 metadata/%{name}-javaws.appdata.xml $RPM_BUILD_ROOT%{_metainfodir}/%{name}-javaws.metainfo.xml
#DESTDIR=%{buildroot} appstream-util install metadata/%{name}-javaws.appdata.xml

# maven fragments generation
mkdir -p $RPM_BUILD_ROOT%{_javadir}/
ln -s ../%{name}/javaws.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
#ln -s ../%{name}/plugin.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-plugin.jar
install -D -p -m 0644 metadata/%{name}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}.pom
#install -D -p -m 0644 metadata/%{name}-plugin.pom $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}-plugin.pom

%mvn_artifact $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}.pom $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
#%%mvn_artifact $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}-plugin.pom $RPM_BUILD_ROOT%{_javadir}/%{name}-plugin.jar

install -D -p -m 0644 netx.build/lib/src.zip $RPM_BUILD_ROOT%{_datadir}/%{name}/javaws.src.zip
#install -D -p -m 0644 liveconnect/lib/src.zip $RPM_BUILD_ROOT%{_datadir}/%{name}/plugin.src.zip

# %%ghost
touch $RPM_BUILD_ROOT{%{_bindir}/{javaws,itweb-settings,policyeditor},%{_mandir}/man1/{javaws,policyeditor}.1}

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.metainfo.xml

%post
alternatives \
  --install %{_bindir}/javaws				javaws.%{_arch}		%{_bindir}/javaws.itweb 110000 --family java-11-openjdk.%{_arch} \
  --slave   %{_bindir}/itweb-settings			itweb-settings		%{_bindir}/itweb-settings.itweb \
  --slave   %{_bindir}/policyeditor			policyeditor		%{_bindir}/policyeditor.itweb \
  --slave   %{_mandir}/man1/javaws.1.gz			javaws.1.gz		%{_mandir}/man1/javaws.itweb.1.gz \
  --slave   %{_mandir}/man1/policyeditor.1.gz		policyeditor.1.gz	%{_mandir}/man1/policyeditor.itweb.1.gz

alternatives \
  --install %{_bindir}/javaws				javaws.%{_arch}		%{_bindir}/javaws.itweb.sh 110000 --family java-11-openjdk.%{_arch} \
  --slave   %{_bindir}/itweb-settings			itweb-settings		%{_bindir}/itweb-settings.itweb.sh \
  --slave   %{_bindir}/policyeditor			policyeditor		%{_bindir}/policyeditor.itweb.sh \
  --slave   %{_mandir}/man1/javaws.1.gz			javaws.1.gz		%{_mandir}/man1/javaws.itweb.1.gz \
  --slave   %{_mandir}/man1/policyeditor.1.gz		policyeditor.1.gz	%{_mandir}/man1/policyeditor.itweb.1.gz

gconftool-2 --set /desktop/gnome/url-handlers/jnlp/command --type=string '%{_bindir}/javaws.itweb %s' &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlp/enabled --type=bool true &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlps/command --type=string '%{_bindir}/javaws.itweb %s' &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlps/enabled --type=bool true &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
  alternatives --remove javaws.%{_arch} %{_bindir}/javaws.itweb
  alternatives --remove javaws.%{_arch} %{_bindir}/javaws.itweb.sh
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlp/command &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlp/enabled &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlps/command &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlps/enabled &> /dev/null || :
fi
exit 0

%files
%license COPYING
%doc AUTHORS NEWS README
%dir %{_sysconfdir}/java/%{name}/
%config(noreplace) %{_sysconfdir}/java/%{name}/itw-modularjdk.args
%ghost %{_bindir}/javaws
%{_bindir}/javaws.itweb
%{_bindir}/javaws.itweb.sh
%ghost %{_bindir}/itweb-settings
%{_bindir}/itweb-settings.itweb
%{_bindir}/itweb-settings.itweb.sh
%ghost %{_bindir}/policyeditor
%{_bindir}/policyeditor.itweb
%{_bindir}/policyeditor.itweb.sh
%{_datadir}/applications/javaws.desktop
%{_datadir}/applications/itweb-settings.desktop
%{_datadir}/applications/policyeditor.desktop
%{_datadir}/bash-completion/completions/javaws
%{_datadir}/bash-completion/completions/itweb-settings
%{_datadir}/bash-completion/completions/policyeditor
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/javaws.jar
#%{_datadir}/%{name}/javaws-plugin.jar
%{_datadir}/%{name}/javaws_splash.png
%{_javadir}/%{name}.jar
#%{_javadir}/%{name}-plugin.jar
%{_mavenpomdir}/%{name}.pom
#%{_mavenpomdir}/%{name}-plugin.pom
%{_metainfodir}/%{name}.metainfo.xml
%{_metainfodir}/%{name}-javaws.metainfo.xml
%{_datadir}/pixmaps/javaws.png
%{_mandir}/man1/%{name}.1*
#%{_mandir}/man1/%{name}-plugin.1*
%{_mandir}/man1/itweb-settings.1*
%ghost %{_mandir}/man1/javaws.1*
%{_mandir}/man1/javaws.itweb.1*
%ghost %{_mandir}/man1/policyeditor.1*
%{_mandir}/man1/policyeditor.itweb.1*

%files javadoc
%license COPYING
%{_datadir}/javadoc/%{name}/

%files devel
%license COPYING
%{_datadir}/%{name}/javaws.src.zip

%changelog
