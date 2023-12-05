# xournalpp-libadwaita-mockup
Mockups for redesiging Xournal++ with Gtk4/Libadwaita are created, using Workbench/blueprint.


## Installation

### Linux

Install Meson, Gtk 4, Poppler, GtkSourceView 5 and Libadwaita 1. 

On Ubuntu:
```term
sudo apt-get install meson libgtk-4-dev libpoppler-glib-dev libgtksourceview-5-dev libadwaita-1-dev
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

Enter the build folder and install the project:

```term
cd build
meson install
```

Run the project:

```term
inst/bin/xournalpp-demo
```