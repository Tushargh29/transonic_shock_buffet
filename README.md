# Numerical investigation of 2D transonic shock-buffet around a NACA 0012-34 airfoil using OpenFOAM

## Creating the Singularity image

To make results reproducible, a [Singularity](https://sylabs.io/guides/3.6/user-guide/) image containing OpenFOAM is used to perform simulations. To install Singularity, follow the official [installation instructions](https://sylabs.io/guides/3.6/user-guide/quick_start.html). More information on the image may be found [here](https://github.com/AndreWeiner/of_pytorch_docker). Building the image requires root privileges. Once the image is built, any user can use the image without any extra privileges. To build the image, run:

```
sudo singularity build of2006-py1.6-cpu.sif Singularity.def
```

To check if the image is working, run:

```
singularity run-help of2006-py1.6-cpu.sif
# ...
# expected output
# ...
  Simple Singularity image containing OpenFOAM-v2006
  and libtorch (PyTorch 1.6). The generic syntax to execute
  a command with arguments is

  singularity run image_name.sif command [path] [argument]

  Examples:

  - compile the application tensorCreation using wmake
    singularity run of2006-py1.6-cpu.sif wmake test/tensorCreation/

  - clean tensorCreation build
    singularity run of2006-py1.6-cpu.sif wclean test/tensorCreation/

  - run tensorCreation
    singularity run of2006-py1.6-cpu.sif ./tensorCreation test/tensorCreation/

```

## Performing a simulation

The folder *test_cases* contains all basic OpenFOAM simulation cases. Simulations should be performed in the *run* directory, which is not tracked by the version control system. A typical workflow to run a simulation may look as follows:

```
# top-level folder of the repository
mkdir run
# make a copy of the simulation case
cp -r test_cases/naca0012-34-base/ run/test_base
# execute the runCase script in the top-level folder where the image is located
# the first argument must be the path to the simulation case
./runCase run/test_base/
# post-processing using local ParaView installation
cd run/test_base
paraview post.foam
```

If the simulation is performed in parallel, make sure to select *Case Type -> Decomposed Case* in ParaView. To see the mesh properly, make sure to unselect *Decompose polyhedra*.
