# VSM detector coil geometry
This is a Python 3 script to help plan optimal detection coil geometry for a VSM in Mallinson configuration, pictured below, labeled `a)`. Based on applying the Biot-Savart law and the Reciprocity Theorem to a wire loops arranged parallel to each other using the geometry, shown in picture labeled `b)`.

![geometry](https://user-images.githubusercontent.com/13749006/63816566-b7abff00-c906-11e9-9daf-6c8bb425ab18.png)

This work was originally done for my Bachelor's thesis and published on the [Journal of Magnetism and Magnetic Materials](https://doi.org/10.1016/j.jmmm.2018.01.088).


## Usage

The file `vsm_code.py` contains all the functions needed to compute the sensibility function of a detector coil. If you run it by itself in the terminal using
```bash
$ python vsm_code.py
```
it will return figures similar to the ones published in the paper linked above. I changed some of the parameters but it's the same. The graphs however are not in log-scale.

I would highly recommend using the Jupyter Notebook included since it makes changing the parameters much easier. For example, if one wants to know how close to the sample should the detector coils be to get the most signal on would run the following cell:

![screenshot1](https://user-images.githubusercontent.com/13749006/63824714-1c2a8680-c926-11e9-9359-5e9c5abeef42.png)

and notice that the signal grows as the separation of the coils from the center (where the sample would be located) is reduced, therefore it would be better to get the coils as close as possible, in the y-direction, to the sample.



## Process of optimization
I have tried to use
