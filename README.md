# lmod_generator
To create a module use the following command from the directory your software was installed:

generateModule | install -D /dev/stdin /tgac/software/testing/lmod/6.1/x86_64/lmod/lmod/modulefiles/Core/app/version.lua

If there are any dependencies (check the modules loaded while compiling) please make sure you include those too after
