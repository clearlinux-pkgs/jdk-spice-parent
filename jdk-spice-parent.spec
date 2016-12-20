Name     : jdk-spice-parent
Version  : parent
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/17/spice-parent-17.pom
Source0  : http://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/17/spice-parent-17.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : openjdk-dev
BuildRequires : javapackages-tools
BuildRequires : python3
BuildRequires : six
BuildRequires : lxml

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/maven-poms/spice-parent-parent.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/spice-parent-parent.xml \
%{buildroot}/usr/share/maven-poms/spice-parent-parent.pom \
%{buildroot}/usr/share/java/spice-parent-parent.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/spice-parent-parent.xml
/usr/share/maven-poms/spice-parent-parent.pom
