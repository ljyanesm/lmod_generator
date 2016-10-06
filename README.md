# lmod_generator
To create a module run the following command from the directory your software was installed (**prefix path**):
```
generateModule | install -D /dev/stdin /tgac/software/testing/lmod/6.1/x86_64/lmod/lmod/modulefiles/Core/app/version.lua
```
If there are any dependencies (check the modules loaded while compiling) please make sure you include those too after in the __version.lua__ file that was created on the previous step.

To include the dependencies simply add a line similar to:
load("gcc/4.9.1")

Generally it's recommended to specify the version of the dependency unless you are certain that there is no backwards compatibility problems. Not specifying the version of the dependencies will load the **default** version of that tool which is the latest version unless configured otherwise.
