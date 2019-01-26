try:
    import magic
    MAGIC_INSTALLED=True
except ImportError:
    MAGIC_INSTALLED=False
try:
    import mimetypes
    MIMETYPES_INSTALLED=True
except ImportError:
    MIMETYPES_INSTALLED=False
import subprocess,os
def _disable_magic():
    global MAGIC_INSTALLED
    MAGIC_INSTALLED=False
def _enable_magic():
    global MAGIC_INSTALLED
    MAGIC_INSTALLED=True
def _magic_enabled():
    global MAGIC_INSTALLED
    return MAGIC_INSTALLED
def _enable_mimetypes():
    global MIMETYPES_INSTALLED
    MIMETYPES_INSTALLED=True
def _disable_mimetypes():
    global MIMETYPES_INSTALLED
    MIMETYPES_INSTALLED=False
def _mimetypes_enabled():
    global MIMETYPES_INSTALLED
    return MIMETYPES_INSTALLED
def get_mime(file_path):
    if _magic_enabled():
        print("Using magic installed")
        return magic.from_file(file_path,mime=True)
    else:
        try:
            comm=subprocess.run(["file","-ib",os.path.abspath(file_path)],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if comm.return_code==0:
                outp=comm.stdout
                try:outp=outp.decode()
                except:pass
                #bruh if u got a file that literally says this imma b fugn pissed
                if "no such file or directory" in outp.lower():
                    raise
                else:
                    print("Using file command")
                    mime=outp.split(";")[0]
            else:raise
        except:
            if MIMETYPES_INSTALLED:
                print("Using mimetypes.guess_type")
                return mimetypes.guess_type(file_path)[0]
            else:raise ValueError("Could not determine the mime type of the file")
