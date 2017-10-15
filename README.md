# machine-learning-playground
## Let's explore Machine Learning with scikit-learn!

Having watched [Josh Gordon's](https://twitter.com/random_forests) excellent 
Google Machine Learning Recipes series, I was moved to try my hand at it, despite having only 
a limited and rusty knowledge of Python. What I gathered from that series is that there isn't 
a huge amount of coding required to get really amazing results. 

Scikit gives you a bunch of powerful tools that you can easily use to make predictions about new, 
unlabeled data, based on previously observed labeled data.

The keys to success with it appear to be: 

* Get a lot of _labeled_ data to train and test with. 
* Make sure that the labels have high value. 
* Understand the different types of classifiers, and how to choose the right one for your problem and data set.

## Ok, what are we doing?
To start, I want to use scikit-learn to train and test a simple model. 
Next, build the Nearest Neighbor classifier described in the fifth installment of Mr. Gordon's series: [Writing Our First Classifier](https://youtu.be/AoeEHqVSNOw)

## Fitting our kit...

The key tool we're going to use is [scikit-learn](http://scikit-learn.org/stable/install.html)

It requires:

  * Python (>= 2.7 or >= 3.3)
  * A Python package manager (pip or conda)
  * NumPy (>= 1.8.2)
  * SciPy (>= 0.13.3)

### Python
I Installed [Python 3.6.3](https://www.python.org/downloads/) because, _"Python 2.x is legacy, Python 3.x is the present and future of the language."_

However in a new window python and pythonw still report being version 2.7 (the original version on my Mac).
Turns out you have to run python3. This makes sense because the version the OS comes with is probably relied 
upon by installed applications and we don't want to mess that up.

### Pip
Getting pip is a pain! The python.org page says you should have it if you installed python from their site, 
but a ...

```
which pip
```

... at the command line says nada. Your mileage may vary. 

I had to: [download get-pip.py](https://packaging.python.org/tutorials/installing-packages/)

Then in the same directory, run:
 
```
sudo python3 get-pip.py --prefix=/usr/local/ 
```

This seemed to install wheel but not pip. Afterward there was still no output from which pip. 
Eventually, I found [a way that works](https://stackoverflow.com/a/24151884/203704) even if 
you can't find pip: _supply the pip command to python3 using the '-m' argument._

### Scikit-learn
If you have pip, just run:

```
pip install scikit-learn[alldeps]
```

Otherwise, if you're like me and still can't find pip after installing Python from python.org
after trying from another terminal window, you can still make it happen with:


```
python3 -m pip install scikit-learn[alldeps]
```


Either way, scikit-learn and all its dependencies should now be installed. Wasn't that special?
