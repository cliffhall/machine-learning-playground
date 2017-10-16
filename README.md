# machine-learning-playground
## Let's explore Machine Learning with scikit-learn!

Having watched [Josh Gordon's](https://twitter.com/random_forests) excellent 
Google Machine Learning Recipes series, I was moved to try my hand at it, despite having only 
a limited and rusty knowledge of Python. What I gathered from that series is that there isn't 
a huge amount of coding required to get really amazing results. 

Scikit gives you a bunch of powerful tools that you can easily use to do things like make predictions about 
new, unlabeled data based upon previously observed, labeled data. Read more about its tractable 
[problem domains](http://scikit-learn.org/stable/tutorial/basic/tutorial.html).

You can, for example, take a bunch of 'labeled data' (such as email subject lines labeled 'spam' or 'not spam'), 
split it into two piles, one for _training_ and one for _testing_. 

Next you 'train a model' with the first pile, and test the accuracy of its predictions by feeding it 
the data in the second pile. Then, see if the labels it predicts match the actual labels on the data. 
If accuracy is poor, what can be done to improve it?

The keys to success appear to be: 

* Get a lot of _labeled_ data to train and test with. 
* Make sure that the dimension you choose to label has a high value to the model. 
* Understand the different types of classifiers, and how to choose the right one for your problem and data set.

## Ok, what are we doing?
To start, I want to use scikit-learn to train and test a simple model as described above with just a few lines of code.
Next, we build the Nearest Neighbor classifier described in the fifth installment of 
Josh Gordon's series, [Writing Our First Classifier](https://youtu.be/AoeEHqVSNOw)

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

## Trying out Josh Gordon's simple classifier demo
There are couple of minor problems...

### The module for train_test_split has changed
The video says to do the following...

```
from sklearn.cross_validation import train_test_split
```

But error output tells us that cross_validation is deprecated, use model_selection module instead:

```
from sklearn.model_selection import train_test_split
```

python3 jg-my-first-classifier.py 

### The print statement
The last line that prints out the accuracy score results in the video is:

```
print accuracy_score(y_test, predictions)
```

That threw a syntax error for me, possibly because I'm using Python 3. Anyway the following works:

```
print(accuracy_score(y_test, predictions))
```

## Success!
Running:

```
python3 jg-my-first-classifier.py 
```


yields: 

```
0.973333333333
```