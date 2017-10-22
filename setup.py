#!/usr/bin/python

import os, subprocess, re, sys

def main():
    try:
        action = str(sys.argv[1])
    except:
        action = None

    if action != None:
        s = ""
        sys.argv = sys.argv[1:]
        length = len(sys.argv)
        for index, elem in enumerate(sys.argv):
            if index + 1 == length:
                s += elem
            else:
                s += elem + ", "
    else:
        s = action
    print
    print "Actions: {}".format(s)
    print

    divider = "============================================================="

    def download_resources():
        print("")
        print(divider)
        print("")
        print("-- Downloading resources --")
        print("")
        base = os.path.expanduser('~')
        items = [
            {
                "name" : "Abstract Desktop",
                "id" : "0B0TzE5qCAZXSOUhIdnlCLW5wVEE",
                "filename" : "abstract-desktop.jpg"
            }
            , {
                "name" : "Jade Ambience Desktop",
                "id" : "0B0TzE5qCAZXSdGw3MjNvLVNEQXc",
                "filename" : "jade-ambience.jpg"
            }
            , {
                "name" : "Northern Lights Desktop",
                "id" : "0B0TzE5qCAZXSYnNsVWZhUXpRS1k",
                "filename" : "northern-lights.jpg"
            }
            , {
                "name" : "Albert to Searchkey",
                "id" : "0B0TzE5qCAZXSdlVzNHNYQTF1d2s",
                "filename" : "albert-to-searchkey.py"
            }
            , {
                "name" : "Jade Albert Theme",
                "id" : "0B0TzE5qCAZXScE9BYTNtYWhZVTA",
                "filename" : "jade-theme.qss"
            }
        ]
        for item in items:
            print('\t- {}'.format(item['name']))
            subprocess.call(['wget', '--content-disposition', 'https://drive.google.com/uc?export=download&id=%s' % item['id'], '-P', base + '/Downloads'])

    def handle_gallium_theme():
        print("")
        print(divider)
        print("")
        print("-- Setting Theme to: Arc-Dark-GalliumOS --")
        print("")
        print(divider)
        subprocess.call([
        'xfconf-query'
        , '-c'
        , 'xsettings'
        , '-p'
        , '/Net/ThemeName'
        , '-s'
        , 'Arc-Dark-GalliumOS'
        ])

        raw_input('''
CONFIGURE WINDOWS

1) open Window Manager
2) under "Button Layout", drag buttons to the left in the following order:
    - Close
    - Minimize
    - Maximize
3) under "Title alignment", select "Center"
4) close the Window Manager

... Press "enter" to continue: ''')
        print("")
        print(divider)

    def handle_taskbar():
        print("")
        print("-- Setting panel height to: 25px --")
        # set height
        subprocess.call([
              'xfconf-query'
            , '-c'
            , 'xfce4-panel'
            , '-p'
            , '/panels/panel-1/size'
            , '-s'
            , '25'
        ])

        print("")
        print("-- Turning panel autohide to: ON --")
        print("")
        print(divider)
        # autohide
        subprocess.call([
              'xfconf-query'
            , '-c'
            , 'xfce4-panel'
            , '-p'
            , '/panels/panel-1/autohide-behavior'
            , '-s'
            , '2'
        ])

        raw_input('''
CONFIGURE TASKBAR

1) right click and select "Panel > Panel Preferences"
2) under "Items" tab, select and remove "Window Buttons"
3) close the Panel Preferences window
4) right click each pinned shortcut icon -- next to the gallium start button -- and select "remove"

... Press "enter" to continue:''')
        print("")
        print(divider)
        print("")

    def handle_deb_installs():
        base = os.path.expanduser('~')
        items = [
            {
                "name" : "Chrome",
                "commands" : ['wget', 'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'],
                "location" : base + '/google-chrome-stable_current_amd64.deb'
            }
            , {
                "name" : "Atom",
                "commands" : ['wget', 'https://atom.io/download/deb', '-O', 'atom.deb'],
                "downloadUrl" : "https://atom.io/download/deb",
                "location" : base + '/atom.deb'
            }
        ]
        for item in items:
            subprocess.call(item['commands'])
            subprocess.call([
                  'sudo'
                , 'dpkg'
                , '-i'
                , item['location']
            ])
            subprocess.call([
                  'sudo'
                , 'apt-get'
                , 'install'
                , '-f'
            ])
            subprocess.call(['rm', item['location']])

    def handle_apt_get_Installs():
        # Installation library for Albert
        subprocess.call(['sudo', 'add-apt-repository', 'ppa:nilarimogard/webupd8'])
        subprocess.call(['sudo', 'apt-get', 'update'])

        # Installation library for ksuperkey
        subprocess.call(['sudo', 'add-apt-repository', 'ppa:mehanik/ksuperkey'])
        subprocess.call(['sudo', 'apt-get', 'update'])

        # Install
        subprocess.call(['sudo', 'apt-get', 'install'
        , 'firefox'
        , 'inkscape'
        , 'blender'
        , 'docky'
        , 'albert'
        , 'ksuperkey'
        , 'xdotool'
        , 'tmux'
        ])

    def handle_atom_dependencies():
        print(divider)
        print("")
        print("-- Adding atom dependencies --")
        print("")
        subprocess.call(['apm', 'install', 'platformio-ide-terminal'])
        subprocess.call(['apm', 'install', 'atom-pair'])
        subprocess.call(['apm', 'install', 'atom-runner'])
        print("")

    def handle_desktop_wallpapers():
        base = os.path.expanduser('~') + '/'
        items = [
            'abstract-desktop.jpg',
            'jade-ambience.jpg',
            'northern-lights.jpg'
        ]
        print("")
        print(divider)
        print("")
        print("-- Adding Desktop Wallpapers --")
        print("")
        for item in items:
            print("\t- {}\n".format(item))
        for item in items:
            subprocess.call(['sudo', 'scp', base + 'Downloads/' + item, '/usr/share/backgrounds/xfce'])

    def set_desktop_wallpaper(IMG):
        print("")
        print("-- Setting desktop wallpaper to: {} --".format(IMG))
        print("")
        print(divider)
        base = os.path.expanduser('~')
        subprocess.call([
              'xfconf-query'
            , '--channel'
            , 'xfce4-desktop'
            , '--property'
            , '/backdrop/screen0/monitor0/image-path'
            , '--set'
            , '/home/chrx/Pictures/' + IMG
        ])
        subprocess.call([
              'xfconf-query'
            , '-c'
            , 'xfce4-desktop'
            , '-p'
            , '/backdrop/screen0/monitor0/image-show'
            , '-s'
            , 'true'
        ])
        subprocess.call([
              'xfconf-query'
            , '--channel'
            , 'xfce4-desktop'
            , '--property'
            , '/backdrop/screen0/monitor0/workspace0/last-image'
            , '--set'
            , '/usr/share/backgrounds/xfce/' + IMG
        ])

    def handle_albert_configuration():
        print("")
        print("-- Adding custom Albert theme: jade-theme --")
        print("")
        print(divider)
        base = os.path.expanduser('~') + '/'
        directory = base + '.local/share/albert/themes'
        fileName = 'jade-theme.qss'
        filePath = directory + '/' + fileName

        if not os.path.exists(directory):
            os.makedirs(directory)

        subprocess.call(['scp', base + 'Downloads/' + fileName, directory])

        raw_input('''
ASSIGN SHORTCUT KEY TO ALBERT

1) Launch Albert
2) open Albert Settings (top-right: gear icon)
3) select "Hotkeys"
4) gesture shortcut keys to assign

... Press "enter" to continue: ''')
        print("")
        print(divider)
        raw_input('''
CHANGE ALBERT THEME

1) restart Albert
2) open Albert Settings
3) select "Theme" dropdown
4) select "jade-theme"

... Press "enter" to continue: ''')
        print("")

    def handle_alt_key_status():
        print(divider)
        print("")
        print("-- Disabling alt key binding: easy-click --")
        # Disable easy-click alt binding
        subprocess.call([
              'xfconf-query'
            , '-c'
            , 'xfwm4'
            , '-p'
            , '/general/easy_click'
            , '-s'
            , 'none'
        ])

    def handle_albert_to_searchkey():
        print("")
        print("-- Moving Albert-To-Searchkey into place --")
        print("")
        base = os.path.expanduser('~')
        subprocess.call(['scp', base + '/Downloads/albert-to-searchkey.sh', base])

    def configure_docky():
        print(divider)
        raw_input('''
DOCKY CONFIGURATION

1) Launch the Docky app
2) Select the Docky icon (first icon in dock)
3) Select theme "HUD"
4) Select Hiding "Intellihide"
5) Set zoom to "146%"
6) Select "3D Background"
7) Close Docky Settings
8) Now, on the dock, launch, right-click, and select "Pin" for the following:
    - Thunar File Manager
    - Terminal Emulator
    - Chrome
    - Atom

... Press "enter" to continue: ''')
        print("")
        print(divider)

    def handle_autostart():
        print("")
        print("-- Creating Autostart Sessions: --")
        print("")
        base = base = os.path.expanduser('~')
        path = base + '/.config/autostart/'
        items = [
            {
                "name": "Albert",
                "fileName": "Albert.desktop",
                "content": '''[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=Albert
Comment=
Exec=albert
OnlyShowIn=XFCE;
StartupNotify=false
Terminal=false
Hidden=false
'''
            }
            , {
                "name": "Albert To Searchkey",
                "fileName": "Albert To Searchkey.desktop",
                "content": '''[Desktop Entry]
Encoding=UTF-8
Version=0.9.4
Type=Application
Name=Albert To Searchkey
Comment=
Exec=sh /home/chrx/albert-to-searchkey.sh
OnlyShowIn=XFCE;
StartupNotify=false
Terminal=false
Hidden=false
'''
            }
            , {
                "name": "Docky",
                "fileName": "docky.desktop",
                "content": '''[Desktop Entry]
Name=Docky
Type=Application
Exec=docky
Terminal=false
Icon=docky
Comment=The finest dock no money can buy.
NoDisplay=false
Categories=Utility;
'''
            }
        ]

        for item in items:
            if not os.path.exists(path + item['fileName']):
                FILE = open(path + item['fileName'], 'w')
                FILE.write(item['content'])
                FILE.close()
                print("\t- {} created".format(item['name']))
            else:
                print("")
                print("\t- {} already exists!".format(item['name']))
        print("")

    def handle_auth_file():
        print(divider)
        print("")
        print("-- Adding ssh auth key --")
        base = os.path.expanduser('~')
        directory = base + '/.ssh'
        fileName = 'authorized_keys2'
        filePath = directory + '/' + fileName

        if not os.path.exists(directory):
            os.makedirs(directory)

        if not os.path.exists(filePath):
            file(filePath, 'w').close()

        #== Key to my 13" macbook pro
        key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC4mnzVEZPIB3G719bPU22xLplY/CAfSWQcr7nySI+8FCABrBFWZWMQ7R2+9hBfXwzEYfugu+zdAwqhCCqFh5ytpEbLA/Xc4EKGcOdmMwjMSsYCRhwsE5CGyTek8pvhEYkPgnc00BsC8LBoC7iVVXd9VtzXXBAhjfpjvOJiFERZ+wAgrssCXEer+avYrWS7RTN3kKkOW2Xm6bfq7UjOP9JNYVGqhUp9W1fF01Vu0LRGqIXn5aa5D6e2bOuGjIZaiU+BFZCUWP6iOsS9PVDpxBYbOAJeA8boAZ9FKRlxpLQhG0nM3DIkVQgf29yuyfN5BHZc4zS+/MB/Nj8PiXtjekfb jaderigby@Jades-MacBook-Pro.local'

        def process_auth_file(filePath, key):
            FILE = open(filePath, 'r')
            data = FILE.read()
            FILE.close()
            pat = re.escape(key)
            match = re.search(pat, data)
            if match:
                print("")
                print "\t- key already exists!"
            else:
                FILE = open(filePath, 'w')
                if data == '':
                    FILE.write(key)
                else:
                    FILE.write(data + '\n' + key)
                FILE.close()

        process_auth_file(filePath, key)
        print("")
        print(divider)
        print("")

    def add_tm_alias():
        print("-- Setting tmux alias --")
        base = os.path.expanduser('~')
        alias = '''
alias tm="tmux -S /tmp/shareds attach -t share"
'''
        FILE = open(base + '/.bashrc', 'r')
        data = FILE.read()
        FILE.close()
        pat = re.escape(alias)
        match = re.search(pat, data)
        if match:
            print("")
            print("\t- alias already set!")
        else:
            print("\t- alias tm is set")
            FILE = open(base + '/.bashrc', 'w')
            data += alias
            FILE.write(data)
            FILE.close()
        print("")
        print(divider)

    def configure_caps_lock():
        raw_input('''
MAP CAPS LOCK

1) Launch "Keyboard" app
2) Select "Application Shortcuts" tab
3) Add a new item
4) Command: xdotool key Caps_Lock
5) Click "OK"
6) Gesture with Alt+Super_L

... Press "enter" to continue: ''')
        print("")

    def add_name():
        VAL = raw_input("What name would you like to assign to the command line? ")
        base = os.path.expanduser('~')
        alias = '''
PS1='${debian_chroot:+($debian_chroot)}\u@%s:\w\$ '
''' % VAL
        FILE = open(base + '/.bashrc', 'r')
        data = FILE.read()
        FILE.close()
        pat = re.escape(alias)
        match = re.search(pat, data)
        if match:
            print("name already set!")
        else:
            FILE = open(base + '/.bashrc', 'w')
            data += alias
            FILE.write(data)
            FILE.close()

    def handle_quizes():
        base = os.path.expanduser('~')
        subprocess.call(['git', 'clone', 'https://github.com/jaderigby/codeForLift-quizes.git'], cwd=base+'/Documents')
        FILE = open(base + '/.bashrc', 'r')
        data = FILE.read()
        FILE.close()
        FILE = open(base + '/.bashrc', 'w')
        FILE.write(data + '\nalias quiz="python ~/Documents/codeForLift-quizes/actions.py"')
        FILE.close()
        subprocess.call(['mkdir', 'profiles'], cwd=base+'/Documents/codeForLift-quizes/')
        FILE = open(base + '/Documents/codeForLift-quizes/profiles/profile.py', 'w')
        FILE.write('''{
    "settings" : {
        "name" : "",
        "codeForLift" : {
            "quizes" : [],
            "assignments" : []
        }
    }
}''')
        FILE.close()

    def handle_assignments():
        base = os.path.expanduser('~')
        subprocess.call(['git', 'clone', 'https://github.com/jaderigby/codeForLift-quizes.git'], cwd=base+'/Documents')
        FILE = open(base + '/.bashrc', 'r')
        data = FILE.read()
        FILE.close()
        FILE = open(base + '/.bashrc', 'w')
        FILE.write(data + '\nalias quiz="python ~/Documents/codeForLift-quizes/actions.py"')
        FILE.close()
        subprocess.call(['mkdir', 'profiles'], cwd=base+'/Documents/codeForLift-quizes/')
        FILE = open(base + '/Documents/codeForLift-quizes/profiles/profile.py', 'w')
        FILE.write('''{
    "settings" : {
        "name" : "",
        "codeForLift" : {
            "quizes" : [],
            "assignments" : []
        }
    }
}''')
        FILE.close()

    def handle_executable():
        # Reference: https://stackoverflow.com/questions/15587877/run-a-python-script-in-terminal-without-the-python-command
        print("-- Making setup file executable --")
        base = os.path.expanduser('~')
        alias = '''
export PATH=/home/chrx/Documents/codeForLift-handle-setup:$PATH
'''
        FILE = open(base + '/.bashrc', 'r')
        data = FILE.read()
        FILE.close()
        pat = re.escape(alias)
        match = re.search(pat, data)
        if match:
            print("")
            print("\t- path variable already set!")
        else:
            print("\t- path variable for executable is set")
            FILE = open(base + '/.bashrc', 'w')
            data += alias
            FILE.write(data)
            FILE.close()
        # check if file is already executable
        p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
        out, err = p.communicate()
        selection = None

        def find_setup_file(ELEM):
            print("ELEM: " + ELEM)
            result = re.search('setup\.py', ELEM).group()
            print("result: " + result)
            return True

        for line in out.split('\n'):
            if 'setup.py' in line:
                if '-x' in line:
                    executable = True
                else:
                    executable = False

        if executable:
            print("\t- permissions for setup file already set!")
        else:
            subprocess.call(['chmod', '+x', 'setup.py'])
            print("\t- permissions for setup file set")
        print("")
        print(divider)

    #=== Execute ===
    if action == None:
        print("You need to pass in an argument, such as '-a' for 'all'.")
        print('''
[ -a ]                  Run all processes
[ --tmux ]              Setup tmux, or "tm", alias reference
[ --personalize ]       personalizes the terminal
[ --atom-dep ]          atom dependencies = platformio-ide-terminal, atom-runner, atom-pair
[ --quizes ]            adds the quizes repo and alias reference
[ --exec ]              make script executable from command line by simply typing file name
''')
    else:
        for param in sys.argv:
            if param == '-a':
                download_resources()
                handle_gallium_theme()
                handle_taskbar()
                handle_deb_installs()
                handle_apt_get_Installs()
                handle_desktop_wallpapers()
                set_desktop_wallpaper('jade-ambience.jpg')
                handle_albert_configuration()
                handle_alt_key_status()
                handle_albert_to_searchkey()
                configure_docky()
                handle_autostart()
                handle_auth_file()
                add_tm_alias()
                configure_caps_lock()
                add_name()
                handle_atom_dependencies()
                handle_quizes()
            elif param == '--tmux':
                add_tm_alias()
            elif param == '--personalize':
                add_name()
            elif param == '--atom-dep':
                handle_atom_dependencies()
            elif param == '--quizes':
                handle_quizes()
            elif param == '--exec':
                handle_executable()
            elif param == '--assignments':
                handle_assignments()
        print(divider)
        print("")


if __name__ == '__main__':
    main()
