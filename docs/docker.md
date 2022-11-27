# Docker Host
The docker will be made only to make usage easier and env consistent. It is not designed to be hosted on railway or heroku due to the absolute size of the project

## Using Debian
<!-- https://pythonspeed.com/articles/alpine-docker-python/ -->
If you look at a Ubuntu-based build, you’ll see it’s downloading `matplotlib-3.1.2-cp38-cp38-manylinux1_x86_64.whl`. This is a pre-compiled binary wheel. Alpine, in contrast, downloads the source code (`matplotlib-3.1.2.tar.gz`), because standard Linux wheels don’t work on Alpine Linux.

Why? Most Linux distributions use the GNU version (`glibc`) of the standard C library that is required by pretty much every C program, including Python. But Alpine Linux uses musl, those binary wheels are compiled against `glibc`, and therefore Alpine disabled Linux wheel support.

Most Python packages these days include binary wheels on PyPI, significantly speeding install time. **But if you’re using Alpine Linux you need to compile all the C code in every Python package that you use.**