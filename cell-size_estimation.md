#  Computing an estimate for cell-width at airfoil surface #Issue3 

---

## Working Methodology:

1. Currently, we have _wall-functions_ in the basic simulation setup to correct mu, k, and omega at the airfoil surface. Ideally, we would like to avoid the usage of _wall functions_ because they introduce uncertainty to our simulation (we don't know how well assumptions made in derivation apply to our case).

2. But in order to capture maximum physics near the wall region, _wall-functions_ are not sufficient, the most appropriate way is to resolve boundary layers near the wall region(specifically, in the diagram of _Law of the Wall_ we resolve the boundary layers in the region of viscous sublayer). To see if it is feasible to resolve the boundary layer down to (_yPlus_ = 1), it is useful to make an estimate for the necessary cell-width at the airfoil surface.

3. As we already have _wall-functions_ in our basic simulation setup, we can just give a try for resolving the boundary layer near the wall region by checking its feasibility after estimating the necessary cell-width at the airfoil surface. For this, we need to estimate first the _y_ distance i.e (The distance of the centre of the 1st cell in the layer from the wall in normal direction). The stepwise procedure to calculate this wall distance based on (_yPlus_ = 1) is described briefly in the later stage of the report(_Point 6_).

4. As we have already performed the simulation of basic setup based on _wall functions_(_kOmegaSST_), we have received the simulation results. These results can be elaborately analysed in the _Paraview_ post-processing software. The stepwise post-processing procedure is described briefly in the later stage of the report(_Point 7_).
5. The prime motivation behind this -cell-size estimation_ is getting an idea that how refined our mesh should be(in comparison to what available in the basic setup) in order to reach the condition of _yPlus_ = 1(The condition of resolving boundary layers near the wall region).
---
#### Estimation of cell-size at the airfoil surface for (_yPlus_ = 1):
6. The stepwise procedure of calculating the wall disatance based on _yPlus_ = 1 is as follows:
The physical properties and some important simulation conditions are defined in the [_README.md_](https://github.com/Tushargh29/transonic_shock_buffet/blob/master/test_cases/naca0012-34-base/README.md) file located at _transonic_shock_buffet/test_cases/naca0012-34-base/README.md_ path. Some physical properties required for this case are given below:
- free-stream density: 1.186 kg/m³
- free-stream velocity: 250.8 m/s
- Dynamic viscosity: 0.0000182 N.s/m²
- kinematic viscosity based on free-stream values: 0.000015342 m²/s
- characteristic length (chord length of airfoil): 0.18352 m

  ##### a. Calculation of Reynold's number:

  ![](https://latex.codecogs.com/gif.latex?Re%20%3D%20%5Cfrac%7B%5Cvarrho.U_%7Bfreestream%20%7D.L_%7BBoundary%20Layer%7D%7D%7B%5Cmu%20%7D)
  
     ![](https://latex.codecogs.com/gif.latex?Re%20%3D%20%5Cfrac%7B%281.186%29.%28250.8%29.%280.18352%29%7D%7B0.0000182%7D)
  
  ![](https://latex.codecogs.com/gif.latex?Re%20%3D%203030000)

  ##### b. Estimate the skin friction using the Schlichting skin-friction correlation:
  ![](https://latex.codecogs.com/gif.latex?C_%7Bf%7D%20%3D%20%5B2log_%7B10%7D.%28Re_%7Bx%7D%29%20-%200.65%5D%5E%7B-2.3%7D)
  
  ![](https://latex.codecogs.com/gif.latex?C_%7Bf%7D%20%3D%20%5B12.965%20-%200.65%5D%5E%7B-2.3%7D)
 
  ![](https://latex.codecogs.com/gif.latex?C_%7Bf%7D%20%3D%200.003104)

  #### c. Calculation of Wall Shear stress:
   ![](https://latex.codecogs.com/gif.latex?%5Ctau%20_%7Bw%7D%20%3D%20C_%7Bf%7D.%5Cfrac%7B1%7D%7B2%7D.%5Cvarrho%20.U%5E%7B2%7D)
  
  ![](https://latex.codecogs.com/gif.latex?%5Ctau%20_%7Bw%7D%20%3D%20%280.00314%29.%5Cfrac%7B1%7D%7B2%7D.%281.186%29.%28250.8%29%5E%7B2%7D) 
 
  ![](https://latex.codecogs.com/gif.latex?%5Ctau%20_%7Bw%7D%20%3D%20115.77%20%5Cfrac%7BN%7D%7Bm%5E%7B2%7D%7D)

  ##### d. Calculation of friction velocity:
  ![](https://latex.codecogs.com/gif.latex?u_%7B*%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B%5Ctau%20_%7Bw%7D%7D%7B%5Cvarrho%20%7D%7D)
  
  ![](https://latex.codecogs.com/gif.latex?u_%7B*%7D%20%3D%20%5Csqrt%7B%5Cfrac%7B115.77%7D%7B1.186%7D%7D)
  
  ![](https://latex.codecogs.com/gif.latex?u_%7B*%7D%20%3D%209.88%20%5Cfrac%7Bm%7D%7Bs%7D)

  ##### e. Calculation of the wall distance(considering _yPlus = 1_):
  ![](https://latex.codecogs.com/gif.latex?y%20%3D%20%5Cfrac%7By%5E%7B&plus;%7D.u%7D%7B%5Cvarrho%20.u_%7B*%7D%7D)
  
  ![](https://latex.codecogs.com/gif.latex?y%20%3D%20%5Cfrac%7B%281%29.%280.0000182%29%7D%7B%281.186%29.%289.88%29%7D)
  
  ![](https://latex.codecogs.com/gif.latex?y%20%3D%200.0000015532%20meters)

  **Now, we can say that the wall distance for _yPlus = 1_ is 0.0000015532 in meters**.

---

#### Post processing analysis of _yPlus_ field from the simulation case in _Paraview_:
7. Now we can analyse the _yPlus_ field obtained from the simulation using _Paraview_ software. The stepwise procedure is given as follows:
- Create an empty _.foam_ to get started with the post-processing and load this file in _paraview_
- Select _Decomposed Case_ mode and in _Mesh Region_ menu select only _airfoil_ option. Then, click on _Apply_ and above select the _yPlus_ field.
- Now in the _Information_ tab select only _airfoil patch_. Go to _Properties_ tab and now select _internalMesh_.
- Now select _Select Cells On (s)_ option in the window toolbar.
- Select one random cell in roughly horizontal position. This ensures the correct alignment of the local and global cartesian systems.
- Now select _extractSelection_ filter and click _Apply_.
- Now observe the _Y Range_ bounds in the _Information_ tab. This value represents the thickness of the 1st cell from the wall. So the wall distance would be exactly half of this value.
- **After successfully performing the post processing analysis, we got the value of wall distance roughly around 0.0001288 in meters.**
- After getting both values of _wall distance_, we can calculate the scaling factor:

![](https://latex.codecogs.com/gif.latex?Scaling%20factor%20%3D%20%5Cfrac%7B0.0001288%7D%7B0.00000155%7D%20%3D%2083.096)
- **This means that we should refine our current existing mesh 83.096 times finer in order to reach the condition of resolving the boundary layer near the wall region(_yPlus = 1).**
- Also, the _yPlus_ provided by the function object in the simultion is matching roughly with the above value. This denotes the correlation we made to calculate the skin friction is somewhat correct.


8. The basic simulation setup is implementing basic and random mesh. Now in order to fulfill our objectives we need to perform the mesh refinement study in some particular areas regarding our airfoil case such as:
- Resolving boundary layer near the wall region.
- Shock over the airfoil.
- Wake turbulence at the rear end of the airfoil.


---


- In this way, we have performed the _cell-size estimation_ at the airfoil surface.









