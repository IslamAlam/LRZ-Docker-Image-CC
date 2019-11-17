# create and build this Dockerfile

#FROM mltooling/ml-hub:latest
FROM mltooling/ml-hub:0.1.6
LABEL maintainer="Islam Mansour <is3mansour@gmail.com>"

# you need to use root user for apt-get or make install
USER root
#RUN apt-get update && apt-get install some-package

#RUN useradd -ms /bin/bash -p "$(openssl passwd -1 admin)"  admin
#RUN useradd -ms /bin/bash -p "$(openssl passwd -1 admin)"  admin
#RUN echo "qazwsx123\nqazwsx123\n" | passwd admin
# RUN echo "qazwsx123\nqazwsx123\n" | passwd jupyter
RUN useradd --create-home admin 
RUN echo "admin:cleartext_password" | chpasswd
RUN echo "root:cleartext_password" | chpasswd
# RUN user="admin" \
#     password="test1234" \
#     useradd --create-home $user \
#     echo -e "$password\n$password\n" | passwd --stdin $user\
#     echo $password
#     #     echo "$password" | passwd $user \
# use notebook user for pip/conda
#USER $NB_UID
#RUN pip install --no-cache-dir mxnet-cu92mkl

# always switch back to notebook user at the end
USER $NB_UID