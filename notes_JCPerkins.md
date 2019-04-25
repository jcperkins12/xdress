# Notes to a future self about how I am getting this to work

## Current Environment
* Starting in vscode

__Compilers__
* MSVS 2017, 2019 installed with the 
* Currently no GCC products installed 

__Python__
* python version  = 3.7.2
* have python dependancies installed (pycparser, Cython, lxml)

## Steps for STL Wrapping portion of Tutorial
1. Try to build the program
    ```
    python setup.py build
    ```
2. move directory to `testXdress\mypack`
    ```
    cd mypack
    ```
3. Run try running the STLWrapper run control file (simplest case)
    ```
    (Qorvo) C:\Users\cp035982\Python\Projects\testXdress\mypack> xdress
    ```
    -- Failed. 
    I built it but didn't install it. Trying that...
    ```
    cd ..
    python setup.py install
    ```
    -- xdress installs successfully
    ```
    cd mypack
    xdress
    ```
    -- Successfull run... tests don't work though....

    * note: there was a warning about the import method becoming depreciated, so I went in to fix it, reinstalled and reran it to make sure that it worked. 

## Steps for CythonGen portion of Tutorial

__Pre-requisites__
* LLVM/CLANG 
    * Not sure which is better, building from source or prebuild binary
        * Building from source detailed instructions at http://clang.llvm.org/get_started.html
            * CLANG might need the __GnuWin32 tools__ functionality if the MSys tools (included in Git?) don't work
            * installed CMake as a way to follow LLVM directions more explicityly, but probably could have just used the MSVS developer prompt which has integrated CMake
        * pre-built binaries can be found at http://releases.llvm.org/download.html#8.0.0    
* GCC-XML - has been succeeded by CastXML which can be built from source from https://github.com/CastXML/CastXML#readme
    * Also requires LLVM/CLANG with the same compilers that will build CastXML. 


### Building LLVM/CLANG from source
1. Clone the repo from https://github.com/llvm/llvm-project.git to 'C:\\lib\\LLVM\\'
    * this takes some time (at least >10min)
2. Failed to build the whole project by opening the folder in MSVS 2017, letting the integrated CMake generate the cache files and then building the entire project 
    1. Open 'C:\\lib\\LLVM\\' folder in MSVS 2017 and let project index and CMake generate cashes
        * this also takes some time (at least >10min)
    2. Build the project with MSVS 2017. On the toolbar, select CMake -> Build All
3. Tried to use the sepecial CMake instructions provided and only build the LLVM projects
    1. Open Developer Prompt for MSVS 2017
    2. `cd C:\\lib\\LLVM\\`
    3. `mkdir build` (for building without polluting the source dir)
    4. `cd build`
    5. If you are using Visual Studio 2017: 
        ```
        cmake -DLLVM_ENABLE_PROJECTS=clang -G "Visual Studio 15 2017" -A x64 -Thost=x64 ..\llvm -Thost=x64 
        ```
        is required, since the 32-bit linker will run out of memory.
        * To generate x86 binaries instead of x64, pass -A Win32.
    6. The above, if successful, will have created an LLVM.sln file in the build directory
    7. Build the project with MSVS 2017. On the toolbar, select CMake -> Build Only -> LLVM 
        * this is taking a long time (>30 min)


### Build (or install?) CastXML
1. clone from https://github.com/CastXML/CastXML.git to 'C:\\lib\\CastXML'


