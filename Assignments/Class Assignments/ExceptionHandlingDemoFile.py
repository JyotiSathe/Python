


try:
    fd=open("F:/Python/file.txt","r")
    try:
        fd.write("Hello")
    finally:
        fd.close
except Exception as e:
    print e
    print e.__dict__
    print e.args
    print type(e).__name__
