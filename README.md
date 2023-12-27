# xournalpp-libadwaita-mockup
Mockups for redesiging Xournal++ with Gtk4/Libadwaita are created, using the blueprint format.


## Installation

### Linux

Install Meson, Gtk 4, Poppler, GtkSourceView 5, Libadwaita 1 and pygobject. 

On Ubuntu:
```term
sudo apt-get install meson libgtk-4-dev libpoppler-glib-dev libgtksourceview-5-dev \ libadwaita-1-dev python3-gi python3-gi-cairo
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

Install Meson, Gtk 4, Poppler, GtkSourceView 5, Libadwaita 1 and pygobject.

```term
pacman -S \
  mingw-w64-x86_64-meson \
  mingw-w64-x86_64-gtk4 \
  mingw-w64-x86_64-poppler \
  mingw-w64-x86_64-gtksourceview5 \
  mingw-w64-x86_64-libadwaita1 \
  mingw-w64-x86_64-python-gobject
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

The simplest way is to use [Homebrew](https://brew.sh/) to install the dependencies. Consider creating a new user first if you don't want to mess with jhbuild before installing Homebrew.

Install Meson, Gtk 4, Poppler, svn, GtkSourceView 5, Libadwaita 1 and pygobject via

```term
brew install meson gtk4 poppler svn gtksourceview5 libadwaita pygobject3
```

Install the blueprint-compiler:

```term
git clone https://gitlab.gnome.org/jwestman/blueprint-compiler.git
cd blueprint-compiler
meson setup build
cd build
meson install
```

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
