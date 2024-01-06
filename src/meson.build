pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'xournalpp_demo'

blueprints = custom_target('blueprints',
  input: files(    
    'ui/export.blp',
    'ui/latexeditor.blp',
    'ui/window.blp',
    'ui/pagetemplate.blp',
    'ui/papercolor.blp',
    'ui/paperformat.blp',
    'ui/preferences.blp',
    'ui/marker.blp',
    'ui/pluginmanager.blp',
    'ui/pluginentry.blp',
    'ui/toolbox.blp',
    'ui/sidebarpage.blp',
    'ui/maincontent.blp',
    'gtk/help-overlay.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'])

gnome.compile_resources('xournalpp-demo',
  'xournalpp-demo.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
  dependencies: blueprints
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'xournalpp-demo.in',
  output: 'xournalpp-demo',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr--r--'
)

xournalpp_demo_sources = [
  'main.py',
  'util.py',
  'actions.py',
  'scope.py',
  'uisymbols.py',
  'marker.py',
  'export.py',
  'window.py',
  'marker_config.py',
  'pluginentry.py',
  'pluginmanager.py',
  'toolbox.py',
  'palettecolor.py',
  'sidebarpage.py',
  'tools_config.py',
  'maincontent.py',
]

install_data(xournalpp_demo_sources, install_dir: moduledir)
