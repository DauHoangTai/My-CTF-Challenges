FROM php:8.1-apache
RUN a2enmod rewrite
RUN service apache2 restart

COPY flag1.txt /
COPY full_flag.txt /root/full_flag.txt
COPY readflag /
RUN chmod 7777 /readflag

