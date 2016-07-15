# lmod_generator
To create a module use the following command from the directory your software was installed:

generateModule | install -D /dev/stdin path/to/Core/app/version.lua

If there are any dependencies (check the modules loaded while compiling) please make sure you include those too after
