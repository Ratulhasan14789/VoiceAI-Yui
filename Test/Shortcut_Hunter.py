import os, sys
import winshell

shortcuts = {}
dir_list=[]
dir_list2=[]
user_programs = winshell.programs()
for dirpath, dirnames, filenames in os.walk(user_programs):
    relpath = dirpath[1 + len(user_programs):]
    shortcuts.setdefault(
        relpath, []
    ).extend(
        [winshell.shortcut(os.path.join(dirpath, f)) for f in filenames]
    )

all_programs = winshell.programs(common=1)
for dirpath, dirnames, filenames in os.walk(all_programs):
    relpath = dirpath[1 + len(all_programs):]
    shortcuts.setdefault(
        relpath, []
    ).extend(
        [winshell.shortcut(os.path.join(dirpath, f)) for f in filenames]
    )

for relpath, lnks in sorted(shortcuts.items()):
    level = relpath.count("\\")
    for lnk in lnks:
        name, _ = os.path.splitext(os.path.basename(lnk.lnk_filepath))
        dir_list2.append("%s" % (lnk.path))

for items in dir_list2:
    if items.endswith('.exe') or items.endswith('.EXE'):
        if 'unins' in items or 'Unins' in items or 'UNINS' in items:
            pass
        else:
            dir_list.append(items)
dir_list = list(dict.fromkeys(dir_list))
for items in dir_list:
    print(items)
