# xournalpp-libadwaita-mockup
Mockups for redesiging Xournal++ with Gtk4/Libadwaita are created, using Workbench/blueprint.


## Installation

### Linux

Install Meson, Gtk 4, Poppler, GtkSourceView 5 and Libadwaita 1. 

On Ubuntu:
```term
sudo apt-get install meson libgtk-4-dev libpoppler-glib-dev libgtksourceview-5-dev libadwaita-1-dev
```

Install the blueprint-compiler:

```term
git clone https://gitlab.gnome.org/jwestman/blueprint-compiler.git
cd blueprint-compiler
meson setup build
cd build
meson install
```

### Windows

First install [MSYS2](https://www.msys2.org/) to a short path without spaces.
Start Mingw-w64 64bit. The following steps happen in this console.

Update your packages (maybe multiple times) via 
```term
pacman -Syuu
```

Install Meson, Gtk 4, Poppler, GtkSourceView 5 and Libadwaita 1.

```term
pacman -S \
  mingw-w64-x86_64-meson
  mingw-w64-x86_64-gtk4 \
  mingw-w64-x86_64-poppler \
  mingw-w64-x86_64-gtksourceview5 \
  mingw-w64-x86_64-libadwaita1
```

Install the blueprint-compiler:

```term
git clone https://gitlab.gnome.org/jwestman/blueprint-compiler.git
cd blueprint-compiler
meson setup build
cd build
meson install
```

### MacOS

Yet untested

## Build

Clone the repository and enter the directory:

```term
git clone https://www.github.com/rolandlo/xournalpp-libadwaita-mockup.git
cd xournalpp-libadwaita-mockup
```

Configure the meson project in a `build` folder:

```
meson setup build --prefix=$(pwd)/build/inst
```

Copy the .blp-files to the place they are needed:

```term
python3 scripts/build.py
```

Enter the build folder and install the project:

```term
cd build
meson install
```

Run the project:

```term
inst/bin/xournalpp-demo
```

## Work with Blueprint files

Blueprint is a markup language for Gtk user interfaces. Blueprint files `.blp` are translated to `.ui`-files using the `blueprint-compiler`. Blueprint files are more readable than `.ui` files and easier to modify.

In this project the (original) Blueprint files are stored within different subdirectories of the `workbench` folder.
If you are on Linux we suggest you install [Workbench](https://flathub.org/apps/re.sonny.Workbench), open the different subdirectories in Workbench and make the modifications there. You get live-preview and formatting for free.
The code for the workbench projects is written in JavaScript, since that language
is supported best there. 
In the actual project we use Python, since
it feels easiest to develop in Python.
