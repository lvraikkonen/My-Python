#-*- coding: utf-8 -*-
import sys, os
import urllib, urllib2, re

## change google host
if __name__ == '__main__':

    # load host from 360kb
    html_host  = urllib2.urlopen('http://www.360kb.com/kb/2_122.html')
    html       = html_host.read()
    reg        = r'#base services.*#google hosts 2015 end'
    hostHtmlRe = re.search(reg, html, re.S)
    hostHtml   = hostHtmlRe.group()
    hostHtml   = hostHtml.replace('&nbsp;',' ')
    hostHtml   = hostHtml.replace('<span>','')
    hostHtml   = hostHtml.replace('</span>','')
    hostStr    = hostHtml.replace('<br />','')

    # write host file
    f = open('/etc/hosts','r+')
    host_old = f.read()
    reg = re.compile(r'\r\n#google=.*#google hosts 2015 end', re.S)
    host_new    = re.sub(reg, '', host_old)
    host_new    = host_new + '\r\n#google===========================\r\n' + hostStr

    reg = re.compile(r'account', re.S)
    host_new = re.sub(reg, 'OOXXaccount', host_new)
    print host_new
    f.seek(0)
    f.write(host_new)
    f.close()
    print 'OK'
    f.close()