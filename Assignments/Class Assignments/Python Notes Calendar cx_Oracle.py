>>> import calendar
>>> print calendar.month(2018,06)
     June 2018
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30

>>> print calendar.monthrange(2018,06)
(4, 30)
>>> calendar.prcal(2017)
                                  2017

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31


>>> from datetime import date
>>> f_date = date(2014, 7, 2)
>>> l_date = date(2014, 7, 11)
>>> delta = l_date - f_date
>>> print(delta.days)
9






C:\Python27\Scripts>pip.exe install cx_Oracle --upgrade
Collecting cx_Oracle
  Downloading cx_Oracle-6.2.1-cp27-cp27m-win_amd64.whl (121kB)
    100% |################################| 122kB 266kB/s
Installing collected packages: cx-Oracle
Successfully installed cx-Oracle-6.2.1


>>> import cx_Oracle
>>> connection=cx_Oracle.connect('system/Jyoti2113')
>>> cursor=connection.cursor()
>>> querystring="select * from STOCK"
>>> cursor.execute(querystring)
<cx_Oracle.Cursor on <cx_Oracle.Connection to user system@local>>
>>> row=cursor.fetchone()
>>> print row[1]
"C10"
>>> print row[2]
"Stock 10"
>>> print row[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
>>> print row
(10, '"C10"', '"Stock 10"')
>>> cursor.close()
>>> connection.close()
>>>


>>> help("modules")

Please wait a moment while I gather a list of all available modules...

BaseHTTPServer      antigravity         idlelib             sgmllib
Bastion             anydbm              ihooks              sha
CGIHTTPServer       argparse            imageop             shelve
Canvas              array               imaplib             shlex
ConfigParser        ast                 imghdr              shutil
Cookie              asynchat            imp                 signal
Dialog              asyncore            importlib           site
DocXMLRPCServer     atexit              imputil             smtpd
FileDialog          audiodev            inspect             smtplib
FixTk               audioop             io                  sndhdr
HTMLParser          base64              itertools           socket
MimeWriter          bdb                 json                sqlite3
MySQLdb             binascii            keyword             sre
Queue               binhex              lib2to3             sre_compile
ScrolledText        bisect              linecache           sre_constants
SimpleDialog        bs4                 locale              sre_parse
SimpleHTTPServer    bsddb               logging             ssl
SimpleXMLRPCServer  bz2                 macpath             stat
SocketServer        cPickle             macurl2path         statvfs
StringIO            cProfile            mailbox             string
Tix                 cStringIO           mailcap             stringold
Tkconstants         calendar            markupbase          stringprep
Tkdnd               cgi                 marshal             strop
Tkinter             cgitb               math                struct
UserDict            chunk               md5                 subprocess
UserList            cmath               mhlib               sunau
UserString          cmd                 mimetools           sunaudio
_LWPCookieJar       code                mimetypes           symbol
_MozillaCookieJar   codecs              mimify              symtable
__builtin__         codeop              mmap                sys
__future__          collections         modulefinder        sysconfig
_abcoll             colorsys            msilib              tabnanny
_ast                commands            msvcrt              tarfile
_bisect             compileall          multifile           telnetlib
_bsddb              compiler            multiprocessing     tempfile
_codecs             contextlib          mutex               test
_codecs_cn          cookielib           netrc               textwrap
_codecs_hk          copy                new                 this
_codecs_iso2022     copy_reg            nntplib             thread
_codecs_jp          csv                 nt                  threading
_codecs_kr          ctypes              ntpath              time
_codecs_tw          curses              nturl2path          timeit
_collections        cx_Oracle           numbers             tkColorChooser
_csv                datetime            opcode              tkCommonDialog
_ctypes             dbhash              operator            tkFileDialog
_ctypes_test        decimal             optparse            tkFont
_elementtree        difflib             os                  tkMessageBox
_functools          dircache            os2emxpath          tkSimpleDialog
_hashlib            dis                 parser              toaiff
_heapq              distutils           pdb                 token
_hotshot            doctest             pickle              tokenize
_io                 dumbdbm             pickletools         trace
_json               dummy_thread        pip                 traceback
_locale             dummy_threading     pipes               ttk
_lsprof             easy_install        pkg_resources       tty
_md5                email               pkgutil             turtle
_msi                encodings           platform            types
_multibytecodec     ensurepip           plistlib            unicodedata
_multiprocessing    errno               popen2              unittest
_mysql              exceptions          poplib              urllib
_mysql_exceptions   filecmp             posixfile           urllib2
_osx_support        fileinput           posixpath           urlparse
_pyio               fnmatch             pprint              user
_random             formatter           profile             uu
_sha                fpformat            pstats              uuid
_sha256             fractions           pty                 warnings
_sha512             ftplib              py_compile          wave
_socket             functools           pyclbr              weakref
_sqlite3            future_builtins     pydoc               webbrowser
_sre                gc                  pydoc_data          wheel
_ssl                genericpath         pyexpat             whichdb
_strptime           get-pip             quopri              winsound
_struct             getopt              random              wsgiref
_subprocess         getpass             re                  xdrlib
_symtable           gettext             repr                xml
_testcapi           glob                rexec               xmllib
_threading_local    gzip                rfc822              xmlrpclib
_tkinter            hashlib             rlcompleter         xxsubtype
_warnings           heapq               robotparser         zipfile
_weakref            hmac                runpy               zipimport
_weakrefset         hotshot             sched               zlib
_winreg             htmlentitydefs      select
abc                 htmllib             sets
aifc                httplib             setuptools

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose descriptions contain the word "spam".
