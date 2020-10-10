# SABR\_build

This is the catkin environment for the SABR project. It contains the [SABR repository](https://github.com/AlexS28/SABR) as a submodule and the [Hector Quadrotor](http://wiki.ros.org/hector_quadrotor) packages as subtrees.

All development on the SABR project can and should be done after cloning this repository.


## Build Instructions

Clone all repositories (including submodules)
```
git clone --recursive git@github.com:stephanietsuei/SABR_build.git 
```

Build:
```
cd /path/to/SABR_build
catkin_make
```

Pull changes, including those to submodules:
```
cd /path/to/SABR_build
git pull --recurse-submodules
```


## Commiting Changes to SABR Submodule

1. From the directory `src/SABR`, use git to add and commit the files:
```
cd /path/to/SABR_build/src/SABR
git ...
```

2. Leave the submodule and update the reference. The reference does not need to be updated at every single commit.
```
cd /path/to/SABR_build
git add src/SABR
git commit -m "update reference"
```


## Commiting Changes Hector Quadrotor Packages (subtrees)

Just pretend the subtree is not actually there and work as usual. :)


## Running SABR

Each command in a different terminal, from `SABR_build` directory:
1. `roscore`
2. `./play1.sh`
3. `rosrun sabr_pkg play2.py`
4. (After Terminal 3 is done) `rosrun sabr_pkg play3.py`