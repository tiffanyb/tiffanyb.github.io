---
layout: page
title: "Fuzzing In Class Exercise"
---

This in-class exercise has three learning objectives:
   1. Gain exposure to the AFL tool chain
   2. Writing a *harness* to focus fuzzing on a particular region of code in a
      real application.
   3. If you do both the above and have extra time, experiment with using
      libfuzzer instead of afl.

**The fuzzing archive is at [exercise.tgz](https://www.tiffanybao.com/courses/cse545/labs/week12/exercise.tgz)**

We will be using docker in this exercise. If you don't have docker installed on
your machine, please head to [docker.com](https://docker.com) and install it
now. Docker provides a fully reproducible yet lightweight environment to test
out ideas.

Docker does not save files between `docker run` invocations. This is
intentional. If docker saved files, then it wouldn't be a fully reproducible
environment from one run to the next. We will mount our *local* filesystem
within a docker container (a common docker idiom).


Assuming you have everything downloaded and on your local machine, start this
exercise by executing:

```bash
$ docker run -ti -v `pwd`:/mnt dbrumley/asu-fuzzing-2020
# cd /mnt
# ls
Dockerfile  README.md  afl-example  libfuzzer-example  tinyxml2
```

**If you have issues:**
First, make sure docker itself works on your machine with a simple hello world
example:
```bash
docker run hello-world
```
If this doesn't work, you have a problem with your installation. See docker's
documentation to fix.

Second, see if the problem is with mounting your local filesystem within the
container.
```bash
$ docker run -ti dbrumley/asu-fuzzing-2020
```

Docker does not allow any path name, and this can sometimes cause an
issue. If the above command worked, but the initial version with the `-v` option
did not, then the problem is likely with the path name.
   * Try moving this entire directory to a more standard pathname, such as
`/tmp/asu-fuzzing-2020`.
   * If you cannot make this work, run docker without mounting with `docker run
     -ti dbrumley/asu-fuzzing-2020`. I've copied all material into the docker
     image itself under `asu-fuzzing-2020`. You can edit files within the
     container, though those changes will not persist after the container is
     terminated. That should still be good enough for this class.


## Exercise 1: Running AFL

In this exercise you'll gain exposure to the
[AFL](https://github.com/google/AFL) tool chain. We covered this in the course video;
this is a sanity check to make sure you can replicate the material yourself.

AFL can be installed directly from the [source code
repo](https://github.com/google/AFL) or via a package management tool such as
`apt`. We've already installed AFL inside the container for you, so if you're
following along you need not install anything.

First, run the container and switch to the `afl-example` directory:
```bash
$ docker run -ti -v `pwd`:/mnt dbrumley/asu-2020-fuzzing
# cd /mnt/afl-example
```

**Exercise:** In this exercise, complete the following steps:

  * Modify the `Makefile` to use the AFL tool chain.
  * Create the proper `in` and `out` directories for your corpus, and initialize
    the `in` corpus with `good.txt`
  * Run AFL and have it find the bug. This should take under 1:30.

## Exercise 2: Writing a harness

In this exercise you'll write a *harness* for a library.  Software developers
write test harnesses for regression testing and quality control.  We will write
a harness that calls functionality of interest. You will fuzz with this harness,
so that the fuzzer checks the code of interest for bugs.

We'll be writing a harness for the `tinyxml2` library. In this exercise you will
write a fuzz harness for the `tinyxml2` library and find a bug. A fuzz harness
is a functional test: it takes in an input, and runs the desired function(s) on
the input. In this case, the input will be a file name.

Open `tinyxml2.cpp` in your favorite editor and look for the relevant functions
for:
   1) loading a file for parsing.
   2) printing the result.

First, write a few lines of C code to exercise this code. We have created a
skeleton as `harness.cpp`:

```C
#include <unistd.h>
#include <fcntl.h>
#include "tinyxml2.h"

using namespace tinyxml2;

int main(int argc, char **argv){
  // Your code goes here.
  // TODO: Instantiate an XML objective
  // TODO: Parse content of argv[1] into XML object.
  //       (Hint: look for a function with "Load" in the name)
  // TODO: Print the XML object
  return 0;

}
```

Second, build your harness with `afl-g++`.  You can either edit the `Makefile`
directly or set the `$(CXX)` environment variable before calling `make`.

Third, create an input corpus directory and place an initial test file.  We have
included a number under `resources`.  You should include at least
`utf8test.xml`; we know a properly created harness will find a bug in under 3
minutes with this initial corpus.

Fourth, run AFL to find the bug. It should take less than 3 minutes.

Fifth, inspect the output of AFL. How would you try out the crashing test case?
How would you run a debugger to find out which function is faulty?

## Exercise 3: Migrate to libfuzzer

If you've made it this far, you can use your remaining time to experiment with
libfuzzer.  You can read the libfuzzer [documentation](https://libfuzzer.info).
You will need to write a function called `LLVMFuzzerTestOneInput`.

How does libfuzzer compare to AFL?  Is it faster?
