#!/usr/bin/env python3
import os
import appcache,mimefinder
application_dir="/usr/share/applications"
cache_file=os.path.expanduser("~/.cache/")

#listdir but returns absolute paths
def ldirabs(dirpath):return [os.path.join(dirpath,f) for f in os.listdir(os.path.abspath(dirpath))]

def get_desktop_files():
    try:
        return [f for f in ldirabs(application_dir) if os.path.isfile(f) and ".desktop" in f.lower()]
    except OSError:
        return None
#TODO: check if cached applications still exist before passing off to user, then check if executable exists and is accessible
#TODO: check if the found application is on the PATH, then show the command to the user.
def parse_desktop(desktop_src):
    lines=[f for f in desktop_src.split("\n") if len(f.strip())>0]
    desk_keys={}
    if lines[0].lower()=="[desktop entry]":
        for l in lines[1:]:
            lsplit=l.split("=")
            key=lsplit[0]
            value="=".join(lsplit[1:])
            if "[" in key and "]" in key:
                sub_key=key[key.index("["):key.rindex("]")]
                if key in desk_keys:
                    #sub_key uses the root key which I use for no subkey (like a lil bich)
                    if sub_key=="_":sub_key="__"
                    if type(desk_keys[key])is dict:
                        if sub_key in desk_keys[key]:
                    else:desk_keys[key]={"_":[desk_keys[key]],sub_key:value}
            else:
                #2 lines have exact same key, so converting into a list
                if key in desk_keys:
                    if type(desk_keys[key]) is list:desk_keys[key].append(value)
                    else:desk_keys[key]=[desk_keys[key],value]
    else:raise ValueError("Invalid desktop file")
    return desk_keys





def test():
    print(mimefinder.get_mime("./README.md"))

def main():
    test()

if __name__=="__main__":
    main()
