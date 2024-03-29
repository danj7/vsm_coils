# VSM detector coil geometry
This is a Python 3 script to help plan optimal detection coil geometry for a VSM in Mallinson configuration, pictured below, labeled `a)`. Based on applying the Biot-Savart law and the Reciprocity Theorem to a wire loops arranged parallel to each other using the geometry, shown in picture labeled `b)`. Note also that this procedure assumes a point-like sample in the center (or at least much smaller than the size of the detector coils).

![geometry](https://user-images.githubusercontent.com/13749006/63816566-b7abff00-c906-11e9-9daf-6c8bb425ab18.png)

This work was originally done for my Bachelor's thesis and published on the [Journal of Magnetism and Magnetic Materials](https://doi.org/10.1016/j.jmmm.2018.01.088).

## Description

The general idea, as mentioned briefly above, is to calculate the magnetic field generated by each coil on the location of a point-like magnet. That means that each loop contributes an $dB_y$ to that field,

$$ dB_y = \frac{I}{c} \cdot \frac{ z_c R \cos{\theta} - R^2 }{( R^2 + y_c^2 + z_c^2 - 2 z_c R \cos{\theta} )^{3/2}}
\,, \frac{I}{c}= 1,
$$

where $\frac{I}{c}$ is defined to 1 because we only need relative values. Then the sensitivity is defined as

$$
G_r = \frac{\partial B_y}{\partial z},
$$

which combined with the previous differential then means

$$
G_r = \int_0^{2\pi} d\theta 
\frac{ (R\cos\theta)( R^2 + y_c^2 + z_c^2 - 2 z_c R \cos{\theta} )^{3/2} -
\\
(z_c R \cos{\theta} - R^2 )\frac{3}{2}(R^2 + y_c^2 + z_c^2 - 2 z_c R \cos{\theta})^{1/2}(2z_c - 2R\cos\theta)
}
{( R^2 + y_c^2 + z_c^2 - 2 z_c R \cos{\theta} )^3}
$$

## Usage

The file `vsm_code.py` contains all the functions needed to compute the sensibility function of a detector coil. If you run it by itself in the terminal using
```bash
$ python vsm_code.py
```
it will return figures similar to the ones published in the paper linked above. I changed some of the parameters but it's the same. The graphs however are not in log-scale.

I would highly recommend using the Jupyter Notebook included since it makes changing the parameters much easier. For reference, the following image shows some of the parameters of the coil, namely a __height__ of 0.8 cm, an __interior radius__ of 1.0 cm, and an __exterior radius__ of 1.5 cm. The script assumes one is using centimeters, though the sensitivity is computed in arbitrary units and graphed in a relative scale.

![coil](https://user-images.githubusercontent.com/13749006/63824965-e934c280-c926-11e9-90ff-232e5c1a8df3.png)


For example, if one wants to know how close to the sample should the detector coils be to get the most signal on would run the following cell:

![screenshot1](https://user-images.githubusercontent.com/13749006/63825273-2a79a200-c928-11e9-830b-b02207a49c13.png)

and notice that the signal grows as the separation of the coils from the center (where the sample would be located) is reduced, therefore it would be better to get the coils as close as possible, in the y-direction, to the sample.

Then, one might be interested to find out how big a radii should the coils have. Let's say one starts with coils with an __interior radius__ of 1.0 cm and a __height__ of 0.5 cm, one would run this other cell

![screenshot2](https://user-images.githubusercontent.com/13749006/63825310-4bda8e00-c928-11e9-8506-02fc0c1aee3e.png)

and notice that after 2.0 cm of __external radius__ the sensitivity of the coil decreases. Therefore, it is good enough to keep the coil's __external radius__ under 2.0 cm.

Finally, one might wonder what __height__ would give the highest sensitivity under these conditions, so one runs the final cell:

![screenshot3](https://user-images.githubusercontent.com/13749006/63825414-b68bc980-c928-11e9-9162-6a8d3bbd10d4.png)

and notices that the sensitivity increases with the __height__, but not as fast after 3.0 cm. At 1.0 cm in __height__ the coil already has a sensitivity of ~75% its maximum value, so it is not so bad leaving it at that value.

## Process of optimization
I have not completed a good protocol to visualize all the different variables to help in finding the best dimensions. I have tried using some optimization functions from SciPy but have not had good results. Right now, this mostly works as a guide to understand what happens to the sensitivity as the parameters are changed. The main takeaway from this work is that it's good to keep coils near sample in the y-direction, and near each other in the z-direction (no vertical gap as in the first picture above), then adjust the __height__ and the __radii__ according to what you can manufacture and the space available in your electromagnet.

## To do
* Finish visualizations of different parameters combined.
* Finish an optimization routine that can return suggestions to obtain highest sensitivity.
