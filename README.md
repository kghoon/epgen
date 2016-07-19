# epgen
Eclipse Project Generator

Install
-------

```
$ git clone https://github.com/kghoon/epgen.git ~/.epgen --depth 1
$ ~/.epgen/install.py
# Optional reload bash settings
$ source ~/.bashrc
```

Generate configuration template
-------------------------------

Generate configuration template file
```bash
$ epgen --config default
```

Then, ```default.config``` YAML file will be generated as below,

```
$ cat default.config
name: <project-name>
rootdir: <work-root>
links:
classpaths:
- kind: con
  path: org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-1.4
- kind: output
  path: bin
- kind: src
  path: src
- kind: lib
  path: <work-root>//build/<build-target>/jvmbtclasses.zip
- kind: lib
  path: <work-root>//build/<build-target>/classes.zip
- kind: lib
  path: <work-root>/build/<build-target>/classes
```

You can specify default values for ```project-name``` and ```work-root```, ```build-target``` 

```bash
$ epgen --config default --name lightmw-sdk --workroot ~/lightmw/g4 --buildtarget linux_headless
$ cat ./default.config
name: lightmw-sdk
rootdir: /Users/jhkang/lightmw/g4
links:
classpaths:
- kind: con
  path: org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-1.4
- kind: output
  path: bin
- kind: src
  path: src
- kind: lib
  path: /Users/jhkang/lightmw/g4//build/linux_headless/jvmbtclasses.zip
- kind: lib
  path: /Users/jhkang/lightmw/g4//build/linux_headless/classes.zip
- kind: lib
  path: /Users/jhkang/lightmw/g4/build/linux_headless/classes
```

Predefined configuration templates are placed in ```configs``` directory.

Generate project files
----------------------

```bash
$ epgen ./default.config
$ ls -al ./lightmw-sdk
total 16
drwxr-xr-x   5 jhkang  staff  170  7 19 21:58 .
drwxr-xr-x  15 jhkang  staff  510  7 19 21:58 ..
-rw-r--r--   1 jhkang  staff  567  7 19 21:58 .classpath
-rw-r--r--   1 jhkang  staff  338  7 19 21:58 .project
drwxr-xr-x   4 jhkang  staff  136  7 19 21:58 settings
```

