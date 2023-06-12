#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-BiocManager
Version  : 1.30.21
Release  : 37
URL      : https://cran.r-project.org/src/contrib/BiocManager_1.30.21.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BiocManager_1.30.21.tar.gz
Summary  : Access the Bioconductor Project Package Repository
Group    : Development/Tools
License  : Artistic-2.0
BuildRequires : buildreq-R

%description
# BiocManager
<!-- badges: start -->
[![CRAN
status](https://www.r-pkg.org/badges/version/BiocManager)](https://cran.r-project.org/package=BiocManager)
[![CRAN
release](http://www.r-pkg.org/badges/version-last-release/BiocManager)](https://github.com/Bioconductor/BiocManager/releases)
[![CRAN
downloads](http://cranlogs.r-pkg.org/badges/BiocManager)](https://cran.r-project.org/package=BiocManager)
<!-- badges: end -->

%prep
%setup -q -n BiocManager
pushd ..
cp -a BiocManager buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1686586751

%install
export SOURCE_DATE_EPOCH=1686586751
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BiocManager/DESCRIPTION
/usr/lib64/R/library/BiocManager/INDEX
/usr/lib64/R/library/BiocManager/Meta/Rd.rds
/usr/lib64/R/library/BiocManager/Meta/features.rds
/usr/lib64/R/library/BiocManager/Meta/hsearch.rds
/usr/lib64/R/library/BiocManager/Meta/links.rds
/usr/lib64/R/library/BiocManager/Meta/nsInfo.rds
/usr/lib64/R/library/BiocManager/Meta/package.rds
/usr/lib64/R/library/BiocManager/Meta/vignette.rds
/usr/lib64/R/library/BiocManager/NAMESPACE
/usr/lib64/R/library/BiocManager/NEWS
/usr/lib64/R/library/BiocManager/R/BiocManager
/usr/lib64/R/library/BiocManager/R/BiocManager.rdb
/usr/lib64/R/library/BiocManager/R/BiocManager.rdx
/usr/lib64/R/library/BiocManager/doc/BiocManager.R
/usr/lib64/R/library/BiocManager/doc/BiocManager.Rmd
/usr/lib64/R/library/BiocManager/doc/BiocManager.html
/usr/lib64/R/library/BiocManager/doc/index.html
/usr/lib64/R/library/BiocManager/help/AnIndex
/usr/lib64/R/library/BiocManager/help/BiocManager.rdb
/usr/lib64/R/library/BiocManager/help/BiocManager.rdx
/usr/lib64/R/library/BiocManager/help/aliases.rds
/usr/lib64/R/library/BiocManager/help/paths.rds
/usr/lib64/R/library/BiocManager/html/00Index.html
/usr/lib64/R/library/BiocManager/html/R.css
/usr/lib64/R/library/BiocManager/tests/testthat.R
/usr/lib64/R/library/BiocManager/tests/testthat/test_inet.R
/usr/lib64/R/library/BiocManager/tests/testthat/test_install.R
/usr/lib64/R/library/BiocManager/tests/testthat/test_repositories.R
/usr/lib64/R/library/BiocManager/tests/testthat/test_valid.R
/usr/lib64/R/library/BiocManager/tests/testthat/test_version.R
