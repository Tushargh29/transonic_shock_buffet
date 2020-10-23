# Extraction of the reference data for drag and lift coefficients #Issue 4
---

### Objective:
To extract the reference data for drag and lift coefficients of the airfoil investigated in this project and recreate the data plots roughly using Python.

----

1. As discussed in the _Objective_ section, we have referred the data of _NACA 0012-34_ airfoil to be investigated in this project from the book _THEORY OF WING SECTIONS_Including a Summary of Airfoil Data by IRA H. ABBOTT, ALBERT E. VON DOENHOFF (1959, Dover Publications INC. New York)_.

2. To be precise, we have referred:
**Effect of compressibility on the drag of the NACA 0012-34 airfoil** which provides drag coefficients for varying angle of attack and Mach number (_Fig 175 on page 284_).
**Effect of compressibility on the lift of the NACA 0012-34 airfoil** which provides lift coefficients for varying angle of attack and Mach number (_Fig 161 on page 274_).

3. Firstly, we will extract this reference curves using [Enguage Digitizer](http://markummitchell.github.io/engauge-digitizer/). This is the simple technique to extract measurements of data curves from the source (image file). This software exports the data measurements which can be saved as _.csv files_. Accordingly, we have saved such _.csv_ files for both drag coefficient and lift coefficient measurements respectively.
4. Now, we can recreate these same graphs from the saved _.csv_ files using Python. For this task we have implememted _Matplotlib_, _Numpy_, _Pandas_ python library. A suitable Python scripts are [Compressibility_Cd.py ](https://github.com/Tushargh29/transonic_shock_buffet/blob/master/extracting_the_reference_data/Compressibility_Cd.py) and [Compressibility_Cl.py](https://github.com/Tushargh29/transonic_shock_buffet/blob/master/extracting_the_reference_data/Compressibility_Cl.py) implemented where the data from _.csv_ files are suitably arranged and then plotted roughly same as that of the reference graphs.
---

### Results:
After implementing above steps, the recreating of the Cd and Cl plots is done.
- **Effect of compressibility on the drag of the NACA 0012-34 airfoil:**
![Drag_reference_plot](https://github.com/Tushargh29/transonic_shock_buffet/blob/fbfdc8d2caca35968ecc8709c4f1bdf28fc26ddb/extracting_the_reference_data/Cd_reference_plot.png)
![Drag_Plot](https://github.com/Tushargh29/transonic_shock_buffet/blob/master/extracting_the_reference_data/effect_on_Drag.png)

- **Effect of compressibility on the drag of the NACA 0012-34 airfoil:**
![Lift_reference_plot](https://github.com/Tushargh29/transonic_shock_buffet/blob/master/extracting_the_reference_data/Cl_reference_plot.png)
![Lift_Plot](https://github.com/Tushargh29/transonic_shock_buffet/blob/master/extracting_the_reference_data/effect_on_lift.png)

---
In this way, the task of extracting the reference data of lift and drag coefficients is performed.



