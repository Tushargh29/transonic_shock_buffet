# Numerical investigation of 2D transonic shock-buffet around a NACA 0012-34 airfoil using OpenFOAM

## Creating the Singularity image

To make results reproducible, a [Singularity](https://sylabs.io/guides/3.6/user-guide/) image containing OpenFOAM is used to perform simulations. To install Singularity, follow the official [installation instructions](https://sylabs.io/guides/3.6/user-guide/quick_start.html). The image is built based on the [ESI-OpenCFD Docker image](https://openfoam.com/download/install-binary-linux.php). Building the image requires root privileges. Once the image is built, any user can use the image without any extra privileges. To build the image, run:

```
sudo singularity build openfoam-v2006.sif openfoam-v2006.def
```

To check if the image is working, run:

```
singularity run-help openfoam-v2006.sif
# ...
# expected output
# ...
Simple Singularity container based on the official OpenFOAM-plus
Docker image. Currently, the following execution modes are available:

  run - execute the Allrun script in an OpenFOAM case
    singularity run openfoam-v2006.sif run /path/to/case

  clean - execute the Allclean script in an OpenFOAM case
    singularity run openfoam-v2006.sif clean /path/to/case

  app - execute an OpenFOAM app or utility
    singularity run openfoam-v2006.sif app icoFoam -help
    singularity run openfoam-v2006.sif app paraFoam "-case path/to/case"
```

## Performing a simulation

The folder *test_cases* contains all basic OpenFOAM simulation cases. Simulations should be performed in the *run* directory, which is not tracked by the version control system. A typical workflow to run a simulation may look as follows:

```
# top-level folder of the repository
mkdir run
# make a copy of the simulation case
cp -r test_cases/naca0012-34-base/ run/naca0012-34-test
# execute the Allrun script in the new test case
singularity run openfoam-v2006.sif run run/naca0012-34-test/
# post-processing using ParaView (from the image)
singularity run openfoam-v2006.sif app paraFoam "-case run/naca0012-34-test"
# or using a local ParaView installation
cd run/naca0012-34-test/
paraview post.foam
```

If the simulation is performed in parallel, make sure to select *Case Type -> Decomposed Case* in ParaView. To see the mesh properly, make sure to unselect *Decompose polyhedra*.
