under linux (centos); use tornado framework .

easy_install tornado

easy_install torndb

easy_install geoip2


grant all on sms_service.* to sms_service@'127.0.0.1' identified by 'j94a27K';

grant all on log_general.* to logSmsService@'127.0.0.1' identified by 'lj87dc6Z';

flush privileges;


deploy script work with below dictionary.


drwxr-xr-x. 11 root root 4096 Nov 18 19:36 backup

drwxr-xr-x.  2 root root 4096 Nov 18 19:36 bin

-rwxrwxrwx.  1 root root  573 Nov 18 19:28 deployWithBackup.sh

drwxr-xr-x.  2 root root 4096 Nov 18 19:36 logs

drwxr-xr-x.  2 root root 4096 Nov 18 19:36 swap