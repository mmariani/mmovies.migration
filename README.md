mmovies.migration
=================

Import plain text IMDB data within MongoDB.

The data itself is not provided with this package (except for small excerpts for testing purposes)
and its usage is restricted by the terms provided at http://www.imdb.com/interfaces/

However, a download script is included in the buildout environment.

In order to build:

```
$ git clone https://github.com/mmariani/mongo-facciocose.git -b mmovies
$ cd mongo-facciocose
$ virtualenv --no-site-packages .
$ . bin/activate
$ python bootstrap.py
$ bin/buildout
$ bin/mmovies-download
```

Then you can run bin/start-mongo in a shell, and bin/movies-import in another.

The (optional) virtualenv helps to avoid possible conflicting versions of setuptools.

