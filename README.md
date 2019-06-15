# git-3d

git-3d is yet another git tree viewer.

The reason for this thing to exist is that all of the git graphing tools I have
encountered so far (yes, even the more modern ones) basically show a textual
1D list of commits with lines between them.

I am ususally working with repos that have lots of active branches with many
commits in each and that means sometimes there are many vertical lines and no
chance to keep an overview.

So, I want something more fuid. Something three-dimensional. Something *new*.

# getting this to run

After a brief experiment of using [PyVis](https://pyvis.readthedocs.io/en/latest/index.html), git-3d connects [GitPython](https://github.com/gitpython-developers/GitPython) to an OpenGL-based renderer and uses [pygame](https://www.pygame.org/) for the user interface.

GitPython can be obtained from PyPi, `pip3 install GitPython`.
The global install on my Debian I did through `sudo apt update && sudo apt install python3-git`

Everything else I got via PyPi: `pip3 install pygame pyopengl`

Then, do a 

```
git clone --recursive https://github.com/mgritz/git-3d.git && cd git-3d
./git-3d /path/to/your/repo/root
```

**WIP!** This is under construction. Nothing is actually working right now.

# roadmap

This is what I am going to do here:

* [x] Get GitPython to run and grab the git tree.
* [ ] Add a nize vizualization.
* [ ] Add features to make this more dynamic.

I am going to tweek this stuff to my personal needs first but suggestions are always welcome!