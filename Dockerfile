FROM rocker/verse:3.6.0

WORKDIR /home/inter-testing-feedback-2018

COPY . /home/inter-testing-feedback-2018

RUN Rscript docker-r-packages.R

RUN apt-get purge -y texlive-local texinfo tex-common

# texlive install script has to be run manually because it is interactive. the
# script is located at /home/texlive/install-tl-20190410
RUN mkdir /home/texlive;\
    cd /home/texlive;\
    wget ftp://tug.org/historic/systems/texlive/2019/install-tl-unx.tar.gz;\
    tar -xf install-tl-unx.tar.gz
