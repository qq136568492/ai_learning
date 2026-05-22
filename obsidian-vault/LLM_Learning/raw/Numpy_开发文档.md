---
title: "Aggregated docs (bundle)"
seed_url: "https://numpy.org/devdocs/user/quickstart.html"
page_count: 32
urls:
  - "https://numpy.org/devdocs/user/quickstart.html"
  - "https://numpy.org/devdocs/user/index.html"
  - "https://numpy.org/devdocs/user/basics.indexing.html"
  - "https://numpy.org/devdocs/user/basics.copies.html"
  - "https://numpy.org/devdocs/user/basics.broadcasting.html"
  - "https://numpy.org/devdocs/user/basics.rec.html"
  - "https://numpy.org/devdocs/user/numpy-for-matlab-users.html"
  - "https://numpy.org/devdocs/user/whatisnumpy.html"
  - "https://numpy.org/devdocs/user/absolute_beginners.html"
  - "https://numpy.org/devdocs/user/basics.html"
  - "https://numpy.org/devdocs/user/basics.creation.html"
  - "https://numpy.org/devdocs/user/basics.io.html"
  - "https://numpy.org/devdocs/user/basics.types.html"
  - "https://numpy.org/devdocs/user/basics.strings.html"
  - "https://numpy.org/devdocs/user/basics.ufuncs.html"
  - "https://numpy.org/devdocs/user/howtos_index.html"
  - "https://numpy.org/devdocs/user/c-info.html"
  - "https://numpy.org/devdocs/user/basics.interoperability.html"
  - "https://numpy.org/devdocs/user/how-to-io.html"
  - "https://numpy.org/devdocs/user/basics.io.genfromtxt.html"
  - "https://numpy.org/devdocs/user/how-to-how-to.html"
  - "https://numpy.org/devdocs/user/how-to-index.html"
  - "https://numpy.org/devdocs/user/how-to-verify-bug.html"
  - "https://numpy.org/devdocs/user/how-to-partition.html"
  - "https://numpy.org/devdocs/user/how-to-print.html"
  - "https://numpy.org/devdocs/user/c-info.how-to-extend.html"
  - "https://numpy.org/devdocs/user/c-info.python-as-glue.html"
  - "https://numpy.org/devdocs/user/c-info.ufunc-tutorial.html"
  - "https://numpy.org/devdocs/user/c-info.beyond-basics.html"
  - "https://numpy.org/devdocs/user/basics.subclassing.html"
  - "https://numpy.org/devdocs/user/basics.dispatch.html"
  - "https://numpy.org/devdocs/user/byteswapping.html"
generator_note: "sphinx-html-bundle (urllib + html2text)"
---

# Aggregated bundle

**Seed:** `https://numpy.org/devdocs/user/quickstart.html`  
**Pages merged:** 32

---

## NumPy quickstart

**Source:** [https://numpy.org/devdocs/user/quickstart.html](https://numpy.org/devdocs/user/quickstart.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * NumPy quickstart



# NumPy quickstart[#](#numpy-quickstart "Link to this heading")

## Prerequisites[#](#prerequisites "Link to this heading")

You’ll need to know a bit of Python. For a refresher, see the [Python tutorial](https://docs.python.org/tutorial/).

To work the examples, you’ll need `matplotlib` installed in addition to NumPy.

**Learner profile**

This is a quick overview of arrays in NumPy. It demonstrates how n-dimensional (\\(n>=2\\)) arrays are represented and can be manipulated. In particular, if you don’t know how to apply common functions to n-dimensional arrays (without using for-loops), or if you want to understand axis and shape properties for n-dimensional arrays, this article might be of help.

**Learning Objectives**

After reading, you should be able to:

  * Understand the difference between one-, two- and n-dimensional arrays in NumPy;

  * Understand how to apply some linear algebra operations to n-dimensional arrays without using for-loops;

  * Understand axis and shape properties for n-dimensional arrays.




## The basics[#](#the-basics "Link to this heading")

NumPy’s main object is the homogeneous multidimensional array. It is a table of elements (usually numbers), all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called _axes_.

For example, the array for the coordinates of a point in 3D space, `[1, 2, 1]`, has one axis. That axis has 3 elements in it, so we say it has a length of 3. In the example pictured below, the array has 2 axes. The first axis has a length of 2, the second axis has a length of 3.
    
    
    [[1., 0., 0.],
     [0., 1., 2.]]
    

NumPy’s array class is called `ndarray`. It is also known by the alias `array`. Note that `numpy.array` is not the same as the Standard Python Library class `array.array`, which only handles one-dimensional arrays and offers less functionality. The more important attributes of an `ndarray` object are:

ndarray.ndim
    

the number of axes (dimensions) of the array.

ndarray.shape
    

the dimensions of the array. This is a tuple of integers indicating the size of the array in each dimension. For a matrix with _n_ rows and _m_ columns, `shape` will be `(n,m)`. The length of the `shape` tuple is therefore the number of axes, `ndim`.

ndarray.size
    

the total number of elements of the array. This is equal to the product of the elements of `shape`.

ndarray.dtype
    

an object describing the type of the elements in the array. One can create or specify dtype’s using standard Python types. Additionally NumPy provides types of its own. numpy.int32, numpy.int16, and numpy.float64 are some examples.

ndarray.itemsize
    

the size in bytes of each element of the array. For example, an array of elements of type `float64` has `itemsize` 8 (=64/8), while one of type `complex32` has `itemsize` 4 (=32/8). It is equivalent to `ndarray.dtype.itemsize`.

ndarray.data
    

the buffer containing the actual elements of the array. Normally, we won’t need to use this attribute because we will access the elements in an array using indexing facilities.

### An example[#](#an-example "Link to this heading")
    
    
    >>> import numpy as np
    >>> a = np.arange(15).reshape(3, 5)
    >>> a
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14]])
    >>> a.shape
    (3, 5)
    >>> a.ndim
    2
    >>> a.dtype.name
    'int64'
    >>> a.itemsize
    8
    >>> a.size
    15
    >>> type(a)
    <class 'numpy.ndarray'>
    >>> b = np.array([6, 7, 8])
    >>> b
    array([6, 7, 8])
    >>> type(b)
    <class 'numpy.ndarray'>
    

### Array creation[#](#array-creation "Link to this heading")

There are several ways to create arrays.

For example, you can create an array from a regular Python list or tuple using the `array` function. The type of the resulting array is deduced from the type of the elements in the sequences.
    
    
    >>> import numpy as np
    >>> a = np.array([2, 3, 4])
    >>> a
    array([2, 3, 4])
    >>> a.dtype
    dtype('int64')
    >>> b = np.array([1.2, 3.5, 5.1])
    >>> b.dtype
    dtype('float64')
    

A frequent error consists in calling `array` with multiple arguments, rather than providing a single sequence as an argument.
    
    
    >>> a = np.array(1, 2, 3, 4)    # WRONG
    Traceback (most recent call last):
      ...
    TypeError: array() takes from 1 to 2 positional arguments but 4 were given
    >>> a = np.array([1, 2, 3, 4])  # RIGHT
    

`array` transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.
    
    
    >>> b = np.array([(1.5, 2, 3), (4, 5, 6)])
    >>> b
    array([[1.5, 2. , 3. ],
           [4. , 5. , 6. ]])
    

The type of the array can also be explicitly specified at creation time:
    
    
    >>> c = np.array([[1, 2], [3, 4]], dtype=np.complex128)
    >>> c
    array([[1.+0.j, 2.+0.j],
           [3.+0.j, 4.+0.j]])
    

Often, the elements of an array are originally unknown, but its size is known. Hence, NumPy offers several functions to create arrays with initial placeholder content. These minimize the necessity of growing arrays, an expensive operation.

The function `zeros` creates an array full of zeros, the function `ones` creates an array full of ones, and the function `empty` creates an array whose initial content is random and depends on the state of the memory. By default, the dtype of the created array is `float64`, but it can be specified via the key word argument `dtype`.
    
    
    >>> np.zeros((3, 4))
    array([[0., 0., 0., 0.],
           [0., 0., 0., 0.],
           [0., 0., 0., 0.]])
    >>> np.ones((2, 3, 4), dtype=np.int16)
    array([[[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]],
    
           [[1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1]]], dtype=int16)
    >>> np.empty((2, 3)) 
    array([[3.73603959e-262, 6.02658058e-154, 6.55490914e-260],  # may vary
           [5.30498948e-313, 3.14673309e-307, 1.00000000e+000]])
    

To create sequences of numbers, NumPy provides the `arange` function which is analogous to the Python built-in `range`, but returns an array.
    
    
    >>> np.arange(10, 30, 5)
    array([10, 15, 20, 25])
    >>> np.arange(0, 2, 0.3)  # it accepts float arguments
    array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])
    

When `arange` is used with floating point arguments, it is generally not possible to predict the number of elements obtained, due to the finite floating point precision. For this reason, it is usually better to use the function `linspace` that receives as an argument the number of elements that we want, instead of the step:
    
    
    >>> from numpy import pi
    >>> np.linspace(0, 2, 9)                   # 9 numbers from 0 to 2
    array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
    >>> x = np.linspace(0, 2 * pi, 100)        # useful to evaluate function at lots of points
    >>> f = np.sin(x)
    

See also

[`array`](../reference/generated/numpy.array.html#numpy.array "numpy.array"), [`zeros`](../reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros"), [`zeros_like`](../reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like"), [`ones`](../reference/generated/numpy.ones.html#numpy.ones "numpy.ones"), [`ones_like`](../reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like"), [`empty`](../reference/generated/numpy.empty.html#numpy.empty "numpy.empty"), [`empty_like`](../reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like"), [`arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange"), [`linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace"), [`random.Generator.random`](../reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random"), [`random.Generator.normal`](../reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal "numpy.random.Generator.normal"), [`fromfunction`](../reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction"), [`fromfile`](../reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")

### Printing arrays[#](#printing-arrays "Link to this heading")

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:

  * the last axis is printed from left to right,

  * the second-to-last is printed from top to bottom,

  * the rest are also printed from top to bottom, with each slice separated from the next by an empty line.




One-dimensional arrays are then printed as rows, bidimensionals as matrices and tridimensionals as lists of matrices.
    
    
    >>> a = np.arange(6)                    # 1d array
    >>> print(a)
    [0 1 2 3 4 5]
    >>>
    >>> b = np.arange(12).reshape(4, 3)     # 2d array
    >>> print(b)
    [[ 0  1  2]
     [ 3  4  5]
     [ 6  7  8]
     [ 9 10 11]]
    >>>
    >>> c = np.arange(24).reshape(2, 3, 4)  # 3d array
    >>> print(c)
    [[[ 0  1  2  3]
      [ 4  5  6  7]
      [ 8  9 10 11]]
    
     [[12 13 14 15]
      [16 17 18 19]
      [20 21 22 23]]]
    

See [below](#quickstart-shape-manipulation) to get more details on `reshape`.

If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners:
    
    
    >>> print(np.arange(10000))
    [   0    1    2 ... 9997 9998 9999]
    >>>
    >>> print(np.arange(10000).reshape(100, 100))
    [[   0    1    2 ...   97   98   99]
     [ 100  101  102 ...  197  198  199]
     [ 200  201  202 ...  297  298  299]
     ...
     [9700 9701 9702 ... 9797 9798 9799]
     [9800 9801 9802 ... 9897 9898 9899]
     [9900 9901 9902 ... 9997 9998 9999]]
    

To disable this behaviour and force NumPy to print the entire array, you can change the printing options using `set_printoptions`.
    
    
    >>> np.set_printoptions(threshold=sys.maxsize)  # sys module should be imported
    

### Basic operations[#](#basic-operations "Link to this heading")

Arithmetic operators on arrays apply _elementwise_. A new array is created and filled with the result.
    
    
    >>> a = np.array([20, 30, 40, 50])
    >>> b = np.arange(4)
    >>> b
    array([0, 1, 2, 3])
    >>> c = a - b
    >>> c
    array([20, 29, 38, 47])
    >>> b**2
    array([0, 1, 4, 9])
    >>> 10 * np.sin(a)
    array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
    >>> a < 35
    array([ True,  True, False, False])
    

Unlike in many matrix languages, the product operator `*` operates elementwise in NumPy arrays. The matrix product can be performed using the `@` operator (in python >=3.5) or the `dot` function or method:
    
    
    >>> A = np.array([[1, 1],
    ...               [0, 1]])
    >>> B = np.array([[2, 0],
    ...               [3, 4]])
    >>> A * B     # elementwise product
    array([[2, 0],
           [0, 4]])
    >>> A @ B     # matrix product
    array([[5, 4],
           [3, 4]])
    >>> A.dot(B)  # another matrix product
    array([[5, 4],
           [3, 4]])
    

Some operations, such as `+=` and `*=`, act in place to modify an existing array rather than create a new one.
    
    
    >>> rg = np.random.default_rng(1)  # create instance of default random number generator
    >>> a = np.ones((2, 3), dtype=np.int_)
    >>> b = rg.random((2, 3))
    >>> a *= 3
    >>> a
    array([[3, 3, 3],
           [3, 3, 3]])
    >>> b += a
    >>> b
    array([[3.51182162, 3.9504637 , 3.14415961],
           [3.94864945, 3.31183145, 3.42332645]])
    >>> a += b  # b is not automatically converted to integer type
    Traceback (most recent call last):
        ...
    numpy._core._exceptions._UFuncOutputCastingError: Cannot cast ufunc 'add' output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
    

When operating with arrays of different types, the type of the resulting array corresponds to the more general or precise one (a behavior known as upcasting).
    
    
    >>> a = np.ones(3, dtype=np.int32)
    >>> b = np.linspace(0, pi, 3)
    >>> b.dtype.name
    'float64'
    >>> c = a + b
    >>> c
    array([1.        , 2.57079633, 4.14159265])
    >>> c.dtype.name
    'float64'
    >>> d = np.exp(c * 1j)
    >>> d
    array([ 0.54030231+0.84147098j, -0.84147098+0.54030231j,
           -0.54030231-0.84147098j])
    >>> d.dtype.name
    'complex128'
    

Many unary operations, such as computing the sum of all the elements in the array, are implemented as methods of the `ndarray` class.
    
    
    >>> a = rg.random((2, 3))
    >>> a
    array([[0.82770259, 0.40919914, 0.54959369],
           [0.02755911, 0.75351311, 0.53814331]])
    >>> a.sum()
    3.1057109529998157
    >>> a.min()
    0.027559113243068367
    >>> a.max()
    0.8277025938204418
    

By default, these operations apply to the array as though it were a list of numbers, regardless of its shape. However, by specifying the `axis` parameter you can apply an operation along the specified axis of an array:
    
    
    >>> b = np.arange(12).reshape(3, 4)
    >>> b
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>>
    >>> b.sum(axis=0)     # sum of each column
    array([12, 15, 18, 21])
    >>>
    >>> b.min(axis=1)     # min of each row
    array([0, 4, 8])
    >>>
    >>> b.cumsum(axis=1)  # cumulative sum along each row
    array([[ 0,  1,  3,  6],
           [ 4,  9, 15, 22],
           [ 8, 17, 27, 38]])
    

### Universal functions[#](#universal-functions "Link to this heading")

NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (`ufunc`). Within NumPy, these functions operate elementwise on an array, producing an array as output.
    
    
    >>> B = np.arange(3)
    >>> B
    array([0, 1, 2])
    >>> np.exp(B)
    array([1.        , 2.71828183, 7.3890561 ])
    >>> np.sqrt(B)
    array([0.        , 1.        , 1.41421356])
    >>> C = np.array([2., -1., 4.])
    >>> np.add(B, C)
    array([2., 0., 6.])
    

See also

[`all`](../reference/generated/numpy.all.html#numpy.all "numpy.all"), [`any`](../reference/generated/numpy.any.html#numpy.any "numpy.any"), [`apply_along_axis`](../reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis"), [`argmax`](../reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax"), [`argmin`](../reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin"), [`argsort`](../reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort"), [`average`](../reference/generated/numpy.average.html#numpy.average "numpy.average"), [`bincount`](../reference/generated/numpy.bincount.html#numpy.bincount "numpy.bincount"), [`ceil`](../reference/generated/numpy.ceil.html#numpy.ceil "numpy.ceil"), [`clip`](../reference/generated/numpy.clip.html#numpy.clip "numpy.clip"), [`conj`](../reference/generated/numpy.conj.html#numpy.conj "numpy.conj"), [`corrcoef`](../reference/generated/numpy.corrcoef.html#numpy.corrcoef "numpy.corrcoef"), [`cov`](../reference/generated/numpy.cov.html#numpy.cov "numpy.cov"), [`cross`](../reference/generated/numpy.cross.html#numpy.cross "numpy.cross"), [`cumprod`](../reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod"), [`cumsum`](../reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum"), [`diff`](../reference/generated/numpy.diff.html#numpy.diff "numpy.diff"), [`dot`](../reference/generated/numpy.dot.html#numpy.dot "numpy.dot"), [`floor`](../reference/generated/numpy.floor.html#numpy.floor "numpy.floor"), [`inner`](../reference/generated/numpy.inner.html#numpy.inner "numpy.inner"), [`invert`](../reference/generated/numpy.invert.html#numpy.invert "numpy.invert"), [`lexsort`](../reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort"), [`max`](../reference/generated/numpy.max.html#numpy.max "numpy.max"), [`maximum`](../reference/generated/numpy.maximum.html#numpy.maximum "numpy.maximum"), [`mean`](../reference/generated/numpy.mean.html#numpy.mean "numpy.mean"), [`median`](../reference/generated/numpy.median.html#numpy.median "numpy.median"), [`min`](../reference/generated/numpy.min.html#numpy.min "numpy.min"), [`minimum`](../reference/generated/numpy.minimum.html#numpy.minimum "numpy.minimum"), [`nonzero`](../reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero"), [`outer`](../reference/generated/numpy.outer.html#numpy.outer "numpy.outer"), [`prod`](../reference/generated/numpy.prod.html#numpy.prod "numpy.prod"), [`re`](https://docs.python.org/3/library/re.html#module-re "\(in Python v3.14\)"), [`round`](../reference/generated/numpy.round.html#numpy.round "numpy.round"), [`sort`](../reference/generated/numpy.sort.html#numpy.sort "numpy.sort"), [`std`](../reference/generated/numpy.std.html#numpy.std "numpy.std"), [`sum`](../reference/generated/numpy.sum.html#numpy.sum "numpy.sum"), [`trace`](../reference/generated/numpy.trace.html#numpy.trace "numpy.trace"), [`transpose`](../reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose"), [`var`](../reference/generated/numpy.var.html#numpy.var "numpy.var"), [`vdot`](../reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot"), [`vectorize`](../reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize"), [`where`](../reference/generated/numpy.where.html#numpy.where "numpy.where")

### Indexing, slicing and iterating[#](#indexing-slicing-and-iterating "Link to this heading")

**One-dimensional** arrays can be indexed, sliced and iterated over, much like [lists](https://docs.python.org/tutorial/introduction.html#lists) and other Python sequences.
    
    
    >>> a = np.arange(10)**3
    >>> a
    array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
    >>> a[2]
    8
    >>> a[2:5]
    array([ 8, 27, 64])
    >>> # equivalent to a[0:6:2] = 1000;
    >>> # from start to position 6, exclusive, set every 2nd element to 1000
    >>> a[:6:2] = 1000
    >>> a
    array([1000,    1, 1000,   27, 1000,  125,  216,  343,  512,  729])
    >>> a[::-1]  # reversed a
    array([ 729,  512,  343,  216,  125, 1000,   27, 1000,    1, 1000])
    >>> for i in a:
    ...     print(i**(1 / 3.))
    ...
    9.999999999999998  # may vary
    1.0
    9.999999999999998
    3.0
    9.999999999999998
    4.999999999999999
    5.999999999999999
    6.999999999999999
    7.999999999999999
    8.999999999999998
    

**Multidimensional** arrays can have one index per axis. These indices are given in a tuple separated by commas:
    
    
    >>> def f(x, y):
    ...     return 10 * x + y
    ...
    >>> b = np.fromfunction(f, (5, 4), dtype=np.int_)
    >>> b
    array([[ 0,  1,  2,  3],
           [10, 11, 12, 13],
           [20, 21, 22, 23],
           [30, 31, 32, 33],
           [40, 41, 42, 43]])
    >>> b[2, 3]
    23
    >>> b[0:5, 1]  # each row in the second column of b
    array([ 1, 11, 21, 31, 41])
    >>> b[:, 1]    # equivalent to the previous example
    array([ 1, 11, 21, 31, 41])
    >>> b[1:3, :]  # each column in the second and third row of b
    array([[10, 11, 12, 13],
           [20, 21, 22, 23]])
    

When fewer indices are provided than the number of axes, the missing indices are considered complete slices`:`
    
    
    >>> b[-1]   # the last row. Equivalent to b[-1, :]
    array([40, 41, 42, 43])
    

The expression within brackets in `b[i]` is treated as an `i` followed by as many instances of `:` as needed to represent the remaining axes. NumPy also allows you to write this using dots as `b[i, ...]`.

The **dots** (`...`) represent as many colons as needed to produce a complete indexing tuple. For example, if `x` is an array with 5 axes, then

  * `x[1, 2, ...]` is equivalent to `x[1, 2, :, :, :]`,

  * `x[..., 3]` to `x[:, :, :, :, 3]` and

  * `x[4, ..., 5, :]` to `x[4, :, :, 5, :]`.



    
    
    >>> c = np.array([[[  0,  1,  2],  # a 3D array (two stacked 2D arrays)
    ...                [ 10, 12, 13]],
    ...               [[100, 101, 102],
    ...                [110, 112, 113]]])
    >>> c.shape
    (2, 2, 3)
    >>> c[1, ...]  # same as c[1, :, :] or c[1]
    array([[100, 101, 102],
           [110, 112, 113]])
    >>> c[..., 2]  # same as c[:, :, 2]
    array([[  2,  13],
           [102, 113]])
    

**Iterating** over multidimensional arrays is done with respect to the first axis:
    
    
    >>> for row in b:
    ...     print(row)
    ...
    [0 1 2 3]
    [10 11 12 13]
    [20 21 22 23]
    [30 31 32 33]
    [40 41 42 43]
    

However, if one wants to perform an operation on each element in the array, one can use the `flat` attribute which is an [iterator](https://docs.python.org/tutorial/classes.html#iterators) over all the elements of the array:
    
    
    >>> for element in b.flat:
    ...     print(element)
    ...
    0
    1
    2
    3
    10
    11
    12
    13
    20
    21
    22
    23
    30
    31
    32
    33
    40
    41
    42
    43
    

See also

[Indexing on ndarrays](basics.indexing.html#basics-indexing), [Indexing routines](../reference/routines.indexing.html#arrays-indexing) (reference), [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis"), [`ndenumerate`](../reference/generated/numpy.ndenumerate.html#numpy.ndenumerate "numpy.ndenumerate"), [`indices`](../reference/generated/numpy.indices.html#numpy.indices "numpy.indices")

## Shape manipulation[#](#shape-manipulation "Link to this heading")

### Changing the shape of an array[#](#changing-the-shape-of-an-array "Link to this heading")

An array has a shape given by the number of elements along each axis:
    
    
    >>> a = np.floor(10 * rg.random((3, 4)))
    >>> a
    array([[3., 7., 3., 4.],
           [1., 4., 2., 2.],
           [7., 2., 4., 9.]])
    >>> a.shape
    (3, 4)
    

The shape of an array can be changed with various commands. Note that the following three commands all return a modified array, but do not change the original array:
    
    
    >>> a.ravel()  # returns the array, flattened
    array([3., 7., 3., 4., 1., 4., 2., 2., 7., 2., 4., 9.])
    >>> a.reshape(6, 2)  # returns the array with a modified shape
    array([[3., 7.],
           [3., 4.],
           [1., 4.],
           [2., 2.],
           [7., 2.],
           [4., 9.]])
    >>> a.T  # returns the array, transposed
    array([[3., 1., 7.],
           [7., 4., 2.],
           [3., 2., 4.],
           [4., 2., 9.]])
    >>> a.T.shape
    (4, 3)
    >>> a.shape
    (3, 4)
    

The order of the elements in the array resulting from `ravel` is normally “C-style”, that is, the rightmost index “changes the fastest”, so the element after `a[0, 0]` is `a[0, 1]`. If the array is reshaped to some other shape, again the array is treated as “C-style”. NumPy normally creates arrays stored in this order, so `ravel` will usually not need to copy its argument, but if the array was made by taking slices of another array or created with unusual options, it may need to be copied. The functions `ravel` and `reshape` can also be instructed, using an optional argument, to use FORTRAN-style arrays, in which the leftmost index changes the fastest.

The [`reshape`](../reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape") function returns its argument with a modified shape, whereas the [`ndarray.resize`](../reference/generated/numpy.ndarray.resize.html#numpy.ndarray.resize "numpy.ndarray.resize") method modifies the array itself:
    
    
    >>> a
    array([[3., 7., 3., 4.],
           [1., 4., 2., 2.],
           [7., 2., 4., 9.]])
    >>> a.resize((2, 6))
    >>> a
    array([[3., 7., 3., 4., 1., 4.],
           [2., 2., 7., 2., 4., 9.]])
    

If a dimension is given as `-1` in a reshaping operation, the other dimensions are automatically calculated:
    
    
    >>> a.reshape(3, -1)
    array([[3., 7., 3., 4.],
           [1., 4., 2., 2.],
           [7., 2., 4., 9.]])
    

See also

[`ndarray.shape`](../reference/generated/numpy.ndarray.shape.html#numpy.ndarray.shape "numpy.ndarray.shape"), [`reshape`](../reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape"), [`resize`](../reference/generated/numpy.resize.html#numpy.resize "numpy.resize"), [`ravel`](../reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel")

### Stacking together different arrays[#](#stacking-together-different-arrays "Link to this heading")

Several arrays can be stacked together along different axes:
    
    
    >>> a = np.floor(10 * rg.random((2, 2)))
    >>> a
    array([[9., 7.],
           [5., 2.]])
    >>> b = np.floor(10 * rg.random((2, 2)))
    >>> b
    array([[1., 9.],
           [5., 1.]])
    >>> np.vstack((a, b))
    array([[9., 7.],
           [5., 2.],
           [1., 9.],
           [5., 1.]])
    >>> np.hstack((a, b))
    array([[9., 7., 1., 9.],
           [5., 2., 5., 1.]])
    

The function [`column_stack`](../reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack") stacks 1D arrays as columns into a 2D array. It is equivalent to [`hstack`](../reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack") only for 2D arrays:
    
    
    >>> from numpy import newaxis
    >>> np.column_stack((a, b))  # with 2D arrays
    array([[9., 7., 1., 9.],
           [5., 2., 5., 1.]])
    >>> a = np.array([4., 2.])
    >>> b = np.array([3., 8.])
    >>> np.column_stack((a, b))  # returns a 2D array
    array([[4., 3.],
           [2., 8.]])
    >>> np.hstack((a, b))        # the result is different
    array([4., 2., 3., 8.])
    >>> a[:, newaxis]  # view `a` as a 2D column vector
    array([[4.],
           [2.]])
    >>> np.column_stack((a[:, newaxis], b[:, newaxis]))
    array([[4., 3.],
           [2., 8.]])
    >>> np.hstack((a[:, newaxis], b[:, newaxis]))  # the result is the same
    array([[4., 3.],
           [2., 8.]])
    

In general, for arrays with more than two dimensions, [`hstack`](../reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack") stacks along their second axes, [`vstack`](../reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack") stacks along their first axes, and [`concatenate`](../reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate") allows for an optional arguments giving the number of the axis along which the concatenation should happen.

**Note**

In complex cases, [`r_`](../reference/generated/numpy.r_.html#numpy.r_ "numpy.r_") and [`c_`](../reference/generated/numpy.c_.html#numpy.c_ "numpy.c_") are useful for creating arrays by stacking numbers along one axis. They allow the use of range literals `:`.
    
    
    >>> np.r_[1:4, 0, 4]
    array([1, 2, 3, 0, 4])
    

When used with arrays as arguments, [`r_`](../reference/generated/numpy.r_.html#numpy.r_ "numpy.r_") and [`c_`](../reference/generated/numpy.c_.html#numpy.c_ "numpy.c_") are similar to [`vstack`](../reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack") and [`hstack`](../reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack") in their default behavior, but allow for an optional argument giving the number of the axis along which to concatenate.

See also

[`hstack`](../reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack"), [`vstack`](../reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack"), [`column_stack`](../reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack"), [`concatenate`](../reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate"), [`c_`](../reference/generated/numpy.c_.html#numpy.c_ "numpy.c_"), [`r_`](../reference/generated/numpy.r_.html#numpy.r_ "numpy.r_")

### Splitting one array into several smaller ones[#](#splitting-one-array-into-several-smaller-ones "Link to this heading")

Using [`hsplit`](../reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit"), you can split an array along its horizontal axis, either by specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur:
    
    
    >>> a = np.floor(10 * rg.random((2, 12)))
    >>> a
    array([[6., 7., 6., 9., 0., 5., 4., 0., 6., 8., 5., 2.],
           [8., 5., 5., 7., 1., 8., 6., 7., 1., 8., 1., 0.]])
    >>> # Split `a` into 3
    >>> np.hsplit(a, 3)
    [array([[6., 7., 6., 9.],
           [8., 5., 5., 7.]]), array([[0., 5., 4., 0.],
           [1., 8., 6., 7.]]), array([[6., 8., 5., 2.],
           [1., 8., 1., 0.]])]
    >>> # Split `a` after the third and the fourth column
    >>> np.hsplit(a, (3, 4))
    [array([[6., 7., 6.],
           [8., 5., 5.]]), array([[9.],
           [7.]]), array([[0., 5., 4., 0., 6., 8., 5., 2.],
           [1., 8., 6., 7., 1., 8., 1., 0.]])]
    

[`vsplit`](../reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit") splits along the vertical axis, and [`array_split`](../reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split") allows one to specify along which axis to split.

## Copies and views[#](#copies-and-views "Link to this heading")

When operating and manipulating arrays, their data is sometimes copied into a new array and sometimes not. This is often a source of confusion for beginners. There are three cases:

### No copy at all[#](#no-copy-at-all "Link to this heading")

Simple assignments make no copy of objects or their data.
    
    
    >>> a = np.array([[ 0,  1,  2,  3],
    ...               [ 4,  5,  6,  7],
    ...               [ 8,  9, 10, 11]])
    >>> b = a            # no new object is created
    >>> b is a           # a and b are two names for the same ndarray object
    True
    

Python passes mutable objects as references, so function calls make no copy.
    
    
    >>> def f(x):
    ...     print(id(x))
    ...
    >>> id(a)  # id is a unique identifier of an object 
    148293216  # may vary
    >>> f(a)   
    148293216  # may vary
    

### View or shallow copy[#](#view-or-shallow-copy "Link to this heading")

Different array objects can share the same data. The `view` method creates a new array object that looks at the same data.
    
    
    >>> c = a.view()
    >>> c is a
    False
    >>> c.base is a            # c is a view of the data owned by a
    True
    >>> c.flags.owndata
    False
    >>>
    >>> c = c.reshape((2, 6))  # a's shape doesn't change, reassigned c is still a view of a
    >>> a.shape
    (3, 4)
    >>> c[0, 4] = 1234         # a's data changes
    >>> a
    array([[   0,    1,    2,    3],
           [1234,    5,    6,    7],
           [   8,    9,   10,   11]])
    

Slicing an array returns a view of it:
    
    
    >>> s = a[:, 1:3]
    >>> s[:] = 10  # s[:] is a view of s. Note the difference between s = 10 and s[:] = 10
    >>> a
    array([[   0,   10,   10,    3],
           [1234,   10,   10,    7],
           [   8,   10,   10,   11]])
    

### Deep copy[#](#deep-copy "Link to this heading")

The `copy` method makes a complete copy of the array and its data.
    
    
    >>> d = a.copy()  # a new array object with new data is created
    >>> d is a
    False
    >>> d.base is a  # d doesn't share anything with a
    False
    >>> d[0, 0] = 9999
    >>> a
    array([[   0,   10,   10,    3],
           [1234,   10,   10,    7],
           [   8,   10,   10,   11]])
    

Sometimes `copy` should be called after slicing if the original array is not required anymore. For example, suppose `a` is a huge intermediate result and the final result `b` only contains a small fraction of `a`, a deep copy should be made when constructing `b` with slicing:
    
    
    >>> a = np.arange(int(1e8))
    >>> b = a[:100].copy()
    >>> del a  # the memory of ``a`` can be released.
    

If `b = a[:100]` is used instead, `a` is referenced by `b` and will persist in memory even if `del a` is executed.

See also [Copies and views](basics.copies.html#basics-copies-and-views).

### Functions and methods overview[#](#functions-and-methods-overview "Link to this heading")

Here is a list of some useful NumPy functions and methods names ordered in categories. See [Routines and objects by topic](../reference/routines.html#routines) for the full list.

Array Creation
    

[`arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange"), [`array`](../reference/generated/numpy.array.html#numpy.array "numpy.array"), [`copy`](../reference/generated/numpy.copy.html#numpy.copy "numpy.copy"), [`empty`](../reference/generated/numpy.empty.html#numpy.empty "numpy.empty"), [`empty_like`](../reference/generated/numpy.empty_like.html#numpy.empty_like "numpy.empty_like"), [`eye`](../reference/generated/numpy.eye.html#numpy.eye "numpy.eye"), [`fromfile`](../reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile"), [`fromfunction`](../reference/generated/numpy.fromfunction.html#numpy.fromfunction "numpy.fromfunction"), [`identity`](../reference/generated/numpy.identity.html#numpy.identity "numpy.identity"), [`linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace"), [`logspace`](../reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace"), [`mgrid`](../reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid"), [`ogrid`](../reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid"), [`ones`](../reference/generated/numpy.ones.html#numpy.ones "numpy.ones"), [`ones_like`](../reference/generated/numpy.ones_like.html#numpy.ones_like "numpy.ones_like"), [`r_`](../reference/generated/numpy.r_.html#numpy.r_ "numpy.r_"), [`zeros`](../reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros"), [`zeros_like`](../reference/generated/numpy.zeros_like.html#numpy.zeros_like "numpy.zeros_like")

Conversions
    

[`ndarray.astype`](../reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype"), [`atleast_1d`](../reference/generated/numpy.atleast_1d.html#numpy.atleast_1d "numpy.atleast_1d"), [`atleast_2d`](../reference/generated/numpy.atleast_2d.html#numpy.atleast_2d "numpy.atleast_2d"), [`atleast_3d`](../reference/generated/numpy.atleast_3d.html#numpy.atleast_3d "numpy.atleast_3d"), _mat_

Manipulations
    

[`array_split`](../reference/generated/numpy.array_split.html#numpy.array_split "numpy.array_split"), [`column_stack`](../reference/generated/numpy.column_stack.html#numpy.column_stack "numpy.column_stack"), [`concatenate`](../reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate"), [`diagonal`](../reference/generated/numpy.diagonal.html#numpy.diagonal "numpy.diagonal"), [`dsplit`](../reference/generated/numpy.dsplit.html#numpy.dsplit "numpy.dsplit"), [`dstack`](../reference/generated/numpy.dstack.html#numpy.dstack "numpy.dstack"), [`hsplit`](../reference/generated/numpy.hsplit.html#numpy.hsplit "numpy.hsplit"), [`hstack`](../reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack"), [`ndarray.item`](../reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item"), [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis"), [`ravel`](../reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel"), [`repeat`](../reference/generated/numpy.repeat.html#numpy.repeat "numpy.repeat"), [`reshape`](../reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape"), [`resize`](../reference/generated/numpy.resize.html#numpy.resize "numpy.resize"), [`squeeze`](../reference/generated/numpy.squeeze.html#numpy.squeeze "numpy.squeeze"), [`swapaxes`](../reference/generated/numpy.swapaxes.html#numpy.swapaxes "numpy.swapaxes"), [`take`](../reference/generated/numpy.take.html#numpy.take "numpy.take"), [`transpose`](../reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose"), [`vsplit`](../reference/generated/numpy.vsplit.html#numpy.vsplit "numpy.vsplit"), [`vstack`](../reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack")

Questions
    

[`all`](../reference/generated/numpy.all.html#numpy.all "numpy.all"), [`any`](../reference/generated/numpy.any.html#numpy.any "numpy.any"), [`nonzero`](../reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero"), [`where`](../reference/generated/numpy.where.html#numpy.where "numpy.where")

Ordering
    

[`argmax`](../reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax"), [`argmin`](../reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin"), [`argsort`](../reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort"), [`max`](../reference/generated/numpy.max.html#numpy.max "numpy.max"), [`min`](../reference/generated/numpy.min.html#numpy.min "numpy.min"), [`ptp`](../reference/generated/numpy.ptp.html#numpy.ptp "numpy.ptp"), [`searchsorted`](../reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted"), [`sort`](../reference/generated/numpy.sort.html#numpy.sort "numpy.sort")

Operations
    

[`choose`](../reference/generated/numpy.choose.html#numpy.choose "numpy.choose"), [`compress`](../reference/generated/numpy.compress.html#numpy.compress "numpy.compress"), [`cumprod`](../reference/generated/numpy.cumprod.html#numpy.cumprod "numpy.cumprod"), [`cumsum`](../reference/generated/numpy.cumsum.html#numpy.cumsum "numpy.cumsum"), [`inner`](../reference/generated/numpy.inner.html#numpy.inner "numpy.inner"), [`ndarray.fill`](../reference/generated/numpy.ndarray.fill.html#numpy.ndarray.fill "numpy.ndarray.fill"), [`imag`](../reference/generated/numpy.imag.html#numpy.imag "numpy.imag"), [`prod`](../reference/generated/numpy.prod.html#numpy.prod "numpy.prod"), [`put`](../reference/generated/numpy.put.html#numpy.put "numpy.put"), [`putmask`](../reference/generated/numpy.putmask.html#numpy.putmask "numpy.putmask"), [`real`](../reference/generated/numpy.real.html#numpy.real "numpy.real"), [`sum`](../reference/generated/numpy.sum.html#numpy.sum "numpy.sum")

Basic Statistics
    

[`cov`](../reference/generated/numpy.cov.html#numpy.cov "numpy.cov"), [`mean`](../reference/generated/numpy.mean.html#numpy.mean "numpy.mean"), [`std`](../reference/generated/numpy.std.html#numpy.std "numpy.std"), [`var`](../reference/generated/numpy.var.html#numpy.var "numpy.var")

Basic Linear Algebra
    

[`cross`](../reference/generated/numpy.cross.html#numpy.cross "numpy.cross"), [`dot`](../reference/generated/numpy.dot.html#numpy.dot "numpy.dot"), [`outer`](../reference/generated/numpy.outer.html#numpy.outer "numpy.outer"), [`linalg.svd`](../reference/generated/numpy.linalg.svd.html#numpy.linalg.svd "numpy.linalg.svd"), [`vdot`](../reference/generated/numpy.vdot.html#numpy.vdot "numpy.vdot")

## Less basic[#](#less-basic "Link to this heading")

### Broadcasting rules[#](#broadcasting-rules "Link to this heading")

Broadcasting allows universal functions to deal in a meaningful way with inputs that do not have exactly the same shape.

The first rule of broadcasting is that if all input arrays do not have the same number of dimensions, a “1” will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.

The second rule of broadcasting ensures that arrays with a size of 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the “broadcast” array.

After application of the broadcasting rules, the sizes of all arrays must match. More details can be found in [Broadcasting](basics.broadcasting.html#basics-broadcasting).

## Advanced indexing and index tricks[#](#advanced-indexing-and-index-tricks "Link to this heading")

NumPy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, as we saw before, arrays can be indexed by arrays of integers and arrays of booleans.

### Indexing with arrays of indices[#](#indexing-with-arrays-of-indices "Link to this heading")
    
    
    >>> a = np.arange(12)**2  # the first 12 square numbers
    >>> i = np.array([1, 1, 3, 8, 5])  # an array of indices
    >>> a[i]  # the elements of `a` at the positions `i`
    array([ 1,  1,  9, 64, 25])
    >>>
    >>> j = np.array([[3, 4], [9, 7]])  # a bidimensional array of indices
    >>> a[j]  # the same shape as `j`
    array([[ 9, 16],
           [81, 49]])
    

When the indexed array `a` is multidimensional, a single array of indices refers to the first dimension of `a`. The following example shows this behavior by converting an image of labels into a color image using a palette.
    
    
    >>> palette = np.array([[0, 0, 0],         # black
    ...                     [255, 0, 0],       # red
    ...                     [0, 255, 0],       # green
    ...                     [0, 0, 255],       # blue
    ...                     [255, 255, 255]])  # white
    >>> image = np.array([[0, 1, 2, 0],  # each value corresponds to a color in the palette
    ...                   [0, 3, 4, 0]])
    >>> palette[image]  # the (2, 4, 3) color image
    array([[[  0,   0,   0],
            [255,   0,   0],
            [  0, 255,   0],
            [  0,   0,   0]],
    
           [[  0,   0,   0],
            [  0,   0, 255],
            [255, 255, 255],
            [  0,   0,   0]]])
    

We can also give indexes for more than one dimension. The arrays of indices for each dimension must have the same shape.
    
    
    >>> a = np.arange(12).reshape(3, 4)
    >>> a
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>> i = np.array([[0, 1],  # indices for the first dim of `a`
    ...               [1, 2]])
    >>> j = np.array([[2, 1],  # indices for the second dim
    ...               [3, 3]])
    >>>
    >>> a[i, j]  # i and j must have equal shape
    array([[ 2,  5],
           [ 7, 11]])
    >>>
    >>> a[i, 2]
    array([[ 2,  6],
           [ 6, 10]])
    >>>
    >>> a[:, j]
    array([[[ 2,  1],
            [ 3,  3]],
    
           [[ 6,  5],
            [ 7,  7]],
    
           [[10,  9],
            [11, 11]]])
    

In Python, `arr[i, j]` is exactly the same as `arr[(i, j)]`—so we can put `i` and `j` in a `tuple` and then do the indexing with that.
    
    
    >>> l = (i, j)
    >>> # equivalent to a[i, j]
    >>> a[l]
    array([[ 2,  5],
           [ 7, 11]])
    

However, we can not do this by putting `i` and `j` into an array, because this array will be interpreted as indexing the first dimension of `a`.
    
    
    >>> s = np.array([i, j])
    >>> # not what we want
    >>> a[s]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: index 3 is out of bounds for axis 0 with size 3
    >>> # same as `a[i, j]`
    >>> a[tuple(s)]
    array([[ 2,  5],
           [ 7, 11]])
    

Another common use of indexing with arrays is the search of the maximum value of time-dependent series:
    
    
    >>> time = np.linspace(20, 145, 5)  # time scale
    >>> data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
    >>> time
    array([ 20.  ,  51.25,  82.5 , 113.75, 145.  ])
    >>> data
    array([[ 0.        ,  0.84147098,  0.90929743,  0.14112001],
           [-0.7568025 , -0.95892427, -0.2794155 ,  0.6569866 ],
           [ 0.98935825,  0.41211849, -0.54402111, -0.99999021],
           [-0.53657292,  0.42016704,  0.99060736,  0.65028784],
           [-0.28790332, -0.96139749, -0.75098725,  0.14987721]])
    >>> # index of the maxima for each series
    >>> ind = data.argmax(axis=0)
    >>> ind
    array([2, 0, 3, 1])
    >>> # times corresponding to the maxima
    >>> time_max = time[ind]
    >>>
    >>> data_max = data[ind, range(data.shape[1])]  # => data[ind[0], 0], data[ind[1], 1]...
    >>> time_max
    array([ 82.5 ,  20.  , 113.75,  51.25])
    >>> data_max
    array([0.98935825, 0.84147098, 0.99060736, 0.6569866 ])
    >>> np.all(data_max == data.max(axis=0))
    True
    

You can also use indexing with arrays as a target to assign to:
    
    
    >>> a = np.arange(5)
    >>> a
    array([0, 1, 2, 3, 4])
    >>> a[[1, 3, 4]] = 0
    >>> a
    array([0, 0, 2, 0, 0])
    

However, when the list of indices contains repetitions, the assignment is done several times, leaving behind the last value:
    
    
    >>> a = np.arange(5)
    >>> a[[0, 0, 2]] = [1, 2, 3]
    >>> a
    array([2, 1, 3, 3, 4])
    

This is reasonable enough, but watch out if you want to use Python’s `+=` construct, as it may not do what you expect:
    
    
    >>> a = np.arange(5)
    >>> a[[0, 0, 2]] += 1
    >>> a
    array([1, 1, 3, 3, 4])
    

Even though 0 occurs twice in the list of indices, the 0th element is only incremented once. This is because Python requires `a += 1` to be equivalent to `a = a + 1`.

### Indexing with boolean arrays[#](#indexing-with-boolean-arrays "Link to this heading")

When we index arrays with arrays of (integer) indices we are providing the list of indices to pick. With boolean indices the approach is different; we explicitly choose which items in the array we want and which ones we don’t.

The most natural way one can think of for boolean indexing is to use boolean arrays that have _the same shape_ as the original array:
    
    
    >>> a = np.arange(12).reshape(3, 4)
    >>> b = a > 4
    >>> b  # `b` is a boolean with `a`'s shape
    array([[False, False, False, False],
           [False,  True,  True,  True],
           [ True,  True,  True,  True]])
    >>> a[b]  # 1d array with the selected elements
    array([ 5,  6,  7,  8,  9, 10, 11])
    

This property can be very useful in assignments:
    
    
    >>> a[b] = 0  # All elements of `a` higher than 4 become 0
    >>> a
    array([[0, 1, 2, 3],
           [4, 0, 0, 0],
           [0, 0, 0, 0]])
    

You can look at the following example to see how to use boolean indexing to generate an image of the [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set):
    
    
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> def mandelbrot(h, w, maxit=20, r=2):
    ...     """Returns an image of the Mandelbrot fractal of size (h,w)."""
    ...     x = np.linspace(-2.5, 1.5, 4*h+1)
    ...     y = np.linspace(-1.5, 1.5, 3*w+1)
    ...     A, B = np.meshgrid(x, y)
    ...     C = A + B*1j
    ...     z = np.zeros_like(C)
    ...     divtime = maxit + np.zeros(z.shape, dtype=np.int_)
    ...
    ...     for i in range(maxit):
    ...         z = z**2 + C
    ...         diverge = abs(z) > r                    # who is diverging
    ...         div_now = diverge & (divtime == maxit)  # who is diverging now
    ...         divtime[div_now] = i                    # note when
    ...         z[diverge] = r                          # avoid diverging too much
    ...
    ...     return divtime
    >>> plt.clf()
    >>> plt.imshow(mandelbrot(400, 400))
    

![../_images/quickstart-1.png](../_images/quickstart-1.png)

The second way of indexing with booleans is more similar to integer indexing; for each dimension of the array we give a 1D boolean array selecting the slices we want:
    
    
    >>> a = np.arange(12).reshape(3, 4)
    >>> b1 = np.array([False, True, True])         # first dim selection
    >>> b2 = np.array([True, False, True, False])  # second dim selection
    >>>
    >>> a[b1, :]                                   # selecting rows
    array([[ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>>
    >>> a[b1]                                      # same thing
    array([[ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>>
    >>> a[:, b2]                                   # selecting columns
    array([[ 0,  2],
           [ 4,  6],
           [ 8, 10]])
    >>>
    >>> a[b1, b2]                                  # a weird thing to do
    array([ 4, 10])
    

Note that the length of the 1D boolean array must coincide with the length of the dimension (or axis) you want to slice. In the previous example, `b1` has length 3 (the number of _rows_ in `a`), and `b2` (of length 4) is suitable to index the 2nd axis (columns) of `a`.

### The ix_() function[#](#the-ix-function "Link to this heading")

The [`ix_`](../reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_") function can be used to combine different vectors so as to obtain the result for each n-uplet. For example, if you want to compute all the a+b*c for all the triplets taken from each of the vectors a, b and c:
    
    
    >>> a = np.array([2, 3, 4, 5])
    >>> b = np.array([8, 5, 4])
    >>> c = np.array([5, 4, 6, 8, 3])
    >>> ax, bx, cx = np.ix_(a, b, c)
    >>> ax
    array([[[2]],
    
           [[3]],
    
           [[4]],
    
           [[5]]])
    >>> bx
    array([[[8],
            [5],
            [4]]])
    >>> cx
    array([[[5, 4, 6, 8, 3]]])
    >>> ax.shape, bx.shape, cx.shape
    ((4, 1, 1), (1, 3, 1), (1, 1, 5))
    >>> result = ax + bx * cx
    >>> result
    array([[[42, 34, 50, 66, 26],
            [27, 22, 32, 42, 17],
            [22, 18, 26, 34, 14]],
    
           [[43, 35, 51, 67, 27],
            [28, 23, 33, 43, 18],
            [23, 19, 27, 35, 15]],
    
           [[44, 36, 52, 68, 28],
            [29, 24, 34, 44, 19],
            [24, 20, 28, 36, 16]],
    
           [[45, 37, 53, 69, 29],
            [30, 25, 35, 45, 20],
            [25, 21, 29, 37, 17]]])
    >>> result[3, 2, 4]
    17
    >>> a[3] + b[2] * c[4]
    17
    

You could also implement the reduce as follows:
    
    
    >>> def ufunc_reduce(ufct, *vectors):
    ...    vs = np.ix_(*vectors)
    ...    r = ufct.identity
    ...    for v in vs:
    ...        r = ufct(r, v)
    ...    return r
    

and then use it as:
    
    
    >>> ufunc_reduce(np.add, a, b, c)
    array([[[15, 14, 16, 18, 13],
            [12, 11, 13, 15, 10],
            [11, 10, 12, 14,  9]],
    
           [[16, 15, 17, 19, 14],
            [13, 12, 14, 16, 11],
            [12, 11, 13, 15, 10]],
    
           [[17, 16, 18, 20, 15],
            [14, 13, 15, 17, 12],
            [13, 12, 14, 16, 11]],
    
           [[18, 17, 19, 21, 16],
            [15, 14, 16, 18, 13],
            [14, 13, 15, 17, 12]]])
    

The advantage of this version of reduce compared to the normal ufunc.reduce is that it makes use of the [broadcasting rules](#broadcasting-rules) in order to avoid creating a temporary array that needs as much memory as the output array multiplied by the number of vectors.

### Indexing with strings[#](#indexing-with-strings "Link to this heading")

See [Structured arrays](basics.rec.html#structured-arrays).

## Tricks and tips[#](#tricks-and-tips "Link to this heading")

Here we give a list of short and useful tips.

### “Automatic” reshaping[#](#automatic-reshaping "Link to this heading")

To change the dimensions of an array, you can omit one of the sizes which will then be deduced automatically:
    
    
    >>> a = np.arange(30)
    >>> b = a.reshape((2, -1, 3))  # -1 means "whatever is needed"
    >>> b.shape
    (2, 5, 3)
    >>> b
    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8],
            [ 9, 10, 11],
            [12, 13, 14]],
    
           [[15, 16, 17],
            [18, 19, 20],
            [21, 22, 23],
            [24, 25, 26],
            [27, 28, 29]]])
    

### Vector stacking[#](#vector-stacking "Link to this heading")

How do we construct a 2D array from a list of equally-sized row vectors? In MATLAB this is quite easy: if `x` and `y` are two vectors of the same length you only need do `m=[x;y]`. In NumPy this works via the functions `column_stack`, `dstack`, `hstack` and `vstack`, depending on the dimension in which the stacking is to be done. For example:
    
    
    >>> x = np.arange(0, 10, 2)
    >>> y = np.arange(5)
    >>> m = np.vstack([x, y])
    >>> m
    array([[0, 2, 4, 6, 8],
           [0, 1, 2, 3, 4]])
    >>> xy = np.hstack([x, y])
    >>> xy
    array([0, 2, 4, 6, 8, 0, 1, 2, 3, 4])
    

The logic behind those functions in more than two dimensions can be strange.

See also

[NumPy for MATLAB users](numpy-for-matlab-users.html)

### Histograms[#](#histograms "Link to this heading")

The NumPy `histogram` function applied to an array returns a pair of vectors: the histogram of the array and a vector of the bin edges. Beware: `matplotlib` also has a function to build histograms (called `hist`, as in Matlab) that differs from the one in NumPy. The main difference is that `pylab.hist` plots the histogram automatically, while `numpy.histogram` only generates the data.
    
    
    >>> import numpy as np
    >>> rg = np.random.default_rng(1)
    >>> import matplotlib.pyplot as plt
    >>> # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
    >>> mu, sigma = 2, 0.5
    >>> v = rg.normal(mu, sigma, 10000)
    >>> # Plot a normalized histogram with 50 bins
    >>> plt.hist(v, bins=50, density=True)       # matplotlib version (plot)
    (array...)
    >>> # Compute the histogram with numpy and then plot it
    >>> (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
    >>> plt.plot(.5 * (bins[1:] + bins[:-1]), n) 
    

![../_images/quickstart-2.png](../_images/quickstart-2.png)

With Matplotlib >=3.4 you can also use `plt.stairs(n, bins)`.

## Further reading[#](#further-reading "Link to this heading")

  * The [Python tutorial](https://docs.python.org/tutorial/)

  * [NumPy reference](../reference/index.html#reference)

  * [SciPy Tutorial](https://docs.scipy.org/doc/scipy/tutorial/index.html)

  * [SciPy Lecture Notes](https://scipy-lectures.org)

  * A [matlab, R, IDL, NumPy/SciPy dictionary](https://mathesaurus.sourceforge.net/)

  * [tutorial-svd](https://numpy.org/numpy-tutorials/tutorial-svd "\(in  vundefined\)")




[ __ previous What is NumPy? ](whatisnumpy.html "previous page") [ next NumPy: the absolute basics for beginners __](absolute_beginners.html "next page")

__On this page

  * [Prerequisites](#prerequisites)
  * [The basics](#the-basics)
    * [An example](#an-example)
    * [Array creation](#array-creation)
    * [Printing arrays](#printing-arrays)
    * [Basic operations](#basic-operations)
    * [Universal functions](#universal-functions)
    * [Indexing, slicing and iterating](#indexing-slicing-and-iterating)
  * [Shape manipulation](#shape-manipulation)
    * [Changing the shape of an array](#changing-the-shape-of-an-array)
    * [Stacking together different arrays](#stacking-together-different-arrays)
    * [Splitting one array into several smaller ones](#splitting-one-array-into-several-smaller-ones)
  * [Copies and views](#copies-and-views)
    * [No copy at all](#no-copy-at-all)
    * [View or shallow copy](#view-or-shallow-copy)
    * [Deep copy](#deep-copy)
    * [Functions and methods overview](#functions-and-methods-overview)
  * [Less basic](#less-basic)
    * [Broadcasting rules](#broadcasting-rules)
  * [Advanced indexing and index tricks](#advanced-indexing-and-index-tricks)
    * [Indexing with arrays of indices](#indexing-with-arrays-of-indices)
    * [Indexing with boolean arrays](#indexing-with-boolean-arrays)
    * [The ix_() function](#the-ix-function)
    * [Indexing with strings](#indexing-with-strings)
  * [Tricks and tips](#tricks-and-tips)
    * [“Automatic” reshaping](#automatic-reshaping)
    * [Vector stacking](#vector-stacking)
    * [Histograms](#histograms)
  * [Further reading](#further-reading)

---

## NumPy user guide

**Source:** [https://numpy.org/devdocs/user/index.html](https://numpy.org/devdocs/user/index.html)

* [ __](../index.html)
  * NumPy user guide



# NumPy user guide[#](#numpy-user-guide "Link to this heading")

This guide is an overview and explains the important features; details are found in [NumPy reference](../reference/index.html#reference).

Getting started

  * [What is NumPy?](whatisnumpy.html)
  * [Installation](https://numpy.org/install/)
  * [NumPy quickstart](quickstart.html)
  * [NumPy: the absolute basics for beginners](absolute_beginners.html)



Fundamentals and usage

  * [NumPy fundamentals](basics.html)
    * [Array creation](basics.creation.html)
    * [Indexing on `ndarrays`](basics.indexing.html)
    * [I/O with NumPy](basics.io.html)
    * [Data types](basics.types.html)
    * [Broadcasting](basics.broadcasting.html)
    * [Copies and views](basics.copies.html)
    * [Working with Arrays of Strings And Bytes](basics.strings.html)
    * [Structured arrays](basics.rec.html)
    * [Universal functions (`ufunc`) basics](basics.ufuncs.html)



  * [NumPy for MATLAB users](numpy-for-matlab-users.html)
  * [NumPy tutorials](https://numpy.org/numpy-tutorials/)
  * [NumPy how-tos](howtos_index.html)



Advanced usage and interoperability

  * [Using NumPy C-API](c-info.html)
  * [F2PY user guide and reference manual](../f2py/index.html)
  * [Under-the-hood documentation for developers](../dev/underthehood.html)
  * [Interoperability with NumPy](basics.interoperability.html)



[ __ previous NumPy documentation ](../index.html "previous page") [ next What is NumPy? __](whatisnumpy.html "next page")

---

## Indexing on ndarrays

**Source:** [https://numpy.org/devdocs/user/basics.indexing.html](https://numpy.org/devdocs/user/basics.indexing.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Indexing on `ndarrays`



# Indexing on [`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[#](#indexing-on-ndarrays "Link to this heading")

See also

[Indexing routines](../reference/routines.indexing.html#routines-indexing)

[`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") can be indexed using the standard Python `x[obj]` syntax, where _x_ is the array and _obj_ the selection. There are different kinds of indexing available depending on _obj_ : basic indexing, advanced indexing and field access.

Most of the following examples show the use of indexing when referencing data in an array. The examples work just as well when assigning to an array. See [Assigning values to indexed arrays](#assigning-values-to-indexed-arrays) for specific examples and explanations on how assignments work.

Note that in Python, `x[(exp1, exp2, ..., expN)]` is equivalent to `x[exp1, exp2, ..., expN]`; the latter is just syntactic sugar for the former.

## Basic indexing[#](#basic-indexing "Link to this heading")

### Single element indexing[#](#single-element-indexing "Link to this heading")

Single element indexing works exactly like that for other standard Python sequences. It is 0-based, and accepts negative indices for indexing from the end of the array.
    
    
    >>> x = np.arange(10)
    >>> x[2]
    2
    >>> x[-2]
    8
    

It is not necessary to separate each dimension’s index into its own set of square brackets.
    
    
    >>> x = x.reshape((2, 5))  # now x is 2-dimensional
    >>> x[1, 3]
    8
    >>> x[1, -1]
    9
    

Note that if one indexes a multidimensional array with fewer indices than dimensions, one gets a subdimensional array. For example:
    
    
    >>> x[0]
    array([0, 1, 2, 3, 4])
    

That is, each index specified selects the array corresponding to the rest of the dimensions selected. In the above example, choosing 0 means that the remaining dimension of length 5 is being left unspecified, and that what is returned is an array of that dimensionality and size. It must be noted that the returned array is a [view](../glossary.html#term-view), i.e., it is not a copy of the original, but points to the same values in memory as does the original array. In this case, the 1-D array at the first position (0) is returned. So using a single index on the returned array, results in a single element being returned. That is:
    
    
    >>> x[0][2]
    2
    

So note that `x[0, 2] == x[0][2]` though the second case is more inefficient as a new temporary array is created after the first index that is subsequently indexed by 2.

Note

NumPy uses C-order indexing. That means that the last index usually represents the most rapidly changing memory location, unlike Fortran or IDL, where the first index represents the most rapidly changing location in memory. This difference represents a great potential for confusion.

### Slicing and striding[#](#slicing-and-striding "Link to this heading")

Basic slicing extends Python’s basic concept of slicing to N dimensions. Basic slicing occurs when _obj_ is a [`slice`](https://docs.python.org/3/library/functions.html#slice "\(in Python v3.14\)") object (constructed by `start:stop:step` notation inside of brackets), an integer, or a tuple of slice objects and integers. [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "\(in Python v3.14\)") and [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis") objects can be interspersed with these as well.

The simplest case of indexing with _N_ integers returns an [array scalar](../reference/arrays.scalars.html#arrays-scalars) representing the corresponding item. As in Python, all indices are zero-based: for the _i_ -th index \\(n_i\\), the valid range is \\(0 \le n_i < d_i\\) where \\(d_i\\) is the _i_ -th element of the shape of the array. Negative indices are interpreted as counting from the end of the array (_i.e._ , if \\(n_i < 0\\), it means \\(n_i + d_i\\)).

All arrays generated by basic slicing are always [views](../glossary.html#term-view) of the original array.

Note

NumPy slicing creates a [view](../glossary.html#term-view) instead of a copy as in the case of built-in Python sequences such as string, tuple and list. Care must be taken when extracting a small portion from a large array which becomes useless after the extraction, because the small portion extracted contains a reference to the large original array whose memory will not be released until all arrays derived from it are garbage-collected. In such cases an explicit `copy()` is recommended.

The standard rules of sequence slicing apply to basic slicing on a per-dimension basis (including using a step index). Some useful concepts to remember include:

  * The basic slice syntax is `i:j:k` where _i_ is the starting index, _j_ is the stopping index, and _k_ is the step (\\(k\neq0\\)). This selects the _m_ elements (in the corresponding dimension) with index values _i_ , _i + k_ , …, _i + (m - 1) k_ where \\(m = q + (r\neq0)\\) and _q_ and _r_ are the quotient and remainder obtained by dividing _j - i_ by _k_ : _j - i = q k + r_ , so that _i + (m - 1) k < j_. For example:
        
        >>> x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        >>> x[1:7:2]
        array([1, 3, 5])
        

  * Negative _i_ and _j_ are interpreted as _n + i_ and _n + j_ where _n_ is the number of elements in the corresponding dimension. Negative _k_ makes stepping go towards smaller indices. From the above example:
        
        >>> x[-2:10]
        array([8, 9])
        >>> x[-3:3:-1]
        array([7, 6, 5, 4])
        

  * Assume _n_ is the number of elements in the dimension being sliced. Then, if _i_ is not given it defaults to 0 for _k > 0_ and _n - 1_ for _k < 0_ . If _j_ is not given it defaults to _n_ for _k > 0_ and _-n-1_ for _k < 0_ . If _k_ is not given it defaults to 1. Note that `::` is the same as `:` and means select all indices along this axis. From the above example:
        
        >>> x[5:]
        array([5, 6, 7, 8, 9])
        

  * If the number of objects in the selection tuple is less than _N_ , then `:` is assumed for any subsequent dimensions. For example:
        
        >>> x = np.array([[[1],[2],[3]], [[4],[5],[6]]])
        >>> x.shape
        (2, 3, 1)
        >>> x[1:2]
        array([[[4],
                [5],
                [6]]])
        

  * An integer, _i_ , returns the same values as `i:i+1` **except** the dimensionality of the returned object is reduced by 1\. In particular, a selection tuple with the _p_ -th element an integer (and all other entries `:`) returns the corresponding sub-array with dimension _N - 1_. If _N = 1_ then the returned object is an array scalar. These objects are explained in [Scalars](../reference/arrays.scalars.html#arrays-scalars).

  * If the selection tuple has all entries `:` except the _p_ -th entry which is a slice object `i:j:k`, then the returned array has dimension _N_ formed by stacking, along the _p_ -th axis, the sub-arrays returned by integer indexing of elements _i_ , _i+k_ , …, _i + (m - 1) k < j_.

  * Basic slicing with more than one non-`:` entry in the slicing tuple, acts like repeated application of slicing using a single non-`:` entry, where the non-`:` entries are successively taken (with all other non-`:` entries replaced by `:`). Thus, `x[ind1, ..., ind2,:]` acts like `x[ind1][..., ind2, :]` under basic slicing.

Warning

The above is **not** true for advanced indexing.

  * You may use slicing to set values in the array, but (unlike lists) you can never grow the array. The size of the value to be set in `x[obj] = value` must be (broadcastable to) the same shape as `x[obj]`.

  * A slicing tuple can always be constructed as _obj_ and used in the `x[obj]` notation. Slice objects can be used in the construction in place of the `[start:stop:step]` notation. For example, `x[1:10:5, ::-1]` can also be implemented as `obj = (slice(1, 10, 5), slice(None, None, -1)); x[obj]` . This can be useful for constructing generic code that works on arrays of arbitrary dimensions. See [Dealing with variable numbers of indices within programs](#dealing-with-variable-indices) for more information.




### Dimensional indexing tools[#](#dimensional-indexing-tools "Link to this heading")

There are some tools to facilitate the easy matching of array shapes with expressions and in assignments.

[`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "\(in Python v3.14\)") expands to the number of `:` objects needed for the selection tuple to index all dimensions. In most cases, this means that the length of the expanded selection tuple is `x.ndim`. There may only be a single ellipsis present. From the above example:
    
    
    >>> x[..., 0]
    array([[1, 2, 3],
          [4, 5, 6]])
    

This is equivalent to:
    
    
    >>> x[:, :, 0]
    array([[1, 2, 3],
          [4, 5, 6]])
    

Each [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis") object in the selection tuple serves to expand the dimensions of the resulting selection by one unit-length dimension. The added dimension is the position of the [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis") object in the selection tuple. [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis") is an alias for `None`, and `None` can be used in place of this with the same result. From the above example:
    
    
    >>> x[:, np.newaxis, :, :].shape
    (2, 1, 3, 1)
    >>> x[:, None, :, :].shape
    (2, 1, 3, 1)
    

This can be handy to combine two arrays in a way that otherwise would require explicit reshaping operations. For example:
    
    
    >>> x = np.arange(5)
    >>> x[:, np.newaxis] + x[np.newaxis, :]
    array([[0, 1, 2, 3, 4],
          [1, 2, 3, 4, 5],
          [2, 3, 4, 5, 6],
          [3, 4, 5, 6, 7],
          [4, 5, 6, 7, 8]])
    

## Advanced indexing[#](#advanced-indexing "Link to this heading")

Advanced indexing is triggered when the selection object, _obj_ , is a non-tuple sequence object, an [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") (of data type integer or bool), or a tuple with at least one sequence object or ndarray (of data type integer or bool). There are two types of advanced indexing: integer and Boolean.

Advanced indexing always returns a _copy_ of the data (contrast with basic slicing that returns a [view](../glossary.html#term-view)).

Warning

The definition of advanced indexing means that `x[(1, 2, 3),]` is fundamentally different than `x[(1, 2, 3)]`. The latter is equivalent to `x[1, 2, 3]` which will trigger basic selection while the former will trigger advanced indexing. Be sure to understand why this occurs.

### Integer array indexing[#](#integer-array-indexing "Link to this heading")

Integer array indexing allows selection of arbitrary items in the array based on their _N_ -dimensional index. Each integer array represents a number of indices into that dimension.

Negative values are permitted in the index arrays and work as they do with single indices or slices:
    
    
    >>> x = np.arange(10, 1, -1)
    >>> x
    array([10,  9,  8,  7,  6,  5,  4,  3,  2])
    >>> x[np.array([3, 3, 1, 8])]
    array([7, 7, 9, 2])
    >>> x[np.array([3, 3, -3, 8])]
    array([7, 7, 4, 2])
    

If the index values are out of bounds then an `IndexError` is thrown:
    
    
    >>> x = np.array([[1, 2], [3, 4], [5, 6]])
    >>> x[np.array([1, -1])]
    array([[3, 4],
          [5, 6]])
    >>> x[np.array([3, 4])]
    Traceback (most recent call last):
      ...
    IndexError: index 3 is out of bounds for axis 0 with size 3
    

When the index consists of as many integer arrays as dimensions of the array being indexed, the indexing is straightforward, but different from slicing.

Advanced indices always are [broadcast](basics.broadcasting.html#basics-broadcasting) and iterated as _one_ :
    
    
    result[i_1, ..., i_M] == x[ind_1[i_1, ..., i_M], ind_2[i_1, ..., i_M],
                               ..., ind_N[i_1, ..., i_M]]
    

Note that the resulting shape is identical to the (broadcast) indexing array shapes `ind_1, ..., ind_N`. If the indices cannot be broadcast to the same shape, an exception `IndexError: shape mismatch: indexing arrays could not be broadcast together with shapes...` is raised.

Indexing with multidimensional index arrays tend to be more unusual uses, but they are permitted, and they are useful for some problems. We’ll start with the simplest multidimensional case:
    
    
    >>> y = np.arange(35).reshape(5, 7)
    >>> y
    array([[ 0,  1,  2,  3,  4,  5,  6],
           [ 7,  8,  9, 10, 11, 12, 13],
           [14, 15, 16, 17, 18, 19, 20],
           [21, 22, 23, 24, 25, 26, 27],
           [28, 29, 30, 31, 32, 33, 34]])
    >>> y[np.array([0, 2, 4]), np.array([0, 1, 2])]
    array([ 0, 15, 30])
    

In this case, if the index arrays have a matching shape, and there is an index array for each dimension of the array being indexed, the resultant array has the same shape as the index arrays, and the values correspond to the index set for each position in the index arrays. In this example, the first index value is 0 for both index arrays, and thus the first value of the resultant array is `y[0, 0]`. The next value is `y[2, 1]`, and the last is `y[4, 2]`.

If the index arrays do not have the same shape, there is an attempt to broadcast them to the same shape. If they cannot be broadcast to the same shape, an exception is raised:
    
    
    >>> y[np.array([0, 2, 4]), np.array([0, 1])]
    Traceback (most recent call last):
      ...
    IndexError: shape mismatch: indexing arrays could not be broadcast
    together with shapes (3,) (2,)
    

The broadcasting mechanism permits index arrays to be combined with scalars for other indices. The effect is that the scalar value is used for all the corresponding values of the index arrays:
    
    
    >>> y[np.array([0, 2, 4]), 1]
    array([ 1, 15, 29])
    

Jumping to the next level of complexity, it is possible to only partially index an array with index arrays. It takes a bit of thought to understand what happens in such cases. For example if we just use one index array with y:
    
    
    >>> y[np.array([0, 2, 4])]
    array([[ 0,  1,  2,  3,  4,  5,  6],
           [14, 15, 16, 17, 18, 19, 20],
           [28, 29, 30, 31, 32, 33, 34]])
    

It results in the construction of a new array where each value of the index array selects one row from the array being indexed and the resultant array has the resulting shape (number of index elements, size of row).

In general, the shape of the resultant array will be the concatenation of the shape of the index array (or the shape that all the index arrays were broadcast to) with the shape of any unused dimensions (those not indexed) in the array being indexed.

Example

From each row, a specific element should be selected. The row index is just `[0, 1, 2]` and the column index specifies the element to choose for the corresponding row, here `[0, 1, 0]`. Using both together the task can be solved using advanced indexing:
    
    
    >>> x = np.array([[1, 2], [3, 4], [5, 6]])
    >>> x[[0, 1, 2], [0, 1, 0]]
    array([1, 4, 5])
    

To achieve a behaviour similar to the basic slicing above, broadcasting can be used. The function [`ix_`](../reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_") can help with this broadcasting. This is best understood with an example.

Example

From a 4x3 array the corner elements should be selected using advanced indexing. Thus all elements for which the column is one of `[0, 2]` and the row is one of `[0, 3]` need to be selected. To use advanced indexing one needs to select all elements _explicitly_. Using the method explained previously one could write:
    
    
    >>> x = np.array([[ 0,  1,  2],
    ...               [ 3,  4,  5],
    ...               [ 6,  7,  8],
    ...               [ 9, 10, 11]])
    >>> rows = np.array([[0, 0],
    ...                  [3, 3]], dtype=np.intp)
    >>> columns = np.array([[0, 2],
    ...                     [0, 2]], dtype=np.intp)
    >>> x[rows, columns]
    array([[ 0,  2],
           [ 9, 11]])
    

However, since the indexing arrays above just repeat themselves, broadcasting can be used (compare operations such as `rows[:, np.newaxis] + columns`) to simplify this:
    
    
    >>> rows = np.array([0, 3], dtype=np.intp)
    >>> columns = np.array([0, 2], dtype=np.intp)
    >>> rows[:, np.newaxis]
    array([[0],
           [3]])
    >>> x[rows[:, np.newaxis], columns]
    array([[ 0,  2],
           [ 9, 11]])
    

This broadcasting can also be achieved using the function [`ix_`](../reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_"):
    
    
    >>> x[np.ix_(rows, columns)]
    array([[ 0,  2],
           [ 9, 11]])
    

Note that without the `np.ix_` call, only the diagonal elements would be selected:
    
    
    >>> x[rows, columns]
    array([ 0, 11])
    

This difference is the most important thing to remember about indexing with multiple advanced indices.

Example

A real-life example of where advanced indexing may be useful is for a color lookup table where we want to map the values of an image into RGB triples for display. The lookup table could have a shape (nlookup, 3). Indexing such an array with an image with shape (ny, nx) with dtype=np.uint8 (or any integer type so long as values are with the bounds of the lookup table) will result in an array of shape (ny, nx, 3) where a triple of RGB values is associated with each pixel location.

### Boolean array indexing[#](#boolean-array-indexing "Link to this heading")

This advanced indexing occurs when _obj_ is an array object of Boolean type, such as may be returned from comparison operators. A single boolean index array is practically identical to `x[obj.nonzero()]` where, as described above, [`obj.nonzero()`](../reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero") returns a tuple (of length [`obj.ndim`](../reference/generated/numpy.ndarray.ndim.html#numpy.ndarray.ndim "numpy.ndarray.ndim")) of integer index arrays showing the [`True`](https://docs.python.org/3/library/constants.html#True "\(in Python v3.14\)") elements of _obj_. However, it is faster when `obj.shape == x.shape`.

If `obj.ndim == x.ndim`, `x[obj]` returns a 1-dimensional array filled with the elements of _x_ corresponding to the [`True`](https://docs.python.org/3/library/constants.html#True "\(in Python v3.14\)") values of _obj_. The search order will be [row-major](../glossary.html#term-row-major), C-style. An index error will be raised if the shape of _obj_ does not match the corresponding dimensions of _x_ , regardless of whether those values are [`True`](https://docs.python.org/3/library/constants.html#True "\(in Python v3.14\)") or [`False`](https://docs.python.org/3/library/constants.html#False "\(in Python v3.14\)").

A common use case for this is filtering for desired element values. For example, one may wish to select all entries from an array which are not [`numpy.nan`](../reference/constants.html#numpy.nan "numpy.nan"):
    
    
    >>> x = np.array([[1., 2.], [np.nan, 3.], [np.nan, np.nan]])
    >>> x[~np.isnan(x)]
    array([1., 2., 3.])
    

Or wish to add a constant to all negative elements:
    
    
    >>> x = np.array([1., -1., -2., 3])
    >>> x[x < 0] += 20
    >>> x
    array([ 1., 19., 18., 3.])
    

In general if an index includes a Boolean array, the result will be identical to inserting `obj.nonzero()` into the same position and using the integer array indexing mechanism described above. `x[ind_1, boolean_array, ind_2]` is equivalent to `x[(ind_1,) + boolean_array.nonzero() + (ind_2,)]`.

If there is only one Boolean array and no integer indexing array present, this is straightforward. Care must only be taken to make sure that the boolean index has _exactly_ as many dimensions as it is supposed to work with.

In general, when the boolean array has fewer dimensions than the array being indexed, this is equivalent to `x[b, ...]`, which means x is indexed by b followed by as many `:` as are needed to fill out the rank of x. Thus the shape of the result is one dimension containing the number of True elements of the boolean array, followed by the remaining dimensions of the array being indexed:
    
    
    >>> x = np.arange(35).reshape(5, 7)
    >>> b = x > 20
    >>> b[:, 5]
    array([False, False, False,  True,  True])
    >>> x[b[:, 5]]
    array([[21, 22, 23, 24, 25, 26, 27],
          [28, 29, 30, 31, 32, 33, 34]])
    

Here the 4th and 5th rows are selected from the indexed array and combined to make a 2-D array.

Example

From an array, select all rows which sum up to less or equal two:
    
    
    >>> x = np.array([[0, 1], [1, 1], [2, 2]])
    >>> rowsum = x.sum(-1)
    >>> x[rowsum <= 2, :]
    array([[0, 1],
           [1, 1]])
    

Combining multiple Boolean indexing arrays or a Boolean with an integer indexing array can best be understood with the [`obj.nonzero()`](../reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero") analogy. The function [`ix_`](../reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_") also supports boolean arrays and will work without any surprises.

Example

Use boolean indexing to select all rows adding up to an even number. At the same time columns 0 and 2 should be selected with an advanced integer index. Using the [`ix_`](../reference/generated/numpy.ix_.html#numpy.ix_ "numpy.ix_") function this can be done with:
    
    
    >>> x = np.array([[ 0,  1,  2],
    ...               [ 3,  4,  5],
    ...               [ 6,  7,  8],
    ...               [ 9, 10, 11]])
    >>> rows = (x.sum(-1) % 2) == 0
    >>> rows
    array([False,  True, False,  True])
    >>> columns = [0, 2]
    >>> x[np.ix_(rows, columns)]
    array([[ 3,  5],
           [ 9, 11]])
    

Without the `np.ix_` call, only the diagonal elements would be selected.

Or without `np.ix_` (compare the integer array examples):
    
    
    >>> rows = rows.nonzero()[0]
    >>> x[rows[:, np.newaxis], columns]
    array([[ 3,  5],
           [ 9, 11]])
    

Example

Use a 2-D boolean array of shape (2, 3) with four True elements to select rows from a 3-D array of shape (2, 3, 5) results in a 2-D result of shape (4, 5):
    
    
    >>> x = np.arange(30).reshape(2, 3, 5)
    >>> x
    array([[[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]],
          [[15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29]]])
    >>> b = np.array([[True, True, False], [False, True, True]])
    >>> x[b]
    array([[ 0,  1,  2,  3,  4],
          [ 5,  6,  7,  8,  9],
          [20, 21, 22, 23, 24],
          [25, 26, 27, 28, 29]])
    

### Combining advanced and basic indexing[#](#combining-advanced-and-basic-indexing "Link to this heading")

When there is at least one slice (`:`), ellipsis (`...`) or [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis") in the index (or the array has more dimensions than there are advanced indices), then the behaviour can be more complicated. It is like concatenating the indexing result for each advanced index element.

In the simplest case, there is only a _single_ advanced index combined with a slice. For example:
    
    
    >>> y = np.arange(35).reshape(5,7)
    >>> y[np.array([0, 2, 4]), 1:3]
    array([[ 1,  2],
           [15, 16],
           [29, 30]])
    

In effect, the slice and index array operation are independent. The slice operation extracts columns with index 1 and 2, (i.e. the 2nd and 3rd columns), followed by the index array operation which extracts rows with index 0, 2 and 4 (i.e the first, third and fifth rows). This is equivalent to:
    
    
    >>> y[:, 1:3][np.array([0, 2, 4]), :]
    array([[ 1,  2],
           [15, 16],
           [29, 30]])
    

A single advanced index can, for example, replace a slice and the result array will be the same. However, it is a copy and may have a different memory layout. A slice is preferable when it is possible. For example:
    
    
    >>> x = np.array([[ 0,  1,  2],
    ...               [ 3,  4,  5],
    ...               [ 6,  7,  8],
    ...               [ 9, 10, 11]])
    >>> x[1:2, 1:3]
    array([[4, 5]])
    >>> x[1:2, [1, 2]]
    array([[4, 5]])
    

The easiest way to understand a combination of _multiple_ advanced indices may be to think in terms of the resulting shape. There are two parts to the indexing operation, the subspace defined by the basic indexing (excluding integers) and the subspace from the advanced indexing part. Two cases of index combination need to be distinguished:

  * The advanced indices are separated by a slice, [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "\(in Python v3.14\)") or [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis"). For example `x[arr1, :, arr2]`.

  * The advanced indices are all next to each other. For example `x[..., arr1, arr2, :]` but _not_ `x[arr1, :, 1]` since `1` is an advanced index in this regard.




In the first case, the dimensions resulting from the advanced indexing operation come first in the result array, and the subspace dimensions after that. In the second case, the dimensions from the advanced indexing operations are inserted into the result array at the same spot as they were in the initial array (the latter logic is what makes simple advanced indexing behave just like slicing).

Example

Suppose `x.shape` is (10, 20, 30) and `ind` is a (2, 5, 2)-shaped indexing [`intp`](../reference/arrays.scalars.html#numpy.intp "numpy.intp") array, then `result = x[..., ind, :]` has shape (10, 2, 5, 2, 30) because the (20,)-shaped subspace has been replaced with a (2, 5, 2)-shaped broadcasted indexing subspace. If we let _i, j, k_ loop over the (2, 5, 2)-shaped subspace then `result[..., i, j, k, :] = x[..., ind[i, j, k], :]`. This example produces the same result as [`x.take(ind, axis=-2)`](../reference/generated/numpy.ndarray.take.html#numpy.ndarray.take "numpy.ndarray.take").

Example

Let `x.shape` be (10, 20, 30, 40, 50) and suppose `ind_1` and `ind_2` can be broadcast to the shape (2, 3, 4). Then `x[:, ind_1, ind_2]` has shape (10, 2, 3, 4, 40, 50) because the (20, 30)-shaped subspace from X has been replaced with the (2, 3, 4) subspace from the indices. However, `x[:, ind_1, :, ind_2]` has shape (2, 3, 4, 10, 30, 50) because there is no unambiguous place to drop in the indexing subspace, thus it is tacked-on to the beginning. It is always possible to use [`.transpose()`](../reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose") to move the subspace anywhere desired. Note that this example cannot be replicated using [`take`](../reference/generated/numpy.take.html#numpy.take "numpy.take").

Example

Slicing can be combined with broadcasted boolean indices:
    
    
    >>> x = np.arange(35).reshape(5, 7)
    >>> b = x > 20
    >>> b
    array([[False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False],
          [False, False, False, False, False, False, False],
          [ True,  True,  True,  True,  True,  True,  True],
          [ True,  True,  True,  True,  True,  True,  True]])
    >>> x[b[:, 5], 1:3]
    array([[22, 23],
          [29, 30]])
    

## Field access[#](#field-access "Link to this heading")

See also

[Structured arrays](basics.rec.html#structured-arrays)

If the [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") object is a structured array the [fields](../glossary.html#term-field) of the array can be accessed by indexing the array with strings, dictionary-like.

Indexing `x['field-name']` returns a new [view](../glossary.html#term-view) to the array, which is of the same shape as _x_ (except when the field is a sub-array) but of data type `x.dtype['field-name']` and contains only the part of the data in the specified field. Also, [record array](../reference/arrays.classes.html#arrays-classes-rec) scalars can be “indexed” this way.

Indexing into a structured array can also be done with a list of field names, e.g. `x[['field-name1', 'field-name2']]`. As of NumPy 1.16, this returns a view containing only those fields. In older versions of NumPy, it returned a copy. See the user guide section on [Structured arrays](basics.rec.html#structured-arrays) for more information on multifield indexing.

If the accessed field is a sub-array, the dimensions of the sub-array are appended to the shape of the result. For example:
    
    
    >>> x = np.zeros((2, 2), dtype=[('a', np.int32), ('b', np.float64, (3, 3))])
    >>> x['a'].shape
    (2, 2)
    >>> x['a'].dtype
    dtype('int32')
    >>> x['b'].shape
    (2, 2, 3, 3)
    >>> x['b'].dtype
    dtype('float64')
    

## Flat iterator indexing[#](#flat-iterator-indexing "Link to this heading")

[`x.flat`](../reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat") returns an iterator that will iterate over the entire array (in C-contiguous style with the last index varying the fastest). This iterator object can also be indexed using basic slicing or advanced indexing as long as the selection object is not a tuple. This should be clear from the fact that [`x.flat`](../reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat "numpy.ndarray.flat") is a 1-dimensional view. It can be used for integer indexing with 1-dimensional C-style-flat indices. The shape of any returned array is therefore the shape of the integer indexing object.

## Assigning values to indexed arrays[#](#assigning-values-to-indexed-arrays "Link to this heading")

As mentioned, one can select a subset of an array to assign to using a single index, slices, and index and mask arrays. The value being assigned to the indexed array must be shape consistent (the same shape or broadcastable to the shape the index produces). For example, it is permitted to assign a constant to a slice:
    
    
    >>> x = np.arange(10)
    >>> x[2:7] = 1
    

or an array of the right size:
    
    
    >>> x[2:7] = np.arange(5)
    

Note that assignments may result in changes if assigning higher types to lower types (like floats to ints) or even exceptions (assigning complex to floats or ints):
    
    
    >>> x[1] = 1.2
    >>> x[1]
    1
    >>> x[1] = 1.2j  
    Traceback (most recent call last):
      ...
    TypeError: can't convert complex to int
    

Unlike some of the references (such as array and mask indices) assignments are always made to the original data in the array (indeed, nothing else would make sense!). Note though, that some actions may not work as one may naively expect. This particular example is often surprising to people:
    
    
    >>> x = np.arange(0, 50, 10)
    >>> x
    array([ 0, 10, 20, 30, 40])
    >>> x[np.array([1, 1, 3, 1])] += 1
    >>> x
    array([ 0, 11, 20, 31, 40])
    

Where people expect that the 1st location will be incremented by 3. In fact, it will only be incremented by 1. The reason is that a new array is extracted from the original (as a temporary) containing the values at 1, 1, 3, 1, then the value 1 is added to the temporary, and then the temporary is assigned back to the original array. Thus the value of the array at `x[1] + 1` is assigned to `x[1]` three times, rather than being incremented 3 times.

## Dealing with variable numbers of indices within programs[#](#dealing-with-variable-numbers-of-indices-within-programs "Link to this heading")

The indexing syntax is very powerful but limiting when dealing with a variable number of indices. For example, if you want to write a function that can handle arguments with various numbers of dimensions without having to write special case code for each number of possible dimensions, how can that be done? If one supplies to the index a tuple, the tuple will be interpreted as a list of indices. For example:
    
    
    >>> z = np.arange(81).reshape(3, 3, 3, 3)
    >>> indices = (1, 1, 1, 1)
    >>> z[indices]
    40
    

So one can use code to construct tuples of any number of indices and then use these within an index.

Slices can be specified within programs by using the slice() function in Python. For example:
    
    
    >>> indices = (1, 1, 1, slice(0, 2))  # same as [1, 1, 1, 0:2]
    >>> z[indices]
    array([39, 40])
    

Likewise, ellipsis can be specified by code by using the Ellipsis object:
    
    
    >>> indices = (1, Ellipsis, 1)  # same as [1, ..., 1]
    >>> z[indices]
    array([[28, 31, 34],
           [37, 40, 43],
           [46, 49, 52]])
    

For this reason, it is possible to use the output from the [`np.nonzero()`](../reference/generated/numpy.ndarray.nonzero.html#numpy.ndarray.nonzero "numpy.ndarray.nonzero") function directly as an index since it always returns a tuple of index arrays.

Because of the special treatment of tuples, they are not automatically converted to an array as a list would be. As an example:
    
    
    >>> z[[1, 1, 1, 1]]  # produces a large array
    array([[[[27, 28, 29],
             [30, 31, 32], ...
    >>> z[(1, 1, 1, 1)]  # returns a single value
    40
    

## Detailed notes[#](#detailed-notes "Link to this heading")

These are some detailed notes, which are not of importance for day to day indexing (in no particular order):

  * The native NumPy indexing type is `intp` and may differ from the default integer array type. `intp` is the smallest data type sufficient to safely index any array; for advanced indexing it may be faster than other types.

  * For advanced assignments, there is in general no guarantee for the iteration order. This means that if an element is set more than once, it is not possible to predict the final result.

  * An empty (tuple) index is a full scalar index into a zero-dimensional array. `x[()]` returns a _scalar_ if `x` is zero-dimensional and a view otherwise. On the other hand, `x[...]` always returns a view.

  * If a zero-dimensional array is present in the index _and_ it is a full integer index the result will be a _scalar_ and not a zero-dimensional array. (Advanced indexing is not triggered.)

  * When an ellipsis (`...`) is present but has no size (i.e. replaces zero `:`) the result will still always be an array. A view if no advanced index is present, otherwise a copy.

  * The `nonzero` equivalence for Boolean arrays does not hold for zero dimensional boolean arrays.

  * When the result of an advanced indexing operation has no elements but an individual index is out of bounds, whether or not an `IndexError` is raised is undefined (e.g. `x[[], [123]]` with `123` being out of bounds).

  * When a _casting_ error occurs during assignment (for example updating a numerical array using a sequence of strings), the array being assigned to may end up in an unpredictable partially updated state. However, if any other error (such as an out of bounds index) occurs, the array will remain unchanged.

  * The memory layout of an advanced indexing result is optimized for each indexing operation and no particular memory order can be assumed.

  * When using a subclass (especially one which manipulates its shape), the default `ndarray.__setitem__` behaviour will call `__getitem__` for _basic_ indexing but not for _advanced_ indexing. For such a subclass it may be preferable to call `ndarray.__setitem__` with a _base class_ ndarray view on the data. This _must_ be done if the subclasses `__getitem__` does not return views.




[ __ previous Array creation ](basics.creation.html "previous page") [ next I/O with NumPy __](basics.io.html "next page")

__On this page

  * [Basic indexing](#basic-indexing)
    * [Single element indexing](#single-element-indexing)
    * [Slicing and striding](#slicing-and-striding)
    * [Dimensional indexing tools](#dimensional-indexing-tools)
  * [Advanced indexing](#advanced-indexing)
    * [Integer array indexing](#integer-array-indexing)
    * [Boolean array indexing](#boolean-array-indexing)
    * [Combining advanced and basic indexing](#combining-advanced-and-basic-indexing)
  * [Field access](#field-access)
  * [Flat iterator indexing](#flat-iterator-indexing)
  * [Assigning values to indexed arrays](#assigning-values-to-indexed-arrays)
  * [Dealing with variable numbers of indices within programs](#dealing-with-variable-numbers-of-indices-within-programs)
  * [Detailed notes](#detailed-notes)

---

## Copies and views

**Source:** [https://numpy.org/devdocs/user/basics.copies.html](https://numpy.org/devdocs/user/basics.copies.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Copies and views



# Copies and views[#](#copies-and-views "Link to this heading")

When operating on NumPy arrays, it is possible to access the internal data buffer directly using a [view](#view) without copying data around. This ensures good performance but can also cause unwanted problems if the user is not aware of how this works. Hence, it is important to know the difference between these two terms and to know which operations return copies and which return views.

The NumPy array is a data structure consisting of two parts: the [contiguous](../glossary.html#term-contiguous) data buffer with the actual data elements and the metadata that contains information about the data buffer. The metadata includes data type, strides, and other important information that helps manipulate the [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") easily. See the [Internal organization of NumPy arrays](../dev/internals.html#numpy-internals) section for a detailed look.

## View[#](#view "Link to this heading")

It is possible to access the array differently by just changing certain metadata like [stride](../glossary.html#term-stride) and [dtype](../glossary.html#term-dtype) without changing the data buffer. This creates a new way of looking at the data and these new arrays are called views. The data buffer remains the same, so any changes made to a view reflects in the original copy. A view can be forced through the [`ndarray.view`](../reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view") method.

## Copy[#](#copy "Link to this heading")

When a new array is created by duplicating the data buffer as well as the metadata, it is called a copy. Changes made to the copy do not reflect on the original array. Making a copy is slower and memory-consuming but sometimes necessary. A copy can be forced by using [`ndarray.copy`](../reference/generated/numpy.ndarray.copy.html#numpy.ndarray.copy "numpy.ndarray.copy").

## Indexing operations[#](#indexing-operations "Link to this heading")

See also

[Indexing on ndarrays](basics.indexing.html#basics-indexing)

Views are created when elements can be addressed with offsets and strides in the original array. Hence, basic indexing always creates views. For example:
    
    
    >>> import numpy as np
    >>> x = np.arange(10)
    >>> x
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> y = x[1:3]  # creates a view
    >>> y
    array([1, 2])
    >>> x[1:3] = [10, 11]
    >>> x
    array([ 0, 10, 11,  3,  4,  5,  6,  7,  8,  9])
    >>> y
    array([10, 11])
    

Here, `y` gets changed when `x` is changed because it is a view.

[Advanced indexing](basics.indexing.html#advanced-indexing), on the other hand, always creates copies. For example:
    
    
    >>> import numpy as np
    >>> x = np.arange(9).reshape(3, 3)
    >>> x
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    >>> y = x[[1, 2]]
    >>> y
    array([[3, 4, 5],
           [6, 7, 8]])
    >>> y.base is None
    True
    

Here, `y` is a copy, as signified by the [`base`](../reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base") attribute. We can also confirm this by assigning new values to `x[[1, 2]]` which in turn will not affect `y` at all:
    
    
    >>> x[[1, 2]] = [[10, 11, 12], [13, 14, 15]]
    >>> x
    array([[ 0,  1,  2],
           [10, 11, 12],
           [13, 14, 15]])
    >>> y
    array([[3, 4, 5],
           [6, 7, 8]])
    

It must be noted here that during the assignment of `x[[1, 2]]` no view or copy is created as the assignment happens in-place.

## Other operations[#](#other-operations "Link to this heading")

The [`numpy.reshape`](../reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape") function creates a view where possible or a copy otherwise. In most cases, the strides can be modified to reshape the array with a view. However, in some cases where the array becomes non-contiguous (perhaps after a [`ndarray.transpose`](../reference/generated/numpy.ndarray.transpose.html#numpy.ndarray.transpose "numpy.ndarray.transpose") operation), the reshaping cannot be done by modifying strides and requires a copy.

Taking the example of another operation, [`numpy.ravel`](../reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel") returns a contiguous flattened view of the array wherever possible. On the other hand, [`ndarray.flatten`](../reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten") always returns a flattened copy of the array. However, to guarantee a view in most cases, `x.reshape(-1)` may be preferable.

## How to tell if the array is a view or a copy[#](#how-to-tell-if-the-array-is-a-view-or-a-copy "Link to this heading")

The [`base`](../reference/generated/numpy.ndarray.base.html#numpy.ndarray.base "numpy.ndarray.base") attribute of the ndarray makes it easy to tell if an array is a view or a copy. The base attribute of a view returns the original array while it returns `None` for a copy.
    
    
    >>> import numpy as np
    >>> x = np.arange(9)
    >>> x
    array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    >>> y = x.reshape(3, 3)
    >>> y
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    >>> y.base  # .reshape() creates a view
    array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    >>> z = y[[2, 1]]
    >>> z
    array([[6, 7, 8],
           [3, 4, 5]])
    >>> z.base is None  # advanced indexing creates a copy
    True
    

Note that the `base` attribute should not be used to determine if an ndarray object is _new_ ; only if it is a view or a copy of another ndarray.

[ __ previous Broadcasting ](basics.broadcasting.html "previous page") [ next Working with Arrays of Strings And Bytes __](basics.strings.html "next page")

__On this page

  * [View](#view)
  * [Copy](#copy)
  * [Indexing operations](#indexing-operations)
  * [Other operations](#other-operations)
  * [How to tell if the array is a view or a copy](#how-to-tell-if-the-array-is-a-view-or-a-copy)

---

## Broadcasting

**Source:** [https://numpy.org/devdocs/user/basics.broadcasting.html](https://numpy.org/devdocs/user/basics.broadcasting.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Broadcasting



# Broadcasting[#](#broadcasting "Link to this heading")

See also

[`numpy.broadcast`](../reference/generated/numpy.broadcast.html#numpy.broadcast "numpy.broadcast")

The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have compatible shapes. Broadcasting provides a means of vectorizing array operations so that looping occurs in C instead of Python. It does this without making needless copies of data and usually leads to efficient algorithm implementations. There are, however, cases where broadcasting is a bad idea because it leads to inefficient use of memory that slows computation.

NumPy operations are usually done on pairs of arrays on an element-by-element basis. In the simplest case, the two arrays must have exactly the same shape, as in the following example:
    
    
    >>> import numpy as np
    >>> a = np.array([1.0, 2.0, 3.0])
    >>> b = np.array([2.0, 2.0, 2.0])
    >>> a * b
    array([2.,  4.,  6.])
    

NumPy’s broadcasting rule relaxes this constraint when the arrays’ shapes meet certain constraints. The simplest broadcasting example occurs when an array and a scalar value are combined in an operation:
    
    
    >>> import numpy as np
    >>> a = np.array([1.0, 2.0, 3.0])
    >>> b = 2.0
    >>> a * b
    array([2.,  4.,  6.])
    

The result is equivalent to the previous example where `b` was an array. We can think of the scalar `b` being _stretched_ during the arithmetic operation into an array with the same shape as `a`. The new elements in `b`, as shown in [Figure 1](#broadcasting-figure-1), are simply copies of the original scalar. The stretching analogy is only conceptual. NumPy is smart enough to use the original scalar value without actually making copies so that broadcasting operations are as memory and computationally efficient as possible.

![A scalar is broadcast to match the shape of the 1-d array it is being multiplied to.](../_images/broadcasting_1.png)

_Figure 1_[#](#broadcasting-figure-1 "Link to this image")

_In the simplest example of broadcasting, the scalar_ `b` _is stretched to become an array of same shape as_ `a` _so the shapes are compatible for element-by-element multiplication._

The code in the second example is more efficient than that in the first because broadcasting moves less memory around during the multiplication (`b` is a scalar rather than an array).

## General broadcasting rules[#](#general-broadcasting-rules "Link to this heading")

When operating on two arrays, NumPy compares their shapes element-wise. It starts with the trailing (i.e. rightmost) dimension and works its way left. Two dimensions are compatible when

  1. they are equal, or

  2. one of them is 1.




If these conditions are not met, a `ValueError: operands could not be broadcast together` exception is thrown, indicating that the arrays have incompatible shapes.

Input arrays do not need to have the same _number_ of dimensions. The resulting array will have the same number of dimensions as the input array with the greatest number of dimensions, where the _size_ of each dimension is the largest size of the corresponding dimension among the input arrays. Note that missing dimensions are assumed to have size one.

For example, if you have a `256x256x3` array of RGB values, and you want to scale each color in the image by a different value, you can multiply the image by a one-dimensional array with 3 values. Lining up the sizes of the trailing axes of these arrays according to the broadcast rules, shows that they are compatible:
    
    
    Image  (3d array): 256 x 256 x 3
    Scale  (1d array):             3
    Result (3d array): 256 x 256 x 3
    

When either of the dimensions compared is one, the other is used. In other words, dimensions with size 1 are stretched or “copied” to match the other.

In the following example, both the `A` and `B` arrays have axes with length one that are expanded to a larger size during the broadcast operation:
    
    
    A      (4d array):  8 x 1 x 6 x 1
    B      (3d array):      7 x 1 x 5
    Result (4d array):  8 x 7 x 6 x 5
    

## Broadcastable arrays[#](#broadcastable-arrays "Link to this heading")

A set of arrays is called “broadcastable” to the same shape if the above rules produce a valid result.

For example, if `a.shape` is (5,1), `b.shape` is (1,6), `c.shape` is (6,) and `d.shape` is () so that _d_ is a scalar, then _a_ , _b_ , _c_ , and _d_ are all broadcastable to dimension (5,6); and

  * _a_ acts like a (5,6) array where `a[:,0]` is broadcast to the other columns,

  * _b_ acts like a (5,6) array where `b[0,:]` is broadcast to the other rows,

  * _c_ acts like a (1,6) array and therefore like a (5,6) array where `c[:]` is broadcast to every row, and finally,

  * _d_ acts like a (5,6) array where the single value is repeated.




Here are some more examples:
    
    
    A      (2d array):  5 x 4
    B      (1d array):      1
    Result (2d array):  5 x 4
    
    A      (2d array):  5 x 4
    B      (1d array):      4
    Result (2d array):  5 x 4
    
    A      (3d array):  15 x 3 x 5
    B      (3d array):  15 x 1 x 5
    Result (3d array):  15 x 3 x 5
    
    A      (3d array):  15 x 3 x 5
    B      (2d array):       3 x 5
    Result (3d array):  15 x 3 x 5
    
    A      (3d array):  15 x 3 x 5
    B      (2d array):       3 x 1
    Result (3d array):  15 x 3 x 5
    

Here are examples of shapes that do not broadcast:
    
    
    A      (1d array):  3
    B      (1d array):  4 # trailing dimensions do not match
    
    A      (2d array):      2 x 1
    B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
    

An example of broadcasting when a 1-d array is added to a 2-d array:
    
    
    >>> import numpy as np
    >>> a = np.array([[ 0.0,  0.0,  0.0],
    ...               [10.0, 10.0, 10.0],
    ...               [20.0, 20.0, 20.0],
    ...               [30.0, 30.0, 30.0]])
    >>> b = np.array([1.0, 2.0, 3.0])
    >>> a + b
    array([[  1.,   2.,   3.],
            [11.,  12.,  13.],
            [21.,  22.,  23.],
            [31.,  32.,  33.]])
    >>> b = np.array([1.0, 2.0, 3.0, 4.0])
    >>> a + b
    Traceback (most recent call last):
    ValueError: operands could not be broadcast together with shapes (4,3) (4,)
    

As shown in [Figure 2](#broadcasting-figure-2), `b` is added to each row of `a`. In [Figure 3](#broadcasting-figure-3), an exception is raised because of the incompatible shapes.

![A 1-d array with shape \(3\) is stretched to match the 2-d array of shape \(4, 3\) it is being added to, and the result is a 2-d array of shape \(4, 3\).](../_images/broadcasting_2.png)

_Figure 2_[#](#broadcasting-figure-2 "Link to this image")

_A one dimensional array added to a two dimensional array results in broadcasting if number of 1-d array elements matches the number of 2-d array columns._

![A huge cross over the 2-d array of shape \(4, 3\) and the 1-d array of shape \(4\) shows that they can not be broadcast due to mismatch of shapes and thus produce no result.](../_images/broadcasting_3.png)

_Figure 3_[#](#broadcasting-figure-3 "Link to this image")

_When the trailing dimensions of the arrays are unequal, broadcasting fails because it is impossible to align the values in the rows of the 1st array with the elements of the 2nd arrays for element-by-element addition._

Broadcasting provides a convenient way of taking the outer product (or any other outer operation) of two arrays. The following example shows an outer addition operation of two 1-d arrays:
    
    
    >>> import numpy as np
    >>> a = np.array([0.0, 10.0, 20.0, 30.0])
    >>> b = np.array([1.0, 2.0, 3.0])
    >>> a[:, np.newaxis] + b
    array([[ 1.,   2.,   3.],
           [11.,  12.,  13.],
           [21.,  22.,  23.],
           [31.,  32.,  33.]])
    

![A 2-d array of shape \(4, 1\) and a 1-d array of shape \(3\) are stretched to match their shapes and produce a resultant array of shape \(4, 3\).](../_images/broadcasting_4.png)

_Figure 4_[#](#broadcasting-figure-4 "Link to this image")

_In some cases, broadcasting stretches both arrays to form an output array larger than either of the initial arrays._

Here the `newaxis` index operator inserts a new axis into `a`, making it a two-dimensional `4x1` array. Combining the `4x1` array with `b`, which has shape `(3,)`, yields a `4x3` array.

## A practical example: vector quantization[#](#a-practical-example-vector-quantization "Link to this heading")

Broadcasting comes up quite often in real world problems. A typical example occurs in the vector quantization (VQ) algorithm used in information theory, classification, and other related areas. The basic operation in VQ finds the closest point in a set of points, called `codes` in VQ jargon, to a given point, called the `observation`. In the very simple, two-dimensional case shown below, the values in `observation` describe the weight and height of an athlete to be classified. The `codes` represent different classes of athletes. [[1]](#f1) Finding the closest point requires calculating the distance between observation and each of the codes. The shortest distance provides the best match. In this example, `codes[0]` is the closest class indicating that the athlete is likely a basketball player.
    
    
    >>> from numpy import array, argmin, sqrt, sum
    >>> observation = array([111.0, 188.0])
    >>> codes = array([[102.0, 203.0],
    ...                [132.0, 193.0],
    ...                [45.0, 155.0],
    ...                [57.0, 173.0]])
    >>> diff = codes - observation    # the broadcast happens here
    >>> dist = sqrt(sum(diff**2,axis=-1))
    >>> argmin(dist)
    0
    

In this example, the `observation` array is stretched to match the shape of the `codes` array:
    
    
    Observation      (1d array):      2
    Codes            (2d array):  4 x 2
    Diff             (2d array):  4 x 2
    

![A height versus weight graph that shows data of a female gymnast, marathon runner, basketball player, football lineman and the athlete to be classified. Shortest distance is found between the basketball player and the athlete to be classified.](../_images/broadcasting_5.png)

_Figure 5_[#](#broadcasting-figure-5 "Link to this image")

_The basic operation of vector quantization calculates the distance between an object to be classified, the dark square, and multiple known codes, the gray circles. In this simple case, the codes represent individual classes. More complex cases use multiple codes per class._

Typically, a large number of `observations`, perhaps read from a database, are compared to a set of `codes`. Consider this scenario:
    
    
    Observation      (2d array):      10 x 3
    Codes            (3d array):   5 x 1 x 3
    Diff             (3d array):  5 x 10 x 3
    

The three-dimensional array, `diff`, is a consequence of broadcasting, not a necessity for the calculation. Large data sets will generate a large intermediate array that is computationally inefficient. Instead, if each observation is calculated individually using a Python loop around the code in the two-dimensional example above, a much smaller array is used.

Broadcasting is a powerful tool for writing short and usually intuitive code that does its computations very efficiently in C. However, there are cases when broadcasting uses unnecessarily large amounts of memory for a particular algorithm. In these cases, it is better to write the algorithm’s outer loop in Python. This may also produce more readable code, as algorithms that use broadcasting tend to become more difficult to interpret as the number of dimensions in the broadcast increases.

Footnotes

[[1](#id2)]

In this example, weight has more impact on the distance calculation than height because of the larger values. In practice, it is important to normalize the height and weight, often by their standard deviation across the data set, so that both have equal influence on the distance calculation.

[ __ previous Data types ](basics.types.html "previous page") [ next Copies and views __](basics.copies.html "next page")

__On this page

  * [General broadcasting rules](#general-broadcasting-rules)
  * [Broadcastable arrays](#broadcastable-arrays)
  * [A practical example: vector quantization](#a-practical-example-vector-quantization)

---

## Structured arrays

**Source:** [https://numpy.org/devdocs/user/basics.rec.html](https://numpy.org/devdocs/user/basics.rec.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Structured arrays



# Structured arrays[#](#structured-arrays "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

Structured arrays are ndarrays whose datatype is a composition of simpler datatypes organized as a sequence of named [fields](../glossary.html#term-field). For example,
    
    
    >>> x = np.array([('Rex', 9, 81.0), ('Fido', 3, 27.0)],
    ...              dtype=[('name', 'U10'), ('age', 'i4'), ('weight', 'f4')])
    >>> x
    array([('Rex', 9, 81.), ('Fido', 3, 27.)],
          dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])
    

Here `x` is a one-dimensional array of length two whose datatype is a structure with three fields: 1. A string of length 10 or less named ‘name’, 2. a 32-bit integer named ‘age’, and 3. a 32-bit float named ‘weight’.

If you index `x` at position 1 you get a structure:
    
    
    >>> x[1]
    np.void(('Fido', 3, 27.0), dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])
    

You can access and modify individual fields of a structured array by indexing with the field name:
    
    
    >>> x['age']
    array([9, 3], dtype=int32)
    >>> x['age'] = 5
    >>> x
    array([('Rex', 5, 81.), ('Fido', 5, 27.)],
          dtype=[('name', '<U10'), ('age', '<i4'), ('weight', '<f4')])
    

Structured datatypes are designed to be able to mimic ‘structs’ in the C language, and share a similar memory layout. They are meant for interfacing with C code and for low-level manipulation of structured buffers, for example for interpreting binary blobs. For these purposes they support specialized features such as subarrays, nested datatypes, and unions, and allow control over the memory layout of the structure.

Users looking to manipulate tabular data, such as stored in csv files, may find other pydata projects more suitable, such as xarray, pandas, or DataArray. These provide a high-level interface for tabular data analysis and are better optimized for that use. For instance, the C-struct-like memory layout of structured arrays in numpy can lead to poor cache behavior in comparison.

## Structured datatypes[#](#structured-datatypes "Link to this heading")

A structured datatype can be thought of as a sequence of bytes of a certain length (the structure’s [itemsize](../glossary.html#term-itemsize)) which is interpreted as a collection of fields. Each field has a name, a datatype, and a byte offset within the structure. The datatype of a field may be any numpy datatype including other structured datatypes, and it may also be a [subarray data type](../glossary.html#term-subarray-data-type) which behaves like an ndarray of a specified shape. The offsets of the fields are arbitrary, and fields may even overlap. These offsets are usually determined automatically by numpy, but can also be specified.

### Structured datatype creation[#](#structured-datatype-creation "Link to this heading")

Structured datatypes may be created using the function [`numpy.dtype`](../reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype"). There are 4 alternative forms of specification which vary in flexibility and conciseness. These are further documented in the [Data Type Objects](../reference/arrays.dtypes.html#arrays-dtypes-constructing) reference page, and in summary they are:

  1. A list of tuples, one tuple per field

Each tuple has the form `(fieldname, datatype, shape)` where shape is optional. `fieldname` is a string (or tuple if titles are used, see [Field Titles](#titles) below), `datatype` may be any object convertible to a datatype, and `shape` is a tuple of integers specifying subarray shape.
         
         >>> np.dtype([('x', 'f4'), ('y', np.float32), ('z', 'f4', (2, 2))])
         dtype([('x', '<f4'), ('y', '<f4'), ('z', '<f4', (2, 2))])
         

If `fieldname` is the empty string `''`, the field will be given a default name of the form `f#`, where `#` is the integer index of the field, counting from 0 from the left:
         
         >>> np.dtype([('x', 'f4'), ('', 'i4'), ('z', 'i8')])
         dtype([('x', '<f4'), ('f1', '<i4'), ('z', '<i8')])
         

The byte offsets of the fields within the structure and the total structure itemsize are determined automatically.

  2. A string of comma-separated dtype specifications

In this shorthand notation any of the [string dtype specifications](../reference/arrays.dtypes.html#arrays-dtypes-constructing) may be used in a string and separated by commas. The itemsize and byte offsets of the fields are determined automatically, and the field names are given the default names `f0`, `f1`, etc.
         
         >>> np.dtype('i8, f4, S3')
         dtype([('f0', '<i8'), ('f1', '<f4'), ('f2', 'S3')])
         >>> np.dtype('3int8, float32, (2, 3)float64')
         dtype([('f0', 'i1', (3,)), ('f1', '<f4'), ('f2', '<f8', (2, 3))])
         

  3. A dictionary of field parameter arrays

This is the most flexible form of specification since it allows control over the byte-offsets of the fields and the itemsize of the structure.

The dictionary has two required keys, ‘names’ and ‘formats’, and four optional keys, ‘offsets’, ‘itemsize’, ‘aligned’ and ‘titles’. The values for ‘names’ and ‘formats’ should respectively be a list of field names and a list of dtype specifications, of the same length. The optional ‘offsets’ value should be a list of integer byte-offsets, one for each field within the structure. If ‘offsets’ is not given the offsets are determined automatically. The optional ‘itemsize’ value should be an integer describing the total size in bytes of the dtype, which must be large enough to contain all the fields.
         
         >>> np.dtype({'names': ['col1', 'col2'], 'formats': ['i4', 'f4']})
         dtype([('col1', '<i4'), ('col2', '<f4')])
         >>> np.dtype({'names': ['col1', 'col2'],
         ...           'formats': ['i4', 'f4'],
         ...           'offsets': [0, 4],
         ...           'itemsize': 12})
         dtype({'names': ['col1', 'col2'], 'formats': ['<i4', '<f4'], 'offsets': [0, 4], 'itemsize': 12})
         

Offsets may be chosen such that the fields overlap, though this will mean that assigning to one field may clobber any overlapping field’s data. As an exception, fields of [`numpy.object_`](../reference/arrays.scalars.html#numpy.object_ "numpy.object_") type cannot overlap with other fields, because of the risk of clobbering the internal object pointer and then dereferencing it.

The optional ‘aligned’ value can be set to `True` to make the automatic offset computation use aligned offsets (see [Automatic byte offsets and alignment](#offsets-and-alignment)), as if the ‘align’ keyword argument of [`numpy.dtype`](../reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype") had been set to True.

The optional ‘titles’ value should be a list of titles of the same length as ‘names’, see [Field Titles](#titles) below.

  4. A dictionary of field names

The keys of the dictionary are the field names and the values are tuples specifying type and offset:
         
         >>> np.dtype({'col1': ('i1', 0), 'col2': ('f4', 1)})
         dtype([('col1', 'i1'), ('col2', '<f4')])
         

This form was discouraged because Python dictionaries did not preserve order in Python versions before Python 3.6. [Field Titles](#titles) may be specified by using a 3-tuple, see below.




### Manipulating and displaying structured datatypes[#](#manipulating-and-displaying-structured-datatypes "Link to this heading")

The list of field names of a structured datatype can be found in the `names` attribute of the dtype object:
    
    
    >>> d = np.dtype([('x', 'i8'), ('y', 'f4')])
    >>> d.names
    ('x', 'y')
    

The dtype of each individual field can be looked up by name:
    
    
    >>> d['x']
    dtype('int64')
    

The field names may be modified by assigning to the `names` attribute using a sequence of strings of the same length.

The dtype object also has a dictionary-like attribute, `fields`, whose keys are the field names (and [Field Titles](#titles), see below) and whose values are tuples containing the dtype and byte offset of each field.
    
    
    >>> d.fields
    mappingproxy({'x': (dtype('int64'), 0), 'y': (dtype('float32'), 8)})
    

Both the `names` and `fields` attributes will equal `None` for unstructured arrays. The recommended way to test if a dtype is structured is with _if dt.names is not None_ rather than _if dt.names_ , to account for dtypes with 0 fields.

The string representation of a structured datatype is shown in the “list of tuples” form if possible, otherwise numpy falls back to using the more general dictionary form.

### Automatic byte offsets and alignment[#](#automatic-byte-offsets-and-alignment "Link to this heading")

Numpy uses one of two methods to automatically determine the field byte offsets and the overall itemsize of a structured datatype, depending on whether `align=True` was specified as a keyword argument to [`numpy.dtype`](../reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype").

By default (`align=False`), numpy will pack the fields together such that each field starts at the byte offset the previous field ended, and the fields are contiguous in memory.
    
    
    >>> def print_offsets(d):
    ...     print("offsets:", [d.fields[name][1] for name in d.names])
    ...     print("itemsize:", d.itemsize)
    >>> print_offsets(np.dtype('u1, u1, i4, u1, i8, u2'))
    offsets: [0, 1, 2, 6, 7, 15]
    itemsize: 17
    

If `align=True` is set, numpy will pad the structure in the same way many C compilers would pad a C-struct. Aligned structures can give a performance improvement in some cases, at the cost of increased datatype size. Padding bytes are inserted between fields such that each field’s byte offset will be a multiple of that field’s alignment, which is usually equal to the field’s size in bytes for simple datatypes, see [`PyArray_Descr.alignment`](../reference/c-api/types-and-structures.html#c.PyArray_Descr.alignment "PyArray_Descr.alignment"). The structure will also have trailing padding added so that its itemsize is a multiple of the largest field’s alignment.
    
    
    >>> print_offsets(np.dtype('u1, u1, i4, u1, i8, u2', align=True))
    offsets: [0, 1, 4, 8, 16, 24]
    itemsize: 32
    

Note that although almost all modern C compilers pad in this way by default, padding in C structs is C-implementation-dependent so this memory layout is not guaranteed to exactly match that of a corresponding struct in a C program. Some work may be needed, either on the numpy side or the C side, to obtain exact correspondence.

If offsets were specified using the optional `offsets` key in the dictionary-based dtype specification, setting `align=True` will check that each field’s offset is a multiple of its size and that the itemsize is a multiple of the largest field size, and raise an exception if not.

If the offsets of the fields and itemsize of a structured array satisfy the alignment conditions, the array will have the `ALIGNED` [`flag`](../reference/generated/numpy.ndarray.flags.html#numpy.ndarray.flags "numpy.ndarray.flags") set.

A convenience function [`numpy.lib.recfunctions.repack_fields`](#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields") converts an aligned dtype or array to a packed one and vice versa. It takes either a dtype or structured ndarray as an argument, and returns a copy with fields re-packed, with or without padding bytes.

### Field titles[#](#field-titles "Link to this heading")

In addition to field names, fields may also have an associated [title](../glossary.html#term-title), an alternate name, which is sometimes used as an additional description or alias for the field. The title may be used to index an array, just like a field name.

To add titles when using the list-of-tuples form of dtype specification, the field name may be specified as a tuple of two strings instead of a single string, which will be the field’s title and field name respectively. For example:
    
    
    >>> np.dtype([(('my title', 'name'), 'f4')])
    dtype([(('my title', 'name'), '<f4')])
    

When using the first form of dictionary-based specification, the titles may be supplied as an extra `'titles'` key as described above. When using the second (discouraged) dictionary-based specification, the title can be supplied by providing a 3-element tuple `(datatype, offset, title)` instead of the usual 2-element tuple:
    
    
    >>> np.dtype({'name': ('i4', 0, 'my title')})
    dtype([(('my title', 'name'), '<i4')])
    

The `dtype.fields` dictionary will contain titles as keys, if any titles are used. This means effectively that a field with a title will be represented twice in the fields dictionary. The tuple values for these fields will also have a third element, the field title. Because of this, and because the `names` attribute preserves the field order while the `fields` attribute may not, it is recommended to iterate through the fields of a dtype using the `names` attribute of the dtype, which will not list titles, as in:
    
    
    >>> for name in d.names:
    ...     print(d.fields[name][:2])
    (dtype('int64'), 0)
    (dtype('float32'), 8)
    

### Union types[#](#union-types "Link to this heading")

Structured datatypes are implemented in numpy to have base type [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void") by default, but it is possible to interpret other numpy types as structured types using the `(base_dtype, dtype)` form of dtype specification described in [Data Type Objects](../reference/arrays.dtypes.html#arrays-dtypes-constructing). Here, `base_dtype` is the desired underlying dtype, and fields and flags will be copied from `dtype`. This dtype is similar to a ‘union’ in C.

## Indexing and assignment to structured arrays[#](#indexing-and-assignment-to-structured-arrays "Link to this heading")

### Assigning data to a structured array[#](#assigning-data-to-a-structured-array "Link to this heading")

There are a number of ways to assign values to a structured array: Using python tuples, using scalar values, or using other structured arrays.

#### Assignment from Python Native Types (Tuples)[#](#assignment-from-python-native-types-tuples "Link to this heading")

The simplest way to assign values to a structured array is using python tuples. Each assigned value should be a tuple of length equal to the number of fields in the array, and not a list or array as these will trigger numpy’s broadcasting rules. The tuple’s elements are assigned to the successive fields of the array, from left to right:
    
    
    >>> x = np.array([(1, 2, 3), (4, 5, 6)], dtype='i8, f4, f8')
    >>> x[1] = (7, 8, 9)
    >>> x
    array([(1, 2., 3.), (7, 8., 9.)],
         dtype=[('f0', '<i8'), ('f1', '<f4'), ('f2', '<f8')])
    

#### Assignment from Scalars[#](#assignment-from-scalars "Link to this heading")

A scalar assigned to a structured element will be assigned to all fields. This happens when a scalar is assigned to a structured array, or when an unstructured array is assigned to a structured array:
    
    
    >>> x = np.zeros(2, dtype='i8, f4, ?, S1')
    >>> x[:] = 3
    >>> x
    array([(3, 3., True, b'3'), (3, 3., True, b'3')],
          dtype=[('f0', '<i8'), ('f1', '<f4'), ('f2', '?'), ('f3', 'S1')])
    >>> x[:] = np.arange(2)
    >>> x
    array([(0, 0., False, b'0'), (1, 1., True, b'1')],
          dtype=[('f0', '<i8'), ('f1', '<f4'), ('f2', '?'), ('f3', 'S1')])
    

Structured arrays can also be assigned to unstructured arrays, but only if the structured datatype has just a single field:
    
    
    >>> twofield = np.zeros(2, dtype=[('A', 'i4'), ('B', 'i4')])
    >>> onefield = np.zeros(2, dtype=[('A', 'i4')])
    >>> nostruct = np.zeros(2, dtype='i4')
    >>> nostruct[:] = twofield
    Traceback (most recent call last):
    ...
    TypeError: Cannot cast array data from dtype([('A', '<i4'), ('B', '<i4')]) to dtype('int32') according to the rule 'unsafe'
    

#### Assignment from other Structured Arrays[#](#assignment-from-other-structured-arrays "Link to this heading")

Assignment between two structured arrays occurs as if the source elements had been converted to tuples and then assigned to the destination elements. That is, the first field of the source array is assigned to the first field of the destination array, and the second field likewise, and so on, regardless of field names. Structured arrays with a different number of fields cannot be assigned to each other. Bytes of the destination structure which are not included in any of the fields are unaffected.
    
    
    >>> a = np.zeros(3, dtype=[('a', 'i8'), ('b', 'f4'), ('c', 'S3')])
    >>> b = np.ones(3, dtype=[('x', 'f4'), ('y', 'S3'), ('z', 'O')])
    >>> b[:] = a
    >>> b
    array([(0., b'0.0', b''), (0., b'0.0', b''), (0., b'0.0', b'')],
          dtype=[('x', '<f4'), ('y', 'S3'), ('z', 'O')])
    

#### Assignment involving subarrays[#](#assignment-involving-subarrays "Link to this heading")

When assigning to fields which are subarrays, the assigned value will first be broadcast to the shape of the subarray.

### Indexing structured arrays[#](#indexing-structured-arrays "Link to this heading")

#### Accessing Individual Fields[#](#accessing-individual-fields "Link to this heading")

Individual fields of a structured array may be accessed and modified by indexing the array with the field name.
    
    
    >>> x = np.array([(1, 2), (3, 4)], dtype=[('foo', 'i8'), ('bar', 'f4')])
    >>> x['foo']
    array([1, 3])
    >>> x['foo'] = 10
    >>> x
    array([(10, 2.), (10, 4.)],
          dtype=[('foo', '<i8'), ('bar', '<f4')])
    

The resulting array is a view into the original array. It shares the same memory locations and writing to the view will modify the original array.
    
    
    >>> y = x['bar']
    >>> y[:] = 11
    >>> x
    array([(10, 11.), (10, 11.)],
          dtype=[('foo', '<i8'), ('bar', '<f4')])
    

This view has the same dtype and itemsize as the indexed field, so it is typically a non-structured array, except in the case of nested structures.
    
    
    >>> y.dtype, y.shape, y.strides
    (dtype('float32'), (2,), (12,))
    

If the accessed field is a subarray, the dimensions of the subarray are appended to the shape of the result:
    
    
    >>> x = np.zeros((2, 2), dtype=[('a', np.int32), ('b', np.float64, (3, 3))])
    >>> x['a'].shape
    (2, 2)
    >>> x['b'].shape
    (2, 2, 3, 3)
    

#### Accessing Multiple Fields[#](#accessing-multiple-fields "Link to this heading")

One can index and assign to a structured array with a multi-field index, where the index is a list of field names.

Warning

The behavior of multi-field indexes changed from Numpy 1.15 to Numpy 1.16.

The result of indexing with a multi-field index is a view into the original array, as follows:
    
    
    >>> a = np.zeros(3, dtype=[('a', 'i4'), ('b', 'i4'), ('c', 'f4')])
    >>> a[['a', 'c']]
    array([(0, 0.), (0, 0.), (0, 0.)],
         dtype={'names': ['a', 'c'], 'formats': ['<i4', '<f4'], 'offsets': [0, 8], 'itemsize': 12})
    

Assignment to the view modifies the original array. The view’s fields will be in the order they were indexed. Note that unlike for single-field indexing, the dtype of the view has the same itemsize as the original array, and has fields at the same offsets as in the original array, and unindexed fields are merely missing.

Warning

In Numpy 1.15, indexing an array with a multi-field index returned a copy of the result above, but with fields packed together in memory as if passed through [`numpy.lib.recfunctions.repack_fields`](#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields").

The new behavior as of Numpy 1.16 leads to extra “padding” bytes at the location of unindexed fields compared to 1.15. You will need to update any code which depends on the data having a “packed” layout. For instance code such as:
    
    
    >>> a[['a', 'c']].view('i8')  # Fails in Numpy 1.16
    Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
    ValueError: When changing to a smaller dtype, its size must be a divisor of the size of original dtype
    

will need to be changed. This code has raised a `FutureWarning` since Numpy 1.12, and similar code has raised `FutureWarning` since 1.7.

In 1.16 a number of functions have been introduced in the [`numpy.lib.recfunctions`](#module-numpy.lib.recfunctions "numpy.lib.recfunctions") module to help users account for this change. These are [`numpy.lib.recfunctions.repack_fields`](#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields"). [`numpy.lib.recfunctions.structured_to_unstructured`](#numpy.lib.recfunctions.structured_to_unstructured "numpy.lib.recfunctions.structured_to_unstructured"), [`numpy.lib.recfunctions.unstructured_to_structured`](#numpy.lib.recfunctions.unstructured_to_structured "numpy.lib.recfunctions.unstructured_to_structured"), [`numpy.lib.recfunctions.apply_along_fields`](#numpy.lib.recfunctions.apply_along_fields "numpy.lib.recfunctions.apply_along_fields"), [`numpy.lib.recfunctions.assign_fields_by_name`](#numpy.lib.recfunctions.assign_fields_by_name "numpy.lib.recfunctions.assign_fields_by_name"), and [`numpy.lib.recfunctions.require_fields`](#numpy.lib.recfunctions.require_fields "numpy.lib.recfunctions.require_fields").

The function [`numpy.lib.recfunctions.repack_fields`](#numpy.lib.recfunctions.repack_fields "numpy.lib.recfunctions.repack_fields") can always be used to reproduce the old behavior, as it will return a packed copy of the structured array. The code above, for example, can be replaced with:
    
    
    >>> from numpy.lib.recfunctions import repack_fields
    >>> repack_fields(a[['a', 'c']]).view('i8')  # supported in 1.16
    array([0, 0, 0])
    

Furthermore, numpy now provides a new function [`numpy.lib.recfunctions.structured_to_unstructured`](#numpy.lib.recfunctions.structured_to_unstructured "numpy.lib.recfunctions.structured_to_unstructured") which is a safer and more efficient alternative for users who wish to convert structured arrays to unstructured arrays, as the view above is often intended to do. This function allows safe conversion to an unstructured type taking into account padding, often avoids a copy, and also casts the datatypes as needed, unlike the view. Code such as:
    
    
    >>> b = np.zeros(3, dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
    >>> b[['x', 'z']].view('f4')
    array([0., 0., 0., 0., 0., 0., 0., 0., 0.], dtype=float32)
    

can be made safer by replacing with:
    
    
    >>> from numpy.lib.recfunctions import structured_to_unstructured
    >>> structured_to_unstructured(b[['x', 'z']])
    array([[0., 0.],
           [0., 0.],
           [0., 0.]], dtype=float32)
    

Assignment to an array with a multi-field index modifies the original array:
    
    
    >>> a[['a', 'c']] = (2, 3)
    >>> a
    array([(2, 0, 3.), (2, 0, 3.), (2, 0, 3.)],
          dtype=[('a', '<i4'), ('b', '<i4'), ('c', '<f4')])
    

This obeys the structured array assignment rules described above. For example, this means that one can swap the values of two fields using appropriate multi-field indexes:
    
    
    >>> a[['a', 'c']] = a[['c', 'a']]
    

#### Indexing with an Integer to get a Structured Scalar[#](#indexing-with-an-integer-to-get-a-structured-scalar "Link to this heading")

Indexing a single element of a structured array (with an integer index) returns a structured scalar:
    
    
    >>> x = np.array([(1, 2., 3.)], dtype='i, f, f')
    >>> scalar = x[0]
    >>> scalar
    np.void((1, 2.0, 3.0), dtype=[('f0', '<i4'), ('f1', '<f4'), ('f2', '<f4')])
    >>> type(scalar)
    <class 'numpy.void'>
    

Unlike other numpy scalars, structured scalars are mutable and act like views into the original array, such that modifying the scalar will modify the original array. Structured scalars also support access and assignment by field name:
    
    
    >>> x = np.array([(1, 2), (3, 4)], dtype=[('foo', 'i8'), ('bar', 'f4')])
    >>> s = x[0]
    >>> s['bar'] = 100
    >>> x
    array([(1, 100.), (3, 4.)],
          dtype=[('foo', '<i8'), ('bar', '<f4')])
    

Similarly to tuples, structured scalars can also be indexed with an integer:
    
    
    >>> scalar = np.array([(1, 2., 3.)], dtype='i, f, f')[0]
    >>> scalar[0]
    np.int32(1)
    >>> scalar[1] = 4
    

Thus, tuples might be thought of as the native Python equivalent to numpy’s structured types, much like native python integers are the equivalent to numpy’s integer types. Structured scalars may be converted to a tuple by calling [`numpy.ndarray.item`](../reference/generated/numpy.ndarray.item.html#numpy.ndarray.item "numpy.ndarray.item"):
    
    
    >>> scalar.item(), type(scalar.item())
    ((1, 4.0, 3.0), <class 'tuple'>)
    

### Viewing structured arrays containing objects[#](#viewing-structured-arrays-containing-objects "Link to this heading")

In order to prevent clobbering object pointers in fields of [`object`](https://docs.python.org/3/library/functions.html#object "\(in Python v3.14\)") type, numpy currently does not allow views of structured arrays containing objects.

### Structure comparison and promotion[#](#structure-comparison-and-promotion "Link to this heading")

If the dtypes of two void structured arrays are equal, testing the equality of the arrays will result in a boolean array with the dimensions of the original arrays, with elements set to `True` where all fields of the corresponding structures are equal:
    
    
    >>> a = np.array([(1, 1), (2, 2)], dtype=[('a', 'i4'), ('b', 'i4')])
    >>> b = np.array([(1, 1), (2, 3)], dtype=[('a', 'i4'), ('b', 'i4')])
    >>> a == b
    array([True, False])
    

NumPy will promote individual field datatypes to perform the comparison. So the following is also valid (note the `'f4'` dtype for the `'a'` field):
    
    
    >>> b = np.array([(1.0, 1), (2.5, 2)], dtype=[("a", "f4"), ("b", "i4")])
    >>> a == b
    array([True, False])
    

To compare two structured arrays, it must be possible to promote them to a common dtype as returned by [`numpy.result_type`](../reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type") and [`numpy.promote_types`](../reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types"). This enforces that the number of fields, the field names, and the field titles must match precisely. When promotion is not possible, for example due to mismatching field names, NumPy will raise an error. Promotion between two structured dtypes results in a canonical dtype that ensures native byte-order for all fields:
    
    
    >>> np.result_type(np.dtype("i,>i"))
    dtype([('f0', '<i4'), ('f1', '<i4')])
    >>> np.result_type(np.dtype("i,>i"), np.dtype("i,i"))
    dtype([('f0', '<i4'), ('f1', '<i4')])
    

The resulting dtype from promotion is also guaranteed to be packed, meaning that all fields are ordered contiguously and any unnecessary padding is removed:
    
    
    >>> dt = np.dtype("i1,V3,i4,V1")[["f0", "f2"]]
    >>> dt
    dtype({'names': ['f0', 'f2'], 'formats': ['i1', '<i4'], 'offsets': [0, 4], 'itemsize': 9})
    >>> np.result_type(dt)
    dtype([('f0', 'i1'), ('f2', '<i4')])
    

Note that the result prints without `offsets` or `itemsize` indicating no additional padding. If a structured dtype is created with `align=True` ensuring that `dtype.isalignedstruct` is true, this property is preserved:
    
    
    >>> dt = np.dtype("i1,V3,i4,V1", align=True)[["f0", "f2"]]
    >>> dt
    dtype({'names': ['f0', 'f2'], 'formats': ['i1', '<i4'], 'offsets': [0, 4], 'itemsize': 12}, align=True)
    
    >>> np.result_type(dt)
    dtype([('f0', 'i1'), ('f2', '<i4')], align=True)
    >>> np.result_type(dt).isalignedstruct
    True
    

When promoting multiple dtypes, the result is aligned if any of the inputs is:
    
    
    >>> np.result_type(np.dtype("i,i"), np.dtype("i,i", align=True))
    dtype([('f0', '<i4'), ('f1', '<i4')], align=True)
    

The `<` and `>` operators always return `False` when comparing void structured arrays, and arithmetic and bitwise operations are not supported.

Changed in version 1.23: Before NumPy 1.23, a warning was given and `False` returned when promotion to a common dtype failed. Further, promotion was much more restrictive: It would reject the mixed float/integer comparison example above.

## Record arrays[#](#record-arrays "Link to this heading")

As an optional convenience numpy provides an ndarray subclass, [`numpy.recarray`](../reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray") that allows access to fields of structured arrays by attribute instead of only by index. Record arrays use a special datatype, [`numpy.record`](../reference/generated/numpy.record.html#numpy.record "numpy.record"), that allows field access by attribute on the structured scalars obtained from the array. The `numpy.rec` module provides functions for creating recarrays from various objects. Additional helper functions for creating and manipulating structured arrays can be found in [`numpy.lib.recfunctions`](#module-numpy.lib.recfunctions "numpy.lib.recfunctions").

The simplest way to create a record array is with [`numpy.rec.array`](../reference/generated/numpy.rec.array.html#numpy.rec.array "numpy.rec.array"):
    
    
    >>> recordarr = np.rec.array([(1, 2., 'Hello'), (2, 3., "World")],
    ...                    dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])
    >>> recordarr.bar
    array([2., 3.], dtype=float32)
    >>> recordarr[1:2]
    rec.array([(2, 3., b'World')],
          dtype=[('foo', '<i4'), ('bar', '<f4'), ('baz', 'S10')])
    >>> recordarr[1:2].foo
    array([2], dtype=int32)
    >>> recordarr.foo[1:2]
    array([2], dtype=int32)
    >>> recordarr[1].baz
    b'World'
    

[`numpy.rec.array`](../reference/generated/numpy.rec.array.html#numpy.rec.array "numpy.rec.array") can convert a wide variety of arguments into record arrays, including structured arrays:
    
    
    >>> arr = np.array([(1, 2., 'Hello'), (2, 3., "World")],
    ...             dtype=[('foo', 'i4'), ('bar', 'f4'), ('baz', 'S10')])
    >>> recordarr = np.rec.array(arr)
    

The `numpy.rec` module provides a number of other convenience functions for creating record arrays, see [record array creation routines](../reference/routines.array-creation.html#routines-array-creation-rec).

A record array representation of a structured array can be obtained using the appropriate [`view`](../reference/generated/numpy.ndarray.view.html#numpy.ndarray.view "numpy.ndarray.view"):
    
    
    >>> arr = np.array([(1, 2., 'Hello'), (2, 3., "World")],
    ...                dtype=[('foo', 'i4'),('bar', 'f4'), ('baz', 'S10')])
    >>> recordarr = arr.view(dtype=np.dtype((np.record, arr.dtype)),
    ...                      type=np.recarray)
    

For convenience, viewing an ndarray as type [`numpy.recarray`](../reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray") will automatically convert to [`numpy.record`](../reference/generated/numpy.record.html#numpy.record "numpy.record") datatype, so the dtype can be left out of the view:
    
    
    >>> recordarr = arr.view(np.recarray)
    >>> recordarr.dtype
    dtype((numpy.record, [('foo', '<i4'), ('bar', '<f4'), ('baz', 'S10')]))
    

To get back to a plain ndarray both the dtype and type must be reset. The following view does so, taking into account the unusual case that the recordarr was not a structured type:
    
    
    >>> arr2 = recordarr.view(recordarr.dtype.fields or recordarr.dtype, np.ndarray)
    

Record array fields accessed by index or by attribute are returned as a record array if the field has a structured type but as a plain ndarray otherwise.
    
    
    >>> recordarr = np.rec.array([('Hello', (1, 2)), ("World", (3, 4))],
    ...                 dtype=[('foo', 'S6'),('bar', [('A', int), ('B', int)])])
    >>> type(recordarr.foo)
    <class 'numpy.ndarray'>
    >>> type(recordarr.bar)
    <class 'numpy.rec.recarray'>
    

Note that if a field has the same name as an ndarray attribute, the ndarray attribute takes precedence. Such fields will be inaccessible by attribute but will still be accessible by index.

### Recarray helper functions[#](#module-numpy.lib.recfunctions "Link to this heading")

Collection of utilities to manipulate structured arrays.

Most of these functions were initially implemented by John Hunter for matplotlib. They have been rewritten and extended for convenience.

numpy.lib.recfunctions.append_fields(_base_ , _names_ , _data_ , _dtypes =None_, _fill_value =-1_, _usemask =True_, _asrecarray =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L654-L722)[#](#numpy.lib.recfunctions.append_fields "Link to this definition")
    

Add new fields to an existing array.

The names of the fields are given with the _names_ arguments, the corresponding values with the _data_ arguments. If a single field is appended, _names_ , _data_ and _dtypes_ do not have to be lists but just values.

Parameters:
    

**base** array
    

Input array to extend.

**names** string, sequence
    

String or sequence of strings corresponding to the names of the new fields.

**data** array or sequence of arrays
    

Array or sequence of arrays storing the fields to add to the base.

**dtypes** sequence of datatypes, optional
    

Datatype or sequence of datatypes. If None, the datatypes are estimated from the _data_.

**fill_value**{float}, optional
    

Filling value used to pad missing data on the shorter arrays.

**usemask**{False, True}, optional
    

Whether to return a masked array or not.

**asrecarray**{False, True}, optional
    

Whether to return a recarray (MaskedRecords) or not.

numpy.lib.recfunctions.apply_along_fields(_func_ , _arr_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1185-L1227)[#](#numpy.lib.recfunctions.apply_along_fields "Link to this definition")
    

Apply function ‘func’ as a reduction across fields of a structured array.

This is similar to [`numpy.apply_along_axis`](../reference/generated/numpy.apply_along_axis.html#numpy.apply_along_axis "numpy.apply_along_axis"), but treats the fields of a structured array as an extra axis. The fields are all first cast to a common type following the type-promotion rules from [`numpy.result_type`](../reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type") applied to the field’s dtypes.

Parameters:
    

**func** function
    

Function to apply on the “field” dimension. This function must support an _axis_ argument, like [`numpy.mean`](../reference/generated/numpy.mean.html#numpy.mean "numpy.mean"), [`numpy.sum`](../reference/generated/numpy.sum.html#numpy.sum "numpy.sum"), etc.

**arr** ndarray
    

Structured array for which to apply func.

Returns:
    

**out** ndarray
    

Result of the reduction operation

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    
    
    
    >>> from numpy.lib import recfunctions as rfn
    >>> b = np.array([(1, 2, 5), (4, 5, 7), (7, 8 ,11), (10, 11, 12)],
    ...              dtype=[('x', 'i4'), ('y', 'f4'), ('z', 'f8')])
    >>> rfn.apply_along_fields(np.mean, b)
    array([ 2.66666667,  5.33333333,  8.66666667, 11.        ])
    >>> rfn.apply_along_fields(np.mean, b[['x', 'z']])
    array([ 3. ,  5.5,  9. , 11. ])
    

Go BackOpen In Tab

numpy.lib.recfunctions.assign_fields_by_name(_dst_ , _src_ , _zero_unassigned =True_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1232-L1268)[#](#numpy.lib.recfunctions.assign_fields_by_name "Link to this definition")
    

Assigns values from one structured array to another by field name.

Normally in numpy >= 1.14, assignment of one structured array to another copies fields “by position”, meaning that the first field from the src is copied to the first field of the dst, and so on, regardless of field name.

This function instead copies “by field name”, such that fields in the dst are assigned from the identically named field in the src. This applies recursively for nested structures. This is how structure assignment worked in numpy >= 1.6 to <= 1.13.

Parameters:
    

**dst** ndarray
    
**src** ndarray
    

The source and destination arrays during assignment.

**zero_unassigned** bool, optional
    

If True, fields in the dst for which there was no matching field in the src are filled with the value 0 (zero). This was the behavior of numpy <= 1.13. If False, those fields are not modified.

numpy.lib.recfunctions.drop_fields(_base_ , _drop_names_ , _usemask =True_, _asrecarray =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L504-L563)[#](#numpy.lib.recfunctions.drop_fields "Link to this definition")
    

Return a new array with fields in _drop_names_ dropped.

Nested fields are supported.

Parameters:
    

**base** array
    

Input array

**drop_names** string or sequence
    

String or sequence of strings corresponding to the names of the fields to drop.

**usemask**{False, True}, optional
    

Whether to return a masked array or not.

**asrecarray** string or sequence, optional
    

Whether to return a recarray or a mrecarray (_asrecarray=True_) or a plain ndarray or masked array with flexible dtype. The default is False.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> a = np.array([(1, (2, 3.0)), (4, (5, 6.0))],
    ...   dtype=[('a', np.int64), ('b', [('ba', np.double), ('bb', np.int64)])])
    >>> rfn.drop_fields(a, 'a')
    array([((2., 3),), ((5., 6),)],
          dtype=[('b', [('ba', '<f8'), ('bb', '<i8')])])
    >>> rfn.drop_fields(a, 'ba')
    array([(1, (3,)), (4, (6,))], dtype=[('a', '<i8'), ('b', [('bb', '<i8')])])
    >>> rfn.drop_fields(a, ['ba', 'bb'])
    array([(1,), (4,)], dtype=[('a', '<i8')])
    

Go BackOpen In Tab

numpy.lib.recfunctions.find_duplicates(_a_ , _key =None_, _ignoremask =True_, _return_index =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1416-L1472)[#](#numpy.lib.recfunctions.find_duplicates "Link to this definition")
    

Find the duplicates in a structured array along a given key

Parameters:
    

**a** array-like
    

Input array

**key**{string, None}, optional
    

Name of the fields along which to check the duplicates. If None, the search is performed by records

**ignoremask**{True, False}, optional
    

Whether masked data should be discarded or considered as duplicates.

**return_index**{False, True}, optional
    

Whether to return the indices of the duplicated values.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> ndtype = [('a', int)]
    >>> a = np.ma.array([1, 1, 1, 2, 2, 3, 3],
    ...         mask=[0, 0, 1, 0, 0, 0, 1]).view(ndtype)
    >>> rfn.find_duplicates(a, ignoremask=True, return_index=True)
    (masked_array(data=[(1,), (1,), (2,), (2,)],
                 mask=[(False,), (False,), (False,), (False,)],
           fill_value=(999999,),
                dtype=[('a', '<i8')]), array([0, 1, 3, 4]))
    

Go BackOpen In Tab

numpy.lib.recfunctions.flatten_descr(_ndtype_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L169-L193)[#](#numpy.lib.recfunctions.flatten_descr "Link to this definition")
    

Flatten a structured data-type description.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> ndtype = np.dtype([('a', '<i4'), ('b', [('ba', '<f8'), ('bb', '<i4')])])
    >>> rfn.flatten_descr(ndtype)
    (('a', dtype('int32')), ('ba', dtype('float64')), ('bb', dtype('int32')))
    

Go BackOpen In Tab

numpy.lib.recfunctions.get_fieldstructure(_adtype_ , _lastname =None_, _parents =None_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L226-L271)[#](#numpy.lib.recfunctions.get_fieldstructure "Link to this definition")
    

Returns a dictionary with fields indexing lists of their parent fields.

This function is used to simplify access to fields nested in other fields.

Parameters:
    

**adtype** np.dtype
    

Input datatype

**lastname** optional
    

Last processed field name (used internally during recursion).

**parents** dictionary
    

Dictionary of parent fields (used internally during recursion).

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> ndtype =  np.dtype([('A', int),
    ...                     ('B', [('BA', int),
    ...                            ('BB', [('BBA', int), ('BBB', int)])])])
    >>> rfn.get_fieldstructure(ndtype)
    ... # XXX: possible regression, order of BBA and BBB is swapped
    {'A': [], 'B': [], 'BA': ['B'], 'BB': ['B'], 'BBA': ['B', 'BB'], 'BBB': ['B', 'BB']}
    

Go BackOpen In Tab

numpy.lib.recfunctions.get_names(_adtype_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L103-L133)[#](#numpy.lib.recfunctions.get_names "Link to this definition")
    

Returns the field names of the input datatype as a tuple. Input datatype must have fields otherwise error is raised.

Parameters:
    

**adtype** dtype
    

Input datatype

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> rfn.get_names(np.empty((1,), dtype=[('A', int)]).dtype)
    ('A',)
    >>> rfn.get_names(np.empty((1,), dtype=[('A',int), ('B', float)]).dtype)
    ('A', 'B')
    >>> adtype = np.dtype([('a', int), ('b', [('ba', int), ('bb', int)])])
    >>> rfn.get_names(adtype)
    ('a', ('b', ('ba', 'bb')))
    

Go BackOpen In Tab

numpy.lib.recfunctions.get_names_flat(_adtype_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L136-L166)[#](#numpy.lib.recfunctions.get_names_flat "Link to this definition")
    

Returns the field names of the input datatype as a tuple. Input datatype must have fields otherwise error is raised. Nested structure are flattened beforehand.

Parameters:
    

**adtype** dtype
    

Input datatype

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> rfn.get_names_flat(np.empty((1,), dtype=[('A', int)]).dtype) is None
    False
    >>> rfn.get_names_flat(np.empty((1,), dtype=[('A',int), ('B', str)]).dtype)
    ('A', 'B')
    >>> adtype = np.dtype([('a', int), ('b', [('ba', int), ('bb', int)])])
    >>> rfn.get_names_flat(adtype)
    ('a', 'b', 'ba', 'bb')
    

Go BackOpen In Tab

numpy.lib.recfunctions.join_by(_key_ , _r1_ , _r2_ , _jointype ='inner'_, _r1postfix ='1'_, _r2postfix ='2'_, _defaults =None_, _usemask =True_, _asrecarray =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1481-L1656)[#](#numpy.lib.recfunctions.join_by "Link to this definition")
    

Join arrays _r1_ and _r2_ on key _key_.

The key should be either a string or a sequence of string corresponding to the fields used to join the array. An exception is raised if the _key_ field cannot be found in the two input arrays. Neither _r1_ nor _r2_ should have any duplicates along _key_ : the presence of duplicates will make the output quite unreliable. Note that duplicates are not looked for by the algorithm.

Parameters:
    

**key**{string, sequence}
    

A string or a sequence of strings corresponding to the fields used for comparison.

**r1, r2** arrays
    

Structured arrays.

**jointype**{‘inner’, ‘outer’, ‘leftouter’}, optional
    

If ‘inner’, returns the elements common to both r1 and r2. If ‘outer’, returns the common elements as well as the elements of r1 not in r2 and the elements of not in r2. If ‘leftouter’, returns the common elements and the elements of r1 not in r2.

**r1postfix** string, optional
    

String appended to the names of the fields of r1 that are present in r2 but absent of the key.

**r2postfix** string, optional
    

String appended to the names of the fields of r2 that are present in r1 but absent of the key.

**defaults**{dictionary}, optional
    

Dictionary mapping field names to the corresponding default values.

**usemask**{True, False}, optional
    

Whether to return a MaskedArray (or MaskedRecords is _asrecarray==True_) or an ndarray.

**asrecarray**{False, True}, optional
    

Whether to return a recarray (or MaskedRecords if _usemask==True_) or just a flexible-type ndarray.

Notes

  * The output is sorted along the key.

  * A temporary array is formed by dropping the fields not in the key for the two arrays and concatenating the result. This array is then sorted, and the common entries selected. The output is constructed by filling the fields with the selected entries. Matching is not preserved if there are some duplicates…




numpy.lib.recfunctions.merge_arrays(_seqarrays_ , _fill_value =-1_, _flatten =False_, _usemask =False_, _asrecarray =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L363-L497)[#](#numpy.lib.recfunctions.merge_arrays "Link to this definition")
    

Merge arrays field by field.

Parameters:
    

**seqarrays** sequence of ndarrays
    

Sequence of arrays

**fill_value**{float}, optional
    

Filling value used to pad missing data on the shorter arrays.

**flatten**{False, True}, optional
    

Whether to collapse nested fields.

**usemask**{False, True}, optional
    

Whether to return a masked array or not.

**asrecarray**{False, True}, optional
    

Whether to return a recarray (MaskedRecords) or not.

Notes

  * Without a mask, the missing value will be filled with something, depending on what its corresponding type:

    * `-1` for integers

    * `-1.0` for floating point numbers

    * `'-'` for characters

    * `'-1'` for strings

    * `True` for boolean values

  * XXX: I just obtained these values empirically




Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> rfn.merge_arrays((np.array([1, 2]), np.array([10., 20., 30.])))
    array([( 1, 10.), ( 2, 20.), (-1, 30.)],
          dtype=[('f0', '<i8'), ('f1', '<f8')])
    
    
    
    >>> rfn.merge_arrays((np.array([1, 2], dtype=np.int64),
    ...         np.array([10., 20., 30.])), usemask=False)
     array([(1, 10.0), (2, 20.0), (-1, 30.0)],
             dtype=[('f0', '<i8'), ('f1', '<f8')])
    >>> rfn.merge_arrays((np.array([1, 2]).view([('a', np.int64)]),
    ...               np.array([10., 20., 30.])),
    ...              usemask=False, asrecarray=True)
    rec.array([( 1, 10.), ( 2, 20.), (-1, 30.)],
              dtype=[('a', '<i8'), ('f1', '<f8')])
    

Go BackOpen In Tab

numpy.lib.recfunctions.rec_append_fields(_base_ , _names_ , _data_ , _dtypes =None_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L730-L762)[#](#numpy.lib.recfunctions.rec_append_fields "Link to this definition")
    

Add new fields to an existing array.

The names of the fields are given with the _names_ arguments, the corresponding values with the _data_ arguments. If a single field is appended, _names_ , _data_ and _dtypes_ do not have to be lists but just values.

Parameters:
    

**base** array
    

Input array to extend.

**names** string, sequence
    

String or sequence of strings corresponding to the names of the new fields.

**data** array or sequence of arrays
    

Array or sequence of arrays storing the fields to add to the base.

**dtypes** sequence of datatypes, optional
    

Datatype or sequence of datatypes. If None, the datatypes are estimated from the _data_.

Returns:
    

**appended_array** np.recarray
    

See also

[`append_fields`](#numpy.lib.recfunctions.append_fields "numpy.lib.recfunctions.append_fields")
    

numpy.lib.recfunctions.rec_drop_fields(_base_ , _drop_names_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L595-L600)[#](#numpy.lib.recfunctions.rec_drop_fields "Link to this definition")
    

Returns a new numpy.recarray with fields in _drop_names_ dropped.

numpy.lib.recfunctions.rec_join(_key_ , _r1_ , _r2_ , _jointype ='inner'_, _r1postfix ='1'_, _r2postfix ='2'_, _defaults =None_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1665-L1678)[#](#numpy.lib.recfunctions.rec_join "Link to this definition")
    

Join arrays _r1_ and _r2_ on keys. Alternative to join_by, that always returns a np.recarray.

See also

[`join_by`](#numpy.lib.recfunctions.join_by "numpy.lib.recfunctions.join_by")
    

equivalent function

numpy.lib.recfunctions.recursive_fill_fields(_input_ , _output_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L31-L68)[#](#numpy.lib.recfunctions.recursive_fill_fields "Link to this definition")
    

Fills fields from output with fields from input, with support for nested structures.

Parameters:
    

**input** ndarray
    

Input array.

**output** ndarray
    

Output array.

Notes

  * _output_ should be at least the same size as _input_




Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> a = np.array([(1, 10.), (2, 20.)], dtype=[('A', np.int64), ('B', np.float64)])
    >>> b = np.zeros((3,), dtype=a.dtype)
    >>> rfn.recursive_fill_fields(a, b)
    array([(1, 10.), (2, 20.), (0,  0.)], dtype=[('A', '<i8'), ('B', '<f8')])
    

Go BackOpen In Tab

numpy.lib.recfunctions.rename_fields(_base_ , _namemapper_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L607-L645)[#](#numpy.lib.recfunctions.rename_fields "Link to this definition")
    

Rename the fields from a flexible-datatype ndarray or recarray.

Nested fields are supported.

Parameters:
    

**base** ndarray
    

Input array whose fields must be modified.

**namemapper** dictionary
    

Dictionary mapping old field names to their new version.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> a = np.array([(1, (2, [3.0, 30.])), (4, (5, [6.0, 60.]))],
    ...   dtype=[('a', int),('b', [('ba', float), ('bb', (float, 2))])])
    >>> rfn.rename_fields(a, {'a':'A', 'bb':'BB'})
    array([(1, (2., [ 3., 30.])), (4, (5., [ 6., 60.]))],
          dtype=[('A', '<i8'), ('b', [('ba', '<f8'), ('BB', '<f8', (2,))])])
    

Go BackOpen In Tab

numpy.lib.recfunctions.repack_fields(_a_ , _align =False_, _recurse =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L769-L851)[#](#numpy.lib.recfunctions.repack_fields "Link to this definition")
    

Re-pack the fields of a structured array or dtype in memory.

The memory layout of structured datatypes allows fields at arbitrary byte offsets. This means the fields can be separated by padding bytes, their offsets can be non-monotonically increasing, and they can overlap.

This method removes any overlaps and reorders the fields in memory so they have increasing byte offsets, and adds or removes padding bytes depending on the _align_ option, which behaves like the _align_ option to [`numpy.dtype`](../reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype").

If _align=False_ , this method produces a “packed” memory layout in which each field starts at the byte the previous field ended, and any padding bytes are removed.

If _align=True_ , this methods produces an “aligned” memory layout in which each field’s offset is a multiple of its alignment, and the total itemsize is a multiple of the largest alignment, by adding padding bytes as needed.

Parameters:
    

**a** ndarray or dtype
    

array or dtype for which to repack the fields.

**align** boolean
    

If true, use an “aligned” memory layout, otherwise use a “packed” layout.

**recurse** boolean
    

If True, also repack nested structures.

Returns:
    

**repacked** ndarray or dtype
    

Copy of _a_ with fields repacked, or _a_ itself if no repacking was needed.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    
    
    
    >>> from numpy.lib import recfunctions as rfn
    >>> def print_offsets(d):
    ...     print("offsets:", [d.fields[name][1] for name in d.names])
    ...     print("itemsize:", d.itemsize)
    ...
    >>> dt = np.dtype('u1, <i8, <f8', align=True)
    >>> dt
    dtype({'names': ['f0', 'f1', 'f2'], 'formats': ['u1', '<i8', '<f8'], 'offsets': [0, 8, 16], 'itemsize': 24}, align=True)
    >>> print_offsets(dt)
    offsets: [0, 8, 16]
    itemsize: 24
    >>> packed_dt = rfn.repack_fields(dt)
    >>> packed_dt
    dtype([('f0', 'u1'), ('f1', '<i8'), ('f2', '<f8')])
    >>> print_offsets(packed_dt)
    offsets: [0, 1, 9]
    itemsize: 17
    

Go BackOpen In Tab

numpy.lib.recfunctions.require_fields(_array_ , _required_dtype_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1273-L1315)[#](#numpy.lib.recfunctions.require_fields "Link to this definition")
    

Casts a structured array to a new dtype using assignment by field-name.

This function assigns from the old to the new array by name, so the value of a field in the output array is the value of the field with the same name in the source array. This has the effect of creating a new ndarray containing only the fields “required” by the required_dtype.

If a field name in the required_dtype does not exist in the input array, that field is created and set to 0 in the output array.

Parameters:
    

**a** ndarray
    

array to cast

**required_dtype** dtype
    

datatype for output array

Returns:
    

**out** ndarray
    

array with the new dtype, with field values copied from the fields in the input array with the same name

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    
    
    
    >>> from numpy.lib import recfunctions as rfn
    >>> a = np.ones(4, dtype=[('a', 'i4'), ('b', 'f8'), ('c', 'u1')])
    >>> rfn.require_fields(a, [('b', 'f4'), ('c', 'u1')])
    array([(1., 1), (1., 1), (1., 1), (1., 1)],
      dtype=[('b', '<f4'), ('c', 'u1')])
    >>> rfn.require_fields(a, [('b', 'f4'), ('newf', 'u1')])
    array([(1., 0), (1., 0), (1., 0), (1., 0)],
      dtype=[('b', '<f4'), ('newf', 'u1')])
    

Go BackOpen In Tab

numpy.lib.recfunctions.stack_arrays(_arrays_ , _defaults =None_, _usemask =True_, _asrecarray =False_, _autoconvert =False_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1323-L1408)[#](#numpy.lib.recfunctions.stack_arrays "Link to this definition")
    

Superposes arrays fields by fields

Parameters:
    

**arrays** array or sequence
    

Sequence of input arrays.

**defaults** dictionary, optional
    

Dictionary mapping field names to the corresponding default values.

**usemask**{True, False}, optional
    

Whether to return a MaskedArray (or MaskedRecords is _asrecarray==True_) or an ndarray.

**asrecarray**{False, True}, optional
    

Whether to return a recarray (or MaskedRecords if _usemask==True_) or just a flexible-type ndarray.

**autoconvert**{False, True}, optional
    

Whether automatically cast the type of the field to the maximum.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    >>> from numpy.lib import recfunctions as rfn
    >>> x = np.array([1, 2,])
    >>> rfn.stack_arrays(x) is x
    True
    >>> z = np.array([('A', 1), ('B', 2)], dtype=[('A', '|S3'), ('B', float)])
    >>> zz = np.array([('a', 10., 100.), ('b', 20., 200.), ('c', 30., 300.)],
    ...   dtype=[('A', '|S3'), ('B', np.double), ('C', np.double)])
    >>> test = rfn.stack_arrays((z,zz))
    >>> test
    masked_array(data=[(b'A', 1.0, --), (b'B', 2.0, --), (b'a', 10.0, 100.0),
                       (b'b', 20.0, 200.0), (b'c', 30.0, 300.0)],
                 mask=[(False, False,  True), (False, False,  True),
                       (False, False, False), (False, False, False),
                       (False, False, False)],
           fill_value=(b'N/A', 1e+20, 1e+20),
                dtype=[('A', 'S3'), ('B', '<f8'), ('C', '<f8')])
    

Go BackOpen In Tab

numpy.lib.recfunctions.structured_to_unstructured(_arr_ , _dtype =None_, _copy =False_, _casting ='unsafe'_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L939-L1067)[#](#numpy.lib.recfunctions.structured_to_unstructured "Link to this definition")
    

Converts an n-D structured array into an (n+1)-D unstructured array.

The new array will have a new last dimension equal in size to the number of field-elements of the input array. If not supplied, the output datatype is determined from the numpy type promotion rules applied to all the field datatypes.

Nested fields, as well as each element of any subarray fields, all count as a single field-elements.

Parameters:
    

**arr** ndarray
    

Structured array or dtype to convert. Cannot contain object datatype.

**dtype** dtype, optional
    

The dtype of the output unstructured array.

**copy** bool, optional
    

If true, always return a copy. If false, a view is returned if possible, such as when the _dtype_ and strides of the fields are suitable and the array subtype is one of [`numpy.ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), [`numpy.recarray`](../reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray") or [`numpy.memmap`](../reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap").

Changed in version 1.25.0: A view can now be returned if the fields are separated by a uniform stride.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional
    

See casting argument of [`numpy.ndarray.astype`](../reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype"). Controls what kind of data casting may occur.

Returns:
    

**unstructured** ndarray
    

Unstructured array with one more dimension.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    
    
    
    >>> from numpy.lib import recfunctions as rfn
    >>> a = np.zeros(4, dtype=[('a', 'i4'), ('b', 'f4,u2'), ('c', 'f4', 2)])
    >>> a
    array([(0, (0., 0), [0., 0.]), (0, (0., 0), [0., 0.]),
           (0, (0., 0), [0., 0.]), (0, (0., 0), [0., 0.])],
          dtype=[('a', '<i4'), ('b', [('f0', '<f4'), ('f1', '<u2')]), ('c', '<f4', (2,))])
    >>> rfn.structured_to_unstructured(a)
    array([[0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0.]])
    
    
    
    >>> b = np.array([(1, 2, 5), (4, 5, 7), (7, 8 ,11), (10, 11, 12)],
    ...              dtype=[('x', 'i4'), ('y', 'f4'), ('z', 'f8')])
    >>> np.mean(rfn.structured_to_unstructured(b[['x', 'z']]), axis=-1)
    array([ 3. ,  5.5,  9. , 11. ])
    

Go BackOpen In Tab

numpy.lib.recfunctions.unstructured_to_structured(_arr_ , _dtype =None_, _names =None_, _align =False_, _copy =False_, _casting ='unsafe'_)[[source]](https://github.com/numpy/numpy/blob/main/numpy/lib/recfunctions.py#L1074-L1180)[#](#numpy.lib.recfunctions.unstructured_to_structured "Link to this definition")
    

Converts an n-D unstructured array into an (n-1)-D structured array.

The last dimension of the input array is converted into a structure, with number of field-elements equal to the size of the last dimension of the input array. By default all output fields have the input array’s dtype, but an output structured dtype with an equal number of fields-elements can be supplied instead.

Nested fields, as well as each element of any subarray fields, all count towards the number of field-elements.

Parameters:
    

**arr** ndarray
    

Unstructured array or dtype to convert.

**dtype** dtype, optional
    

The structured dtype of the output array

**names** list of strings, optional
    

If dtype is not supplied, this specifies the field names for the output dtype, in order. The field dtypes will be the same as the input array.

**align** boolean, optional
    

Whether to create an aligned memory layout.

**copy** bool, optional
    

See copy argument to [`numpy.ndarray.astype`](../reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype"). If true, always return a copy. If false, and _dtype_ requirements are satisfied, a view is returned.

**casting**{‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’}, optional
    

See casting argument of [`numpy.ndarray.astype`](../reference/generated/numpy.ndarray.astype.html#numpy.ndarray.astype "numpy.ndarray.astype"). Controls what kind of data casting may occur.

Returns:
    

**structured** ndarray
    

Structured array with fewer dimensions.

Examples

Try it in your browser!
    
    
    >>> import numpy as np
    
    
    
    >>> from numpy.lib import recfunctions as rfn
    >>> dt = np.dtype([('a', 'i4'), ('b', 'f4,u2'), ('c', 'f4', 2)])
    >>> a = np.arange(20).reshape((4,5))
    >>> a
    array([[ 0,  1,  2,  3,  4],
           [ 5,  6,  7,  8,  9],
           [10, 11, 12, 13, 14],
           [15, 16, 17, 18, 19]])
    >>> rfn.unstructured_to_structured(a, dt)
    array([( 0, ( 1.,  2), [ 3.,  4.]), ( 5, ( 6.,  7), [ 8.,  9.]),
           (10, (11., 12), [13., 14.]), (15, (16., 17), [18., 19.])],
          dtype=[('a', '<i4'), ('b', [('f0', '<f4'), ('f1', '<u2')]), ('c', '<f4', (2,))])
    

Go BackOpen In Tab

[ __ previous Working with Arrays of Strings And Bytes ](basics.strings.html "previous page") [ next Universal functions (`ufunc`) basics __](basics.ufuncs.html "next page")

__On this page

  * [Introduction](#introduction)
  * [Structured datatypes](#structured-datatypes)
    * [Structured datatype creation](#structured-datatype-creation)
    * [Manipulating and displaying structured datatypes](#manipulating-and-displaying-structured-datatypes)
    * [Automatic byte offsets and alignment](#automatic-byte-offsets-and-alignment)
    * [Field titles](#field-titles)
    * [Union types](#union-types)
  * [Indexing and assignment to structured arrays](#indexing-and-assignment-to-structured-arrays)
    * [Assigning data to a structured array](#assigning-data-to-a-structured-array)
      * [Assignment from Python Native Types (Tuples)](#assignment-from-python-native-types-tuples)
      * [Assignment from Scalars](#assignment-from-scalars)
      * [Assignment from other Structured Arrays](#assignment-from-other-structured-arrays)
      * [Assignment involving subarrays](#assignment-involving-subarrays)
    * [Indexing structured arrays](#indexing-structured-arrays)
      * [Accessing Individual Fields](#accessing-individual-fields)
      * [Accessing Multiple Fields](#accessing-multiple-fields)
      * [Indexing with an Integer to get a Structured Scalar](#indexing-with-an-integer-to-get-a-structured-scalar)
    * [Viewing structured arrays containing objects](#viewing-structured-arrays-containing-objects)
    * [Structure comparison and promotion](#structure-comparison-and-promotion)
  * [Record arrays](#record-arrays)
    * [Recarray helper functions](#module-numpy.lib.recfunctions)
      * [`append_fields`](#numpy.lib.recfunctions.append_fields)
      * [`apply_along_fields`](#numpy.lib.recfunctions.apply_along_fields)
      * [`assign_fields_by_name`](#numpy.lib.recfunctions.assign_fields_by_name)
      * [`drop_fields`](#numpy.lib.recfunctions.drop_fields)
      * [`find_duplicates`](#numpy.lib.recfunctions.find_duplicates)
      * [`flatten_descr`](#numpy.lib.recfunctions.flatten_descr)
      * [`get_fieldstructure`](#numpy.lib.recfunctions.get_fieldstructure)
      * [`get_names`](#numpy.lib.recfunctions.get_names)
      * [`get_names_flat`](#numpy.lib.recfunctions.get_names_flat)
      * [`join_by`](#numpy.lib.recfunctions.join_by)
      * [`merge_arrays`](#numpy.lib.recfunctions.merge_arrays)
      * [`rec_append_fields`](#numpy.lib.recfunctions.rec_append_fields)
      * [`rec_drop_fields`](#numpy.lib.recfunctions.rec_drop_fields)
      * [`rec_join`](#numpy.lib.recfunctions.rec_join)
      * [`recursive_fill_fields`](#numpy.lib.recfunctions.recursive_fill_fields)
      * [`rename_fields`](#numpy.lib.recfunctions.rename_fields)
      * [`repack_fields`](#numpy.lib.recfunctions.repack_fields)
      * [`require_fields`](#numpy.lib.recfunctions.require_fields)
      * [`stack_arrays`](#numpy.lib.recfunctions.stack_arrays)
      * [`structured_to_unstructured`](#numpy.lib.recfunctions.structured_to_unstructured)
      * [`unstructured_to_structured`](#numpy.lib.recfunctions.unstructured_to_structured)

---

## NumPy for MATLAB users

**Source:** [https://numpy.org/devdocs/user/numpy-for-matlab-users.html](https://numpy.org/devdocs/user/numpy-for-matlab-users.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * NumPy for MATLAB users



# NumPy for MATLAB users[#](#numpy-for-matlab-users "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

MATLAB® and NumPy have a lot in common, but NumPy was created to work with Python, not to be a MATLAB clone. This guide will help MATLAB users get started with NumPy.

## Some key differences[#](#some-key-differences "Link to this heading")

In MATLAB, the basic type, even for scalars, is a multidimensional array. Array assignments in MATLAB are stored as 2D arrays of double precision floating point numbers, unless you specify the number of dimensions and type. Operations on the 2D instances of these arrays are modeled on matrix operations in linear algebra. | In NumPy, the basic type is a multidimensional `array`. Array assignments in NumPy are usually stored as [n-dimensional arrays](../reference/arrays.html#arrays) with the minimum type required to hold the objects in sequence, unless you specify the number of dimensions and type. NumPy performs operations element-by-element, so multiplying 2D arrays with `*` is not a matrix multiplication – it’s an element-by-element multiplication. (The `@` operator, available since Python 3.5, can be used for conventional matrix multiplication.)  
---|---  
MATLAB numbers indices from 1; `a(1)` is the first element. [See note INDEXING](#numpy-for-matlab-users-notes) | NumPy, like Python, numbers indices from 0; `a[0]` is the first element.  
MATLAB’s scripting language was created for linear algebra so the syntax for some array manipulations is more compact than NumPy’s. On the other hand, the API for adding GUIs and creating full-fledged applications is more or less an afterthought. | NumPy is based on Python, a general-purpose language. The advantage to NumPy is access to Python libraries including: [SciPy](https://www.scipy.org/), [Matplotlib](https://matplotlib.org/), [Pandas](https://pandas.pydata.org/), [OpenCV](https://opencv.org/), and more. In addition, Python is often [embedded as a scripting language](https://en.wikipedia.org/wiki/List_of_Python_software#Embedded_as_a_scripting_language) in other software, allowing NumPy to be used there too.  
MATLAB array slicing uses pass-by-value semantics, with a lazy copy-on-write scheme to prevent creating copies until they are needed. Slicing operations copy parts of the array. | NumPy array slicing uses pass-by-reference, that does not copy the arguments. Slicing operations are views into an array.  
  
## Rough equivalents[#](#rough-equivalents "Link to this heading")

The table below gives rough equivalents for some common MATLAB expressions. These are similar expressions, not equivalents. For details, see the [documentation](../reference/index.html#reference).

In the table below, it is assumed that you have executed the following commands in Python:
    
    
    import numpy as np
    from scipy import io, integrate, linalg, signal
    from scipy.sparse.linalg import cg, eigs
    

Also assume below that if the Notes talk about “matrix” that the arguments are two-dimensional entities.

### General purpose equivalents[#](#general-purpose-equivalents "Link to this heading")

MATLAB | NumPy | Notes  
---|---|---  
`help func` | `info(func)` or `help(func)` or `func?` (in IPython) | get help on the function _func_  
`which func` | [see note HELP](#numpy-for-matlab-users-notes) | find out where _func_ is defined  
`type func` | `np.source(func)` or `func??` (in IPython) | print source for _func_ (if not a native function)  
`% comment` | `# comment` | comment a line of code with the text `comment`  
      
    
    for i=1:3
        fprintf('%i\n',i)
    end
    

| 
    
    
    for i in range(1, 4):
       print(i)
    

| use a for-loop to print the numbers 1, 2, and 3 using [`range`](https://docs.python.org/3/library/stdtypes.html#range "\(in Python v3.14\)")  
`a && b` | `a and b` | short-circuiting logical AND operator ([Python native operator](https://docs.python.org/3/library/stdtypes.html#boolean "\(in Python v3.14\)")); scalar arguments only  
`a || b` | `a or b` | short-circuiting logical OR operator ([Python native operator](https://docs.python.org/3/library/stdtypes.html#boolean "\(in Python v3.14\)")); scalar arguments only  
      
    
    >> 4 == 4
    ans = 1
    >> 4 == 5
    ans = 0
    

| 
    
    
    >>> 4 == 4
    True
    >>> 4 == 5
    False
    

| The [boolean objects](https://docs.python.org/3/library/stdtypes.html#bltin-boolean-values "\(in Python v3.14\)") in Python are `True` and `False`, as opposed to MATLAB logical types of `1` and `0`.  
      
    
    a=4
    if a==4
        fprintf('a = 4\n')
    elseif a==5
        fprintf('a = 5\n')
    end
    

| 
    
    
    a = 4
    if a == 4:
        print('a = 4')
    elif a == 5:
        print('a = 5')
    

| create an if-else statement to check if `a` is 4 or 5 and print result  
`1*i`, `1*j`, `1i`, `1j` | `1j` | complex numbers  
`eps` | `np.finfo(float).eps` or `np.spacing(1)` | distance from 1 to the next larger representable real number in double precision  
`load data.mat` | `io.loadmat('data.mat')` | Load MATLAB variables saved to the file `data.mat`. (Note: When saving arrays to `data.mat` in MATLAB/Octave, use a recent binary format. [`scipy.io.loadmat`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.loadmat.html#scipy.io.loadmat "\(in SciPy v1.17.0\)") will create a dictionary with the saved arrays and further information.)  
`ode45` | `integrate.solve_ivp(f)` | integrate an ODE with Runge-Kutta 4,5  
`ode15s` | `integrate.solve_ivp(f, method='BDF')` | integrate an ODE with BDF method  
  
### Linear algebra equivalents[#](#linear-algebra-equivalents "Link to this heading")

MATLAB | NumPy | Notes  
---|---|---  
`ndims(a)` | `np.ndim(a)` or `a.ndim` | number of dimensions of array `a`  
`numel(a)` | `np.size(a)` or `a.size` | number of elements of array `a`  
`size(a)` | `np.shape(a)` or `a.shape` | “size” of array `a`  
`size(a,n)` | `a.shape[n-1]` | get the number of elements of the n-th dimension of array `a`. (Note that MATLAB uses 1 based indexing while Python uses 0 based indexing, See note [INDEXING](#numpy-for-matlab-users-notes))  
`[ 1 2 3; 4 5 6 ]` | `np.array([[1., 2., 3.], [4., 5., 6.]])` | define a 2x3 2D array  
`[ a b; c d ]` | `np.block([[a, b], [c, d]])` | construct a matrix from blocks `a`, `b`, `c`, and `d`  
`a(end)` | `a[-1]` | access last element in MATLAB vector (1xn or nx1) or 1D NumPy array `a` (length n)  
`a(2,5)` | `a[1, 4]` | access element in second row, fifth column in 2D array `a`  
`a(2,:)` | `a[1]` or `a[1, :]` | entire second row of 2D array `a`  
`a(1:5,:)` | `a[0:5]` or `a[:5]` or `a[0:5, :]` | first 5 rows of 2D array `a`  
`a(end-4:end,:)` | `a[-5:]` | last 5 rows of 2D array `a`  
`a(1:3,5:9)` | `a[0:3, 4:9]` | The first through third rows and fifth through ninth columns of a 2D array, `a`.  
`a([2,4,5],[1,3])` | `a[np.ix_([1, 3, 4], [0, 2])]` | rows 2,4 and 5 and columns 1 and 3. This allows the matrix to be modified, and doesn’t require a regular slice.  
`a(3:2:21,:)` | `a[2:21:2,:]` | every other row of `a`, starting with the third and going to the twenty-first  
`a(1:2:end,:)` | `a[::2, :]` | every other row of `a`, starting with the first  
`a(end:-1:1,:)` or `flipud(a)` | `a[::-1,:]` | `a` with rows in reverse order  
`a([1:end 1],:)` | `a[np.r_[:len(a),0]]` | `a` with copy of the first row appended to the end  
`a.'` | `a.transpose()` or `a.T` | transpose of `a`  
`a'` | `a.conj().transpose()` or `a.conj().T` | conjugate transpose of `a`  
`a * b` | `a @ b` | matrix multiply  
`a .* b` | `a * b` | element-wise multiply  
`a./b` | `a/b` | element-wise divide  
`a.^3` | `a**3` | element-wise exponentiation  
`(a > 0.5)` | `(a > 0.5)` | matrix whose i,jth element is (a_ij > 0.5). The MATLAB result is an array of logical values 0 and 1. The NumPy result is an array of the boolean values `False` and `True`.  
`find(a > 0.5)` | `np.nonzero(a > 0.5)` | find the indices where (`a` > 0.5)  
`a(:,find(v > 0.5))` | `a[:,np.nonzero(v > 0.5)[0]]` | extract the columns of `a` where vector v > 0.5  
`a(:,find(v>0.5))` | `a[:, v.T > 0.5]` | extract the columns of `a` where column vector v > 0.5  
`a(a<0.5)=0` | `a[a < 0.5]=0` | `a` with elements less than 0.5 zeroed out  
`a .* (a>0.5)` | `a * (a > 0.5)` | `a` with elements less than 0.5 zeroed out  
`a(:) = 3` | `a[:] = 3` | set all values to the same scalar value  
`y=x` | `y = x.copy()` | NumPy assigns by reference  
`y=x(2,:)` | `y = x[1, :].copy()` | NumPy slices are by reference  
`y=x(:)` | `y = x.flatten()` | turn array into vector (note that this forces a copy). To obtain the same data ordering as in MATLAB, use `x.flatten('F')`.  
`1:10` | `np.arange(1., 11.)` or `np.r_[1.:11.]` or `np.r_[1:10:10j]` | create an increasing vector (see note [RANGES](#numpy-for-matlab-users-notes))  
`0:9` | `np.arange(10.)` or `np.r_[:10.]` or `np.r_[:9:10j]` | create an increasing vector (see note [RANGES](#numpy-for-matlab-users-notes))  
`[1:10]'` | `np.arange(1.,11.)[:, np.newaxis]` | create a column vector  
`zeros(3,4)` | `np.zeros((3, 4))` | 3x4 two-dimensional array full of 64-bit floating point zeros  
`zeros(3,4,5)` | `np.zeros((3, 4, 5))` | 3x4x5 three-dimensional array full of 64-bit floating point zeros  
`ones(3,4)` | `np.ones((3, 4))` | 3x4 two-dimensional array full of 64-bit floating point ones  
`eye(3)` | `np.eye(3)` | 3x3 identity matrix  
`diag(a)` | `np.diag(a)` | returns a vector of the diagonal elements of 2D array, `a`  
`diag(v,0)` | `np.diag(v, 0)` | returns a square diagonal matrix whose nonzero values are the elements of vector, `v`  
      
    
    rng(42,'twister')
    rand(3,4)
    

| 
    
    
    from numpy.random import default_rng
    rng = default_rng(42)
    rng.random((3, 4))
    

or older version: `random.rand((3, 4))` | generate a random 3x4 array with default random number generator and seed = 42  
`linspace(1,3,4)` | `np.linspace(1,3,4)` | 4 equally spaced samples between 1 and 3, inclusive  
`[x,y]=meshgrid(0:8,0:5)` | `np.mgrid[0:9.,0:6.]` or `np.meshgrid(r_[0:9.],r_[0:6.])` | two 2D arrays: one of x values, the other of y values  
| `ogrid[0:9.,0:6.]` or `np.ix_(np.r_[0:9.],np.r_[0:6.]` | the best way to eval functions on a grid  
`[x,y]=meshgrid([1,2,4],[2,4,5])` | `np.meshgrid([1,2,4],[2,4,5])` |   
| `np.ix_([1,2,4],[2,4,5])` | the best way to eval functions on a grid  
`repmat(a, m, n)` | `np.tile(a, (m, n))` | create m by n copies of `a`  
`[a b]` | `np.concatenate((a,b),1)` or `np.hstack((a,b))` or `np.column_stack((a,b))` or `np.c_[a,b]` | concatenate columns of `a` and `b`  
`[a; b]` | `np.concatenate((a,b))` or `np.vstack((a,b))` or `np.r_[a,b]` | concatenate rows of `a` and `b`  
`max(max(a))` | `a.max()` or `np.nanmax(a)` | maximum element of `a` (with ndims(a)<=2 for MATLAB, if there are NaN’s, `nanmax` will ignore these and return largest value)  
`max(a)` | `a.max(0)` | maximum element of each column of array `a`  
`max(a,[],2)` | `a.max(1)` | maximum element of each row of array `a`  
`max(a,b)` | `np.maximum(a, b)` | compares `a` and `b` element-wise, and returns the maximum value from each pair  
`norm(v)` | `np.sqrt(v @ v)` or `np.linalg.norm(v)` | L2 norm of vector `v`  
`a & b` | `logical_and(a,b)` | element-by-element AND operator (NumPy ufunc) [See note LOGICOPS](#numpy-for-matlab-users-notes)  
`a | b` | `np.logical_or(a,b)` | element-by-element OR operator (NumPy ufunc) [See note LOGICOPS](#numpy-for-matlab-users-notes)  
`bitand(a,b)` | `a & b` | bitwise AND operator (Python native and NumPy ufunc)  
`bitor(a,b)` | `a | b` | bitwise OR operator (Python native and NumPy ufunc)  
`inv(a)` | `linalg.inv(a)` | inverse of square 2D array `a`  
`pinv(a)` | `linalg.pinv(a)` | pseudo-inverse of 2D array `a`  
`rank(a)` | `np.linalg.matrix_rank(a)` | matrix rank of a 2D array `a`  
`a\b` | `linalg.solve(a, b)` if `a` is square; `linalg.lstsq(a, b)` otherwise | solution of a x = b for x  
`b/a` | Solve `a.T x.T = b.T` instead | solution of x a = b for x  
`[U,S,V]=svd(a)` | `U, S, Vh = linalg.svd(a); V = Vh.T` | singular value decomposition of `a`  
`chol(a)` | `linalg.cholesky(a)` | Cholesky factorization of a 2D array  
`[V,D]=eig(a)` | `D,V = linalg.eig(a)` | eigenvalues \\(\lambda\\) and eigenvectors \\(v\\) of `a`, where \\(\mathbf{a} v = \lambda v\\)  
`[V,D]=eig(a,b)` | `D,V = linalg.eig(a, b)` | eigenvalues \\(\lambda\\) and eigenvectors \\(v\\) of `a`, `b` where \\(\mathbf{a} v = \lambda \mathbf{b} v\\)  
`[V,D]=eigs(a,3)` | `D,V = eigs(a, k=3)` | find the `k=3` largest eigenvalues and eigenvectors of 2D array, `a`  
`[Q,R]=qr(a,0)` | `Q,R = linalg.qr(a)` | QR decomposition  
`[L,U,P]=lu(a)` where `a==P'*L*U` | `P,L,U = linalg.lu(a)` where `a == P@L@U` | LU decomposition with partial pivoting (note: P(MATLAB) == transpose(P(NumPy)))  
`conjgrad` | `cg` | conjugate gradients solver  
`fft(a)` | `np.fft.fft(a)` | Fourier transform of `a`  
`ifft(a)` | `np.fft.ifft(a)` | inverse Fourier transform of `a`  
`sort(a)` | `np.sort(a)` or `a.sort(axis=0)` | sort each column of a 2D array, `a`  
`sort(a, 2)` | `np.sort(a, axis=1)` or `a.sort(axis=1)` | sort the each row of 2D array, `a`  
`[b,I]=sortrows(a,1)` | `I = np.argsort(a[:, 0]); b = a[I,:]` | save the array `a` as array `b` with rows sorted by the first column  
`x = Z\y` | `x = linalg.lstsq(Z, y)` | perform a linear regression of the form \\(\mathbf{Zx}=\mathbf{y}\\)  
`decimate(x, q)` | `signal.resample(x, np.ceil(len(x)/q))` | downsample with low-pass filtering  
`unique(a)` | `np.unique(a)` | a vector of unique values in array `a`  
`squeeze(a)` | `a.squeeze()` | remove singleton dimensions of array `a`. Note that MATLAB will always return arrays of 2D or higher while NumPy will return arrays of 0D or higher  
  
## Notes[#](#notes "Link to this heading")

**Submatrix** : Assignment to a submatrix can be done with lists of indices using the `ix_` command. E.g., for 2D array `a`, one might do: `ind=[1, 3]; a[np.ix_(ind, ind)] += 100`.

**HELP** : There is no direct equivalent of MATLAB’s `which` command, but the commands [`help`](https://docs.python.org/3/library/functions.html#help "\(in Python v3.14\)") will usually list the filename where the function is located. Python also has an `inspect` module (do `import inspect`) which provides a `getfile` that often works.

**INDEXING** : MATLAB uses one based indexing, so the initial element of a sequence has index 1. Python uses zero based indexing, so the initial element of a sequence has index 0. Confusion and flamewars arise because each has advantages and disadvantages. One based indexing is consistent with common human language usage, where the “first” element of a sequence has index 1. Zero based indexing [simplifies indexing](https://groups.google.com/group/comp.lang.python/msg/1bf4d925dfbf368?q=g:thl3498076713d&hl=en). See also [a text by prof.dr. Edsger W. Dijkstra](https://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html).

**RANGES** : In MATLAB, `0:5` can be used as both a range literal and a ‘slice’ index (inside parentheses); however, in Python, constructs like `0:5` can _only_ be used as a slice index (inside square brackets). Thus the somewhat quirky `r_` object was created to allow NumPy to have a similarly terse range construction mechanism. Note that `r_` is not called like a function or a constructor, but rather _indexed_ using square brackets, which allows the use of Python’s slice syntax in the arguments.

**LOGICOPS** : `&` or `|` in NumPy is bitwise AND/OR, while in MATLAB & and `|` are logical AND/OR. The two can appear to work the same, but there are important differences. If you would have used MATLAB’s `&` or `|` operators, you should use the NumPy ufuncs `logical_and`/`logical_or`. The notable differences between MATLAB’s and NumPy’s `&` and `|` operators are:

  * Non-logical {0,1} inputs: NumPy’s output is the bitwise AND of the inputs. MATLAB treats any non-zero value as 1 and returns the logical AND. For example `(3 & 4)` in NumPy is `0`, while in MATLAB both `3` and `4` are considered logical true and `(3 & 4)` returns `1`.

  * Precedence: NumPy’s & operator is higher precedence than logical operators like `<` and `>`; MATLAB’s is the reverse.




If you know you have boolean arguments, you can get away with using NumPy’s bitwise operators, but be careful with parentheses, like this: `z = (x > 1) & (x < 2)`. The absence of NumPy operator forms of `logical_and` and `logical_or` is an unfortunate consequence of Python’s design.

**RESHAPE and LINEAR INDEXING** : MATLAB always allows multi-dimensional arrays to be accessed using scalar or linear indices, NumPy does not. Linear indices are common in MATLAB programs, e.g. `find()` on a matrix returns them, whereas NumPy’s find behaves differently. When converting MATLAB code it might be necessary to first reshape a matrix to a linear sequence, perform some indexing operations and then reshape back. As reshape (usually) produces views onto the same storage, it should be possible to do this fairly efficiently. Note that the scan order used by reshape in NumPy defaults to the ‘C’ order, whereas MATLAB uses the Fortran order. If you are simply converting to a linear sequence and back this doesn’t matter. But if you are converting reshapes from MATLAB code which relies on the scan order, then this MATLAB code: `z = reshape(x,3,4);` should become `z = x.reshape(3,4,order='F').copy()` in NumPy.

## ‘array’ or ‘matrix’? Which should I use?[#](#array-or-matrix-which-should-i-use "Link to this heading")

Historically, NumPy has provided a special matrix type, _np.matrix_ , which is a subclass of ndarray which makes binary operations linear algebra operations. You may see it used in some existing code instead of _np.array_. So, which one to use?

### Short answer[#](#short-answer "Link to this heading")

**Use arrays**.

  * They support multidimensional array algebra that is supported in MATLAB

  * They are the standard vector/matrix/tensor type of NumPy. Many NumPy functions return arrays, not matrices.

  * There is a clear distinction between element-wise operations and linear algebra operations.

  * You can have standard vectors or row/column vectors if you like.




Until Python 3.5 the only disadvantage of using the array type was that you had to use `dot` instead of `*` to multiply (reduce) two tensors (scalar product, matrix vector multiplication etc.). Since Python 3.5 you can use the matrix multiplication `@` operator.

Given the above, we intend to deprecate `matrix` eventually.

### Long answer[#](#long-answer "Link to this heading")

NumPy contains both an `array` class and a `matrix` class. The `array` class is intended to be a general-purpose n-dimensional array for many kinds of numerical computing, while `matrix` is intended to facilitate linear algebra computations specifically. In practice there are only a handful of key differences between the two.

  * Operators `*` and `@`, functions `dot()`, and `multiply()`:

    * For `array`, `*` **means element-wise multiplication** , while `@` **means matrix multiplication** ; they have associated functions `multiply()` and `dot()`.

    * For `matrix`, `*` **means matrix multiplication** , and for element-wise multiplication one has to use the `multiply()` function.

  * Handling of vectors (one-dimensional arrays)

    * For `array`, the **vector shapes 1xN, Nx1, and N are all different things**. Operations like `A[:,1]` return a one-dimensional array of shape N, not a two-dimensional array of shape Nx1. Transpose on a one-dimensional `array` does nothing.

    * For `matrix`, **one-dimensional arrays are always upconverted to 1xN or Nx1 matrices** (row or column vectors). `A[:,1]` returns a two-dimensional matrix of shape Nx1.

  * Handling of higher-dimensional arrays (ndim > 2)

    * `array` objects **can have number of dimensions > 2**;

    * `matrix` objects **always have exactly two dimensions**.

  * Convenience attributes

    * `array` **has a .T attribute** , which returns the transpose of the data.

    * `matrix` **also has .H, .I, and .A attributes** , which return the conjugate transpose, inverse, and `asarray()` of the matrix, respectively.

  * Convenience constructor

    * The `array` constructor **takes (nested) Python sequences as initializers**. As in, `array([[1,2,3],[4,5,6]])`.

    * The `matrix` constructor additionally **takes a convenient string initializer**. As in `matrix("[1 2 3; 4 5 6]")`.




There are pros and cons to using both:

  * `array`

    * `:)` Element-wise multiplication is easy: `A*B`.

    * `:(` You have to remember that matrix multiplication has its own operator, `@`.

    * `:)` You can treat one-dimensional arrays as _either_ row or column vectors. `A @ v` treats `v` as a column vector, while `v @ A` treats `v` as a row vector. This can save you having to type a lot of transposes.

    * `:)` `array` is the “default” NumPy type, so it gets the most testing, and is the type most likely to be returned by 3rd party code that uses NumPy.

    * `:)` Is quite at home handling data of any number of dimensions.

    * `:)` Closer in semantics to tensor algebra, if you are familiar with that.

    * `:)` _All_ operations (`*`, `/`, `+`, `-` etc.) are element-wise.

    * `:(` Sparse matrices from `scipy.sparse` do not interact as well with arrays.

  * `matrix`

    * `:\\` Behavior is more like that of MATLAB matrices.

    * `<:(` Maximum of two-dimensional. To hold three-dimensional data you need `array` or perhaps a Python list of `matrix`.

    * `<:(` Minimum of two-dimensional. You cannot have vectors. They must be cast as single-column or single-row matrices.

    * `<:(` Since `array` is the default in NumPy, some functions may return an `array` even if you give them a `matrix` as an argument. This shouldn’t happen with NumPy functions (if it does it’s a bug), but 3rd party code based on NumPy may not honor type preservation like NumPy does.

    * `:)` `A*B` is matrix multiplication, so it looks just like you write it in linear algebra (For Python >= 3.5 plain arrays have the same convenience with the `@` operator).

    * `<:(` Element-wise multiplication requires calling a function, `multiply(A,B)`.

    * `<:(` The use of operator overloading is a bit illogical: `*` does not work element-wise but `/` does.

    * Interaction with `scipy.sparse` is a bit cleaner.




The `array` is thus much more advisable to use. Indeed, we intend to deprecate `matrix` eventually.

## Customizing your environment[#](#customizing-your-environment "Link to this heading")

In MATLAB the main tool available to you for customizing the environment is to modify the search path with the locations of your favorite functions. You can put such customizations into a startup script that MATLAB will run on startup.

NumPy, or rather Python, has similar facilities.

  * To modify your Python search path to include the locations of your own modules, define the `PYTHONPATH` environment variable.

  * To have a particular script file executed when the interactive Python interpreter is started, define the `PYTHONSTARTUP` environment variable to contain the name of your startup script.




Unlike MATLAB, where anything on your path can be called immediately, with Python you need to first do an ‘import’ statement to make functions in a particular file accessible.

For example you might make a startup script that looks like this (Note: this is just an example, not a statement of “best practices”):
    
    
    # Make all numpy available via shorter 'np' prefix
    import numpy as np
    #
    # Make the SciPy linear algebra functions available as linalg.func()
    # e.g. linalg.lu, linalg.eig (for general l*B@u==A@u solution)
    from scipy import linalg
    #
    # Define a Hermitian function
    def hermitian(A, **kwargs):
        return np.conj(A,**kwargs).T
    # Make a shortcut for hermitian:
    #    hermitian(A) --> H(A)
    H = hermitian
    

To use the deprecated _matrix_ and other _matlib_ functions:
    
    
    # Make all matlib functions accessible at the top level via M.func()
    import numpy.matlib as M
    # Make some matlib functions accessible directly at the top level via, e.g. rand(3,3)
    from numpy.matlib import matrix,rand,zeros,ones,empty,eye
    

## Links[#](#links "Link to this heading")

Another somewhat outdated MATLAB/NumPy cross-reference can be found at <https://mathesaurus.sf.net/>

An extensive list of tools for scientific work with Python can be found in the [topical software page](https://projects.scipy.org/topical-software.html).

See [List of Python software: scripting](https://en.wikipedia.org/wiki/List_of_Python_software#Embedded_as_a_scripting_language) for a list of software that use Python as a scripting language

MATLAB® and SimuLink® are registered trademarks of The MathWorks, Inc.

[ __ previous Universal functions (`ufunc`) basics ](basics.ufuncs.html "previous page") [ next NumPy how-tos __](howtos_index.html "next page")

__On this page

  * [Introduction](#introduction)
  * [Some key differences](#some-key-differences)
  * [Rough equivalents](#rough-equivalents)
    * [General purpose equivalents](#general-purpose-equivalents)
    * [Linear algebra equivalents](#linear-algebra-equivalents)
  * [Notes](#notes)
  * [‘array’ or ‘matrix’? Which should I use?](#array-or-matrix-which-should-i-use)
    * [Short answer](#short-answer)
    * [Long answer](#long-answer)
  * [Customizing your environment](#customizing-your-environment)
  * [Links](#links)

---

## What is NumPy?

**Source:** [https://numpy.org/devdocs/user/whatisnumpy.html](https://numpy.org/devdocs/user/whatisnumpy.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * What is NumPy?



# What is NumPy?[#](#what-is-numpy "Link to this heading")

NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") object. This encapsulates _n_ -dimensional arrays of homogeneous data types, with many operations being performed in compiled code for performance. There are several important differences between NumPy arrays and the standard Python sequences:

  * NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") will create a new array and delete the original.

  * The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory. The exception: one can have arrays of (Python, including NumPy) objects, thereby allowing for arrays of different sized elements.

  * NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python’s built-in sequences.

  * A growing plethora of scientific and mathematical Python-based packages are using NumPy arrays; though these typically support Python-sequence input, they convert such input to NumPy arrays prior to processing, and they often output NumPy arrays. In other words, in order to efficiently use much (perhaps even most) of today’s scientific/mathematical Python-based software, just knowing how to use Python’s built-in sequence types is insufficient - one also needs to know how to use NumPy arrays.




The points about sequence size and speed are particularly important in scientific computing. As a simple example, consider the case of multiplying each element in a 1-D sequence with the corresponding element in another sequence of the same length. If the data are stored in two Python lists, `a` and `b`, we could iterate over each element:
    
    
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    

This produces the correct answer, but if `a` and `b` each contain millions of numbers, we will pay the price for the inefficiencies of looping in Python. We could accomplish the same task much more quickly in C by writing (for clarity we neglect variable declarations and initializations, memory allocation, etc.)
    
    
    for (i = 0; i < rows; i++) {
      c[i] = a[i]*b[i];
    }
    

This saves all the overhead involved in interpreting the Python code and manipulating Python objects, but at the expense of the benefits gained from coding in Python. Furthermore, the coding work required increases with the dimensionality of our data. In the case of a 2-D array, for example, the C code (abridged as before) expands to
    
    
    for (i = 0; i < rows; i++) {
      for (j = 0; j < columns; j++) {
        c[i][j] = a[i][j]*b[i][j];
      }
    }
    

NumPy gives us the best of both worlds: element-by-element operations are the “default mode” when an [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") is involved, but the element-by-element operation is speedily executed by pre-compiled C code. In NumPy
    
    
    c = a * b
    

does what the earlier examples do, at near-C speeds, but with the code simplicity we expect from something based on Python. Indeed, the NumPy idiom is even simpler! This last example illustrates two of NumPy’s features which are the basis of much of its power: vectorization and broadcasting.

## Why is NumPy fast?[#](#why-is-numpy-fast "Link to this heading")

Vectorization describes the absence of any explicit looping, indexing, etc., in the code - these things are taking place, of course, just “behind the scenes” in optimized, pre-compiled C code. Vectorized code has many advantages, among which are:

  * vectorized code is more concise and easier to read

  * fewer lines of code generally means fewer bugs

  * the code more closely resembles standard mathematical notation (making it easier, typically, to correctly code mathematical constructs)

  * vectorization results in more “Pythonic” code. Without vectorization, our code would be littered with inefficient and difficult to read `for` loops.




Broadcasting is the term used to describe the implicit element-by-element behavior of operations; generally speaking, in NumPy all operations, not just arithmetic operations, but logical, bit-wise, functional, etc., behave in this implicit element-by-element fashion, i.e., they broadcast. Moreover, in the example above, `a` and `b` could be multidimensional arrays of the same shape, or a scalar and an array, or even two arrays with different shapes, provided that the smaller array is “expandable” to the shape of the larger in such a way that the resulting broadcast is unambiguous. For detailed “rules” of broadcasting see [Broadcasting](basics.broadcasting.html#basics-broadcasting).

## Who else uses NumPy?[#](#who-else-uses-numpy "Link to this heading")

NumPy fully supports an object-oriented approach, starting, once again, with [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"). For example, [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") is a class, possessing numerous methods and attributes. Many of its methods are mirrored by functions in the outer-most NumPy namespace, allowing the programmer to code in whichever paradigm they prefer. This flexibility has allowed the NumPy array dialect and NumPy [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") class to become the _de-facto_ language of multi-dimensional data interchange used in Python.

[ __ previous NumPy user guide ](index.html "previous page") [ next NumPy quickstart __](quickstart.html "next page")

__On this page

  * [Why is NumPy fast?](#why-is-numpy-fast)
  * [Who else uses NumPy?](#who-else-uses-numpy)

---

## NumPy: the absolute basics for beginners

**Source:** [https://numpy.org/devdocs/user/absolute_beginners.html](https://numpy.org/devdocs/user/absolute_beginners.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * NumPy: the absolute basics for beginners



# NumPy: the absolute basics for beginners[#](#numpy-the-absolute-basics-for-beginners "Link to this heading")

Welcome to the absolute beginner’s guide to NumPy!

NumPy (**Num** erical **Py** thon) is an open source Python library that’s widely used in science and engineering. The NumPy library contains multidimensional array data structures, such as the homogeneous, N-dimensional `ndarray`, and a large library of functions that operate efficiently on these data structures. Learn more about NumPy at [What is NumPy](whatisnumpy.html#whatisnumpy), and if you have comments or suggestions, please [reach out](https://numpy.org/community/)!

## How to import NumPy[#](#how-to-import-numpy "Link to this heading")

After [installing NumPy](https://numpy.org/install/), it may be imported into Python code like:
    
    
    import numpy as np
    

This widespread convention allows access to NumPy features with a short, recognizable prefix (`np.`) while distinguishing NumPy features from others that have the same name.

## Reading the example code[#](#reading-the-example-code "Link to this heading")

Throughout the NumPy documentation, you will find blocks that look like:
    
    
    >>> a = np.array([[1, 2, 3],
    ...               [4, 5, 6]])
    >>> a.shape
    (2, 3)
    

Text preceded by `>>>` or `...` is **input** , the code that you would enter in a script or at a Python prompt. Everything else is **output** , the results of running your code. Note that `>>>` and `...` are not part of the code and may cause an error if entered at a Python prompt.

To run the code in the examples, you can copy and paste it into a Python script or REPL, or use the experimental interactive examples in the browser provided in various locations in the documentation.

## Why use NumPy?[#](#why-use-numpy "Link to this heading")

Python lists are excellent, general-purpose containers. They can be “heterogeneous”, meaning that they can contain elements of a variety of types, and they are quite fast when used to perform individual operations on a handful of elements.

Depending on the characteristics of the data and the types of operations that need to be performed, other containers may be more appropriate; by exploiting these characteristics, we can improve speed, reduce memory consumption, and offer a high-level syntax for performing a variety of common processing tasks. NumPy shines when there are large quantities of “homogeneous” (same-type) data to be processed on the CPU.

## What is an “array”?[#](#what-is-an-array "Link to this heading")

In computer programming, an array is a structure for storing and retrieving data. We often talk about an array as if it were a grid in space, with each cell storing one element of the data. For instance, if each element of the data were a number, we might visualize a “one-dimensional” array like a list:

\\[\begin{split}\begin{array}{|c||c|c|c|} \hline 1 & 5 & 2 & 0 \\\ \hline \end{array}\end{split}\\]

A two-dimensional array would be like a table:

\\[\begin{split}\begin{array}{|c||c|c|c|} \hline 1 & 5 & 2 & 0 \\\ \hline 8 & 3 & 6 & 1 \\\ \hline 1 & 7 & 2 & 9 \\\ \hline \end{array}\end{split}\\]

A three-dimensional array would be like a set of tables, perhaps stacked as though they were printed on separate pages. In NumPy, this idea is generalized to an arbitrary number of dimensions, and so the fundamental array class is called `ndarray`: it represents an “N-dimensional array”.

Most NumPy arrays have some restrictions. For instance:

  * All elements of the array must be of the same type of data.

  * Once created, the total size of the array can’t change.

  * The shape must be “rectangular”, not “jagged”; e.g., each row of a two-dimensional array must have the same number of columns.




When these conditions are met, NumPy exploits these characteristics to make the array faster, more memory efficient, and more convenient to use than less restrictive data structures.

For the remainder of this document, we will use the word “array” to refer to an instance of `ndarray`.

## Array fundamentals[#](#array-fundamentals "Link to this heading")

One way to initialize an array is using a Python sequence, such as a list. For example:
    
    
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> a
    array([1, 2, 3, 4, 5, 6])
    

Elements of an array can be accessed in [various ways](quickstart.html#quickstart-indexing-slicing-and-iterating). For instance, we can access an individual element of this array as we would access an element in the original list: using the integer index of the element within square brackets.
    
    
    >>> a[0]
    1
    

Note

As with built-in Python sequences, NumPy arrays are “0-indexed”: the first element of the array is accessed using index `0`, not `1`.

Like the original list, the array is mutable.
    
    
    >>> a[0] = 10
    >>> a
    array([10,  2,  3,  4,  5,  6])
    

Also like the original list, Python slice notation can be used for indexing.
    
    
    >>> a[:3]
    array([10, 2, 3])
    

One major difference is that slice indexing of a list copies the elements into a new list, but slicing an array returns a _view_ : an object that refers to the data in the original array. The original array can be mutated using the view.
    
    
    >>> b = a[3:]
    >>> b
    array([4, 5, 6])
    >>> b[0] = 40
    >>> a
    array([ 10,  2,  3, 40,  5,  6])
    

See [Copies and views](basics.copies.html#basics-copies-and-views) for a more comprehensive explanation of when array operations return views rather than copies.

Two- and higher-dimensional arrays can be initialized from nested Python sequences:
    
    
    >>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    >>> a
    array([[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12]])
    

In NumPy, a dimension of an array is sometimes referred to as an “axis”. This terminology may be useful to disambiguate between the dimensionality of an array and the dimensionality of the data represented by the array. For instance, the array `a` could represent three points, each lying within a four-dimensional space, but `a` has only two “axes”.

Another difference between an array and a list of lists is that an element of the array can be accessed by specifying the index along each axis within a _single_ set of square brackets, separated by commas. For instance, the element `8` is in row `1` and column `3`:
    
    
    >>> a[1, 3]
    8
    

Note

It is familiar practice in mathematics to refer to elements of a matrix by the row index first and the column index second. This happens to be true for two-dimensional arrays, but a better mental model is to think of the column index as coming _last_ and the row index as _second to last_. This generalizes to arrays with _any_ number of dimensions.

Note

You might hear of a 0-D (zero-dimensional) array referred to as a “scalar”, a 1-D (one-dimensional) array as a “vector”, a 2-D (two-dimensional) array as a “matrix”, or an N-D (N-dimensional, where “N” is typically an integer greater than 2) array as a “tensor”. For clarity, it is best to avoid the mathematical terms when referring to an array because the mathematical objects with these names behave differently than arrays (e.g. “matrix” multiplication is fundamentally different from “array” multiplication), and there are other objects in the scientific Python ecosystem that have these names (e.g. the fundamental data structure of PyTorch is the “tensor”).

## Array attributes[#](#array-attributes "Link to this heading")

_This section covers the_ `ndim`, `shape`, `size`, _and_ `dtype` _attributes of an array_.

* * *

The number of dimensions of an array is contained in the `ndim` attribute.
    
    
    >>> a.ndim
    2
    

The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension.
    
    
    >>> a.shape
    (3, 4)
    >>> len(a.shape) == a.ndim
    True
    

The fixed, total number of elements in array is contained in the `size` attribute.
    
    
    >>> a.size
    12
    >>> import math
    >>> a.size == math.prod(a.shape)
    True
    

Arrays are typically “homogeneous”, meaning that they contain elements of only one “data type”. The data type is recorded in the `dtype` attribute.
    
    
    >>> a.dtype
    dtype('int64')  # "int" for integer, "64" for 64-bit
    

[Read more about array attributes here](../reference/arrays.ndarray.html#arrays-ndarray) and learn about [array objects here](../reference/arrays.html#arrays).

## How to create a basic array[#](#how-to-create-a-basic-array "Link to this heading")

_This section covers_ `np.zeros()`, `np.ones()`, `np.empty()`, `np.arange()`, `np.linspace()`

* * *

Besides creating an array from a sequence of elements, you can easily create an array filled with `0`’s:
    
    
    >>> np.zeros(2)
    array([0., 0.])
    

Or an array filled with `1`’s:
    
    
    >>> np.ones(2)
    array([1., 1.])
    

Or even an empty array! The function `empty` creates an array whose initial content is random and depends on the state of the memory. The reason to use `empty` over `zeros` (or something similar) is speed - just make sure to fill every element afterwards!
    
    
    >>> # Create an empty array with 2 elements
    >>> np.empty(2) 
    array([3.14, 42.  ])  # may vary
    

You can create an array with a range of elements:
    
    
    >>> np.arange(4)
    array([0, 1, 2, 3])
    

And even an array that contains a range of evenly spaced intervals. To do this, you will specify the **first number** , **last number** , and the **step size**.
    
    
    >>> np.arange(2, 9, 2)
    array([2, 4, 6, 8])
    

You can also use `np.linspace()` to create an array with values that are spaced linearly in a specified interval:
    
    
    >>> np.linspace(0, 10, num=5)
    array([ 0. ,  2.5,  5. ,  7.5, 10. ])
    

**Specifying your data type**

While the default data type is floating point (`np.float64`), you can explicitly specify which data type you want using the `dtype` keyword.
    
    
    >>> x = np.ones(2, dtype=np.int64)
    >>> x
    array([1, 1])
    

[Learn more about creating arrays here](quickstart.html#quickstart-array-creation)

## Adding, removing, and sorting elements[#](#adding-removing-and-sorting-elements "Link to this heading")

_This section covers_ `np.sort()`, `np.concatenate()`

* * *

Sorting an array is simple with `np.sort()`. You can specify the axis, kind, and order when you call the function.

If you start with this array:
    
    
    >>> arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
    

You can quickly sort the numbers in ascending order with:
    
    
    >>> np.sort(arr)
    array([1, 2, 3, 4, 5, 6, 7, 8])
    

In addition to sort, which returns a sorted copy of an array, you can use:

  * [`argsort`](../reference/generated/numpy.argsort.html#numpy.argsort "numpy.argsort"), which is an indirect sort along a specified axis,

  * [`lexsort`](../reference/generated/numpy.lexsort.html#numpy.lexsort "numpy.lexsort"), which is an indirect stable sort on multiple keys,

  * [`searchsorted`](../reference/generated/numpy.searchsorted.html#numpy.searchsorted "numpy.searchsorted"), which will find elements in a sorted array, and

  * [`partition`](../reference/generated/numpy.partition.html#numpy.partition "numpy.partition"), which is a partial sort.




To read more about sorting an array, see: [`sort`](../reference/generated/numpy.sort.html#numpy.sort "numpy.sort").

If you start with these arrays:
    
    
    >>> a = np.array([1, 2, 3, 4])
    >>> b = np.array([5, 6, 7, 8])
    

You can concatenate them with `np.concatenate()`.
    
    
    >>> np.concatenate((a, b))
    array([1, 2, 3, 4, 5, 6, 7, 8])
    

Or, if you start with these arrays:
    
    
    >>> x = np.array([[1, 2], [3, 4]])
    >>> y = np.array([[5, 6]])
    

You can concatenate them with:
    
    
    >>> np.concatenate((x, y), axis=0)
    array([[1, 2],
           [3, 4],
           [5, 6]])
    

In order to remove elements from an array, it’s simple to use indexing to select the elements that you want to keep.

To read more about concatenate, see: [`concatenate`](../reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate").

## How do you know the shape and size of an array?[#](#how-do-you-know-the-shape-and-size-of-an-array "Link to this heading")

_This section covers_ `ndarray.ndim`, `ndarray.size`, `ndarray.shape`

* * *

`ndarray.ndim` will tell you the number of axes, or dimensions, of the array.

`ndarray.size` will tell you the total number of elements of the array. This is the _product_ of the elements of the array’s shape.

`ndarray.shape` will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is `(2, 3)`.

For example, if you create this array:
    
    
    >>> array_example = np.array([[[0, 1, 2, 3],
    ...                            [4, 5, 6, 7]],
    ...
    ...                           [[0, 1, 2, 3],
    ...                            [4, 5, 6, 7]],
    ...
    ...                           [[0 ,1 ,2, 3],
    ...                            [4, 5, 6, 7]]])
    

To find the number of dimensions of the array, run:
    
    
    >>> array_example.ndim
    3
    

To find the total number of elements in the array, run:
    
    
    >>> array_example.size
    24
    

And to find the shape of your array, run:
    
    
    >>> array_example.shape
    (3, 2, 4)
    

## Can you reshape an array?[#](#can-you-reshape-an-array "Link to this heading")

_This section covers_ `arr.reshape()`

* * *

**Yes!**

Using `arr.reshape()` will give a new shape to an array without changing the data. Just remember that when you use the reshape method, the array you want to produce needs to have the same number of elements as the original array. If you start with an array with 12 elements, you’ll need to make sure that your new array also has a total of 12 elements.

If you start with this array:
    
    
    >>> a = np.arange(6)
    >>> print(a)
    [0 1 2 3 4 5]
    

You can use `reshape()` to reshape your array. For example, you can reshape this array to an array with three rows and two columns:
    
    
    >>> b = a.reshape(3, 2)
    >>> print(b)
    [[0 1]
     [2 3]
     [4 5]]
    

With `np.reshape`, you can specify a few optional parameters:
    
    
    >>> np.reshape(a, shape=(1, 6), order='C')
    array([[0, 1, 2, 3, 4, 5]])
    

`a` is the array to be reshaped.

`shape` is the new shape you want. You can specify an integer or a tuple of integers. If you specify an integer, the result will be an array of that length. The shape should be compatible with the original shape.

`order:` `C` means to read/write the elements using C-like index order, `F` means to read/write the elements using Fortran-like index order, `A` means to read/write the elements in Fortran-like index order if a is Fortran contiguous in memory, C-like order otherwise. (This is an optional parameter and doesn’t need to be specified.)

If you want to learn more about C and Fortran order, you can [read more about the internal organization of NumPy arrays here](../dev/internals.html#numpy-internals). Essentially, C and Fortran orders have to do with how indices correspond to the order the array is stored in memory. In Fortran, when moving through the elements of a two-dimensional array as it is stored in memory, the **first** index is the most rapidly varying index. As the first index moves to the next row as it changes, the matrix is stored one column at a time. This is why Fortran is thought of as a **Column-major language**. In C on the other hand, the **last** index changes the most rapidly. The matrix is stored by rows, making it a **Row-major language**. What you do for C or Fortran depends on whether it’s more important to preserve the indexing convention or not reorder the data.

[Learn more about shape manipulation here](quickstart.html#quickstart-shape-manipulation).

## How to convert a 1D array into a 2D array (how to add a new axis to an array)[#](#how-to-convert-a-1d-array-into-a-2d-array-how-to-add-a-new-axis-to-an-array "Link to this heading")

_This section covers_ `np.newaxis`, `np.expand_dims`

* * *

You can use `np.newaxis` and `np.expand_dims` to increase the dimensions of your existing array.

Using `np.newaxis` will increase the dimensions of your array by one dimension when used once. This means that a **1D** array will become a **2D** array, a **2D** array will become a **3D** array, and so on.

For example, if you start with this array:
    
    
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> a.shape
    (6,)
    

You can use `np.newaxis` to add a new axis:
    
    
    >>> a2 = a[np.newaxis, :]
    >>> a2.shape
    (1, 6)
    

You can explicitly convert a 1D array to either a row vector or a column vector using `np.newaxis`. For example, you can convert a 1D array to a row vector by inserting an axis along the first dimension:
    
    
    >>> row_vector = a[np.newaxis, :]
    >>> row_vector.shape
    (1, 6)
    

Or, for a column vector, you can insert an axis along the second dimension:
    
    
    >>> col_vector = a[:, np.newaxis]
    >>> col_vector.shape
    (6, 1)
    

You can also expand an array by inserting a new axis at a specified position with `np.expand_dims`.

For example, if you start with this array:
    
    
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> a.shape
    (6,)
    

You can use `np.expand_dims` to add an axis at index position 1 with:
    
    
    >>> b = np.expand_dims(a, axis=1)
    >>> b.shape
    (6, 1)
    

You can add an axis at index position 0 with:
    
    
    >>> c = np.expand_dims(a, axis=0)
    >>> c.shape
    (1, 6)
    

Find more information about [newaxis here](../reference/routines.indexing.html#arrays-indexing) and `expand_dims` at [`expand_dims`](../reference/generated/numpy.expand_dims.html#numpy.expand_dims "numpy.expand_dims").

## Indexing and slicing[#](#indexing-and-slicing "Link to this heading")

You can index and slice NumPy arrays in the same ways you can slice Python lists.
    
    
    >>> data = np.array([1, 2, 3])
    
    >>> data[1]
    2
    >>> data[0:2]
    array([1, 2])
    >>> data[1:]
    array([2, 3])
    >>> data[-2:]
    array([2, 3])
    

You can visualize it this way:

![../_images/np_indexing.png](../_images/np_indexing.png)

You may want to take a section of your array or specific array elements to use in further analysis or additional operations. To do that, you’ll need to subset, slice, and/or index your arrays.

If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.

For example, if you start with this array:
    
    
    >>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    

You can easily print all of the values in the array that are less than 5.
    
    
    >>> print(a[a < 5])
    [1 2 3 4]
    

You can also select, for example, numbers that are equal to or greater than 5, and use that condition to index an array.
    
    
    >>> five_up = (a >= 5)
    >>> print(a[five_up])
    [ 5  6  7  8  9 10 11 12]
    

You can select elements that are divisible by 2:
    
    
    >>> divisible_by_2 = a[a%2==0]
    >>> print(divisible_by_2)
    [ 2  4  6  8 10 12]
    

Or you can select elements that satisfy two conditions using the `&` and `|` operators:
    
    
    >>> c = a[(a > 2) & (a < 11)]
    >>> print(c)
    [ 3  4  5  6  7  8  9 10]
    

You can also make use of the logical operators **&** and **|** in order to return boolean values that specify whether or not the values in an array fulfill a certain condition. This can be useful with arrays that contain names or other categorical values.
    
    
    >>> five_up = (a > 5) | (a == 5)
    >>> print(five_up)
    [[False False False False]
     [ True  True  True  True]
     [ True  True  True True]]
    

You can also use `np.nonzero()` to select elements or indices from an array.

Starting with this array:
    
    
    >>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    

You can use `np.nonzero()` to print the indices of elements that are, for example, less than 5:
    
    
    >>> b = np.nonzero(a < 5)
    >>> print(b)
    (array([0, 0, 0, 0]), array([0, 1, 2, 3]))
    

In this example, a tuple of arrays was returned: one for each dimension. The first array represents the row indices where these values are found, and the second array represents the column indices where the values are found.

If you want to generate a list of coordinates where the elements exist, you can zip the arrays, iterate over the list of coordinates, and print them. For example:
    
    
    >>> list_of_coordinates= list(zip(b[0], b[1]))
    
    >>> for coord in list_of_coordinates:
    ...     print(coord)
    (np.int64(0), np.int64(0))
    (np.int64(0), np.int64(1))
    (np.int64(0), np.int64(2))
    (np.int64(0), np.int64(3))
    

You can also use `np.nonzero()` to print the elements in an array that are less than 5 with:
    
    
    >>> print(a[b])
    [1 2 3 4]
    

If the element you’re looking for doesn’t exist in the array, then the returned array of indices will be empty. For example:
    
    
    >>> not_there = np.nonzero(a == 42)
    >>> print(not_there)
    (array([], dtype=int64), array([], dtype=int64))
    

Learn more about [indexing and slicing here](quickstart.html#quickstart-indexing-slicing-and-iterating) and [here](basics.indexing.html#basics-indexing).

Read more about using the nonzero function at: [`nonzero`](../reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero").

## How to create an array from existing data[#](#how-to-create-an-array-from-existing-data "Link to this heading")

_This section covers_ `slicing and indexing`, `np.vstack()`, `np.hstack()`, `np.hsplit()`, `.view()`, `copy()`

* * *

You can easily create a new array from a section of an existing array.

Let’s say you have this array:
    
    
    >>> a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])
    

You can create a new array from a section of your array any time by specifying where you want to slice your array.
    
    
    >>> arr1 = a[3:8]
    >>> arr1
    array([4, 5, 6, 7, 8])
    

Here, you grabbed a section of your array from index position 3 through index position 8 but not including position 8 itself.

_Reminder: Array indexes begin at 0. This means the first element of the array is at index 0, the second element is at index 1, and so on._

You can also stack two existing arrays, both vertically and horizontally. Let’s say you have two arrays, `a1` and `a2`:
    
    
    >>> a1 = np.array([[1, 1],
    ...                [2, 2]])
    
    >>> a2 = np.array([[3, 3],
    ...                [4, 4]])
    

You can stack them vertically with `vstack`:
    
    
    >>> np.vstack((a1, a2))
    array([[1, 1],
           [2, 2],
           [3, 3],
           [4, 4]])
    

Or stack them horizontally with `hstack`:
    
    
    >>> np.hstack((a1, a2))
    array([[1, 1, 3, 3],
           [2, 2, 4, 4]])
    

You can split an array into several smaller arrays using `hsplit`. You can specify either the number of equally shaped arrays to return or the columns _after_ which the division should occur.

Let’s say you have this array:
    
    
    >>> x = np.arange(1, 25).reshape(2, 12)
    >>> x
    array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
           [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])
    

If you wanted to split this array into three equally shaped arrays, you would run:
    
    
    >>> np.hsplit(x, 3)
      [array([[ 1,  2,  3,  4],
             [13, 14, 15, 16]]), array([[ 5,  6,  7,  8],
             [17, 18, 19, 20]]), array([[ 9, 10, 11, 12],
             [21, 22, 23, 24]])]
    

If you wanted to split your array after the third and fourth column, you’d run:
    
    
    >>> np.hsplit(x, (3, 4))
      [array([[ 1,  2,  3],
             [13, 14, 15]]), array([[ 4],
             [16]]), array([[ 5,  6,  7,  8,  9, 10, 11, 12],
             [17, 18, 19, 20, 21, 22, 23, 24]])]
    

[Learn more about stacking and splitting arrays here](quickstart.html#quickstart-stacking-arrays).

You can use the `view` method to create a new array object that looks at the same data as the original array (a _shallow copy_).

Views are an important NumPy concept! NumPy functions, as well as operations like indexing and slicing, will return views whenever possible. This saves memory and is faster (no copy of the data has to be made). However it’s important to be aware of this - modifying data in a view also modifies the original array!

Let’s say you create this array:
    
    
    >>> a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    

Now we create an array `b1` by slicing `a` and modify the first element of `b1`. This will modify the corresponding element in `a` as well!
    
    
    >>> b1 = a[0, :]
    >>> b1
    array([1, 2, 3, 4])
    >>> b1[0] = 99
    >>> b1
    array([99,  2,  3,  4])
    >>> a
    array([[99,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12]])
    

Using the `copy` method will make a complete copy of the array and its data (a _deep copy_). To use this on your array, you could run:
    
    
    >>> b2 = a.copy()
    

[Learn more about copies and views here](quickstart.html#quickstart-copies-and-views).

## Basic array operations[#](#basic-array-operations "Link to this heading")

_This section covers addition, subtraction, multiplication, division, and more_

* * *

Once you’ve created your arrays, you can start to work with them. Let’s say, for example, that you’ve created two arrays, one called “data” and one called “ones”

![../_images/np_array_dataones.png](../_images/np_array_dataones.png)

You can add the arrays together with the plus sign.
    
    
    >>> data = np.array([1, 2])
    >>> ones = np.ones(2, dtype=np.int_)
    >>> data + ones
    array([2, 3])
    

![../_images/np_data_plus_ones.png](../_images/np_data_plus_ones.png)

You can, of course, do more than just addition!
    
    
    >>> data - ones
    array([0, 1])
    >>> data * data
    array([1, 4])
    >>> data / data
    array([1., 1.])
    

![../_images/np_sub_mult_divide.png](../_images/np_sub_mult_divide.png)

Basic operations are simple with NumPy. If you want to find the sum of the elements in an array, you’d use `sum()`. This works for 1D arrays, 2D arrays, and arrays in higher dimensions.
    
    
    >>> a = np.array([1, 2, 3, 4])
    
    >>> a.sum()
    10
    

To add the rows or the columns in a 2D array, you would specify the axis.

If you start with this array:
    
    
    >>> b = np.array([[1, 1], [2, 2]])
    

You can sum over the axis of rows with:
    
    
    >>> b.sum(axis=0)
    array([3, 3])
    

You can sum over the axis of columns with:
    
    
    >>> b.sum(axis=1)
    array([2, 4])
    

[Learn more about basic operations here](quickstart.html#quickstart-basic-operations).

## Broadcasting[#](#broadcasting "Link to this heading")

There are times when you might want to carry out an operation between an array and a single number (also called _an operation between a vector and a scalar_) or between arrays of two different sizes. For example, your array (we’ll call it “data”) might contain information about distance in miles but you want to convert the information to kilometers. You can perform this operation with:
    
    
    >>> data = np.array([1.0, 2.0])
    >>> data * 1.6
    array([1.6, 3.2])
    

![../_images/np_multiply_broadcasting.png](../_images/np_multiply_broadcasting.png)

NumPy understands that the multiplication should happen with each cell. That concept is called **broadcasting**. Broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes. The dimensions of your array must be compatible, for example, when the dimensions of both arrays are equal or when one of them is 1. If the dimensions are not compatible, you will get a `ValueError`.

[Learn more about broadcasting here](basics.broadcasting.html#basics-broadcasting).

## More useful array operations[#](#more-useful-array-operations "Link to this heading")

_This section covers maximum, minimum, sum, mean, product, standard deviation, and more_

* * *

NumPy also performs aggregation functions. In addition to `min`, `max`, and `sum`, you can easily run `mean` to get the average, `prod` to get the result of multiplying the elements together, `std` to get the standard deviation, and more.
    
    
    >>> data = np.array([1, 2, 3])
    >>> data.max()
    3
    >>> data.min()
    1
    >>> data.sum()
    6
    

![../_images/np_aggregation.png](../_images/np_aggregation.png)

Let’s start with this array, called “a”
    
    
    >>> a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
    ...               [0.54627315, 0.05093587, 0.40067661, 0.55645993],
    ...               [0.12697628, 0.82485143, 0.26590556, 0.56917101]])
    

It’s very common to want to aggregate along a row or column. By default, every NumPy aggregation function will return the aggregate of the entire array. To find the sum or the minimum of the elements in your array, run:
    
    
    >>> a.sum()
    4.8595784
    

Or:
    
    
    >>> a.min()
    0.05093587
    

You can specify on which axis you want the aggregation function to be computed. For example, you can find the minimum value within each column by specifying `axis=0`.
    
    
    >>> a.min(axis=0)
    array([0.12697628, 0.05093587, 0.26590556, 0.5510652 ])
    

The four values listed above correspond to the number of columns in your array. With a four-column array, you will get four values as your result.

Read more about [array methods here](../reference/arrays.ndarray.html#array-ndarray-methods).

## Creating matrices[#](#creating-matrices "Link to this heading")

You can pass Python lists of lists to create a 2-D array (or “matrix”) to represent them in NumPy.
    
    
    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> data
    array([[1, 2],
           [3, 4],
           [5, 6]])
    

![../_images/np_create_matrix.png](../_images/np_create_matrix.png)

Indexing and slicing operations are useful when you’re manipulating matrices:
    
    
    >>> data[0, 1]
    2
    >>> data[1:3]
    array([[3, 4],
           [5, 6]])
    >>> data[0:2, 0]
    array([1, 3])
    

![../_images/np_matrix_indexing.png](../_images/np_matrix_indexing.png)

You can aggregate matrices the same way you aggregated vectors:
    
    
    >>> data.max()
    6
    >>> data.min()
    1
    >>> data.sum()
    21
    

![../_images/np_matrix_aggregation.png](../_images/np_matrix_aggregation.png)

You can aggregate all the values in a matrix and you can aggregate them across columns or rows using the `axis` parameter. To illustrate this point, let’s look at a slightly modified dataset:
    
    
    >>> data = np.array([[1, 2], [5, 3], [4, 6]])
    >>> data
    array([[1, 2],
           [5, 3],
           [4, 6]])
    >>> data.max(axis=0)
    array([5, 6])
    >>> data.max(axis=1)
    array([2, 5, 6])
    

![../_images/np_matrix_aggregation_row.png](../_images/np_matrix_aggregation_row.png)

Once you’ve created your matrices, you can add and multiply them using arithmetic operators if you have two matrices that are the same size.
    
    
    >>> data = np.array([[1, 2], [3, 4]])
    >>> ones = np.array([[1, 1], [1, 1]])
    >>> data + ones
    array([[2, 3],
           [4, 5]])
    

![../_images/np_matrix_arithmetic.png](../_images/np_matrix_arithmetic.png)

You can do these arithmetic operations on matrices of different sizes, but only if one matrix has only one column or one row. In this case, NumPy will use its broadcast rules for the operation.
    
    
    >>> data = np.array([[1, 2], [3, 4], [5, 6]])
    >>> ones_row = np.array([[1, 1]])
    >>> data + ones_row
    array([[2, 3],
           [4, 5],
           [6, 7]])
    

![../_images/np_matrix_broadcasting.png](../_images/np_matrix_broadcasting.png)

Be aware that when NumPy prints N-dimensional arrays, the last axis is looped over the fastest while the first axis is the slowest. For instance:
    
    
    >>> np.ones((4, 3, 2))
    array([[[1., 1.],
            [1., 1.],
            [1., 1.]],
    
           [[1., 1.],
            [1., 1.],
            [1., 1.]],
    
           [[1., 1.],
            [1., 1.],
            [1., 1.]],
    
           [[1., 1.],
            [1., 1.],
            [1., 1.]]])
    

There are often instances where we want NumPy to initialize the values of an array. NumPy offers functions like `ones()` and `zeros()`, and the `random.Generator` class for random number generation for that. All you need to do is pass in the number of elements you want it to generate:
    
    
    >>> np.ones(3)
    array([1., 1., 1.])
    >>> np.zeros(3)
    array([0., 0., 0.])
    >>> rng = np.random.default_rng()  # the simplest way to generate random numbers
    >>> rng.random(3) 
    array([0.63696169, 0.26978671, 0.04097352])
    

![../_images/np_ones_zeros_random.png](../_images/np_ones_zeros_random.png)

You can also use `ones()`, `zeros()`, and `random()` to create a 2D array if you give them a tuple describing the dimensions of the matrix:
    
    
    >>> np.ones((3, 2))
    array([[1., 1.],
           [1., 1.],
           [1., 1.]])
    >>> np.zeros((3, 2))
    array([[0., 0.],
           [0., 0.],
           [0., 0.]])
    >>> rng.random((3, 2)) 
    array([[0.01652764, 0.81327024],
           [0.91275558, 0.60663578],
           [0.72949656, 0.54362499]])  # may vary
    

![../_images/np_ones_zeros_matrix.png](../_images/np_ones_zeros_matrix.png)

Read more about creating arrays, filled with `0`’s, `1`’s, other values or uninitialized, at [array creation routines](../reference/routines.array-creation.html#routines-array-creation).

## Generating random numbers[#](#generating-random-numbers "Link to this heading")

The use of random number generation is an important part of the configuration and evaluation of many numerical and machine learning algorithms. Whether you need to randomly initialize weights in an artificial neural network, split data into random sets, or randomly shuffle your dataset, being able to generate random numbers (actually, repeatable pseudo-random numbers) is essential.

With `Generator.integers`, you can generate random integers from low (remember that this is inclusive with NumPy) to high (exclusive). You can set `endpoint=True` to make the high number inclusive.

You can generate a 2 x 4 array of random integers between 0 and 4 with:
    
    
    >>> rng.integers(5, size=(2, 4)) 
    array([[2, 1, 1, 0],
           [0, 0, 0, 4]])  # may vary
    

[Read more about random number generation here](../reference/random/index.html#numpyrandom).

## How to get unique items and counts[#](#how-to-get-unique-items-and-counts "Link to this heading")

_This section covers_ `np.unique()`

* * *

You can find the unique elements in an array easily with `np.unique`.

For example, if you start with this array:
    
    
    >>> a = np.array([11, 11, 12, 13, 14, 15, 16, 17, 12, 13, 11, 14, 18, 19, 20])
    

you can use `np.unique` to print the unique values in your array:
    
    
    >>> unique_values = np.unique(a)
    >>> print(unique_values)
    [11 12 13 14 15 16 17 18 19 20]
    

To get the indices of unique values in a NumPy array (an array of first index positions of unique values in the array), just pass the `return_index` argument in `np.unique()` as well as your array.
    
    
    >>> unique_values, indices_list = np.unique(a, return_index=True)
    >>> print(indices_list)
    [ 0  2  3  4  5  6  7 12 13 14]
    

You can pass the `return_counts` argument in `np.unique()` along with your array to get the frequency count of unique values in a NumPy array.
    
    
    >>> unique_values, occurrence_count = np.unique(a, return_counts=True)
    >>> print(occurrence_count)
    [3 2 2 2 1 1 1 1 1 1]
    

This also works with 2D arrays! If you start with this array:
    
    
    >>> a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
    

You can find unique values with:
    
    
    >>> unique_values = np.unique(a_2d)
    >>> print(unique_values)
    [ 1  2  3  4  5  6  7  8  9 10 11 12]
    

If the axis argument isn’t passed, your 2D array will be flattened.

If you want to get the unique rows or columns, make sure to pass the `axis` argument. To find the unique rows, specify `axis=0` and for columns, specify `axis=1`.
    
    
    >>> unique_rows = np.unique(a_2d, axis=0)
    >>> print(unique_rows)
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    

To get the unique rows, index position, and occurrence count, you can use:
    
    
    >>> unique_rows, indices, occurrence_count = np.unique(
    ...      a_2d, axis=0, return_counts=True, return_index=True)
    >>> print(unique_rows)
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    >>> print(indices)
    [0 1 2]
    >>> print(occurrence_count)
    [2 1 1]
    

To learn more about finding the unique elements in an array, see [`unique`](../reference/generated/numpy.unique.html#numpy.unique "numpy.unique").

## Transposing and reshaping a matrix[#](#transposing-and-reshaping-a-matrix "Link to this heading")

_This section covers_ `arr.reshape()`, `arr.transpose()`, `arr.T`

* * *

It’s common to need to transpose your matrices. NumPy arrays have the property `T` that allows you to transpose a matrix.

![../_images/np_transposing_reshaping.png](../_images/np_transposing_reshaping.png)

You may also need to switch the dimensions of a matrix. This can happen when, for example, you have a model that expects a certain input shape that is different from your dataset. This is where the `reshape` method can be useful. You simply need to pass in the new dimensions that you want for the matrix.
    
    
    >>> data.reshape(2, 3)
    array([[1, 2, 3],
           [4, 5, 6]])
    >>> data.reshape(3, 2)
    array([[1, 2],
           [3, 4],
           [5, 6]])
    

![../_images/np_reshape.png](../_images/np_reshape.png)

You can also use `.transpose()` to reverse or change the axes of an array according to the values you specify.

If you start with this array:
    
    
    >>> arr = np.arange(6).reshape((2, 3))
    >>> arr
    array([[0, 1, 2],
           [3, 4, 5]])
    

You can transpose your array with `arr.transpose()`.
    
    
    >>> arr.transpose()
    array([[0, 3],
           [1, 4],
           [2, 5]])
    

You can also use `arr.T`:
    
    
    >>> arr.T
    array([[0, 3],
           [1, 4],
           [2, 5]])
    

To learn more about transposing and reshaping arrays, see [`transpose`](../reference/generated/numpy.transpose.html#numpy.transpose "numpy.transpose") and [`reshape`](../reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape").

## How to reverse an array[#](#how-to-reverse-an-array "Link to this heading")

_This section covers_ `np.flip()`

* * *

NumPy’s `np.flip()` function allows you to flip, or reverse, the contents of an array along an axis. When using `np.flip()`, specify the array you would like to reverse and the axis. If you don’t specify the axis, NumPy will reverse the contents along all of the axes of your input array.

**Reversing a 1D array**

If you begin with a 1D array like this one:
    
    
    >>> arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    

You can reverse it with:
    
    
    >>> reversed_arr = np.flip(arr)
    

If you want to print your reversed array, you can run:
    
    
    >>> print('Reversed Array: ', reversed_arr)
    Reversed Array:  [8 7 6 5 4 3 2 1]
    

**Reversing a 2D array**

A 2D array works much the same way.

If you start with this array:
    
    
    >>> arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    

You can reverse the content in all of the rows and all of the columns with:
    
    
    >>> reversed_arr = np.flip(arr_2d)
    >>> print(reversed_arr)
    [[12 11 10  9]
     [ 8  7  6  5]
     [ 4  3  2  1]]
    

You can easily reverse only the _rows_ with:
    
    
    >>> reversed_arr_rows = np.flip(arr_2d, axis=0)
    >>> print(reversed_arr_rows)
    [[ 9 10 11 12]
     [ 5  6  7  8]
     [ 1  2  3  4]]
    

Or reverse only the _columns_ with:
    
    
    >>> reversed_arr_columns = np.flip(arr_2d, axis=1)
    >>> print(reversed_arr_columns)
    [[ 4  3  2  1]
     [ 8  7  6  5]
     [12 11 10  9]]
    

You can also reverse the contents of only one column or row. For example, you can reverse the contents of the row at index position 1 (the second row):
    
    
    >>> arr_2d[1] = np.flip(arr_2d[1])
    >>> print(arr_2d)
    [[ 1  2  3  4]
     [ 8  7  6  5]
     [ 9 10 11 12]]
    

You can also reverse the column at index position 1 (the second column):
    
    
    >>> arr_2d[:,1] = np.flip(arr_2d[:,1])
    >>> print(arr_2d)
    [[ 1 10  3  4]
     [ 8  7  6  5]
     [ 9  2 11 12]]
    

Read more about reversing arrays at [`flip`](../reference/generated/numpy.flip.html#numpy.flip "numpy.flip").

## Reshaping and flattening multidimensional arrays[#](#reshaping-and-flattening-multidimensional-arrays "Link to this heading")

_This section covers_ `.flatten()`, `ravel()`

* * *

There are two popular ways to flatten an array: `.flatten()` and `.ravel()`. The primary difference between the two is that the new array created using `ravel()` is actually a reference to the parent array (i.e., a “view”). This means that any changes to the new array will affect the parent array as well. Since `ravel` does not create a copy, it’s memory efficient.

If you start with this array:
    
    
    >>> x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    

You can use `flatten` to flatten your array into a 1D array.
    
    
    >>> x.flatten()
    array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12])
    

When you use `flatten`, changes to your new array won’t change the parent array.

For example:
    
    
    >>> a1 = x.flatten()
    >>> a1[0] = 99
    >>> print(x)  # Original array
    [[ 1  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    >>> print(a1)  # New array
    [99  2  3  4  5  6  7  8  9 10 11 12]
    

But when you use `ravel`, the changes you make to the new array will affect the parent array.

For example:
    
    
    >>> a2 = x.ravel()
    >>> a2[0] = 98
    >>> print(x)  # Original array
    [[98  2  3  4]
     [ 5  6  7  8]
     [ 9 10 11 12]]
    >>> print(a2)  # New array
    [98  2  3  4  5  6  7  8  9 10 11 12]
    

Read more about `flatten` at [`ndarray.flatten`](../reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten "numpy.ndarray.flatten") and `ravel` at [`ravel`](../reference/generated/numpy.ravel.html#numpy.ravel "numpy.ravel").

## How to access the docstring for more information[#](#how-to-access-the-docstring-for-more-information "Link to this heading")

_This section covers_ `help()`, `?`, `??`

* * *

When it comes to the data science ecosystem, Python and NumPy are built with the user in mind. One of the best examples of this is the built-in access to documentation. Every object contains the reference to a string, which is known as the **docstring**. In most cases, this docstring contains a quick and concise summary of the object and how to use it. Python has a built-in `help()` function that can help you access this information. This means that nearly any time you need more information, you can use `help()` to quickly find the information that you need.

For example:
    
    
    >>> help(max)
    Help on built-in function max in module builtins:
    
    max(...)
        max(iterable, *[, default=obj, key=func]) -> value
        max(arg1, arg2, *args, *[, key=func]) -> value
    
        With a single iterable argument, return its biggest item. The
        default keyword-only argument specifies an object to return if
        the provided iterable is empty.
        With two or more ...arguments, return the largest argument.
    

Because access to additional information is so useful, IPython uses the `?` character as a shorthand for accessing this documentation along with other relevant information. IPython is a command shell for interactive computing in multiple languages. [You can find more information about IPython here](https://ipython.org/).

For example:
    
    
    In [0]: max?
    max(iterable, *[, default=obj, key=func]) -> value
    max(arg1, arg2, *args, *[, key=func]) -> value
    
    With a single iterable argument, return its biggest item. The
    default keyword-only argument specifies an object to return if
    the provided iterable is empty.
    With two or more arguments, return the largest argument.
    Type:      builtin_function_or_method
    

You can even use this notation for object methods and objects themselves.

Let’s say you create this array:
    
    
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    

Then you can obtain a lot of useful information (first details about `a` itself, followed by the docstring of `ndarray` of which `a` is an instance):
    
    
    In [1]: a?
    Type:            ndarray
    String form:     [1 2 3 4 5 6]
    Length:          6
    File:            ~/anaconda3/lib/python3.9/site-packages/numpy/__init__.py
    Docstring:       <no docstring>
    Class docstring:
    ndarray(shape, dtype=float, buffer=None, offset=0,
            strides=None, order=None)
    
    An array object represents a multidimensional, homogeneous array
    of fixed-size items.  An associated data-type object describes the
    format of each element in the array (its byte-order, how many bytes it
    occupies in memory, whether it is an integer, a floating point number,
    or something else, etc.)
    
    Arrays should be constructed using `array`, `zeros` or `empty` (refer
    to the See Also section below).  The parameters given here refer to
    a low-level method (`ndarray(...)`) for instantiating an array.
    
    For more information, refer to the `numpy` module and examine the
    methods and attributes of an array.
    
    Parameters
    ----------
    (for the __new__ method; see Notes below)
    
    shape : tuple of ints
            Shape of created array.
    ...
    

This also works for functions and other objects that **you** create. Just remember to include a docstring with your function using a string literal (`""" """` or `''' '''` around your documentation).

For example, if you create this function:
    
    
    >>> def double(a):
    ...   '''Return a * 2'''
    ...   return a * 2
    

You can obtain information about the function:
    
    
    In [2]: double?
    Signature: double(a)
    Docstring: Return a * 2
    File:      ~/Desktop/<ipython-input-23-b5adf20be596>
    Type:      function
    

You can reach another level of information by reading the source code of the object you’re interested in. Using a double question mark (`??`) allows you to access the source code.

For example:
    
    
    In [3]: double??
    Signature: double(a)
    Source:
    def double(a):
        '''Return a * 2'''
        return a * 2
    File:      ~/Desktop/<ipython-input-23-b5adf20be596>
    Type:      function
    

If the object in question is compiled in a language other than Python, using `??` will return the same information as `?`. You’ll find this with a lot of built-in objects and types, for example:
    
    
    In [4]: len?
    Signature: len(obj, /)
    Docstring: Return the number of items in a container.
    Type:      builtin_function_or_method
    

and :
    
    
    In [5]: len??
    Signature: len(obj, /)
    Docstring: Return the number of items in a container.
    Type:      builtin_function_or_method
    

have the same output because they were compiled in a programming language other than Python.

## Working with mathematical formulas[#](#working-with-mathematical-formulas "Link to this heading")

The ease of implementing mathematical formulas that work on arrays is one of the things that make NumPy so widely used in the scientific Python community.

For example, this is the mean square error formula (a central formula used in supervised machine learning models that deal with regression):

![../_images/np_MSE_formula.png](../_images/np_MSE_formula.png)

Implementing this formula is simple and straightforward in NumPy:

![../_images/np_MSE_implementation.png](../_images/np_MSE_implementation.png)

What makes this work so well is that `predictions` and `labels` can contain one or a thousand values. They only need to be the same size.

You can visualize it this way:

![../_images/np_mse_viz1.png](../_images/np_mse_viz1.png)

In this example, both the predictions and labels vectors contain three values, meaning `n` has a value of three. After we carry out subtractions the values in the vector are squared. Then NumPy sums the values, and your result is the error value for that prediction and a score for the quality of the model.

![../_images/np_mse_viz2.png](../_images/np_mse_viz2.png) ![../_images/np_MSE_explanation2.png](../_images/np_MSE_explanation2.png)

## How to save and load NumPy objects[#](#how-to-save-and-load-numpy-objects "Link to this heading")

_This section covers_ `np.save`, `np.savez`, `np.savetxt`, `np.load`, `np.loadtxt`

* * *

You will, at some point, want to save your arrays to disk and load them back without having to re-run the code. Fortunately, there are several ways to save and load objects with NumPy. The ndarray objects can be saved to and loaded from the disk files with `loadtxt` and `savetxt` functions that handle normal text files, `load` and `save` functions that handle NumPy binary files with a **.npy** file extension, and a `savez` function that handles NumPy files with a **.npz** file extension.

The **.npy** and **.npz** files store data, shape, dtype, and other information required to reconstruct the ndarray in a way that allows the array to be correctly retrieved, even when the file is on another machine with different architecture.

If you want to store a single ndarray object, store it as a .npy file using `np.save`. If you want to store more than one ndarray object in a single file, save it as a .npz file using `np.savez`. You can also save several arrays into a single file in compressed npz format with [`savez_compressed`](../reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed").

It’s easy to save and load an array with `np.save()`. Just make sure to specify the array you want to save and a file name. For example, if you create this array:
    
    
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    

You can save it as “filename.npy” with:
    
    
    >>> np.save('filename', a)
    

You can use `np.load()` to reconstruct your array.
    
    
    >>> b = np.load('filename.npy')
    

If you want to check your array, you can run:
    
    
    >>> print(b)
    [1 2 3 4 5 6]
    

You can save a NumPy array as a plain text file like a **.csv** or **.txt** file with `np.savetxt`.

For example, if you create this array:
    
    
    >>> csv_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    

You can easily save it as a .csv file with the name “new_file.csv” like this:
    
    
    >>> np.savetxt('new_file.csv', csv_arr)
    

You can quickly and easily load your saved text file using `loadtxt()`:
    
    
    >>> np.loadtxt('new_file.csv')
    array([1., 2., 3., 4., 5., 6., 7., 8.])
    

The `savetxt()` and `loadtxt()` functions accept additional optional parameters such as header, footer, and delimiter. While text files can be easier for sharing, .npy and .npz files are smaller and faster to read. If you need more sophisticated handling of your text file (for example, if you need to work with lines that contain missing values), you will want to use the [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") function.

With [`savetxt`](../reference/generated/numpy.savetxt.html#numpy.savetxt "numpy.savetxt"), you can specify headers, footers, comments, and more.

Learn more about [input and output routines here](../reference/routines.io.html#routines-io).

## Importing and exporting a CSV[#](#importing-and-exporting-a-csv "Link to this heading")

It’s simple to read in a CSV that contains existing information. The best and easiest way to do this is to use [Pandas](https://pandas.pydata.org).
    
    
    >>> import pandas as pd
    
    >>> # If all of your columns are the same type:
    >>> x = pd.read_csv('music.csv', header=0).values
    >>> print(x)
    [['Billie Holiday' 'Jazz' 1300000 27000000]
     ['Jimmie Hendrix' 'Rock' 2700000 70000000]
     ['Miles Davis' 'Jazz' 1500000 48000000]
     ['SIA' 'Pop' 2000000 74000000]]
    
    >>> # You can also simply select the columns you need:
    >>> x = pd.read_csv('music.csv', usecols=['Artist', 'Plays']).values
    >>> print(x)
    [['Billie Holiday' 27000000]
     ['Jimmie Hendrix' 70000000]
     ['Miles Davis' 48000000]
     ['SIA' 74000000]]
    

![../_images/np_pandas.png](../_images/np_pandas.png)

It’s simple to use Pandas in order to export your array as well. If you are new to NumPy, you may want to create a Pandas dataframe from the values in your array and then write the data frame to a CSV file with Pandas.

If you created this array “a”
    
    
    >>> a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
    ...               [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
    ...               [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
    ...               [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])
    

You could create a Pandas dataframe
    
    
    >>> df = pd.DataFrame(a)
    >>> print(df)
              0         1         2         3
    0 -2.582892  0.430148 -1.240820  1.595726
    1  0.990278  1.171510  0.941257 -0.146925
    2  0.769893  0.812997 -0.950684  0.117696
    3  0.204840  0.347845  1.969792  0.519928
    

You can easily save your dataframe with:
    
    
    >>> df.to_csv('pd.csv')
    

And read your CSV with:
    
    
    >>> data = pd.read_csv('pd.csv')
    

![../_images/np_readcsv.png](../_images/np_readcsv.png)

You can also save your array with the NumPy `savetxt` method.
    
    
    >>> np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')
    

If you’re using the command line, you can read your saved CSV any time with a command such as:
    
    
    $ cat np.csv
    #  1,  2,  3,  4
    -2.58,0.43,-1.24,1.60
    0.99,1.17,0.94,-0.15
    0.77,0.81,-0.95,0.12
    0.20,0.35,1.97,0.52
    

Or you can open the file any time with a text editor!

If you’re interested in learning more about Pandas, take a look at the [official Pandas documentation](https://pandas.pydata.org/index.html). Learn how to install Pandas with the [official Pandas installation information](https://pandas.pydata.org/pandas-docs/stable/install.html).

## Plotting arrays with Matplotlib[#](#plotting-arrays-with-matplotlib "Link to this heading")

If you need to generate a plot for your values, it’s very simple with [Matplotlib](https://matplotlib.org/).

For example, you may have an array like this one:
    
    
    >>> a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])
    

If you already have Matplotlib installed, you can import it with:
    
    
    >>> import matplotlib.pyplot as plt
    
    # If you're using Jupyter Notebook, you may also want to run the following
    # line of code to display your code in the notebook:
    
    %matplotlib inline
    

All you need to do to plot your values is run:
    
    
    >>> plt.plot(a)
    
    # If you are running from a command line, you may need to do this:
    # >>> plt.show()
    

![../_images/matplotlib1.png](../_images/matplotlib1.png)

For example, you can plot a 1D array like this:
    
    
    >>> x = np.linspace(0, 5, 20)
    >>> y = np.linspace(0, 10, 20)
    >>> plt.plot(x, y, 'purple') # line
    >>> plt.plot(x, y, 'o')      # dots
    

![../_images/matplotlib2.png](../_images/matplotlib2.png)

With Matplotlib, you have access to an enormous number of visualization options.
    
    
    >>> fig = plt.figure()
    >>> ax = fig.add_subplot(projection='3d')
    >>> X = np.arange(-5, 5, 0.15)
    >>> Y = np.arange(-5, 5, 0.15)
    >>> X, Y = np.meshgrid(X, Y)
    >>> R = np.sqrt(X**2 + Y**2)
    >>> Z = np.sin(R)
    
    >>> ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis')
    

![../_images/matplotlib3.png](../_images/matplotlib3.png)

To read more about Matplotlib and what it can do, take a look at [the official documentation](https://matplotlib.org/). For directions regarding installing Matplotlib, see the official [installation section](https://matplotlib.org/users/installing.html).

* * *

_Image credits: Jay Alammar_ <https://jalammar.github.io/>

[ __ previous NumPy quickstart ](quickstart.html "previous page") [ next NumPy fundamentals __](basics.html "next page")

__On this page

  * [How to import NumPy](#how-to-import-numpy)
  * [Reading the example code](#reading-the-example-code)
  * [Why use NumPy?](#why-use-numpy)
  * [What is an “array”?](#what-is-an-array)
  * [Array fundamentals](#array-fundamentals)
  * [Array attributes](#array-attributes)
  * [How to create a basic array](#how-to-create-a-basic-array)
  * [Adding, removing, and sorting elements](#adding-removing-and-sorting-elements)
  * [How do you know the shape and size of an array?](#how-do-you-know-the-shape-and-size-of-an-array)
  * [Can you reshape an array?](#can-you-reshape-an-array)
  * [How to convert a 1D array into a 2D array (how to add a new axis to an array)](#how-to-convert-a-1d-array-into-a-2d-array-how-to-add-a-new-axis-to-an-array)
  * [Indexing and slicing](#indexing-and-slicing)
  * [How to create an array from existing data](#how-to-create-an-array-from-existing-data)
  * [Basic array operations](#basic-array-operations)
  * [Broadcasting](#broadcasting)
  * [More useful array operations](#more-useful-array-operations)
  * [Creating matrices](#creating-matrices)
  * [Generating random numbers](#generating-random-numbers)
  * [How to get unique items and counts](#how-to-get-unique-items-and-counts)
  * [Transposing and reshaping a matrix](#transposing-and-reshaping-a-matrix)
  * [How to reverse an array](#how-to-reverse-an-array)
  * [Reshaping and flattening multidimensional arrays](#reshaping-and-flattening-multidimensional-arrays)
  * [How to access the docstring for more information](#how-to-access-the-docstring-for-more-information)
  * [Working with mathematical formulas](#working-with-mathematical-formulas)
  * [How to save and load NumPy objects](#how-to-save-and-load-numpy-objects)
  * [Importing and exporting a CSV](#importing-and-exporting-a-csv)
  * [Plotting arrays with Matplotlib](#plotting-arrays-with-matplotlib)

---

## NumPy fundamentals

**Source:** [https://numpy.org/devdocs/user/basics.html](https://numpy.org/devdocs/user/basics.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * NumPy fundamentals



# NumPy fundamentals[#](#numpy-fundamentals "Link to this heading")

These documents clarify concepts, design decisions, and technical constraints in NumPy. This is a great place to understand the fundamental NumPy ideas and philosophy.

  * [Array creation](basics.creation.html)
  * [Indexing on `ndarrays`](basics.indexing.html)
  * [I/O with NumPy](basics.io.html)
  * [Data types](basics.types.html)
  * [Broadcasting](basics.broadcasting.html)
  * [Copies and views](basics.copies.html)
  * [Working with Arrays of Strings And Bytes](basics.strings.html)
  * [Structured arrays](basics.rec.html)
  * [Universal functions (`ufunc`) basics](basics.ufuncs.html)



[ __ previous NumPy: the absolute basics for beginners ](absolute_beginners.html "previous page") [ next Array creation __](basics.creation.html "next page")

---

## Array creation

**Source:** [https://numpy.org/devdocs/user/basics.creation.html](https://numpy.org/devdocs/user/basics.creation.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Array creation



# Array creation[#](#array-creation "Link to this heading")

See also

[Array creation routines](../reference/routines.array-creation.html#routines-array-creation)

## Introduction[#](#introduction "Link to this heading")

There are 6 general mechanisms for creating arrays:

  1. Conversion from other Python structures (i.e. lists and tuples)

  2. Intrinsic NumPy array creation functions (e.g. arange, ones, zeros, etc.)

  3. Replicating, joining, or mutating existing arrays

  4. Reading arrays from disk, either from standard or custom formats

  5. Creating arrays from raw bytes through the use of strings or buffers

  6. Use of special library functions (e.g., random)




You can use these methods to create ndarrays or [Structured arrays](basics.rec.html#structured-arrays). This document will cover general methods for ndarray creation.

## 1) Converting Python sequences to NumPy arrays[#](#converting-python-sequences-to-numpy-arrays "Link to this heading")

NumPy arrays can be defined using Python sequences such as lists and tuples. Lists and tuples are defined using `[...]` and `(...)`, respectively. Lists and tuples can define ndarray creation:

  * a list of numbers will create a 1D array,

  * a list of lists will create a 2D array,

  * further nested lists will create higher-dimensional arrays. In general, any array object is called an **ndarray** in NumPy.



    
    
    >>> import numpy as np
    >>> a1D = np.array([1, 2, 3, 4])
    >>> a2D = np.array([[1, 2], [3, 4]])
    >>> a3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    

When you use [`numpy.array`](../reference/generated/numpy.array.html#numpy.array "numpy.array") to define a new array, you should consider the [dtype](basics.types.html) of the elements in the array, which can be specified explicitly. This feature gives you more control over the underlying data structures and how the elements are handled in C/C++ functions. When values do not fit and you are using a `dtype`, NumPy may raise an error:
    
    
    >>> import numpy as np
    >>> np.array([127, 128, 129], dtype=np.int8)
    Traceback (most recent call last):
    ...
    OverflowError: Python integer 128 out of bounds for int8
    

An 8-bit signed integer represents integers from -128 to 127. Assigning the `int8` array to integers outside of this range results in overflow. This feature can often be misunderstood. If you perform calculations with mismatching `dtypes`, you can get unwanted results, for example:
    
    
    >>> import numpy as np
    >>> a = np.array([2, 3, 4], dtype=np.uint32)
    >>> b = np.array([5, 6, 7], dtype=np.uint32)
    >>> c_unsigned32 = a - b
    >>> print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
    unsigned c: [4294967293 4294967293 4294967293] uint32
    >>> c_signed32 = a - b.astype(np.int32)
    >>> print('signed c:', c_signed32, c_signed32.dtype)
    signed c: [-3 -3 -3] int64
    

Notice when you perform operations with two arrays of the same `dtype`: `uint32`, the resulting array is the same type. When you perform operations with different `dtype`, NumPy will assign a new type that satisfies all of the array elements involved in the computation, here `uint32` and `int32` can both be represented in as `int64`.

The default NumPy behavior is to create arrays in either 32 or 64-bit signed integers (platform dependent and matches C `long` size) or double precision floating point numbers. If you expect your integer arrays to be a specific type, then you need to specify the dtype while you create the array.

## 2) Intrinsic NumPy array creation functions[#](#intrinsic-numpy-array-creation-functions "Link to this heading")

NumPy has over 40 built-in functions for creating arrays as laid out in the [Array creation routines](../reference/routines.array-creation.html#routines-array-creation). These functions can be split into roughly three categories, based on the dimension of the array they create:

  1. 1D arrays

  2. 2D arrays

  3. ndarrays




### 1 - 1D array creation functions[#](#d-array-creation-functions "Link to this heading")

The 1D array creation functions e.g. [`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") and [`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") generally need at least two inputs, `start` and `stop`.

[`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") creates arrays with regularly incrementing values. Check the documentation for complete information and examples. A few examples are shown:
    
    
    >>> import numpy as np
    >>> np.arange(10)
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> np.arange(2, 10, dtype=np.float64)
    array([2., 3., 4., 5., 6., 7., 8., 9.])
    >>> np.arange(2, 3, 0.1)
    array([2. , 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9])
    

Note: best practice for [`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") is to use integer start, end, and step values. There are some subtleties regarding `dtype`. In the second example, the `dtype` is defined. In the third example, the array is `dtype=np.float64` to accommodate the step size of `0.1`. Due to roundoff error, the `stop` value is sometimes included.

[`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") will create arrays with a specified number of elements, and spaced equally between the specified beginning and end values. For example:
    
    
    >>> import numpy as np
    >>> np.linspace(1., 4., 6)
    array([1. ,  1.6,  2.2,  2.8,  3.4,  4. ])
    

The advantage of this creation function is that you guarantee the number of elements and the starting and end point. The previous `arange(start, stop, step)` will not include the value `stop`.

### 2 - 2D array creation functions[#](#id1 "Link to this heading")

The 2D array creation functions e.g. [`numpy.eye`](../reference/generated/numpy.eye.html#numpy.eye "numpy.eye"), [`numpy.diag`](../reference/generated/numpy.diag.html#numpy.diag "numpy.diag"), and [`numpy.vander`](../reference/generated/numpy.vander.html#numpy.vander "numpy.vander") define properties of special matrices represented as 2D arrays.

`np.eye(n, m)` defines a 2D identity matrix. The elements where i=j (row index and column index are equal) are 1 and the rest are 0, as such:
    
    
    >>> import numpy as np
    >>> np.eye(3)
    array([[1., 0., 0.],
           [0., 1., 0.],
           [0., 0., 1.]])
    >>> np.eye(3, 5)
    array([[1., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0.],
           [0., 0., 1., 0., 0.]])
    

[`numpy.diag`](../reference/generated/numpy.diag.html#numpy.diag "numpy.diag") can define either a square 2D array with given values along the diagonal _or_ if given a 2D array returns a 1D array that is only the diagonal elements. The two array creation functions can be helpful while doing linear algebra, as such:
    
    
    >>> import numpy as np
    >>> np.diag([1, 2, 3])
    array([[1, 0, 0],
           [0, 2, 0],
           [0, 0, 3]])
    >>> np.diag([1, 2, 3], 1)
    array([[0, 1, 0, 0],
           [0, 0, 2, 0],
           [0, 0, 0, 3],
           [0, 0, 0, 0]])
    >>> a = np.array([[1, 2], [3, 4]])
    >>> np.diag(a)
    array([1, 4])
    

`vander(x, n)` defines a Vandermonde matrix as a 2D NumPy array. Each column of the Vandermonde matrix is a decreasing power of the input 1D array or list or tuple, `x` where the highest polynomial order is `n-1`. This array creation routine is helpful in generating linear least squares models, as such:
    
    
    >>> import numpy as np
    >>> np.vander(np.linspace(0, 2, 5), 2)
    array([[0. , 1. ],
          [0.5, 1. ],
          [1. , 1. ],
          [1.5, 1. ],
          [2. , 1. ]])
    >>> np.vander([1, 2, 3, 4], 2)
    array([[1, 1],
           [2, 1],
           [3, 1],
           [4, 1]])
    >>> np.vander((1, 2, 3, 4), 4)
    array([[ 1,  1,  1,  1],
           [ 8,  4,  2,  1],
           [27,  9,  3,  1],
           [64, 16,  4,  1]])
    

### 3 - general ndarray creation functions[#](#general-ndarray-creation-functions "Link to this heading")

The ndarray creation functions e.g. [`numpy.ones`](../reference/generated/numpy.ones.html#numpy.ones "numpy.ones"), [`numpy.zeros`](../reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros"), and [`random`](../reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random") define arrays based upon the desired shape. The ndarray creation functions can create arrays with any dimension by specifying how many dimensions and length along that dimension in a tuple or list.

[`numpy.zeros`](../reference/generated/numpy.zeros.html#numpy.zeros "numpy.zeros") will create an array filled with 0 values with the specified shape. The default dtype is `float64`:
    
    
    >>> import numpy as np
    >>> np.zeros((2, 3))
    array([[0., 0., 0.],
           [0., 0., 0.]])
    >>> np.zeros((2, 3, 2))
    array([[[0., 0.],
            [0., 0.],
            [0., 0.]],
    
           [[0., 0.],
            [0., 0.],
            [0., 0.]]])
    

[`numpy.ones`](../reference/generated/numpy.ones.html#numpy.ones "numpy.ones") will create an array filled with 1 values. It is identical to `zeros` in all other respects as such:
    
    
    >>> import numpy as np
    >>> np.ones((2, 3))
    array([[1., 1., 1.],
           [1., 1., 1.]])
    >>> np.ones((2, 3, 2))
    array([[[1., 1.],
            [1., 1.],
            [1., 1.]],
    
           [[1., 1.],
            [1., 1.],
            [1., 1.]]])
    

The [`random`](../reference/random/generated/numpy.random.Generator.random.html#numpy.random.Generator.random "numpy.random.Generator.random") method of the result of `default_rng` will create an array filled with random values between 0 and 1. It is included with the [`numpy.random`](../reference/random/index.html#module-numpy.random "numpy.random") library. Below, two arrays are created with shapes (2,3) and (2,3,2), respectively. The seed is set to 42 so you can reproduce these pseudorandom numbers:
    
    
    >>> import numpy as np
    >>> from numpy.random import default_rng
    >>> default_rng(42).random((2,3))
    array([[0.77395605, 0.43887844, 0.85859792],
           [0.69736803, 0.09417735, 0.97562235]])
    >>> default_rng(42).random((2,3,2))
    array([[[0.77395605, 0.43887844],
            [0.85859792, 0.69736803],
            [0.09417735, 0.97562235]],
           [[0.7611397 , 0.78606431],
            [0.12811363, 0.45038594],
            [0.37079802, 0.92676499]]])
    

[`numpy.indices`](../reference/generated/numpy.indices.html#numpy.indices "numpy.indices") will create a set of arrays (stacked as a one-higher dimensioned array), one per dimension with each representing variation in that dimension:
    
    
    >>> import numpy as np
    >>> np.indices((3,3))
    array([[[0, 0, 0],
            [1, 1, 1],
            [2, 2, 2]],
           [[0, 1, 2],
            [0, 1, 2],
            [0, 1, 2]]])
    

This is particularly useful for evaluating functions of multiple dimensions on a regular grid.

## 3) Replicating, joining, or mutating existing arrays[#](#replicating-joining-or-mutating-existing-arrays "Link to this heading")

Once you have created arrays, you can replicate, join, or mutate those existing arrays to create new arrays. When you assign an array or its elements to a new variable, you have to explicitly [`numpy.copy`](../reference/generated/numpy.copy.html#numpy.copy "numpy.copy") the array, otherwise the variable is a view into the original array. Consider the following example:
    
    
    >>> import numpy as np
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> b = a[:2]
    >>> b += 1
    >>> print('a =', a, '; b =', b)
    a = [2 3 3 4 5 6] ; b = [2 3]
    

In this example, you did not create a new array. You created a variable, `b` that viewed the first 2 elements of `a`. When you added 1 to `b` you would get the same result by adding 1 to `a[:2]`. If you want to create a _new_ array, use the [`numpy.copy`](../reference/generated/numpy.copy.html#numpy.copy "numpy.copy") array creation routine as such:
    
    
    >>> import numpy as np
    >>> a = np.array([1, 2, 3, 4])
    >>> b = a[:2].copy()
    >>> b += 1
    >>> print('a = ', a, 'b = ', b)
    a =  [1 2 3 4] b =  [2 3]
    

For more information and examples look at [Copies and Views](quickstart.html#quickstart-copies-and-views).

There are a number of routines to join existing arrays e.g. [`numpy.vstack`](../reference/generated/numpy.vstack.html#numpy.vstack "numpy.vstack"), [`numpy.hstack`](../reference/generated/numpy.hstack.html#numpy.hstack "numpy.hstack"), and [`numpy.block`](../reference/generated/numpy.block.html#numpy.block "numpy.block"). Here is an example of joining four 2-by-2 arrays into a 4-by-4 array using `block`:
    
    
    >>> import numpy as np
    >>> A = np.ones((2, 2))
    >>> B = np.eye(2, 2)
    >>> C = np.zeros((2, 2))
    >>> D = np.diag((-3, -4))
    >>> np.block([[A, B], [C, D]])
    array([[ 1.,  1.,  1.,  0.],
           [ 1.,  1.,  0.,  1.],
           [ 0.,  0., -3.,  0.],
           [ 0.,  0.,  0., -4.]])
    

Other routines use similar syntax to join ndarrays. Check the routine’s documentation for further examples and syntax.

## 4) Reading arrays from disk, either from standard or custom formats[#](#reading-arrays-from-disk-either-from-standard-or-custom-formats "Link to this heading")

This is the most common case of large array creation. The details depend greatly on the format of data on disk. This section gives general pointers on how to handle various formats. For more detailed examples of IO look at [How to Read and Write files](how-to-io.html#how-to-io).

### Standard binary formats[#](#standard-binary-formats "Link to this heading")

Various fields have standard formats for array data. The following lists the ones with known Python libraries to read them and return NumPy arrays (there may be others for which it is possible to read and convert to NumPy arrays so check the last section as well)
    
    
    HDF5: h5py
    FITS: Astropy
    

Examples of formats that cannot be read directly but for which it is not hard to convert are those formats supported by libraries like PIL (able to read and write many image formats such as jpg, png, etc).

### Common ASCII formats[#](#common-ascii-formats "Link to this heading")

Delimited files such as comma separated value (csv) and tab separated value (tsv) files are used for programs like Excel and LabView. Python functions can read and parse these files line-by-line. NumPy has two standard routines for importing a file with delimited data [`numpy.loadtxt`](../reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt") and [`numpy.genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt"). These functions have more involved use cases in [Reading and writing files](how-to-io.html). A simple example given a `simple.csv`:
    
    
    $ cat simple.csv
    x, y
    0, 0
    1, 1
    2, 4
    3, 9
    

Importing `simple.csv` is accomplished using [`numpy.loadtxt`](../reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt"):
    
    
    >>> import numpy as np
    >>> np.loadtxt('simple.csv', delimiter = ',', skiprows = 1) 
    array([[0., 0.],
           [1., 1.],
           [2., 4.],
           [3., 9.]])
    

More generic ASCII files can be read using [`scipy.io`](https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io "\(in SciPy v1.17.0\)") and [Pandas](https://pandas.pydata.org/).

## 5) Creating arrays from raw bytes through the use of strings or buffers[#](#creating-arrays-from-raw-bytes-through-the-use-of-strings-or-buffers "Link to this heading")

There are a variety of approaches one can use. If the file has a relatively simple format then one can write a simple I/O library and use the NumPy `fromfile()` function and `.tofile()` method to read and write NumPy arrays directly (mind your byteorder though!) If a good C or C++ library exists that read the data, one can wrap that library with a variety of techniques though that certainly is much more work and requires significantly more advanced knowledge to interface with C or C++.

## 6) Use of special library functions (e.g., SciPy, pandas, and OpenCV)[#](#use-of-special-library-functions-e-g-scipy-pandas-and-opencv "Link to this heading")

NumPy is the fundamental library for array containers in the Python Scientific Computing stack. Many Python libraries, including SciPy, Pandas, and OpenCV, use NumPy ndarrays as the common format for data exchange, These libraries can create, operate on, and work with NumPy arrays.

[ __ previous NumPy fundamentals ](basics.html "previous page") [ next Indexing on `ndarrays` __](basics.indexing.html "next page")

__On this page

  * [Introduction](#introduction)
  * [1) Converting Python sequences to NumPy arrays](#converting-python-sequences-to-numpy-arrays)
  * [2) Intrinsic NumPy array creation functions](#intrinsic-numpy-array-creation-functions)
    * [1 - 1D array creation functions](#d-array-creation-functions)
    * [2 - 2D array creation functions](#id1)
    * [3 - general ndarray creation functions](#general-ndarray-creation-functions)
  * [3) Replicating, joining, or mutating existing arrays](#replicating-joining-or-mutating-existing-arrays)
  * [4) Reading arrays from disk, either from standard or custom formats](#reading-arrays-from-disk-either-from-standard-or-custom-formats)
    * [Standard binary formats](#standard-binary-formats)
    * [Common ASCII formats](#common-ascii-formats)
  * [5) Creating arrays from raw bytes through the use of strings or buffers](#creating-arrays-from-raw-bytes-through-the-use-of-strings-or-buffers)
  * [6) Use of special library functions (e.g., SciPy, pandas, and OpenCV)](#use-of-special-library-functions-e-g-scipy-pandas-and-opencv)

---

## I/O with NumPy

**Source:** [https://numpy.org/devdocs/user/basics.io.html](https://numpy.org/devdocs/user/basics.io.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * I/O with NumPy



# I/O with NumPy[#](#i-o-with-numpy "Link to this heading")

  * [Importing data with `genfromtxt`](basics.io.genfromtxt.html)
    * [Defining the input](basics.io.genfromtxt.html#defining-the-input)
    * [Splitting the lines into columns](basics.io.genfromtxt.html#splitting-the-lines-into-columns)
    * [Skipping lines and choosing columns](basics.io.genfromtxt.html#skipping-lines-and-choosing-columns)
    * [Choosing the data type](basics.io.genfromtxt.html#choosing-the-data-type)
    * [Setting the names](basics.io.genfromtxt.html#setting-the-names)
    * [Tweaking the conversion](basics.io.genfromtxt.html#tweaking-the-conversion)



[ __ previous Indexing on `ndarrays` ](basics.indexing.html "previous page") [ next Importing data with `genfromtxt` __](basics.io.genfromtxt.html "next page")

---

## Data types

**Source:** [https://numpy.org/devdocs/user/basics.types.html](https://numpy.org/devdocs/user/basics.types.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Data types



# Data types[#](#data-types "Link to this heading")

See also

[Data type objects](../reference/arrays.dtypes.html#arrays-dtypes)

## Array types and conversions between types[#](#array-types-and-conversions-between-types "Link to this heading")

NumPy supports a much greater variety of numerical types than Python does. This section shows which are available, and how to modify an array’s data-type.

NumPy numerical types are instances of [`numpy.dtype`](../reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype") (data-type) objects, each having unique characteristics. Once you have imported NumPy using `import numpy as np` you can create arrays with a specified dtype using the scalar types in the numpy top-level API, e.g. [`numpy.bool`](../reference/arrays.scalars.html#numpy.bool "numpy.bool"), [`numpy.float32`](../reference/arrays.scalars.html#numpy.float32 "numpy.float32"), etc.

These scalar types as arguments to the dtype keyword that many numpy functions or methods accept. For example:
    
    
    >>> z = np.arange(3, dtype=np.uint8)
    >>> z
    array([0, 1, 2], dtype=uint8)
    

Array types can also be referred to by character codes, for example:
    
    
    >>> np.array([1, 2, 3], dtype='f')
    array([1.,  2.,  3.], dtype=float32)
    >>> np.array([1, 2, 3], dtype='d')
    array([1.,  2.,  3.], dtype=float64)
    

See [Specifying and constructing data types](../reference/arrays.dtypes.html#arrays-dtypes-constructing) for more information about specifying and constructing data type objects, including how to specify parameters like the byte order.

To determine the type of an array, look at the dtype attribute:
    
    
    >>> z.dtype
    dtype('uint8')
    

dtype objects also contain information about the type, such as its bit-width and its byte-order. The data type can also be used indirectly to query properties of the type, such as whether it is an integer:
    
    
    >>> d = np.dtype(np.int64)
    >>> d
    dtype('int64')
    
    >>> np.issubdtype(d, np.integer)
    True
    
    >>> np.issubdtype(d, np.floating)
    False
    

To convert the type of an array, use the .astype() method. For example:
    
    
    >>> z.astype(np.float64)                 
    array([0.,  1.,  2.])
    

Note that, above, we could have used the _Python_ float object as a dtype instead of [`numpy.float64`](../reference/arrays.scalars.html#numpy.float64 "numpy.float64"). NumPy knows that [`int`](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") refers to [`numpy.int_`](../reference/arrays.scalars.html#numpy.int_ "numpy.int_"), [`bool`](https://docs.python.org/3/library/functions.html#bool "\(in Python v3.14\)") means [`numpy.bool`](../reference/arrays.scalars.html#numpy.bool "numpy.bool"), that [`float`](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)") is [`numpy.float64`](../reference/arrays.scalars.html#numpy.float64 "numpy.float64") and [`complex`](https://docs.python.org/3/library/functions.html#complex "\(in Python v3.14\)") is [`numpy.complex128`](../reference/arrays.scalars.html#numpy.complex128 "numpy.complex128"). The other data-types do not have Python equivalents.

Sometimes the conversion can overflow, for instance when converting a [`numpy.int64`](../reference/arrays.scalars.html#numpy.int64 "numpy.int64") value 300 to [`numpy.int8`](../reference/arrays.scalars.html#numpy.int8 "numpy.int8"). NumPy follows C casting rules, so that value would overflow and become 44 `(300 - 256)`. If you wish to avoid such overflows, you can specify that the overflow action fail by using `same_value` for the `casting` argument (see also [Overflow errors](#overflow-errors)):
    
    
    >>> z.astype(np.float64, casting="same_value")   
    array([0.,  1.,  2.])
    

### Numerical Data Types[#](#numerical-data-types "Link to this heading")

There are 5 basic numerical types representing booleans (`bool`), integers (`int`), unsigned integers (`uint`) floating point (`float`) and `complex`. A basic numerical type name combined with a numeric bitsize defines a concrete type. The bitsize is the number of bits that are needed to represent a single value in memory. For example, [`numpy.float64`](../reference/arrays.scalars.html#numpy.float64 "numpy.float64") is a 64 bit floating point data type. Some types, such as [`numpy.int_`](../reference/arrays.scalars.html#numpy.int_ "numpy.int_") and [`numpy.intp`](../reference/arrays.scalars.html#numpy.intp "numpy.intp"), have differing bitsizes, dependent on the platforms (e.g. 32-bit vs. 64-bit CPU architectures). This should be taken into account when interfacing with low-level code (such as C or Fortran) where the raw memory is addressed.

### Data Types for Strings and Bytes[#](#data-types-for-strings-and-bytes "Link to this heading")

In addition to numerical types, NumPy also supports storing unicode strings, via the [`numpy.str_`](../reference/arrays.scalars.html#numpy.str_ "numpy.str_") dtype (`U` character code), null-terminated byte sequences via [`numpy.bytes_`](../reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_") (`S` character code), and arbitrary byte sequences, via [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void") (`V` character code).

All of the above are _fixed-width_ data types. They are parameterized by a width, in either bytes or unicode points, that a single data element in the array must fit inside. This means that storing an array of byte sequences or strings using this dtype requires knowing or calculating the sizes of the longest text or byte sequence in advance.

As an example, we can create an array storing the words `"hello"` and `"world!"`:
    
    
    >>> np.array(["hello", "world!"])
    array(['hello', 'world!'], dtype='<U6')
    

Here the data type is detected as a unicode string that is a maximum of 6 code points long, enough to store both entries without truncation. If we specify a shorter or longer data type, the string is either truncated or zero-padded to fit in the specified width:
    
    
    >>> np.array(["hello", "world!"], dtype="U5")
    array(['hello', 'world'], dtype='<U5')
    >>> np.array(["hello", "world!"], dtype="U7")
    array(['hello', 'world!'], dtype='<U7')
    

We can see the zero-padding a little more clearly if we use the bytes data type and ask NumPy to print out the bytes in the array buffer:
    
    
    >>> np.array(["hello", "world"], dtype="S7").tobytes()
    b'hello\x00\x00world\x00\x00'
    

Each entry is padded with two extra null bytes. Note however that NumPy cannot tell the difference between intentionally stored trailing nulls and padding nulls:
    
    
    >>> x = [b"hello\0\0", b"world"]
    >>> a = np.array(x, dtype="S7")
    >>> print(a[0])
    b"hello"
    >>> a[0] == x[0]
    False
    

If you need to store and round-trip any trailing null bytes, you will need to use an unstructured void data type:
    
    
    >>> a = np.array(x, dtype="V7")
    >>> a
    array([b'\x68\x65\x6C\x6C\x6F\x00\x00', b'\x77\x6F\x72\x6C\x64\x00\x00'],
          dtype='|V7')
    >>> a[0] == np.void(x[0])
    True
    

Advanced types, not listed above, are explored in section [Structured arrays](basics.rec.html#structured-arrays).

## Relationship Between NumPy Data Types and C Data Types[#](#relationship-between-numpy-data-types-and-c-data-types "Link to this heading")

NumPy provides both bit sized type names and names based on the names of C types. Since the definition of C types are platform dependent, this means the explicitly bit sized should be preferred to avoid platform-dependent behavior in programs using NumPy.

To ease integration with C code, where it is more natural to refer to platform-dependent C types, NumPy also provides type aliases that correspond to the C types for the platform. Some dtypes have trailing underscore to avoid confusion with builtin python type names, such as [`numpy.bool_`](../reference/arrays.scalars.html#numpy.bool_ "numpy.bool_").

Canonical Python API name | Python API “C-like” name | Actual C type | Description  
---|---|---|---  
[`numpy.bool`](../reference/arrays.scalars.html#numpy.bool "numpy.bool") or [`numpy.bool_`](../reference/arrays.scalars.html#numpy.bool_ "numpy.bool_") | N/A | `bool` (defined in `stdbool.h`) | Boolean (True or False) stored as a byte.  
[`numpy.int8`](../reference/arrays.scalars.html#numpy.int8 "numpy.int8") | [`numpy.byte`](../reference/arrays.scalars.html#numpy.byte "numpy.byte") | `signed char` | Platform-defined integer type with 8 bits.  
[`numpy.uint8`](../reference/arrays.scalars.html#numpy.uint8 "numpy.uint8") | [`numpy.ubyte`](../reference/arrays.scalars.html#numpy.ubyte "numpy.ubyte") | `unsigned char` | Platform-defined integer type with 8 bits without sign.  
[`numpy.int16`](../reference/arrays.scalars.html#numpy.int16 "numpy.int16") | [`numpy.short`](../reference/arrays.scalars.html#numpy.short "numpy.short") | `short` | Platform-defined integer type with 16 bits.  
[`numpy.uint16`](../reference/arrays.scalars.html#numpy.uint16 "numpy.uint16") | [`numpy.ushort`](../reference/arrays.scalars.html#numpy.ushort "numpy.ushort") | `unsigned short` | Platform-defined integer type with 16 bits without sign.  
[`numpy.int32`](../reference/arrays.scalars.html#numpy.int32 "numpy.int32") | [`numpy.intc`](../reference/arrays.scalars.html#numpy.intc "numpy.intc") | `int` | Platform-defined integer type with 32 bits.  
[`numpy.uint32`](../reference/arrays.scalars.html#numpy.uint32 "numpy.uint32") | [`numpy.uintc`](../reference/arrays.scalars.html#numpy.uintc "numpy.uintc") | `unsigned int` | Platform-defined integer type with 32 bits without sign.  
[`numpy.intp`](../reference/arrays.scalars.html#numpy.intp "numpy.intp") | N/A | `ssize_t`/`Py_ssize_t` | Platform-defined integer of size `size_t`; used e.g. for sizes.  
[`numpy.uintp`](../reference/arrays.scalars.html#numpy.uintp "numpy.uintp") | N/A | `size_t` | Platform-defined integer type capable of storing the maximum allocation size.  
N/A | `'p'` | `intptr_t` | Guaranteed to hold pointers. Character code only (Python and C).  
N/A | `'P'` | `uintptr_t` | Guaranteed to hold pointers without sign. Character code only (Python and C).  
[`numpy.int32`](../reference/arrays.scalars.html#numpy.int32 "numpy.int32") or [`numpy.int64`](../reference/arrays.scalars.html#numpy.int64 "numpy.int64") | [`numpy.long`](../reference/arrays.scalars.html#numpy.long "numpy.long") | `long` | Platform-defined integer type with at least 32 bits.  
[`numpy.uint32`](../reference/arrays.scalars.html#numpy.uint32 "numpy.uint32") or [`numpy.uint64`](../reference/arrays.scalars.html#numpy.uint64 "numpy.uint64") | [`numpy.ulong`](../reference/arrays.scalars.html#numpy.ulong "numpy.ulong") | `unsigned long` | Platform-defined integer type with at least 32 bits without sign.  
N/A | [`numpy.longlong`](../reference/arrays.scalars.html#numpy.longlong "numpy.longlong") | `long long` | Platform-defined integer type with at least 64 bits.  
N/A | [`numpy.ulonglong`](../reference/arrays.scalars.html#numpy.ulonglong "numpy.ulonglong") | `unsigned long long` | Platform-defined integer type with at least 64 bits without sign.  
[`numpy.float16`](../reference/arrays.scalars.html#numpy.float16 "numpy.float16") | [`numpy.half`](../reference/arrays.scalars.html#numpy.half "numpy.half") | N/A | Half precision float: sign bit, 5 bits exponent, 10 bits mantissa.  
[`numpy.float32`](../reference/arrays.scalars.html#numpy.float32 "numpy.float32") | [`numpy.single`](../reference/arrays.scalars.html#numpy.single "numpy.single") | `float` | Platform-defined single precision float: typically sign bit, 8 bits exponent, 23 bits mantissa.  
[`numpy.float64`](../reference/arrays.scalars.html#numpy.float64 "numpy.float64") | [`numpy.double`](../reference/arrays.scalars.html#numpy.double "numpy.double") | `double` | Platform-defined double precision float: typically sign bit, 11 bits exponent, 52 bits mantissa.  
`numpy.float96` or [`numpy.float128`](../reference/arrays.scalars.html#numpy.float128 "numpy.float128") | [`numpy.longdouble`](../reference/arrays.scalars.html#numpy.longdouble "numpy.longdouble") | `long double` | Platform-defined extended-precision float.  
[`numpy.complex64`](../reference/arrays.scalars.html#numpy.complex64 "numpy.complex64") | [`numpy.csingle`](../reference/arrays.scalars.html#numpy.csingle "numpy.csingle") | `float complex` | Complex number, represented by two single-precision floats (real and imaginary components).  
[`numpy.complex128`](../reference/arrays.scalars.html#numpy.complex128 "numpy.complex128") | [`numpy.cdouble`](../reference/arrays.scalars.html#numpy.cdouble "numpy.cdouble") | `double complex` | Complex number, represented by two double-precision floats (real and imaginary components).  
`numpy.complex192` or [`numpy.complex256`](../reference/arrays.scalars.html#numpy.complex256 "numpy.complex256") | [`numpy.clongdouble`](../reference/arrays.scalars.html#numpy.clongdouble "numpy.clongdouble") | `long double complex` | Complex number, represented by two extended-precision floats (real and imaginary components).  
  
Since many of these have platform-dependent definitions, a set of fixed-size aliases are provided (See [Sized aliases](../reference/arrays.scalars.html#sized-aliases)).

## Array scalars[#](#array-scalars "Link to this heading")

NumPy generally returns elements of arrays as array scalars (a scalar with an associated dtype). Array scalars differ from Python scalars, but for the most part they can be used interchangeably (the primary exception is for versions of Python older than v2.x, where integer array scalars cannot act as indices for lists and tuples). There are some exceptions, such as when code requires very specific attributes of a scalar or when it checks specifically whether a value is a Python scalar. Generally, problems are easily fixed by explicitly converting array scalars to Python scalars, using the corresponding Python type function (e.g., [`int`](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"), [`float`](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), [`complex`](https://docs.python.org/3/library/functions.html#complex "\(in Python v3.14\)"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "\(in Python v3.14\)")).

The primary advantage of using array scalars is that they preserve the array type (Python may not have a matching scalar type available, e.g. `int16`). Therefore, the use of array scalars ensures identical behaviour between arrays and scalars, irrespective of whether the value is inside an array or not. NumPy scalars also have many of the same methods arrays do.

## Overflow errors[#](#overflow-errors "Link to this heading")

The fixed size of NumPy numeric types may cause overflow errors when a value requires more memory than available in the data type. For example, [`numpy.power`](../reference/generated/numpy.power.html#numpy.power "numpy.power") evaluates `100 ** 9` correctly for 64-bit integers, but gives -1486618624 (incorrect) for a 32-bit integer.
    
    
    >>> np.power(100, 9, dtype=np.int64)
    1000000000000000000
    >>> np.power(100, 9, dtype=np.int32)
    np.int32(-1486618624)
    

The behaviour of NumPy and Python integer types differs significantly for integer overflows and may confuse users expecting NumPy integers to behave similar to Python’s [`int`](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)"). Unlike NumPy, the size of Python’s [`int`](https://docs.python.org/3/library/functions.html#int "\(in Python v3.14\)") is flexible. This means Python integers may expand to accommodate any integer and will not overflow.

NumPy provides [`numpy.iinfo`](../reference/generated/numpy.iinfo.html#numpy.iinfo "numpy.iinfo") and [`numpy.finfo`](../reference/generated/numpy.finfo.html#numpy.finfo "numpy.finfo") to verify the minimum or maximum values of NumPy integer and floating point values respectively
    
    
    >>> np.iinfo(int) # Bounds of the default integer on this system.
    iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
    >>> np.iinfo(np.int32) # Bounds of a 32-bit integer
    iinfo(min=-2147483648, max=2147483647, dtype=int32)
    >>> np.iinfo(np.int64) # Bounds of a 64-bit integer
    iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)
    

If 64-bit integers are still too small the result may be cast to a floating point number. Floating point numbers offer a larger, but inexact, range of possible values.
    
    
    >>> np.power(100, 100, dtype=np.int64) # Incorrect even with 64-bit int
    0
    >>> np.power(100, 100, dtype=np.float64)
    1e+200
    

## Floating point precision[#](#floating-point-precision "Link to this heading")

Many functions in NumPy, especially those in [`numpy.linalg`](../reference/routines.linalg.html#module-numpy.linalg "numpy.linalg"), involve floating-point arithmetic, which can introduce small inaccuracies due to the way computers represent decimal numbers. For instance, when performing basic arithmetic operations involving floating-point numbers:
    
    
    >>> 0.3 - 0.2 - 0.1  # This does not equal 0 due to floating-point precision
    -2.7755575615628914e-17
    

To handle such cases, it’s advisable to use functions like _np.isclose_ to compare values, rather than checking for exact equality:
    
    
    >>> np.isclose(0.3 - 0.2 - 0.1, 0, rtol=1e-05)  # Check for closeness to 0
    True
    

In this example, _np.isclose_ accounts for the minor inaccuracies that occur in floating-point calculations by applying a relative tolerance, ensuring that results within a small threshold are considered close.

For information about precision in calculations, see [Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

## Extended precision[#](#extended-precision "Link to this heading")

Python’s floating-point numbers are usually 64-bit floating-point numbers, nearly equivalent to [`numpy.float64`](../reference/arrays.scalars.html#numpy.float64 "numpy.float64"). In some unusual situations it may be useful to use floating-point numbers with more precision. Whether this is possible in numpy depends on the hardware and on the development environment: specifically, x86 machines provide hardware floating-point with 80-bit precision, and while most C compilers provide this as their `long double` type, MSVC (standard for Windows builds) makes `long double` identical to `double` (64 bits). NumPy makes the compiler’s `long double` available as [`numpy.longdouble`](../reference/arrays.scalars.html#numpy.longdouble "numpy.longdouble") (and `np.clongdouble` for the complex numbers). You can find out what your numpy provides with `np.finfo(np.longdouble)`.

NumPy does not provide a dtype with more precision than C’s `long double`; in particular, the 128-bit IEEE quad precision data type (FORTRAN’s `REAL*16`) is not available.

For efficient memory alignment, [`numpy.longdouble`](../reference/arrays.scalars.html#numpy.longdouble "numpy.longdouble") is usually stored padded with zero bits, either to 96 or 128 bits. Which is more efficient depends on hardware and development environment; typically on 32-bit systems they are padded to 96 bits, while on 64-bit systems they are typically padded to 128 bits. `np.longdouble` is padded to the system default; `np.float96` and `np.float128` are provided for users who want specific padding. In spite of the names, `np.float96` and `np.float128` provide only as much precision as `np.longdouble`, that is, 80 bits on most x86 machines and 64 bits in standard Windows builds.

Be warned that even if [`numpy.longdouble`](../reference/arrays.scalars.html#numpy.longdouble "numpy.longdouble") offers more precision than python [`float`](https://docs.python.org/3/library/functions.html#float "\(in Python v3.14\)"), it is easy to lose that extra precision, since python often forces values to pass through `float`. For example, the `%` formatting operator requires its arguments to be converted to standard python types, and it is therefore impossible to preserve extended precision even if many decimal places are requested. It can be useful to test your code with the value `1 + np.finfo(np.longdouble).eps`.

[ __ previous Importing data with `genfromtxt` ](basics.io.genfromtxt.html "previous page") [ next Broadcasting __](basics.broadcasting.html "next page")

__On this page

  * [Array types and conversions between types](#array-types-and-conversions-between-types)
    * [Numerical Data Types](#numerical-data-types)
    * [Data Types for Strings and Bytes](#data-types-for-strings-and-bytes)
  * [Relationship Between NumPy Data Types and C Data Types](#relationship-between-numpy-data-types-and-c-data-types)
  * [Array scalars](#array-scalars)
  * [Overflow errors](#overflow-errors)
  * [Floating point precision](#floating-point-precision)
  * [Extended precision](#extended-precision)

---

## Working with Arrays of Strings And Bytes

**Source:** [https://numpy.org/devdocs/user/basics.strings.html](https://numpy.org/devdocs/user/basics.strings.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Working with Arrays of Strings And Bytes



# Working with Arrays of Strings And Bytes[#](#working-with-arrays-of-strings-and-bytes "Link to this heading")

While NumPy is primarily a numerical library, it is often convenient to work with NumPy arrays of strings or bytes. The two most common use cases are:

  * Working with data loaded or memory-mapped from a data file, where one or more of the fields in the data is a string or bytestring, and the maximum length of the field is known ahead of time. This often is used for a name or label field.

  * Using NumPy indexing and broadcasting with arrays of Python strings of unknown length, which may or may not have data defined for every value.




For the first use case, NumPy provides the fixed-width [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void"), [`numpy.str_`](../reference/arrays.scalars.html#numpy.str_ "numpy.str_") and [`numpy.bytes_`](../reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_") data types. For the second use case, numpy provides [`numpy.dtypes.StringDType`](../reference/routines.dtypes.html#numpy.dtypes.StringDType "numpy.dtypes.StringDType"). Below we describe how to work with both fixed-width and variable-width string arrays, how to convert between the two representations, and provide some advice for most efficiently working with string data in NumPy.

## Fixed-width data types[#](#fixed-width-data-types "Link to this heading")

Before NumPy 2.0, the fixed-width [`numpy.str_`](../reference/arrays.scalars.html#numpy.str_ "numpy.str_"), [`numpy.bytes_`](../reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_"), and [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void") data types were the only types available for working with strings and bytestrings in NumPy. For this reason, they are used as the default dtype for strings and bytestrings, respectively:
    
    
    >>> np.array(["hello", "world"])
    array(['hello', 'world'], dtype='<U5')
    

Here the detected data type is `'<U5'`, or little-endian unicode string data, with a maximum length of 5 unicode code points.

Similarly for bytestrings:
    
    
    >>> np.array([b"hello", b"world"])
    array([b'hello', b'world'], dtype='|S5')
    

Since this is a one-byte encoding, the byteorder is _‘|’_ (not applicable), and the data type detected is a maximum 5 character bytestring.

You can also use [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void") to represent bytestrings:
    
    
    >>> np.array([b"hello", b"world"]).astype(np.void)
    array([b'\x68\x65\x6C\x6C\x6F', b'\x77\x6F\x72\x6C\x64'], dtype='|V5')
    

This is most useful when working with byte streams that are not well represented as bytestrings, and instead are better thought of as collections of 8-bit integers.

## Variable-width strings[#](#variable-width-strings "Link to this heading")

New in version 2.0.

Note

[`numpy.dtypes.StringDType`](../reference/routines.dtypes.html#numpy.dtypes.StringDType "numpy.dtypes.StringDType") is a new addition to NumPy, implemented using the new support in NumPy for flexible user-defined data types and is not as extensively tested in production workflows as the older NumPy data types.

Often, real-world string data does not have a predictable length. In these cases it is awkward to use fixed-width strings, since storing all the data without truncation requires knowing the length of the longest string one would like to store in the array before the array is created.

To support situations like this, NumPy provides [`numpy.dtypes.StringDType`](../reference/routines.dtypes.html#numpy.dtypes.StringDType "numpy.dtypes.StringDType"), which stores variable-width string data in a UTF-8 encoding in a NumPy array:
    
    
    >>> from numpy.dtypes import StringDType
    >>> data = ["this is a longer string", "short string"]
    >>> arr = np.array(data, dtype=StringDType())
    >>> arr
    array(['this is a longer string', 'short string'], dtype=StringDType())
    

Note that unlike fixed-width strings, `StringDType` is not parameterized by the maximum length of an array element, arbitrarily long or short strings can live in the same array without needing to reserve storage for padding bytes in the short strings.

Also note that unlike fixed-width strings and most other NumPy data types, `StringDType` does not store the string data in the “main” `ndarray` data buffer. Instead, the array buffer is used to store metadata about where the string data are stored in memory. This difference means that code expecting the array buffer to contain string data will not function correctly, and will need to be updated to support `StringDType`.

### Missing data support[#](#missing-data-support "Link to this heading")

Often string datasets are not complete, and a special label is needed to indicate that a value is missing. By default `StringDType` does not have any special support for missing values, besides the fact that empty strings are used to populate empty arrays:
    
    
    >>> np.empty(3, dtype=StringDType())
    array(['', '', ''], dtype=StringDType())
    

Optionally, you can create an instance of `StringDType` with support for missing values by passing `na_object` as a keyword argument for the initializer:
    
    
    >>> dt = StringDType(na_object=None)
    >>> arr = np.array(["this array has", None, "as an entry"], dtype=dt)
    >>> arr
    array(['this array has', None, 'as an entry'],
          dtype=StringDType(na_object=None))
    >>> arr[1] is None
    True
    

The `na_object` can be any arbitrary python object. Common choices are [`numpy.nan`](../reference/constants.html#numpy.nan "numpy.nan"), `float('nan')`, `None`, an object specifically intended to represent missing data like `pandas.NA`, or a (hopefully) unique string like `"__placeholder__"`.

NumPy has special handling for NaN-like sentinels and string sentinels.

#### NaN-like Missing Data Sentinels[#](#nan-like-missing-data-sentinels "Link to this heading")

A NaN-like sentinel returns itself as the result of arithmetic operations. This includes the python `nan` float and the Pandas missing data sentinel `pd.NA`. NaN-like sentinels inherit these behaviors in string operations. This means that, for example, the result of addition with any other string is the sentinel:
    
    
    >>> dt = StringDType(na_object=np.nan)
    >>> arr = np.array(["hello", np.nan, "world"], dtype=dt)
    >>> arr + arr
    array(['hellohello', nan, 'worldworld'], dtype=StringDType(na_object=nan))
    

Following the behavior of `nan` in float arrays, NaN-like sentinels sort to the end of the array:
    
    
    >>> np.sort(arr)
    array(['hello', 'world', nan], dtype=StringDType(na_object=nan))
    

#### String Missing Data Sentinels[#](#string-missing-data-sentinels "Link to this heading")

A string missing data value is an instance of `str` or subtype of `str`. If such an array is passed to a string operation or a cast, “missing” entries are treated as if they have a value given by the string sentinel. Comparison operations similarly use the sentinel value directly for missing entries.

#### Other Sentinels[#](#other-sentinels "Link to this heading")

Other objects, such as `None` are also supported as missing data sentinels. If any missing data are present in an array using such a sentinel, then string operations will raise an error:
    
    
    >>> dt = StringDType(na_object=None)
    >>> arr = np.array(["this array has", None, "as an entry"])
    >>> np.sort(arr)
    Traceback (most recent call last):
    ...
    TypeError: '<' not supported between instances of 'NoneType' and 'str'
    

### Coercing Non-strings[#](#coercing-non-strings "Link to this heading")

By default, non-string data are coerced to strings:
    
    
    >>> np.array([1, object(), 3.4], dtype=StringDType())
    array(['1', '<object object at 0x7faa2497dde0>', '3.4'], dtype=StringDType())
    

If this behavior is not desired, an instance of the DType can be created that disables string coercion by setting `coerce=False` in the initializer:
    
    
    >>> np.array([1, object(), 3.4], dtype=StringDType(coerce=False))
    Traceback (most recent call last):
    ...
    ValueError: StringDType only allows string data when string coercion is disabled.
    

This allows strict data validation in the same pass over the data NumPy uses to create the array. Setting `coerce=True` recovers the default behavior allowing coercion to strings.

### Casting To and From Fixed-Width Strings[#](#casting-to-and-from-fixed-width-strings "Link to this heading")

`StringDType` supports round-trip casts between [`numpy.str_`](../reference/arrays.scalars.html#numpy.str_ "numpy.str_"), [`numpy.bytes_`](../reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_"), and [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void"). Casting to a fixed-width string is most useful when strings need to be memory-mapped in an ndarray or when a fixed-width string is needed for reading and writing to a columnar data format with a known maximum string length.

In all cases, casting to a fixed-width string requires specifying the maximum allowed string length:
    
    
    >>> arr = np.array(["hello", "world"], dtype=StringDType())
    >>> arr.astype(np.str_)  
    Traceback (most recent call last):
    ...
    TypeError: Casting from StringDType to a fixed-width dtype with an
    unspecified size is not currently supported, specify an explicit
    size for the output dtype instead.
    
    The above exception was the direct cause of the following
    exception:
    
    TypeError: cannot cast dtype StringDType() to <class 'numpy.dtypes.StrDType'>.
    >>> arr.astype("U5")
    array(['hello', 'world'], dtype='<U5')
    

The [`numpy.bytes_`](../reference/arrays.scalars.html#numpy.bytes_ "numpy.bytes_") cast is most useful for string data that is known to contain only ASCII characters, as characters outside this range cannot be represented in a single byte in the UTF-8 encoding and are rejected.

Any valid unicode string can be cast to [`numpy.str_`](../reference/arrays.scalars.html#numpy.str_ "numpy.str_"), although since [`numpy.str_`](../reference/arrays.scalars.html#numpy.str_ "numpy.str_") uses a 32-bit UCS4 encoding for all characters, this will often waste memory for real-world textual data that can be well-represented by a more memory-efficient encoding.

Additionally, any valid unicode string can be cast to [`numpy.void`](../reference/arrays.scalars.html#numpy.void "numpy.void"), storing the UTF-8 bytes directly in the output array:
    
    
    >>> arr = np.array(["hello", "world"], dtype=StringDType())
    >>> arr.astype("V5")
    array([b'\x68\x65\x6C\x6C\x6F', b'\x77\x6F\x72\x6C\x64'], dtype='|V5')
    

Care must be taken to ensure that the output array has enough space for the UTF-8 bytes in the string, since the size of a UTF-8 bytestream in bytes is not necessarily the same as the number of characters in the string.

[ __ previous Copies and views ](basics.copies.html "previous page") [ next Structured arrays __](basics.rec.html "next page")

__On this page

  * [Fixed-width data types](#fixed-width-data-types)
  * [Variable-width strings](#variable-width-strings)
    * [Missing data support](#missing-data-support)
      * [NaN-like Missing Data Sentinels](#nan-like-missing-data-sentinels)
      * [String Missing Data Sentinels](#string-missing-data-sentinels)
      * [Other Sentinels](#other-sentinels)
    * [Coercing Non-strings](#coercing-non-strings)
    * [Casting To and From Fixed-Width Strings](#casting-to-and-from-fixed-width-strings)

---

## Universal functions (ufunc) basics

**Source:** [https://numpy.org/devdocs/user/basics.ufuncs.html](https://numpy.org/devdocs/user/basics.ufuncs.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * Universal functions (`ufunc`) basics



# Universal functions ([`ufunc`](../reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc")) basics[#](#universal-functions-ufunc-basics "Link to this heading")

See also

[Universal functions (ufunc)](../reference/ufuncs.html#ufuncs)

A universal function (or [ufunc](../glossary.html#term-ufunc) for short) is a function that operates on [`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") in an element-by-element fashion, supporting [array broadcasting](#ufuncs-broadcasting), [type casting](#ufuncs-casting), and several other standard features. That is, a ufunc is a “[vectorized](../glossary.html#term-vectorization)” wrapper for a function that takes a fixed number of specific inputs and produces a fixed number of specific outputs.

There are also [generalized ufuncs](../reference/c-api/generalized-ufuncs.html#c-api-generalized-ufuncs) which are functions over vectors (or arrays) instead of single-element scalars. For example, [`numpy.add`](../reference/generated/numpy.add.html#numpy.add "numpy.add") is a ufunc that operates element-by-element, while [`numpy.matmul`](../reference/generated/numpy.matmul.html#numpy.matmul "numpy.matmul") is a gufunc that operates on vectors/matrices:
    
    
    >>> a = np.arange(6).reshape(3, 2)
    >>> a
    array([[0, 1],
           [2, 3],
           [4, 5]])
    >>> np.add(a, a)  # element-wise addition
    array([[ 0,  2],
           [ 4,  6],
           [ 8, 10]])
    >>> np.matmul(a, a.T)  # matrix multiplication (3x2) @ (2x3) -> (3x3)
    array([[ 1,  3,  5],
           [ 3, 13, 23],
           [ 5, 23, 41]])
    

In NumPy, universal functions are instances of the [`numpy.ufunc`](../reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc") class. Many of the built-in functions are implemented in compiled C code. The basic ufuncs operate on scalars, but there is also a generalized kind for which the basic elements are sub-arrays (vectors, matrices, etc.), and broadcasting is done over other dimensions. The simplest example is the addition operator:
    
    
    >>> np.array([0,2,3,4]) + np.array([1,1,-1,2])
    array([1, 3, 2, 6])
    

One can also produce custom [`numpy.ufunc`](../reference/generated/numpy.ufunc.html#numpy.ufunc "numpy.ufunc") instances using the [`numpy.frompyfunc`](../reference/generated/numpy.frompyfunc.html#numpy.frompyfunc "numpy.frompyfunc") factory function.

## Ufunc methods[#](#ufunc-methods "Link to this heading")

All ufuncs have 5 methods. 4 reduce-like methods ([`reduce`](../reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce"), [`accumulate`](../reference/generated/numpy.ufunc.accumulate.html#numpy.ufunc.accumulate "numpy.ufunc.accumulate"), [`reduceat`](../reference/generated/numpy.ufunc.reduceat.html#numpy.ufunc.reduceat "numpy.ufunc.reduceat"), [`outer`](../reference/generated/numpy.ufunc.outer.html#numpy.ufunc.outer "numpy.ufunc.outer")) and one for inplace operations ([`at`](../reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "numpy.ufunc.at")). See [Methods](../reference/ufuncs.html#ufuncs-methods) for more. However, these methods only make sense on ufuncs that take two input arguments and return one output argument (so-called “scalar” ufuncs since the inner loop operates on a single scalar value). Attempting to call these methods on other ufuncs will cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "\(in Python v3.14\)").

For example, [`numpy.add`](../reference/generated/numpy.add.html#numpy.add "numpy.add") takes two inputs and returns one output, so its methods work:
    
    
    >>> np.add.reduce([1, 2, 3])
    6
    

But [`numpy.divmod`](../reference/generated/numpy.divmod.html#numpy.divmod "numpy.divmod") returns two outputs (quotient and remainder), so calling its methods raises an error:
    
    
    >>> np.divmod.reduce([1, 2, 3])
    Traceback (most recent call last):
        ...
    ValueError: reduce only supported for functions returning a single value
    

The reduce-like methods all take an _axis_ keyword, a _dtype_ keyword, and an _out_ keyword, and the arrays must all have dimension >= 1. The _axis_ keyword specifies the axis of the array over which the reduction will take place (with negative values counting backwards). Generally, it is an integer, though for [`numpy.ufunc.reduce`](../reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce"), it can also be a tuple of `int` to reduce over several axes at once, or `None`, to reduce over all axes. For example:
    
    
    >>> x = np.arange(9).reshape(3,3)
    >>> x
    array([[0, 1, 2],
          [3, 4, 5],
          [6, 7, 8]])
    >>> np.add.reduce(x, 1)
    array([ 3, 12, 21])
    >>> np.add.reduce(x, (0, 1))
    36
    

The _dtype_ keyword allows you to manage a very common problem that arises when naively using [`ufunc.reduce`](../reference/generated/numpy.ufunc.reduce.html#numpy.ufunc.reduce "numpy.ufunc.reduce"). Sometimes you may have an array of a certain data type and wish to add up all of its elements, but the result does not fit into the data type of the array. This commonly happens if you have an array of single-byte integers. The _dtype_ keyword allows you to alter the data type over which the reduction takes place (and therefore the type of the output). Thus, you can ensure that the output is a data type with precision large enough to handle your output. The responsibility of altering the reduce type is mostly up to you. There is one exception: if no _dtype_ is given for a reduction on the “add” or “multiply” operations, then if the input type is an integer (or Boolean) data-type and smaller than the size of the [`numpy.int_`](../reference/arrays.scalars.html#numpy.int_ "numpy.int_") data type, it will be internally upcast to the [`int_`](../reference/arrays.scalars.html#numpy.int_ "numpy.int_") (or [`numpy.uint`](../reference/arrays.scalars.html#numpy.uint "numpy.uint")) data-type. In the previous example:
    
    
    >>> x.dtype
    dtype('int64')
    >>> np.multiply.reduce(x, dtype=np.float64)
    array([ 0., 28., 80.])
    

Finally, the _out_ keyword allows you to provide an output array (or a tuple of output arrays for multi-output ufuncs). If _out_ is given, the _dtype_ argument is only used for the internal computations. Considering `x` from the previous example:
    
    
    >>> y = np.zeros(3, dtype=np.int_)
    >>> y
    array([0, 0, 0])
    >>> np.multiply.reduce(x, dtype=np.float64, out=y)
    array([ 0, 28, 80])
    

Ufuncs also have a fifth method, [`numpy.ufunc.at`](../reference/generated/numpy.ufunc.at.html#numpy.ufunc.at "numpy.ufunc.at"), that allows in place operations to be performed using advanced indexing. No [buffering](#use-of-internal-buffers) is used on the dimensions where advanced indexing is used, so the advanced index can list an item more than once and the operation will be performed on the result of the previous operation for that item.

## Output type determination[#](#output-type-determination "Link to this heading")

If the input arguments of the ufunc (or its methods) are [`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), then the output will be as well. The exception is when the result is zero-dimensional, in which case the output will be converted to an _array scalar_. This can be avoided by passing in `out=...` or `out=Ellipsis`.

If some or all of the input arguments are not [`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), then the output may not be an [`ndarray`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray") either. Indeed, if any input defines an [`__array_ufunc__`](../reference/arrays.classes.html#numpy.class.__array_ufunc__ "numpy.class.__array_ufunc__") method, control will be passed completely to that function, i.e., the ufunc is [overridden](#ufuncs-overrides).

If none of the inputs overrides the ufunc, then all output arrays will be passed to the [`__array_wrap__`](../reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__") method of the input (besides [`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray"), and scalars) that defines it **and** has the highest [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") of any other input to the universal function. The default [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") of the ndarray is 0.0, and the default [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") of a subtype is 0.0. Matrices have [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") equal to 10.0.

All ufuncs can also take output arguments which must be arrays or subclasses. If necessary, the result will be cast to the data-type(s) of the provided output array(s). If the output has an [`__array_wrap__`](../reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__") method it is called instead of the one found on the inputs.

## Broadcasting[#](#broadcasting "Link to this heading")

See also

[Broadcasting basics](basics.broadcasting.html)

Each universal function takes array inputs and produces array outputs by performing the core function element-wise on the inputs (where an element is generally a scalar, but can be a vector or higher-order sub-array for generalized ufuncs). Standard [broadcasting rules](basics.broadcasting.html#general-broadcasting-rules) are applied so that inputs not sharing exactly the same shapes can still be usefully operated on.

By these rules, if an input has a dimension size of 1 in its shape, the first data entry in that dimension will be used for all calculations along that dimension. In other words, the stepping machinery of the [ufunc](../glossary.html#term-ufunc) will simply not step along that dimension (the [stride](../reference/arrays.ndarray.html#memory-layout) will be 0 for that dimension).

## Type casting rules[#](#type-casting-rules "Link to this heading")

Note

In NumPy 1.6.0, a type promotion API was created to encapsulate the mechanism for determining output types. See the functions [`numpy.result_type`](../reference/generated/numpy.result_type.html#numpy.result_type "numpy.result_type"), [`numpy.promote_types`](../reference/generated/numpy.promote_types.html#numpy.promote_types "numpy.promote_types"), and [`numpy.min_scalar_type`](../reference/generated/numpy.min_scalar_type.html#numpy.min_scalar_type "numpy.min_scalar_type") for more details.

At the core of every ufunc is a one-dimensional strided loop that implements the actual function for a specific type combination. When a ufunc is created, it is given a static list of inner loops and a corresponding list of type signatures over which the ufunc operates. The ufunc machinery uses this list to determine which inner loop to use for a particular case. You can inspect the [`.types`](../reference/generated/numpy.ufunc.types.html#numpy.ufunc.types "numpy.ufunc.types") attribute for a particular ufunc to see which type combinations have a defined inner loop and which output type they produce ([character codes](../reference/arrays.scalars.html#arrays-scalars-character-codes) are used in said output for brevity).

Casting must be done on one or more of the inputs whenever the ufunc does not have a core loop implementation for the input types provided. If an implementation for the input types cannot be found, then the algorithm searches for an implementation with a type signature to which all of the inputs can be cast “safely.” The first one it finds in its internal list of loops is selected and performed, after all necessary type casting. Recall that internal copies during ufuncs (even for casting) are limited to the size of an internal buffer (which is user settable).

Note

Universal functions in NumPy are flexible enough to have mixed type signatures. Thus, for example, a universal function could be defined that works with floating-point and integer values. See [`numpy.ldexp`](../reference/generated/numpy.ldexp.html#numpy.ldexp "numpy.ldexp") for an example.

By the above description, the casting rules are essentially implemented by the question of when a data type can be cast “safely” to another data type. The answer to this question can be determined in Python with a function call: [`can_cast(fromtype, totype)`](../reference/generated/numpy.can_cast.html#numpy.can_cast "numpy.can_cast"). The example below shows the results of this call for the 24 internally supported types on the author’s 64-bit system. You can generate this table for your system with the code given in the example.

Example

Code segment showing the “can cast safely” table for a 64-bit system. Generally the output depends on the system; your system might result in a different table.
    
    
    >>> mark = {False: ' -', True: ' Y'}
    >>> def print_table(ntypes):
    ...     print('X ' + ' '.join(ntypes))
    ...     for row in ntypes:
    ...         print(row, end='')
    ...         for col in ntypes:
    ...             print(mark[np.can_cast(row, col)], end='')
    ...         print()
    ...
    >>> print_table(np.typecodes['All'])
    X ? b h i l q n p B H I L Q N P e f d g F D G S U V O M m
    ? Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y - Y
    b - Y Y Y Y Y Y Y - - - - - - - Y Y Y Y Y Y Y Y Y Y Y - Y
    h - - Y Y Y Y Y Y - - - - - - - - Y Y Y Y Y Y Y Y Y Y - Y
    i - - - Y Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
    l - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
    q - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
    n - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
    p - - - - Y Y Y Y - - - - - - - - - Y Y - Y Y Y Y Y Y - Y
    B - - Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y Y - Y
    H - - - Y Y Y Y Y - Y Y Y Y Y Y - Y Y Y Y Y Y Y Y Y Y - Y
    I - - - - Y Y Y Y - - Y Y Y Y Y - - Y Y - Y Y Y Y Y Y - Y
    L - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
    Q - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
    N - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
    P - - - - - - - - - - - Y Y Y Y - - Y Y - Y Y Y Y Y Y - -
    e - - - - - - - - - - - - - - - Y Y Y Y Y Y Y Y Y Y Y - -
    f - - - - - - - - - - - - - - - - Y Y Y Y Y Y Y Y Y Y - -
    d - - - - - - - - - - - - - - - - - Y Y - Y Y Y Y Y Y - -
    g - - - - - - - - - - - - - - - - - - Y - - Y Y Y Y Y - -
    F - - - - - - - - - - - - - - - - - - - Y Y Y Y Y Y Y - -
    D - - - - - - - - - - - - - - - - - - - - Y Y Y Y Y Y - -
    G - - - - - - - - - - - - - - - - - - - - - Y Y Y Y Y - -
    S - - - - - - - - - - - - - - - - - - - - - - Y Y Y Y - -
    U - - - - - - - - - - - - - - - - - - - - - - - Y Y Y - -
    V - - - - - - - - - - - - - - - - - - - - - - - - Y Y - -
    O - - - - - - - - - - - - - - - - - - - - - - - - - Y - -
    M - - - - - - - - - - - - - - - - - - - - - - - - Y Y Y -
    m - - - - - - - - - - - - - - - - - - - - - - - - Y Y - Y
    

You should note that, while included in the table for completeness, the ‘S’, ‘U’, and ‘V’ types cannot be operated on by ufuncs. Also, note that on a 32-bit system the integer types may have different sizes, resulting in a slightly altered table.

Mixed scalar-array operations use a different set of casting rules that ensure that a scalar cannot “upcast” an array unless the scalar is of a fundamentally different kind of data (i.e., under a different hierarchy in the data-type hierarchy) than the array. This rule enables you to use scalar constants in your code (which, as Python types, are interpreted accordingly in ufuncs) without worrying about whether the precision of the scalar constant will cause upcasting on your large (small precision) array.

## Use of internal buffers[#](#use-of-internal-buffers "Link to this heading")

Internally, buffers are used for misaligned data, swapped data, and data that has to be converted from one data type to another. The size of internal buffers is settable on a per-thread basis. There can be up to \\(2 (n_{\mathrm{inputs}} + n_{\mathrm{outputs}})\\) buffers of the specified size created to handle the data from all the inputs and outputs of a ufunc. The default size of a buffer is 10,000 elements. Whenever buffer-based calculation would be needed, but all input arrays are smaller than the buffer size, those misbehaved or incorrectly-typed arrays will be copied before the calculation proceeds. Adjusting the size of the buffer may therefore alter the speed at which ufunc calculations of various sorts are completed. A simple interface for setting this variable is accessible using the function [`numpy.setbufsize`](../reference/generated/numpy.setbufsize.html#numpy.setbufsize "numpy.setbufsize").

## Error handling[#](#error-handling "Link to this heading")

Universal functions can trip special floating-point status registers in your hardware (such as divide-by-zero). If available on your platform, these registers will be regularly checked during calculation. Error handling is controlled on a per-thread basis, and can be configured using the functions [`numpy.seterr`](../reference/generated/numpy.seterr.html#numpy.seterr "numpy.seterr") and [`numpy.seterrcall`](../reference/generated/numpy.seterrcall.html#numpy.seterrcall "numpy.seterrcall").

## Overriding ufunc behavior[#](#overriding-ufunc-behavior "Link to this heading")

Classes (including ndarray subclasses) can override how ufuncs act on them by defining certain special methods. For details, see [Standard array subclasses](../reference/arrays.classes.html#arrays-classes).

[ __ previous Structured arrays ](basics.rec.html "previous page") [ next NumPy for MATLAB users __](numpy-for-matlab-users.html "next page")

__On this page

  * [Ufunc methods](#ufunc-methods)
  * [Output type determination](#output-type-determination)
  * [Broadcasting](#broadcasting)
  * [Type casting rules](#type-casting-rules)
  * [Use of internal buffers](#use-of-internal-buffers)
  * [Error handling](#error-handling)
  * [Overriding ufunc behavior](#overriding-ufunc-behavior)

---

## NumPy how-tos

**Source:** [https://numpy.org/devdocs/user/howtos_index.html](https://numpy.org/devdocs/user/howtos_index.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * NumPy how-tos



# NumPy how-tos[#](#numpy-how-tos "Link to this heading")

These documents are intended as recipes to common tasks using NumPy. For detailed reference documentation of the functions and classes contained in the package, see the [API reference](../reference/index.html#reference).

  * [How to write a NumPy how-to](how-to-how-to.html)
  * [Reading and writing files](how-to-io.html)
  * [How to index `ndarrays`](how-to-index.html)
  * [Verifying bugs and bug fixes in NumPy](how-to-verify-bug.html)
  * [How to create arrays with regularly-spaced values](how-to-partition.html)
  * [Printing NumPy Arrays](how-to-print.html)



[ __ previous NumPy for MATLAB users ](numpy-for-matlab-users.html "previous page") [ next How to write a NumPy how-to __](how-to-how-to.html "next page")

---

## Using NumPy C-API

**Source:** [https://numpy.org/devdocs/user/c-info.html](https://numpy.org/devdocs/user/c-info.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * Using NumPy C-API



# Using NumPy C-API[#](#using-numpy-c-api "Link to this heading")

  * [How to extend NumPy](c-info.how-to-extend.html)
    * [Writing an extension module](c-info.how-to-extend.html#writing-an-extension-module)
    * [Required subroutine](c-info.how-to-extend.html#required-subroutine)
    * [Defining functions](c-info.how-to-extend.html#defining-functions)
      * [Functions without keyword arguments](c-info.how-to-extend.html#functions-without-keyword-arguments)
      * [Functions with keyword arguments](c-info.how-to-extend.html#functions-with-keyword-arguments)
      * [Reference counting](c-info.how-to-extend.html#reference-counting)
    * [Dealing with array objects](c-info.how-to-extend.html#dealing-with-array-objects)
      * [Converting an arbitrary sequence object](c-info.how-to-extend.html#converting-an-arbitrary-sequence-object)
      * [Creating a brand-new ndarray](c-info.how-to-extend.html#creating-a-brand-new-ndarray)
      * [Getting at ndarray memory and accessing elements of the ndarray](c-info.how-to-extend.html#getting-at-ndarray-memory-and-accessing-elements-of-the-ndarray)
    * [Example](c-info.how-to-extend.html#example)
  * [Using Python as glue](c-info.python-as-glue.html)
    * [Calling other compiled libraries from Python](c-info.python-as-glue.html#calling-other-compiled-libraries-from-python)
    * [Hand-generated wrappers](c-info.python-as-glue.html#hand-generated-wrappers)
    * [F2PY](c-info.python-as-glue.html#f2py)
    * [Cython](c-info.python-as-glue.html#cython)
      * [Complex addition in Cython](c-info.python-as-glue.html#complex-addition-in-cython)
      * [Image filter in Cython](c-info.python-as-glue.html#image-filter-in-cython)
      * [Conclusion](c-info.python-as-glue.html#conclusion)
    * [ctypes](c-info.python-as-glue.html#index-2)
      * [Having a shared library](c-info.python-as-glue.html#having-a-shared-library)
      * [Loading the shared library](c-info.python-as-glue.html#loading-the-shared-library)
      * [Converting arguments](c-info.python-as-glue.html#converting-arguments)
      * [Calling the function](c-info.python-as-glue.html#calling-the-function)
        * [`ndpointer`](c-info.python-as-glue.html#ndpointer)
      * [Complete example](c-info.python-as-glue.html#complete-example)
      * [Conclusion](c-info.python-as-glue.html#id4)
    * [Additional tools you may find useful](c-info.python-as-glue.html#additional-tools-you-may-find-useful)
      * [SWIG](c-info.python-as-glue.html#swig)
      * [SIP](c-info.python-as-glue.html#sip)
      * [Boost Python](c-info.python-as-glue.html#boost-python)
      * [Pyfort](c-info.python-as-glue.html#pyfort)
  * [Writing your own ufunc](c-info.ufunc-tutorial.html)
    * [Creating a new universal function](c-info.ufunc-tutorial.html#creating-a-new-universal-function)
    * [Example non-ufunc extension](c-info.ufunc-tutorial.html#example-non-ufunc-extension)
    * [Example NumPy ufunc for one dtype](c-info.ufunc-tutorial.html#example-numpy-ufunc-for-one-dtype)
    * [Example NumPy ufunc with multiple dtypes](c-info.ufunc-tutorial.html#example-numpy-ufunc-with-multiple-dtypes)
    * [Example NumPy ufunc with multiple arguments/return values](c-info.ufunc-tutorial.html#example-numpy-ufunc-with-multiple-arguments-return-values)
    * [Example NumPy ufunc with structured array dtype arguments](c-info.ufunc-tutorial.html#example-numpy-ufunc-with-structured-array-dtype-arguments)
  * [Beyond the basics](c-info.beyond-basics.html)
    * [Iterating over elements in the array](c-info.beyond-basics.html#iterating-over-elements-in-the-array)
      * [Basic iteration](c-info.beyond-basics.html#basic-iteration)
      * [Iterating over all but one axis](c-info.beyond-basics.html#iterating-over-all-but-one-axis)
      * [Iterating over multiple arrays](c-info.beyond-basics.html#iterating-over-multiple-arrays)
      * [Broadcasting over multiple arrays](c-info.beyond-basics.html#broadcasting-over-multiple-arrays)
    * [User-defined data-types](c-info.beyond-basics.html#user-defined-data-types)
      * [Adding the new data-type](c-info.beyond-basics.html#adding-the-new-data-type)
      * [Registering a casting function](c-info.beyond-basics.html#registering-a-casting-function)
      * [Registering coercion rules](c-info.beyond-basics.html#registering-coercion-rules)
      * [Registering a ufunc loop](c-info.beyond-basics.html#registering-a-ufunc-loop)
    * [Subtyping the ndarray in C](c-info.beyond-basics.html#subtyping-the-ndarray-in-c)
      * [Creating sub-types](c-info.beyond-basics.html#creating-sub-types)
      * [Specific features of ndarray sub-typing](c-info.beyond-basics.html#specific-features-of-ndarray-sub-typing)
        * [The __array_finalize__ method](c-info.beyond-basics.html#the-array-finalize-method)
          * [`ndarray.__array_finalize__`](c-info.beyond-basics.html#ndarray.__array_finalize__)
        * [The __array_priority__ attribute](c-info.beyond-basics.html#the-array-priority-attribute)
          * [`ndarray.__array_priority__`](c-info.beyond-basics.html#ndarray.__array_priority__)
        * [The __array_wrap__ method](c-info.beyond-basics.html#the-array-wrap-method)
          * [`ndarray.__array_wrap__`](c-info.beyond-basics.html#ndarray.__array_wrap__)



[ __ previous Printing NumPy Arrays ](how-to-print.html "previous page") [ next How to extend NumPy __](c-info.how-to-extend.html "next page")

---

## Interoperability with NumPy

**Source:** [https://numpy.org/devdocs/user/basics.interoperability.html](https://numpy.org/devdocs/user/basics.interoperability.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * Interoperability with NumPy



# Interoperability with NumPy[#](#interoperability-with-numpy "Link to this heading")

NumPy’s ndarray objects provide both a high-level API for operations on array-structured data and a concrete implementation of the API based on [strided in-RAM storage](../reference/arrays.html#arrays). While this API is powerful and fairly general, its concrete implementation has limitations. As datasets grow and NumPy becomes used in a variety of new environments and architectures, there are cases where the strided in-RAM storage strategy is inappropriate, which has caused different libraries to reimplement this API for their own uses. This includes GPU arrays ([CuPy](https://cupy.dev/)), Sparse arrays ([`scipy.sparse`](https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse "\(in SciPy v1.17.0\)"), [PyData/Sparse](https://sparse.pydata.org/)) and parallel arrays ([Dask](https://docs.dask.org/) arrays) as well as various NumPy-like implementations in deep learning frameworks, like [TensorFlow](https://www.tensorflow.org/) and [PyTorch](https://pytorch.org/). Similarly, there are many projects that build on top of the NumPy API for labeled and indexed arrays ([XArray](https://xarray.dev/)), automatic differentiation ([JAX](https://jax.readthedocs.io/)), masked arrays ([`numpy.ma`](../reference/maskedarray.generic.html#module-numpy.ma "numpy.ma")), physical units ([astropy.units](https://docs.astropy.org/en/stable/units/), [pint](https://pint.readthedocs.io/), [unyt](https://unyt.readthedocs.io/)), among others that add additional functionality on top of the NumPy API.

Yet, users still want to work with these arrays using the familiar NumPy API and reuse existing code with minimal (ideally zero) porting overhead. With this goal in mind, various protocols are defined for implementations of multi-dimensional arrays with high-level APIs matching NumPy.

Broadly speaking, there are three groups of features used for interoperability with NumPy:

  1. Methods of turning a foreign object into an ndarray;

  2. Methods of deferring execution from a NumPy function to another array library;

  3. Methods that use NumPy functions and return an instance of a foreign object.




We describe these features below.

## 1\. Using arbitrary objects in NumPy[#](#using-arbitrary-objects-in-numpy "Link to this heading")

The first set of interoperability features from the NumPy API allows foreign objects to be treated as NumPy arrays whenever possible. When NumPy functions encounter a foreign object, they will try (in order):

  1. The buffer protocol, described [in the Python C-API documentation](https://docs.python.org/3/c-api/buffer.html "\(in Python v3.14\)").

  2. The `__array_interface__` protocol, described [in this page](../reference/arrays.interface.html#arrays-interface). A precursor to Python’s buffer protocol, it defines a way to access the contents of a NumPy array from other C extensions.

  3. The `__array__()` method, which asks an arbitrary object to convert itself into an array.




For both the buffer and the `__array_interface__` protocols, the object describes its memory layout and NumPy does everything else (zero-copy if possible). If that’s not possible, the object itself is responsible for returning a `ndarray` from `__array__()`.

[DLPack](https://dmlc.github.io/dlpack/latest/index.html "\(in DLPack\)") is yet another protocol to convert foreign objects to NumPy arrays in a language and device agnostic manner. NumPy doesn’t implicitly convert objects to ndarrays using DLPack. It provides the function [`numpy.from_dlpack`](../reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack") that accepts any object implementing the `__dlpack__` method and outputs a NumPy ndarray (which is generally a view of the input object’s data buffer). The [Python Specification for DLPack](https://dmlc.github.io/dlpack/latest/python_spec.html#python-spec "\(in DLPack\)") page explains the `__dlpack__` protocol in detail.

### `dtype` interoperability[#](#dtype-interoperability "Link to this heading")

Similar to `__array__()` for array objects, defining `__numpy_dtype__` allows a custom dtype object to be interoperable with NumPy. The `__numpy_dtype__` must return a NumPy dtype instance (note that `np.float64` is not a dtype instance, `np.dtype(np.float64)` is).

New in version 2.4: Before NumPy 2.4 a `.dtype` attribute was treated similarly. As of NumPy 2.4 both is accepted and implementing `__numpy_dtype__` prevents `.dtype` from being checked.

### The array interface protocol[#](#the-array-interface-protocol "Link to this heading")

The [array interface protocol](../reference/arrays.interface.html#arrays-interface) defines a way for array-like objects to reuse each other’s data buffers. Its implementation relies on the existence of the following attributes or methods:

  * `__array_interface__`: a Python dictionary containing the shape, the element type, and optionally, the data buffer address and the strides of an array-like object;

  * `__array__()`: a method returning the NumPy ndarray copy or a view of an array-like object;




The `__array_interface__` attribute can be inspected directly:
    
    
    >>> import numpy as np
    >>> x = np.array([1, 2, 5.0, 8])
    >>> x.__array_interface__
    {'data': (94708397920832, False), 'strides': None, 'descr': [('', '<f8')], 'typestr': '<f8', 'shape': (4,), 'version': 3}
    

The `__array_interface__` attribute can also be used to manipulate the object data in place:
    
    
    >>> class wrapper():
    ...     pass
    ...
    >>> arr = np.array([1, 2, 3, 4])
    >>> buf = arr.__array_interface__
    >>> buf
    {'data': (140497590272032, False), 'strides': None, 'descr': [('', '<i8')], 'typestr': '<i8', 'shape': (4,), 'version': 3}
    >>> buf['shape'] = (2, 2)
    >>> w = wrapper()
    >>> w.__array_interface__ = buf
    >>> new_arr = np.array(w, copy=False)
    >>> new_arr
    array([[1, 2],
           [3, 4]])
    

We can check that `arr` and `new_arr` share the same data buffer:
    
    
    >>> new_arr[0, 0] = 1000
    >>> new_arr
    array([[1000,    2],
           [   3,    4]])
    >>> arr
    array([1000, 2, 3, 4])
    

### The `__array__()` method[#](#the-array-method "Link to this heading")

The [__array__()](../reference/arrays.classes.html#numpy.class.__array__) method ensures that any NumPy-like object (an array, any object exposing the array interface, an object whose `__array__()` method returns an array or any nested sequence) that implements it can be used as a NumPy array. If possible, this will mean using `__array__()` to create a NumPy ndarray view of the array-like object. Otherwise, this copies the data into a new ndarray object. This is not optimal, as coercing arrays into ndarrays may cause performance problems or create the need for copies and loss of metadata, as the original object and any attributes/behavior it may have had, is lost.

The signature of the method should be `__array__(self, dtype=None, copy=None)`. If a passed `dtype` isn’t `None` and different than the object’s data type, a casting should happen to a specified type. If `copy` is `None`, a copy should be made only if `dtype` argument enforces it. For `copy=True`, a copy should always be made, where `copy=False` should raise an exception if a copy is needed.

If a class implements the old signature `__array__(self)`, for `np.array(a)` a warning will be raised saying that `dtype` and `copy` arguments are missing.

### The DLPack Protocol[#](#the-dlpack-protocol "Link to this heading")

The [DLPack](https://dmlc.github.io/dlpack/latest/index.html "\(in DLPack\)") protocol defines a memory-layout of strided n-dimensional array objects. It offers the following syntax for data exchange:

  1. A [`numpy.from_dlpack`](../reference/generated/numpy.from_dlpack.html#numpy.from_dlpack "numpy.from_dlpack") function, which accepts (array) objects with a `__dlpack__` method and uses that method to construct a new array containing the data from `x`.

  2. `__dlpack__(self, stream=None)` and `__dlpack_device__` methods on the array object, which will be called from within `from_dlpack`, to query what device the array is on (may be needed to pass in the correct stream, e.g. in the case of multiple GPUs) and to access the data.




Unlike the buffer protocol, DLPack allows exchanging arrays containing data on devices other than the CPU (e.g. Vulkan or GPU). Since NumPy only supports CPU, it can only convert objects whose data exists on the CPU. But other libraries, like [PyTorch](https://pytorch.org/) and [CuPy](https://cupy.dev/), may exchange data on GPU using this protocol.

## 2\. Operating on foreign objects without converting[#](#operating-on-foreign-objects-without-converting "Link to this heading")

A second set of methods defined by the NumPy API allows us to defer the execution from a NumPy function to another array library.

Consider the following function.
    
    
    >>> import numpy as np
    >>> def f(x):
    ...     return np.mean(np.exp(x))
    

Note that [`np.exp`](../reference/generated/numpy.exp.html#numpy.exp "numpy.exp") is a [ufunc](basics.ufuncs.html#ufuncs-basics), which means that it operates on ndarrays in an element-by-element fashion. On the other hand, [`np.mean`](../reference/generated/numpy.mean.html#numpy.mean "numpy.mean") operates along one of the array’s axes.

We can apply `f` to a NumPy ndarray object directly:
    
    
    >>> x = np.array([1, 2, 3, 4])
    >>> f(x)
    21.1977562209304
    

We would like this function to work equally well with any NumPy-like array object.

NumPy allows a class to indicate that it would like to handle computations in a custom-defined way through the following interfaces:

  * `__array_ufunc__`: allows third-party objects to support and override [ufuncs](basics.ufuncs.html#ufuncs-basics).

  * `__array_function__`: a catch-all for NumPy functionality that is not covered by the `__array_ufunc__` protocol for universal functions.




As long as foreign objects implement the `__array_ufunc__` or `__array_function__` protocols, it is possible to operate on them without the need for explicit conversion.

### The `__array_ufunc__` protocol[#](#the-array-ufunc-protocol "Link to this heading")

A [universal function (or ufunc for short)](basics.ufuncs.html#ufuncs-basics) is a “vectorized” wrapper for a function that takes a fixed number of specific inputs and produces a fixed number of specific outputs. The output of the ufunc (and its methods) is not necessarily an ndarray, if not all input arguments are ndarrays. Indeed, if any input defines an `__array_ufunc__` method, control will be passed completely to that function, i.e., the ufunc is overridden. The `__array_ufunc__` method defined on that (non-ndarray) object has access to the NumPy ufunc. Because ufuncs have a well-defined structure, the foreign `__array_ufunc__` method may rely on ufunc attributes like `.at()`, `.reduce()`, and others.

A subclass can override what happens when executing NumPy ufuncs on it by overriding the default `ndarray.__array_ufunc__` method. This method is executed instead of the ufunc and should return either the result of the operation, or `NotImplemented` if the operation requested is not implemented.

### The `__array_function__` protocol[#](#the-array-function-protocol "Link to this heading")

To achieve enough coverage of the NumPy API to support downstream projects, there is a need to go beyond `__array_ufunc__` and implement a protocol that allows arguments of a NumPy function to take control and divert execution to another function (for example, a GPU or parallel implementation) in a way that is safe and consistent across projects.

The semantics of `__array_function__` are very similar to `__array_ufunc__`, except the operation is specified by an arbitrary callable object rather than a ufunc instance and method. For more details, see [NEP 18 — A dispatch mechanism for NumPy’s high level array functions](https://numpy.org/neps/nep-0018-array-function-protocol.html#nep18 "\(in NumPy Enhancement Proposals\)").

## 3\. Returning foreign objects[#](#returning-foreign-objects "Link to this heading")

A third type of feature set is meant to use the NumPy function implementation and then convert the return value back into an instance of the foreign object. The `__array_finalize__` and `__array_wrap__` methods act behind the scenes to ensure that the return type of a NumPy function can be specified as needed.

The `__array_finalize__` method is the mechanism that NumPy provides to allow subclasses to handle the various ways that new instances get created. This method is called whenever the system internally allocates a new array from an object which is a subclass (subtype) of the ndarray. It can be used to change attributes after construction, or to update meta-information from the “parent.”

The `__array_wrap__` method “wraps up the action” in the sense of allowing any object (such as user-defined functions) to set the type of its return value and update attributes and metadata. This can be seen as the opposite of the `__array__` method. At the end of every object that implements `__array_wrap__`, this method is called on the input object with the highest _array priority_ , or the output object if one was specified. The `__array_priority__` attribute is used to determine what type of object to return in situations where there is more than one possibility for the Python type of the returned object. For example, subclasses may opt to use this method to transform the output array into an instance of the subclass and update metadata before returning the array to the user.

For more information on these methods, see [Subclassing ndarray](basics.subclassing.html#basics-subclassing) and [Specific features of ndarray sub-typing](c-info.beyond-basics.html#specific-array-subtyping).

## Interoperability examples[#](#interoperability-examples "Link to this heading")

### Example: Pandas `Series` objects[#](#example-pandas-series-objects "Link to this heading")

Consider the following:
    
    
    >>> import pandas as pd
    >>> ser = pd.Series([1, 2, 3, 4])
    >>> type(ser)
    pandas.core.series.Series
    

Now, `ser` is **not** an ndarray, but because it [implements the __array_ufunc__ protocol](https://pandas.pydata.org/docs/user_guide/dsintro.html#dataframe-interoperability-with-numpy-functions), we can apply ufuncs to it as if it were an ndarray:
    
    
    >>> np.exp(ser)
       0     2.718282
       1     7.389056
       2    20.085537
       3    54.598150
       dtype: float64
    >>> np.sin(ser)
       0    0.841471
       1    0.909297
       2    0.141120
       3   -0.756802
       dtype: float64
    

We can even do operations with other ndarrays:
    
    
    >>> np.add(ser, np.array([5, 6, 7, 8]))
       0     6
       1     8
       2    10
       3    12
       dtype: int64
    >>> f(ser)
    21.1977562209304
    >>> result = ser.__array__()
    >>> type(result)
    numpy.ndarray
    

### Example: PyTorch tensors[#](#example-pytorch-tensors "Link to this heading")

[PyTorch](https://pytorch.org/) is an optimized tensor library for deep learning using GPUs and CPUs. PyTorch arrays are commonly called _tensors_. Tensors are similar to NumPy’s ndarrays, except that tensors can run on GPUs or other hardware accelerators. In fact, tensors and NumPy arrays can often share the same underlying memory, eliminating the need to copy data.
    
    
    >>> import torch
    >>> data = [[1, 2],[3, 4]]
    >>> x_np = np.array(data)
    >>> x_tensor = torch.tensor(data)
    

Note that `x_np` and `x_tensor` are different kinds of objects:
    
    
    >>> x_np
    array([[1, 2],
           [3, 4]])
    >>> x_tensor
    tensor([[1, 2],
            [3, 4]])
    

However, we can treat PyTorch tensors as NumPy arrays without the need for explicit conversion:
    
    
    >>> np.exp(x_tensor)
    tensor([[ 2.7183,  7.3891],
            [20.0855, 54.5982]], dtype=torch.float64)
    

Also, note that the return type of this function is compatible with the initial data type.

Warning

While this mixing of ndarrays and tensors may be convenient, it is not recommended. It will not work for non-CPU tensors, and will have unexpected behavior in corner cases. Users should prefer explicitly converting the ndarray to a tensor.

Note

PyTorch does not implement `__array_function__` or `__array_ufunc__`. Under the hood, the `Tensor.__array__()` method returns a NumPy ndarray as a view of the tensor data buffer. See [this issue](https://github.com/pytorch/pytorch/issues/24015) and the [__torch_function__ implementation](https://github.com/pytorch/pytorch/blob/master/torch/overrides.py) for details.

Note also that we can see `__array_wrap__` in action here, even though `torch.Tensor` is not a subclass of ndarray:
    
    
    >>> import torch
    >>> t = torch.arange(4)
    >>> np.abs(t)
    tensor([0, 1, 2, 3])
    

PyTorch implements `__array_wrap__` to be able to get tensors back from NumPy functions, and we can modify it directly to control which type of objects are returned from these functions.

### Example: CuPy arrays[#](#example-cupy-arrays "Link to this heading")

CuPy is a NumPy/SciPy-compatible array library for GPU-accelerated computing with Python. CuPy implements a subset of the NumPy interface by implementing `cupy.ndarray`, [a counterpart to NumPy ndarrays](https://docs.cupy.dev/en/stable/reference/ndarray.html).
    
    
    >>> import cupy as cp
    >>> x_gpu = cp.array([1, 2, 3, 4])
    

The `cupy.ndarray` object implements the `__array_ufunc__` interface. This enables NumPy ufuncs to be applied to CuPy arrays (this will defer operation to the matching CuPy CUDA/ROCm implementation of the ufunc):
    
    
    >>> np.mean(np.exp(x_gpu))
    array(21.19775622)
    

Note that the return type of these operations is still consistent with the initial type:
    
    
    >>> arr = cp.random.randn(1, 2, 3, 4).astype(cp.float32)
    >>> result = np.sum(arr)
    >>> print(type(result))
    <class 'cupy._core.core.ndarray'>
    

See [this page in the CuPy documentation for details](https://docs.cupy.dev/en/stable/reference/ufunc.html).

`cupy.ndarray` also implements the `__array_function__` interface, meaning it is possible to do operations such as
    
    
    >>> a = np.random.randn(100, 100)
    >>> a_gpu = cp.asarray(a)
    >>> qr_gpu = np.linalg.qr(a_gpu)
    

CuPy implements many NumPy functions on `cupy.ndarray` objects, but not all. See [the CuPy documentation](https://docs.cupy.dev/en/stable/user_guide/difference.html) for details.

### Example: Dask arrays[#](#example-dask-arrays "Link to this heading")

Dask is a flexible library for parallel computing in Python. Dask Array implements a subset of the NumPy ndarray interface using blocked algorithms, cutting up the large array into many small arrays. This allows computations on larger-than-memory arrays using multiple cores.

Dask supports `__array__()` and `__array_ufunc__`.
    
    
    >>> import dask.array as da
    >>> x = da.random.normal(1, 0.1, size=(20, 20), chunks=(10, 10))
    >>> np.mean(np.exp(x))
    dask.array<mean_agg-aggregate, shape=(), dtype=float64, chunksize=(), chunktype=numpy.ndarray>
    >>> np.mean(np.exp(x)).compute()
    5.090097550553843
    

Note

Dask is lazily evaluated, and the result from a computation isn’t computed until you ask for it by invoking `compute()`.

See [the Dask array documentation](https://docs.dask.org/en/stable/array.html) and the [scope of Dask arrays interoperability with NumPy arrays](https://docs.dask.org/en/stable/array.html#scope) for details.

### Example: DLPack[#](#example-dlpack "Link to this heading")

Several Python data science libraries implement the `__dlpack__` protocol. Among them are [PyTorch](https://pytorch.org/) and [CuPy](https://cupy.dev/). A full list of libraries that implement this protocol can be found on [this page of DLPack documentation](https://dmlc.github.io/dlpack/latest/index.html "\(in DLPack\)").

Convert a PyTorch CPU tensor to NumPy array:
    
    
    >>> import torch
    >>> x_torch = torch.arange(5)
    >>> x_torch
    tensor([0, 1, 2, 3, 4])
    >>> x_np = np.from_dlpack(x_torch)
    >>> x_np
    array([0, 1, 2, 3, 4])
    >>> # note that x_np is a view of x_torch
    >>> x_torch[1] = 100
    >>> x_torch
    tensor([  0, 100,   2,   3,   4])
    >>> x_np
    array([  0, 100,   2,   3,   4])
    

The imported arrays are read-only so writing or operating in-place will fail:
    
    
    >>> x_np.flags.writeable
    False
    >>> x_np[1] = 1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: assignment destination is read-only
    

A copy must be created in order to operate on the imported arrays in-place, but will mean duplicating the memory. Do not do this for very large arrays:
    
    
    >>> x_np_copy = x_np.copy()
    >>> x_np_copy.sort()  # works
    

Note

GPU tensors cannot be directly zero-copy converted to NumPy arrays since NumPy does not support GPU devices. However, since DLPack v1, cross-device copy is supported via the `device` parameter:
    
    
    >>> x_torch = torch.arange(5, device='cuda')
    >>> np.from_dlpack(x_torch)  # fails: implicit device=None means same device
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    RuntimeError: Unsupported device in DLTensor.
    >>> np.from_dlpack(x_torch, device='cpu')  # works: explicit copy to CPU
    array([0, 1, 2, 3, 4])
    

If both libraries support the device the data buffer is on, it is possible to use the `__dlpack__` protocol (e.g. [PyTorch](https://pytorch.org/) and [CuPy](https://cupy.dev/)):
    
    
    >>> x_torch = torch.arange(5, device='cuda')
    >>> x_cupy = cupy.from_dlpack(x_torch)
    

Similarly, a NumPy array can be converted to a PyTorch tensor:
    
    
    >>> x_np = np.arange(5)
    >>> x_torch = torch.from_dlpack(x_np)
    

Read-only arrays cannot be exported:
    
    
    >>> x_np = np.arange(5)
    >>> x_np.flags.writeable = False
    >>> torch.from_dlpack(x_np)  
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File ".../site-packages/torch/utils/dlpack.py", line 63, in from_dlpack
        dlpack = ext_tensor.__dlpack__()
    TypeError: NumPy currently only supports dlpack for writeable arrays
    

## Further reading[#](#further-reading "Link to this heading")

  * [The array interface protocol](../reference/arrays.interface.html#arrays-interface)

  * [Writing custom array containers](basics.dispatch.html#basics-dispatch)

  * [Special attributes and methods](../reference/arrays.classes.html#special-attributes-and-methods) (details on the `__array_ufunc__` and `__array_function__` protocols)

  * [Subclassing ndarray](basics.subclassing.html#basics-subclassing) (details on the `__array_wrap__` and `__array_finalize__` methods)

  * [Specific features of ndarray sub-typing](c-info.beyond-basics.html#specific-array-subtyping) (more details on the implementation of `__array_finalize__`, `__array_wrap__` and `__array_priority__`)

  * [NumPy roadmap: interoperability](https://numpy.org/neps/roadmap.html "\(in NumPy Enhancement Proposals\)")

  * [PyTorch documentation on the Bridge with NumPy](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#bridge-to-np-label)




[ __ previous Subclassing ndarray ](basics.subclassing.html "previous page") [ next Glossary __](../glossary.html "next page")

__On this page

  * [1\. Using arbitrary objects in NumPy](#using-arbitrary-objects-in-numpy)
    * [`dtype` interoperability](#dtype-interoperability)
    * [The array interface protocol](#the-array-interface-protocol)
    * [The `__array__()` method](#the-array-method)
    * [The DLPack Protocol](#the-dlpack-protocol)
  * [2\. Operating on foreign objects without converting](#operating-on-foreign-objects-without-converting)
    * [The `__array_ufunc__` protocol](#the-array-ufunc-protocol)
    * [The `__array_function__` protocol](#the-array-function-protocol)
  * [3\. Returning foreign objects](#returning-foreign-objects)
  * [Interoperability examples](#interoperability-examples)
    * [Example: Pandas `Series` objects](#example-pandas-series-objects)
    * [Example: PyTorch tensors](#example-pytorch-tensors)
    * [Example: CuPy arrays](#example-cupy-arrays)
    * [Example: Dask arrays](#example-dask-arrays)
    * [Example: DLPack](#example-dlpack)
  * [Further reading](#further-reading)

---

## Reading and writing files

**Source:** [https://numpy.org/devdocs/user/how-to-io.html](https://numpy.org/devdocs/user/how-to-io.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy how-tos](howtos_index.html)
  * Reading and writing files



# Reading and writing files[#](#reading-and-writing-files "Link to this heading")

This page tackles common applications; for the full collection of I/O routines, see [Input and output](../reference/routines.io.html#routines-io).

## Reading text and [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) files[#](#reading-text-and-csv-files "Link to this heading")

### With no missing values[#](#with-no-missing-values "Link to this heading")

Use [`numpy.loadtxt`](../reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt").

### With missing values[#](#with-missing-values "Link to this heading")

Use [`numpy.genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt").

[`numpy.genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") will either

  * return a [masked array](../reference/maskedarray.generic.html#maskedarray-generic) **masking out missing values** (if `usemask=True`), or

  * **fill in the missing value** with the value specified in `filling_values` (default is `np.nan` for float, -1 for int).




#### With non-whitespace delimiters[#](#with-non-whitespace-delimiters "Link to this heading")
    
    
    >>> with open("csv.txt", "r") as f:
    ...     print(f.read())
    1, 2, 3
    4,, 6
    7, 8, 9
    

##### Masked-array output[#](#masked-array-output "Link to this heading")
    
    
    >>> np.genfromtxt("csv.txt", delimiter=",", usemask=True)
    masked_array(
      data=[[1.0, 2.0, 3.0],
            [4.0, --, 6.0],
            [7.0, 8.0, 9.0]],
      mask=[[False, False, False],
            [False,  True, False],
            [False, False, False]],
      fill_value=1e+20)
    

##### Array output[#](#array-output "Link to this heading")
    
    
    >>> np.genfromtxt("csv.txt", delimiter=",")
    array([[ 1.,  2.,  3.],
           [ 4., nan,  6.],
           [ 7.,  8.,  9.]])
    

##### Array output, specified fill-in value[#](#array-output-specified-fill-in-value "Link to this heading")
    
    
    >>> np.genfromtxt("csv.txt", delimiter=",", dtype=np.int8, filling_values=99)
    array([[ 1,  2,  3],
           [ 4, 99,  6],
           [ 7,  8,  9]], dtype=int8)
    

#### Whitespace-delimited[#](#whitespace-delimited "Link to this heading")

[`numpy.genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") can also parse whitespace-delimited data files that have missing values if

  * **Each field has a fixed width** : Use the width as the _delimiter_ argument.:
        
        # File with width=4. The data does not have to be justified (for example,
        # the 2 in row 1), the last column can be less than width (for example, the 6
        # in row 2), and no delimiting character is required (for instance 8888 and 9
        # in row 3)
        
        >>> with open("fixedwidth.txt", "r") as f:
        ...    data = (f.read())
        >>> print(data)
        1   2      3
        44      6
        7   88889
        
        # Showing spaces as ^
        >>> print(data.replace(" ","^"))
        1^^^2^^^^^^3
        44^^^^^^6
        7^^^88889
        
        >>> np.genfromtxt("fixedwidth.txt", delimiter=4)
        array([[1.000e+00, 2.000e+00, 3.000e+00],
               [4.400e+01,       nan, 6.000e+00],
               [7.000e+00, 8.888e+03, 9.000e+00]])
        

  * **A special value (e.g. “x”) indicates a missing field** : Use it as the _missing_values_ argument.
        
        >>> with open("nan.txt", "r") as f:
        ...     print(f.read())
        1 2 3
        44 x 6
        7  8888 9
        
        
        >>> np.genfromtxt("nan.txt", missing_values="x")
        array([[1.000e+00, 2.000e+00, 3.000e+00],
               [4.400e+01,       nan, 6.000e+00],
               [7.000e+00, 8.888e+03, 9.000e+00]])
        

  * **You want to skip the rows with missing values** : Set _invalid_raise=False_.
        
        >>> with open("skip.txt", "r") as f:
        ...     print(f.read())
        1 2   3
        44    6
        7 888 9
        
        
        >>> np.genfromtxt("skip.txt", invalid_raise=False)  
        __main__:1: ConversionWarning: Some errors were detected !
            Line #2 (got 2 columns instead of 3)
        array([[  1.,   2.,   3.],
               [  7., 888.,   9.]])
        

  * **The delimiter whitespace character is different from the whitespace that indicates missing data**. For instance, if columns are delimited by `\t`, then missing data will be recognized if it consists of one or more spaces.:
        
        >>> with open("tabs.txt", "r") as f:
        ...    data = (f.read())
        >>> print(data)
        1       2       3
        44              6
        7       888     9
        
        # Tabs vs. spaces
        >>> print(data.replace("\t","^"))
        1^2^3
        44^ ^6
        7^888^9
        
        >>> np.genfromtxt("tabs.txt", delimiter="\t", missing_values=" +")
        array([[  1.,   2.,   3.],
               [ 44.,  nan,   6.],
               [  7., 888.,   9.]])
        




## Read a file in .npy or .npz format[#](#read-a-file-in-npy-or-npz-format "Link to this heading")

Choices:

  * Use [`numpy.load`](../reference/generated/numpy.load.html#numpy.load "numpy.load"). It can read files generated by any of [`numpy.save`](../reference/generated/numpy.save.html#numpy.save "numpy.save"), [`numpy.savez`](../reference/generated/numpy.savez.html#numpy.savez "numpy.savez"), or [`numpy.savez_compressed`](../reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed").

  * Use memory mapping. See [`numpy.lib.format.open_memmap`](../reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap").




## Write to a file to be read back by NumPy[#](#write-to-a-file-to-be-read-back-by-numpy "Link to this heading")

### Binary[#](#binary "Link to this heading")

Use [`numpy.save`](../reference/generated/numpy.save.html#numpy.save "numpy.save"), or to store multiple arrays [`numpy.savez`](../reference/generated/numpy.savez.html#numpy.savez "numpy.savez") or [`numpy.savez_compressed`](../reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed").

For [security and portability](#how-to-io-pickle-file), set `allow_pickle=False` unless the dtype contains Python objects, which requires pickling.

Masked arrays [`can't currently be saved`](../reference/generated/numpy.ma.MaskedArray.tofile.html#numpy.ma.MaskedArray.tofile "numpy.ma.MaskedArray.tofile"), nor can other arbitrary array subclasses.

### Human-readable[#](#human-readable "Link to this heading")

[`numpy.save`](../reference/generated/numpy.save.html#numpy.save "numpy.save") and [`numpy.savez`](../reference/generated/numpy.savez.html#numpy.savez "numpy.savez") create binary files. To **write a human-readable file** , use [`numpy.savetxt`](../reference/generated/numpy.savetxt.html#numpy.savetxt "numpy.savetxt"). The array can only be 1- or 2-dimensional, and there’s no `savetxtz` for multiple files.

### Large arrays[#](#large-arrays "Link to this heading")

See [Write or read large arrays](#how-to-io-large-arrays).

## Read an arbitrarily formatted binary file (“binary blob”)[#](#read-an-arbitrarily-formatted-binary-file-binary-blob "Link to this heading")

Use a [structured array](basics.rec.html).

**Example:**

The `.wav` file header is a 44-byte block preceding `data_size` bytes of the actual sound data:
    
    
    chunk_id         "RIFF"
    chunk_size       4-byte unsigned little-endian integer
    format           "WAVE"
    fmt_id           "fmt "
    fmt_size         4-byte unsigned little-endian integer
    audio_fmt        2-byte unsigned little-endian integer
    num_channels     2-byte unsigned little-endian integer
    sample_rate      4-byte unsigned little-endian integer
    byte_rate        4-byte unsigned little-endian integer
    block_align      2-byte unsigned little-endian integer
    bits_per_sample  2-byte unsigned little-endian integer
    data_id          "data"
    data_size        4-byte unsigned little-endian integer
    

The `.wav` file header as a NumPy structured dtype:
    
    
    wav_header_dtype = np.dtype([
        ("chunk_id", (bytes, 4)), # flexible-sized scalar type, item size 4
        ("chunk_size", "<u4"),    # little-endian unsigned 32-bit integer
        ("format", "S4"),         # 4-byte string, alternate spelling of (bytes, 4)
        ("fmt_id", "S4"),
        ("fmt_size", "<u4"),
        ("audio_fmt", "<u2"),     #
        ("num_channels", "<u2"),  # .. more of the same ...
        ("sample_rate", "<u4"),   #
        ("byte_rate", "<u4"),
        ("block_align", "<u2"),
        ("bits_per_sample", "<u2"),
        ("data_id", "S4"),
        ("data_size", "<u4"),
        #
        # the sound data itself cannot be represented here:
        # it does not have a fixed size
    ])
    
    header = np.fromfile(f, dtype=wave_header_dtype, count=1)[0]
    

This `.wav` example is for illustration; to read a `.wav` file in real life, use Python’s built-in module [`wave`](https://docs.python.org/3/library/wave.html#module-wave "\(in Python v3.14\)").

(Adapted from Pauli Virtanen, [Advanced NumPy](https://scipy-lectures.org/advanced/advanced_numpy/index.html#advanced-numpy "\(in Scipy lecture notes v2022.1\)"), licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).)

## Write or read large arrays[#](#write-or-read-large-arrays "Link to this heading")

**Arrays too large to fit in memory** can be treated like ordinary in-memory arrays using memory mapping.

  * Raw array data written with [`numpy.ndarray.tofile`](../reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile") or [`numpy.ndarray.tobytes`](../reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes") can be read with [`numpy.memmap`](../reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap"):
        
        array = numpy.memmap("mydata/myarray.arr", mode="r", dtype=np.int16, shape=(1024, 1024))
        

  * Files output by [`numpy.save`](../reference/generated/numpy.save.html#numpy.save "numpy.save") (that is, using the numpy format) can be read using [`numpy.load`](../reference/generated/numpy.load.html#numpy.load "numpy.load") with the `mmap_mode` keyword argument:
        
        large_array[some_slice] = np.load("path/to/small_array", mmap_mode="r")
        




Memory mapping lacks features like data chunking and compression; more full-featured formats and libraries usable with NumPy include:

  * **HDF5** : [h5py](https://www.h5py.org/) or [PyTables](https://www.pytables.org/).

  * **Zarr** : [here](https://zarr.readthedocs.io/en/stable/tutorial.html#reading-and-writing-data).

  * **NetCDF** : [`scipy.io.netcdf_file`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.netcdf_file.html#scipy.io.netcdf_file "\(in SciPy v1.17.0\)").




For tradeoffs among memmap, Zarr, and HDF5, see [pythonspeed.com](https://pythonspeed.com/articles/mmap-vs-zarr-hdf5/).

## Write files for reading by other (non-NumPy) tools[#](#write-files-for-reading-by-other-non-numpy-tools "Link to this heading")

Formats for **exchanging data** with other tools include HDF5, Zarr, and NetCDF (see [Write or read large arrays](#how-to-io-large-arrays)).

## Write or read a JSON file[#](#write-or-read-a-json-file "Link to this heading")

NumPy arrays and most NumPy scalars are **not** directly [JSON serializable](https://github.com/numpy/numpy/issues/12481). Instead, use a custom [`json.JSONEncoder`](https://docs.python.org/3/library/json.html#json.JSONEncoder "\(in Python v3.14\)") for NumPy types, which can be found using your favorite search engine.

## Save/restore using a pickle file[#](#save-restore-using-a-pickle-file "Link to this heading")

Avoid when possible; [pickles](https://docs.python.org/3/library/pickle.html "\(in Python v3.14\)") are not secure against erroneous or maliciously constructed data.

Use [`numpy.save`](../reference/generated/numpy.save.html#numpy.save "numpy.save") and [`numpy.load`](../reference/generated/numpy.load.html#numpy.load "numpy.load"). Set `allow_pickle=False`, unless the array dtype includes Python objects, in which case pickling is required.

[`numpy.load`](../reference/generated/numpy.load.html#numpy.load "numpy.load") and [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "\(in Python v3.14\)") submodule also support unpickling files created with NumPy 1.26.

## Convert from a pandas DataFrame to a NumPy array[#](#convert-from-a-pandas-dataframe-to-a-numpy-array "Link to this heading")

See [`pandas.Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "\(in pandas v3.0.3\)").

## Save/restore using [`tofile`](../reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile") and [`fromfile`](../reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")[#](#save-restore-using-tofile-and-fromfile "Link to this heading")

In general, prefer [`numpy.save`](../reference/generated/numpy.save.html#numpy.save "numpy.save") and [`numpy.load`](../reference/generated/numpy.load.html#numpy.load "numpy.load").

[`numpy.ndarray.tofile`](../reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile") and [`numpy.fromfile`](../reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile") lose information on endianness and precision and so are unsuitable for anything but scratch storage.

[ __ previous How to write a NumPy how-to ](how-to-how-to.html "previous page") [ next How to index `ndarrays` __](how-to-index.html "next page")

__On this page

  * [Reading text and CSV files](#reading-text-and-csv-files)
    * [With no missing values](#with-no-missing-values)
    * [With missing values](#with-missing-values)
      * [With non-whitespace delimiters](#with-non-whitespace-delimiters)
        * [Masked-array output](#masked-array-output)
        * [Array output](#array-output)
        * [Array output, specified fill-in value](#array-output-specified-fill-in-value)
      * [Whitespace-delimited](#whitespace-delimited)
  * [Read a file in .npy or .npz format](#read-a-file-in-npy-or-npz-format)
  * [Write to a file to be read back by NumPy](#write-to-a-file-to-be-read-back-by-numpy)
    * [Binary](#binary)
    * [Human-readable](#human-readable)
    * [Large arrays](#large-arrays)
  * [Read an arbitrarily formatted binary file (“binary blob”)](#read-an-arbitrarily-formatted-binary-file-binary-blob)
  * [Write or read large arrays](#write-or-read-large-arrays)
  * [Write files for reading by other (non-NumPy) tools](#write-files-for-reading-by-other-non-numpy-tools)
  * [Write or read a JSON file](#write-or-read-a-json-file)
  * [Save/restore using a pickle file](#save-restore-using-a-pickle-file)
  * [Convert from a pandas DataFrame to a NumPy array](#convert-from-a-pandas-dataframe-to-a-numpy-array)
  * [Save/restore using `tofile` and `fromfile`](#save-restore-using-tofile-and-fromfile)

---

## Importing data with genfromtxt

**Source:** [https://numpy.org/devdocs/user/basics.io.genfromtxt.html](https://numpy.org/devdocs/user/basics.io.genfromtxt.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy fundamentals](basics.html)
  * [I/O with NumPy](basics.io.html)
  * Importing data with `genfromtxt`



# Importing data with [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")[#](#importing-data-with-genfromtxt "Link to this heading")

NumPy provides several functions to create arrays from tabular data. We focus here on the [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") function.

In a nutshell, [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") runs two main loops. The first loop converts each line of the file in a sequence of strings. The second loop converts each string to the appropriate data type. This mechanism is slower than a single loop, but gives more flexibility. In particular, [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") is able to take missing data into account, when other faster and simpler functions like [`loadtxt`](../reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt") cannot.

Note

When giving examples, we will use the following conventions:
    
    
    >>> import numpy as np
    >>> from io import StringIO
    

## Defining the input[#](#defining-the-input "Link to this heading")

The only mandatory argument of [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") is the source of the data. It can be a string, a list of strings, a generator or an open file-like object with a `read` method, for example, a file or [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "\(in Python v3.14\)") object. If a single string is provided, it is assumed to be the name of a local or remote file. If a list of strings or a generator returning strings is provided, each string is treated as one line in a file. When the URL of a remote file is passed, the file is automatically downloaded to the current directory and opened.

Recognized file types are text files and archives. Currently, the function recognizes `gzip` and `bz2` (`bzip2`) archives. The type of the archive is determined from the extension of the file: if the filename ends with `'.gz'`, a `gzip` archive is expected; if it ends with `'bz2'`, a `bzip2` archive is assumed.

## Splitting the lines into columns[#](#splitting-the-lines-into-columns "Link to this heading")

### The `delimiter` argument[#](#the-delimiter-argument "Link to this heading")

Once the file is defined and open for reading, [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") splits each non-empty line into a sequence of strings. Empty or commented lines are just skipped. The `delimiter` keyword is used to define how the splitting should take place.

Quite often, a single character marks the separation between columns. For example, comma-separated files (CSV) use a comma (`,`) or a semicolon (`;`) as delimiter:
    
    
    >>> data = "1, 2, 3\n4, 5, 6"
    >>> np.genfromtxt(StringIO(data), delimiter=",")
    array([[1.,  2.,  3.],
           [4.,  5.,  6.]])
    

Another common separator is `"\t"`, the tabulation character. However, we are not limited to a single character, any string will do. By default, [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") assumes `delimiter=None`, meaning that the line is split along white spaces (including tabs) and that consecutive white spaces are considered as a single white space.

Alternatively, we may be dealing with a fixed-width file, where columns are defined as a given number of characters. In that case, we need to set `delimiter` to a single integer (if all the columns have the same size) or to a sequence of integers (if columns can have different sizes):
    
    
    >>> data = "  1  2  3\n  4  5 67\n890123  4"
    >>> np.genfromtxt(StringIO(data), delimiter=3)
    array([[  1.,    2.,    3.],
           [  4.,    5.,   67.],
           [890.,  123.,    4.]])
    >>> data = "123456789\n   4  7 9\n   4567 9"
    >>> np.genfromtxt(StringIO(data), delimiter=(4, 3, 2))
    array([[1234.,   567.,    89.],
           [   4.,     7.,     9.],
           [   4.,   567.,     9.]])
    

### The `autostrip` argument[#](#the-autostrip-argument "Link to this heading")

By default, when a line is decomposed into a series of strings, the individual entries are not stripped of leading nor trailing white spaces. This behavior can be overwritten by setting the optional argument `autostrip` to a value of `True`:
    
    
    >>> data = "1, abc , 2\n 3, xxx, 4"
    >>> # Without autostrip
    >>> np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5")
    array([['1', ' abc ', ' 2'],
           ['3', ' xxx', ' 4']], dtype='<U5')
    >>> # With autostrip
    >>> np.genfromtxt(StringIO(data), delimiter=",", dtype="|U5", autostrip=True)
    array([['1', 'abc', '2'],
           ['3', 'xxx', '4']], dtype='<U5')
    

### The `comments` argument[#](#the-comments-argument "Link to this heading")

The optional argument `comments` is used to define a character string that marks the beginning of a comment. By default, [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") assumes `comments='#'`. The comment marker may occur anywhere on the line. Any character present after the comment marker(s) is simply ignored:
    
    
    >>> data = """#
    ... # Skip me !
    ... # Skip me too !
    ... 1, 2
    ... 3, 4
    ... 5, 6 #This is the third line of the data
    ... 7, 8
    ... # And here comes the last line
    ... 9, 0
    ... """
    >>> np.genfromtxt(StringIO(data), comments="#", delimiter=",")
    array([[1., 2.],
           [3., 4.],
           [5., 6.],
           [7., 8.],
           [9., 0.]])
    

Note

There is one notable exception to this behavior: if the optional argument `names=True`, the first commented line will be examined for names.

## Skipping lines and choosing columns[#](#skipping-lines-and-choosing-columns "Link to this heading")

### The `skip_header` and `skip_footer` arguments[#](#the-skip-header-and-skip-footer-arguments "Link to this heading")

The presence of a header in the file can hinder data processing. In that case, we need to use the `skip_header` optional argument. The values of this argument must be an integer which corresponds to the number of lines to skip at the beginning of the file, before any other action is performed. Similarly, we can skip the last `n` lines of the file by using the `skip_footer` attribute and giving it a value of `n`:
    
    
    >>> data = "\n".join(str(i) for i in range(10))
    >>> np.genfromtxt(StringIO(data),)
    array([0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9.])
    >>> np.genfromtxt(StringIO(data),
    ...               skip_header=3, skip_footer=5)
    array([3.,  4.])
    

By default, `skip_header=0` and `skip_footer=0`, meaning that no lines are skipped.

### The `usecols` argument[#](#the-usecols-argument "Link to this heading")

In some cases, we are not interested in all the columns of the data but only a few of them. We can select which columns to import with the `usecols` argument. This argument accepts a single integer or a sequence of integers corresponding to the indices of the columns to import. Remember that by convention, the first column has an index of 0. Negative integers behave the same as regular Python negative indexes.

For example, if we want to import only the first and the last columns, we can use `usecols=(0, -1)`:
    
    
    >>> data = "1 2 3\n4 5 6"
    >>> np.genfromtxt(StringIO(data), usecols=(0, -1))
    array([[1.,  3.],
           [4.,  6.]])
    

If the columns have names, we can also select which columns to import by giving their name to the `usecols` argument, either as a sequence of strings or a comma-separated string:
    
    
    >>> data = "1 2 3\n4 5 6"
    >>> np.genfromtxt(StringIO(data),
    ...               names="a, b, c", usecols=("a", "c"))
    array([(1., 3.), (4., 6.)], dtype=[('a', '<f8'), ('c', '<f8')])
    >>> np.genfromtxt(StringIO(data),
    ...               names="a, b, c", usecols=("a, c"))
        array([(1., 3.), (4., 6.)], dtype=[('a', '<f8'), ('c', '<f8')])
    

## Choosing the data type[#](#choosing-the-data-type "Link to this heading")

The main way to control how the sequences of strings we have read from the file are converted to other types is to set the `dtype` argument. Acceptable values for this argument are:

  * a single type, such as `dtype=np.float64`. The output will be 2D with the given dtype, unless a name has been associated with each column with the use of the `names` argument (see below). Note that `dtype=np.float64` is the default for [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt").

  * a sequence of types, such as `dtype=(np.int_, np.float64, np.float64)`.

  * a comma-separated string, such as `dtype="i4,f8,|U3"`.

  * a dictionary with two keys `'names'` and `'formats'`.

  * a sequence of tuples `(name, type)`, such as `dtype=[('A', np.int_), ('B', np.float64)]`.

  * an existing [`numpy.dtype`](../reference/generated/numpy.dtype.html#numpy.dtype "numpy.dtype") object.

  * the special value `None`. In that case, the type of the columns will be determined from the data itself (see below).




In all the cases but the first one, the output will be a 1D array with a structured dtype. This dtype has as many fields as items in the sequence. The field names are defined with the `names` keyword.

When `dtype=None`, the type of each column is determined iteratively from its data. We start by checking whether a string can be converted to a boolean (that is, if the string matches `true` or `false` in lower cases); then whether it can be converted to an integer, then to a float, then to a complex and eventually to a string.

The option `dtype=None` is provided for convenience. However, it is significantly slower than setting the dtype explicitly.

## Setting the names[#](#setting-the-names "Link to this heading")

### The `names` argument[#](#the-names-argument "Link to this heading")

A natural approach when dealing with tabular data is to allocate a name to each column. A first possibility is to use an explicit structured dtype, as mentioned previously:
    
    
    >>> data = StringIO("1 2 3\n 4 5 6")
    >>> np.genfromtxt(data, dtype=[(_, np.int_) for _ in "abc"])
    array([(1, 2, 3), (4, 5, 6)],
          dtype=[('a', '<i8'), ('b', '<i8'), ('c', '<i8')])
    

Another simpler possibility is to use the `names` keyword with a sequence of strings or a comma-separated string:
    
    
    >>> data = StringIO("1 2 3\n 4 5 6")
    >>> np.genfromtxt(data, names="A, B, C")
    array([(1., 2., 3.), (4., 5., 6.)],
          dtype=[('A', '<f8'), ('B', '<f8'), ('C', '<f8')])
    

In the example above, we used the fact that by default, `dtype=np.float64`. By giving a sequence of names, we are forcing the output to a structured dtype.

We may sometimes need to define the column names from the data itself. In that case, we must use the `names` keyword with a value of `True`. The names will then be read from the first line (after the `skip_header` ones), even if the line is commented out:
    
    
    >>> data = StringIO("So it goes\n#a b c\n1 2 3\n 4 5 6")
    >>> np.genfromtxt(data, skip_header=1, names=True)
    array([(1., 2., 3.), (4., 5., 6.)],
          dtype=[('a', '<f8'), ('b', '<f8'), ('c', '<f8')])
    

The default value of `names` is `None`. If we give any other value to the keyword, the new names will overwrite the field names we may have defined with the dtype:
    
    
    >>> data = StringIO("1 2 3\n 4 5 6")
    >>> ndtype=[('a', np.int_), ('b', np.float64), ('c', np.int_)]
    >>> names = ["A", "B", "C"]
    >>> np.genfromtxt(data, names=names, dtype=ndtype)
    array([(1, 2., 3), (4, 5., 6)],
          dtype=[('A', '<i8'), ('B', '<f8'), ('C', '<i8')])
    

### The `defaultfmt` argument[#](#the-defaultfmt-argument "Link to this heading")

If `names=None` but a structured dtype is expected, names are defined with the standard NumPy default of `"f%i"`, yielding names like `f0`, `f1` and so forth:
    
    
    >>> data = StringIO("1 2 3\n 4 5 6")
    >>> np.genfromtxt(data, dtype=(np.int_, np.float64, np.int_))
    array([(1, 2., 3), (4, 5., 6)],
          dtype=[('f0', '<i8'), ('f1', '<f8'), ('f2', '<i8')])
    

In the same way, if we don’t give enough names to match the length of the dtype, the missing names will be defined with this default template:
    
    
    >>> data = StringIO("1 2 3\n 4 5 6")
    >>> np.genfromtxt(data, dtype=(np.int_, np.float64, np.int_), names="a")
    array([(1, 2., 3), (4, 5., 6)],
          dtype=[('a', '<i8'), ('f0', '<f8'), ('f1', '<i8')])
    

We can overwrite this default with the `defaultfmt` argument, that takes any format string:
    
    
    >>> data = StringIO("1 2 3\n 4 5 6")
    >>> np.genfromtxt(data, dtype=(np.int_, np.float64, np.int_), defaultfmt="var_%02i")
    array([(1, 2., 3), (4, 5., 6)],
          dtype=[('var_00', '<i8'), ('var_01', '<f8'), ('var_02', '<i8')])
    

Note

We need to keep in mind that `defaultfmt` is used only if some names are expected but not defined.

### Validating names[#](#validating-names "Link to this heading")

NumPy arrays with a structured dtype can also be viewed as [`recarray`](../reference/generated/numpy.recarray.html#numpy.recarray "numpy.recarray"), where a field can be accessed as if it were an attribute. For that reason, we may need to make sure that the field name doesn’t contain any space or invalid character, or that it does not correspond to the name of a standard attribute (like `size` or `shape`), which would confuse the interpreter. [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") accepts three optional arguments that provide a finer control on the names:

`deletechars`
    

Gives a string combining all the characters that must be deleted from the name. By default, invalid characters are `~!@#$%^&*()-=+~\|]}[{';: /?.>,<`.

`excludelist`
    

Gives a list of the names to exclude, such as `return`, `file`, `print`… If one of the input name is part of this list, an underscore character (`'_'`) will be appended to it.

`case_sensitive`
    

Whether the names should be case-sensitive (`case_sensitive=True`), converted to upper case (`case_sensitive=False` or `case_sensitive='upper'`) or to lower case (`case_sensitive='lower'`).

## Tweaking the conversion[#](#tweaking-the-conversion "Link to this heading")

### The `converters` argument[#](#the-converters-argument "Link to this heading")

Usually, defining a dtype is sufficient to define how the sequence of strings must be converted. However, some additional control may sometimes be required. For example, we may want to make sure that a date in a format `YYYY/MM/DD` is converted to a [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "\(in Python v3.14\)") object, or that a string like `xx%` is properly converted to a float between 0 and 1. In such cases, we should define conversion functions with the `converters` arguments.

The value of this argument is typically a dictionary with column indices or column names as keys and a conversion functions as values. These conversion functions can either be actual functions or lambda functions. In any case, they should accept only a string as input and output only a single element of the wanted type.

In the following example, the second column is converted from as string representing a percentage to a float between 0 and 1:
    
    
    >>> convertfunc = lambda x: float(x.strip("%"))/100.
    >>> data = "1, 2.3%, 45.\n6, 78.9%, 0"
    >>> names = ("i", "p", "n")
    >>> # General case .....
    >>> np.genfromtxt(StringIO(data), delimiter=",", names=names)
    array([(1., nan, 45.), (6., nan, 0.)],
          dtype=[('i', '<f8'), ('p', '<f8'), ('n', '<f8')])
    

We need to keep in mind that by default, `dtype=np.float64`. A float is therefore expected for the second column. However, the strings `' 2.3%'` and `' 78.9%'` cannot be converted to float and we end up having `np.nan` instead. Let’s now use a converter:
    
    
    >>> # Converted case ...
    >>> np.genfromtxt(StringIO(data), delimiter=",", names=names,
    ...               converters={1: convertfunc})
    array([(1., 0.023, 45.), (6., 0.789, 0.)],
          dtype=[('i', '<f8'), ('p', '<f8'), ('n', '<f8')])
    

The same results can be obtained by using the name of the second column (`"p"`) as key instead of its index (1):
    
    
    >>> # Using a name for the converter ...
    >>> np.genfromtxt(StringIO(data), delimiter=",", names=names,
    ...               converters={"p": convertfunc})
    array([(1., 0.023, 45.), (6., 0.789, 0.)],
          dtype=[('i', '<f8'), ('p', '<f8'), ('n', '<f8')])
    

Converters can also be used to provide a default for missing entries. In the following example, the converter `convert` transforms a stripped string into the corresponding float or into -999 if the string is empty. We need to explicitly strip the string from white spaces as it is not done by default:
    
    
    >>> data = "1, , 3\n 4, 5, 6"
    >>> convert = lambda x: float(x.strip() or -999)
    >>> np.genfromtxt(StringIO(data), delimiter=",",
    ...               converters={1: convert})
    array([[   1., -999.,    3.],
           [   4.,    5.,    6.]])
    

### Using missing and filling values[#](#using-missing-and-filling-values "Link to this heading")

Some entries may be missing in the dataset we are trying to import. In a previous example, we used a converter to transform an empty string into a float. However, user-defined converters may rapidly become cumbersome to manage.

The [`genfromtxt`](../reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt") function provides two other complementary mechanisms: the `missing_values` argument is used to recognize missing data and a second argument, `filling_values`, is used to process these missing data.

### `missing_values`[#](#missing-values "Link to this heading")

By default, any empty string is marked as missing. We can also consider more complex strings, such as `"N/A"` or `"???"` to represent missing or invalid data. The `missing_values` argument accepts three kinds of values:

a string or a comma-separated string
    

This string will be used as the marker for missing data for all the columns

a sequence of strings
    

In that case, each item is associated to a column, in order.

a dictionary
    

Values of the dictionary are strings or sequence of strings. The corresponding keys can be column indices (integers) or column names (strings). In addition, the special key `None` can be used to define a default applicable to all columns.

### `filling_values`[#](#filling-values "Link to this heading")

We know how to recognize missing data, but we still need to provide a value for these missing entries. By default, this value is determined from the expected dtype according to this table:

Expected type | Default  
---|---  
`bool` | `False`  
`int` | `-1`  
`float` | `np.nan`  
`complex` | `np.nan+0j`  
`string` | `'???'`  
  
We can get a finer control on the conversion of missing values with the `filling_values` optional argument. Like `missing_values`, this argument accepts different kind of values:

a single value
    

This will be the default for all columns

a sequence of values
    

Each entry will be the default for the corresponding column

a dictionary
    

Each key can be a column index or a column name, and the corresponding value should be a single object. We can use the special key `None` to define a default for all columns.

In the following example, we suppose that the missing values are flagged with `"N/A"` in the first column and by `"???"` in the third column. We wish to transform these missing values to 0 if they occur in the first and second column, and to -999 if they occur in the last column:
    
    
    >>> data = "N/A, 2, 3\n4, ,???"
    >>> kwargs = dict(delimiter=",",
    ...               dtype=np.int_,
    ...               names="a,b,c",
    ...               missing_values={0:"N/A", 'b':" ", 2:"???"},
    ...               filling_values={0:0, 'b':0, 2:-999})
    >>> np.genfromtxt(StringIO(data), **kwargs)
    array([(0, 2, 3), (4, 0, -999)],
          dtype=[('a', '<i8'), ('b', '<i8'), ('c', '<i8')])
    

### `usemask`[#](#usemask "Link to this heading")

We may also want to keep track of the occurrence of missing data by constructing a boolean mask, with `True` entries where data was missing and `False` otherwise. To do that, we just have to set the optional argument `usemask` to `True` (the default is `False`). The output array will then be a [`MaskedArray`](../reference/maskedarray.baseclass.html#numpy.ma.MaskedArray "numpy.ma.MaskedArray").

[ __ previous I/O with NumPy ](basics.io.html "previous page") [ next Data types __](basics.types.html "next page")

__On this page

  * [Defining the input](#defining-the-input)
  * [Splitting the lines into columns](#splitting-the-lines-into-columns)
    * [The `delimiter` argument](#the-delimiter-argument)
    * [The `autostrip` argument](#the-autostrip-argument)
    * [The `comments` argument](#the-comments-argument)
  * [Skipping lines and choosing columns](#skipping-lines-and-choosing-columns)
    * [The `skip_header` and `skip_footer` arguments](#the-skip-header-and-skip-footer-arguments)
    * [The `usecols` argument](#the-usecols-argument)
  * [Choosing the data type](#choosing-the-data-type)
  * [Setting the names](#setting-the-names)
    * [The `names` argument](#the-names-argument)
    * [The `defaultfmt` argument](#the-defaultfmt-argument)
    * [Validating names](#validating-names)
  * [Tweaking the conversion](#tweaking-the-conversion)
    * [The `converters` argument](#the-converters-argument)
    * [Using missing and filling values](#using-missing-and-filling-values)
    * [`missing_values`](#missing-values)
    * [`filling_values`](#filling-values)
    * [`usemask`](#usemask)

---

## How to write a NumPy how-to

**Source:** [https://numpy.org/devdocs/user/how-to-how-to.html](https://numpy.org/devdocs/user/how-to-how-to.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy how-tos](howtos_index.html)
  * How to write a NumPy how-to



# How to write a NumPy how-to[#](#how-to-write-a-numpy-how-to "Link to this heading")

How-tos get straight to the point – they

  * answer a focused question, or

  * narrow a broad question into focused questions that the user can choose among.




## A stranger has asked for directions…[#](#a-stranger-has-asked-for-directions "Link to this heading")

**“I need to refuel my car.”**

## Give a brief but explicit answer[#](#give-a-brief-but-explicit-answer "Link to this heading")

  * _“Three kilometers/miles, take a right at Hayseed Road, it’s on your left.”_




Add helpful details for newcomers (“Hayseed Road”, even though it’s the only turnoff at three km/mi). But not irrelevant ones:

  * Don’t also give directions from Route 7.

  * Don’t explain why the town has only one filling station.




If there’s related background (tutorial, explanation, reference, alternative approach), bring it to the user’s attention with a link (“Directions from Route 7,” “Why so few filling stations?”).

## Delegate[#](#delegate "Link to this heading")

  * _“Three km/mi, take a right at Hayseed Road, follow the signs.”_




If the information is already documented and succinct enough for a how-to, just link to it, possibly after an introduction (“Three km/mi, take a right”).

## If the question is broad, narrow and redirect it[#](#if-the-question-is-broad-narrow-and-redirect-it "Link to this heading")

**“I want to see the sights.”**

The _See the sights_ how-to should link to a set of narrower how-tos:

  * Find historic buildings

  * Find scenic lookouts

  * Find the town center




and these might in turn link to still narrower how-tos – so the town center page might link to

  * Find the court house

  * Find city hall




By organizing how-tos this way, you not only display the options for people who need to narrow their question, you also have provided answers for users who start with narrower questions (“I want to see historic buildings,” “Which way to city hall?”).

## If there are many steps, break them up[#](#if-there-are-many-steps-break-them-up "Link to this heading")

If a how-to has many steps:

  * Consider breaking a step out into an individual how-to and linking to it.

  * Include subheadings. They help readers grasp what’s coming and return where they left off.




## Why write how-tos when there’s Stack Overflow, Reddit, Gitter…?[#](#why-write-how-tos-when-there-s-stack-overflow-reddit-gitter "Link to this heading")

  * We have authoritative answers.

  * How-tos make the site less forbidding to non-experts.

  * How-tos bring people into the site and help them discover other information that’s here .

  * Creating how-tos helps us see NumPy usability through new eyes.




## Aren’t how-tos and tutorials the same thing?[#](#aren-t-how-tos-and-tutorials-the-same-thing "Link to this heading")

People use the terms “how-to” and “tutorial” interchangeably, but we draw a distinction, following Daniele Procida’s [taxonomy of documentation](https://documentation.divio.com/).

Documentation needs to meet users where they are. _How-tos_ offer get-it-done information; the user wants steps to copy and doesn’t necessarily want to understand NumPy. _Tutorials_ are warm-fuzzy information; the user wants a feel for some aspect of NumPy (and again, may or may not care about deeper knowledge).

We distinguish both tutorials and how-tos from _Explanations_ , which are deep dives intended to give understanding rather than immediate assistance, and _References_ , which give complete, authoritative data on some concrete part of NumPy (like its API) but aren’t obligated to paint a broader picture.

For more on tutorials, see [Learn to write a NumPy tutorial](https://numpy.org/numpy-tutorials/tutorial-style-guide "\(in  vundefined\)")

## Is this page an example of a how-to?[#](#is-this-page-an-example-of-a-how-to "Link to this heading")

Yes – until the sections with question-mark headings; they explain rather than giving directions. In a how-to, those would be links.

[ __ previous NumPy how-tos ](howtos_index.html "previous page") [ next Reading and writing files __](how-to-io.html "next page")

__On this page

  * [A stranger has asked for directions…](#a-stranger-has-asked-for-directions)
  * [Give a brief but explicit answer](#give-a-brief-but-explicit-answer)
  * [Delegate](#delegate)
  * [If the question is broad, narrow and redirect it](#if-the-question-is-broad-narrow-and-redirect-it)
  * [If there are many steps, break them up](#if-there-are-many-steps-break-them-up)
  * [Why write how-tos when there’s Stack Overflow, Reddit, Gitter…?](#why-write-how-tos-when-there-s-stack-overflow-reddit-gitter)
  * [Aren’t how-tos and tutorials the same thing?](#aren-t-how-tos-and-tutorials-the-same-thing)
  * [Is this page an example of a how-to?](#is-this-page-an-example-of-a-how-to)

---

## How to index ndarrays

**Source:** [https://numpy.org/devdocs/user/how-to-index.html](https://numpy.org/devdocs/user/how-to-index.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy how-tos](howtos_index.html)
  * How to index `ndarrays`



# How to index [`ndarrays`](../reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")[#](#how-to-index-ndarrays "Link to this heading")

See also

[Indexing on ndarrays](basics.indexing.html#basics-indexing)

This page tackles common examples. For an in-depth look into indexing, refer to [Indexing on ndarrays](basics.indexing.html#basics-indexing).

## Access specific/arbitrary rows and columns[#](#access-specific-arbitrary-rows-and-columns "Link to this heading")

Use [Basic indexing](basics.indexing.html#basic-indexing) features like [Slicing and striding](basics.indexing.html#slicing-and-striding), and [Dimensional indexing tools](basics.indexing.html#dimensional-indexing-tools).
    
    
    >>> a = np.arange(30).reshape(2, 3, 5)
    >>> a
    array([[[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]],
    
            [[15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29]]])
    >>> a[0, 2, :]
    array([10, 11, 12, 13, 14])
    >>> a[0, :, 3]
    array([ 3,  8, 13])
    

Note that the output from indexing operations can have different shape from the original object. To preserve the original dimensions after indexing, you can use [`newaxis`](../reference/constants.html#numpy.newaxis "numpy.newaxis"). To use other such tools, refer to [Dimensional indexing tools](basics.indexing.html#dimensional-indexing-tools).
    
    
    >>> a[0, :, 3].shape
    (3,)
    >>> a[0, :, 3, np.newaxis].shape
    (3, 1)
    >>> a[0, :, 3, np.newaxis, np.newaxis].shape
    (3, 1, 1)
    

Variables can also be used to index:
    
    
    >>> y = 0
    >>> a[y, :, y+3]
    array([ 3,  8, 13])
    

Refer to [Dealing with variable numbers of indices within programs](basics.indexing.html#dealing-with-variable-indices) to see how to use [slice](https://docs.python.org/3/glossary.html#term-slice "\(in Python v3.14\)") and [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "\(in Python v3.14\)") in your index variables.

### Index columns[#](#index-columns "Link to this heading")

To index columns, you have to index the last axis. Use [Dimensional indexing tools](basics.indexing.html#dimensional-indexing-tools) to get the desired number of dimensions:
    
    
    >>> a = np.arange(24).reshape(2, 3, 4)
    >>> a
    array([[[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]],
    
           [[12, 13, 14, 15],
            [16, 17, 18, 19],
            [20, 21, 22, 23]]])
    >>> a[..., 3]
    array([[ 3,  7, 11],
           [15, 19, 23]])
    

To index specific elements in each column, make use of [Advanced indexing](basics.indexing.html#advanced-indexing) as below:
    
    
    >>> arr = np.arange(3*4).reshape(3, 4)
    >>> arr
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11]])
    >>> column_indices = [[1, 3], [0, 2], [2, 2]]
    >>> np.arange(arr.shape[0])
    array([0, 1, 2])
    >>> row_indices = np.arange(arr.shape[0])[:, np.newaxis]
    >>> row_indices
    array([[0],
           [1],
           [2]])
    

Use the `row_indices` and `column_indices` for advanced indexing:
    
    
    >>> arr[row_indices, column_indices]
    array([[ 1,  3],
           [ 4,  6],
           [10, 10]])
    

### Index along a specific axis[#](#index-along-a-specific-axis "Link to this heading")

Use [`take`](../reference/generated/numpy.take.html#numpy.take "numpy.take"). See also [`take_along_axis`](../reference/generated/numpy.take_along_axis.html#numpy.take_along_axis "numpy.take_along_axis") and [`put_along_axis`](../reference/generated/numpy.put_along_axis.html#numpy.put_along_axis "numpy.put_along_axis").
    
    
    >>> a = np.arange(30).reshape(2, 3, 5)
    >>> a
    array([[[ 0,  1,  2,  3,  4],
            [ 5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14]],
    
            [[15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24],
            [25, 26, 27, 28, 29]]])
    >>> np.take(a, [2, 3], axis=2)
    array([[[ 2,  3],
            [ 7,  8],
            [12, 13]],
    
            [[17, 18],
            [22, 23],
            [27, 28]]])
    >>> np.take(a, [2], axis=1)
    array([[[10, 11, 12, 13, 14]],
    
            [[25, 26, 27, 28, 29]]])
    

## Create subsets of larger matrices[#](#create-subsets-of-larger-matrices "Link to this heading")

Use [Slicing and striding](basics.indexing.html#slicing-and-striding) to access chunks of a large array:
    
    
    >>> a = np.arange(100).reshape(10, 10)
    >>> a
    array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
            [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
            [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
            [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
            [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
            [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
            [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
            [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]])
    >>> a[2:5, 2:5]
    array([[22, 23, 24],
           [32, 33, 34],
           [42, 43, 44]])
    >>> a[2:5, 1:3]
    array([[21, 22],
           [31, 32],
           [41, 42]])
    >>> a[:5, :5]
    array([[ 0,  1,  2,  3,  4],
           [10, 11, 12, 13, 14],
           [20, 21, 22, 23, 24],
           [30, 31, 32, 33, 34],
           [40, 41, 42, 43, 44]])
    

The same thing can be done with advanced indexing in a slightly more complex way. Remember that [advanced indexing creates a copy](basics.copies.html#indexing-operations):
    
    
    >>> a[np.arange(5)[:, None], np.arange(5)[None, :]]
    array([[ 0,  1,  2,  3,  4],
           [10, 11, 12, 13, 14],
           [20, 21, 22, 23, 24],
           [30, 31, 32, 33, 34],
           [40, 41, 42, 43, 44]])
    

You can also use [`mgrid`](../reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid") to generate indices:
    
    
    >>> indices = np.mgrid[0:6:2]
    >>> indices
    array([0, 2, 4])
    >>> a[:, indices]
    array([[ 0,  2,  4],
           [10, 12, 14],
           [20, 22, 24],
           [30, 32, 34],
           [40, 42, 44],
           [50, 52, 54],
           [60, 62, 64],
           [70, 72, 74],
           [80, 82, 84],
           [90, 92, 94]])
    

## Filter values[#](#filter-values "Link to this heading")

### Non-zero elements[#](#non-zero-elements "Link to this heading")

Use [`nonzero`](../reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero") to get a tuple of array indices of non-zero elements corresponding to every dimension:
    
    
    >>> z = np.array([[1, 2, 3, 0], [0, 0, 5, 3], [4, 6, 0, 0]])
    >>> z
    array([[1, 2, 3, 0],
           [0, 0, 5, 3],
           [4, 6, 0, 0]])
    >>> np.nonzero(z)
    (array([0, 0, 0, 1, 1, 2, 2]), array([0, 1, 2, 2, 3, 0, 1]))
    

Use [`flatnonzero`](../reference/generated/numpy.flatnonzero.html#numpy.flatnonzero "numpy.flatnonzero") to fetch indices of elements that are non-zero in the flattened version of the ndarray:
    
    
    >>> np.flatnonzero(z)
    array([0, 1, 2, 6, 7, 8, 9])
    

### Arbitrary conditions[#](#arbitrary-conditions "Link to this heading")

Use [`where`](../reference/generated/numpy.where.html#numpy.where "numpy.where") to generate indices based on conditions and then use [Advanced indexing](basics.indexing.html#advanced-indexing).
    
    
    >>> a = np.arange(30).reshape(2, 3, 5)
    >>> indices = np.where(a % 2 == 0)
    >>> indices
    (array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
    array([0, 0, 0, 1, 1, 2, 2, 2, 0, 0, 1, 1, 1, 2, 2]),
    array([0, 2, 4, 1, 3, 0, 2, 4, 1, 3, 0, 2, 4, 1, 3]))
    >>> a[indices]
    array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])
    

Or, use [Boolean array indexing](basics.indexing.html#boolean-indexing):
    
    
    >>> a > 14
    array([[[False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]],
    
           [[ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True]]])
    >>> a[a > 14]
    array([15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
    

### Replace values after filtering[#](#replace-values-after-filtering "Link to this heading")

Use assignment with filtering to replace desired values:
    
    
    >>> p = np.arange(-10, 10).reshape(2, 2, 5)
    >>> p
    array([[[-10,  -9,  -8,  -7,  -6],
            [ -5,  -4,  -3,  -2,  -1]],
    
           [[  0,   1,   2,   3,   4],
            [  5,   6,   7,   8,   9]]])
    >>> q = p < 0
    >>> q
    array([[[ True,  True,  True,  True,  True],
            [ True,  True,  True,  True,  True]],
    
           [[False, False, False, False, False],
            [False, False, False, False, False]]])
    >>> p[q] = 0
    >>> p
    array([[[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]],
    
           [[0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9]]])
    

## Fetch indices of max/min values[#](#fetch-indices-of-max-min-values "Link to this heading")

Use [`argmax`](../reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax") and [`argmin`](../reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin"):
    
    
    >>> a = np.arange(30).reshape(2, 3, 5)
    >>> np.argmax(a)
    29
    >>> np.argmin(a)
    0
    

Use the `axis` keyword to get the indices of maximum and minimum values along a specific axis:
    
    
    >>> np.argmax(a, axis=0)
    array([[1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1]])
    >>> np.argmax(a, axis=1)
    array([[2, 2, 2, 2, 2],
           [2, 2, 2, 2, 2]])
    >>> np.argmax(a, axis=2)
    array([[4, 4, 4],
           [4, 4, 4]])
    
    >>> np.argmin(a, axis=1)
    array([[0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0]])
    >>> np.argmin(a, axis=2)
    array([[0, 0, 0],
           [0, 0, 0]])
    

Set `keepdims` to `True` to keep the axes which are reduced in the result as dimensions with size one:
    
    
    >>> np.argmin(a, axis=2, keepdims=True)
    array([[[0],
            [0],
            [0]],
    
           [[0],
            [0],
            [0]]])
    >>> np.argmax(a, axis=1, keepdims=True)
    array([[[2, 2, 2, 2, 2]],
    
           [[2, 2, 2, 2, 2]]])
    

To get the indices of each maximum or minimum value for each (N-1)-dimensional array in an N-dimensional array, use [`reshape`](../reference/generated/numpy.reshape.html#numpy.reshape "numpy.reshape") to reshape the array to a 2D array, apply [`argmax`](../reference/generated/numpy.argmax.html#numpy.argmax "numpy.argmax") or [`argmin`](../reference/generated/numpy.argmin.html#numpy.argmin "numpy.argmin") along `axis=1` and use [`unravel_index`](../reference/generated/numpy.unravel_index.html#numpy.unravel_index "numpy.unravel_index") to recover the index of the values per slice:
    
    
    >>> x = np.arange(2*2*3).reshape(2, 2, 3) % 7  # 3D example array
    >>> x
    array([[[0, 1, 2],
            [3, 4, 5]],
    
           [[6, 0, 1],
            [2, 3, 4]]])
    >>> x_2d = np.reshape(x, (x.shape[0], -1))
    >>> indices_2d = np.argmax(x_2d, axis=1)
    >>> indices_2d
    array([5, 0])
    >>> np.unravel_index(indices_2d, x.shape[1:])
    (array([1, 0]), array([2, 0]))
    

The first array returned contains the indices along axis 1 in the original array, the second array contains the indices along axis 2. The highest value in `x[0]` is therefore `x[0, 1, 2]`.

## Index the same ndarray multiple times efficiently[#](#index-the-same-ndarray-multiple-times-efficiently "Link to this heading")

It must be kept in mind that basic indexing produces [views](../glossary.html#term-view) and advanced indexing produces [copies](../glossary.html#term-copy), which are computationally less efficient. Hence, you should take care to use basic indexing wherever possible instead of advanced indexing.

## Further reading[#](#further-reading "Link to this heading")

Nicolas Rougier’s [100 NumPy exercises](https://github.com/rougier/numpy-100) provide a good insight into how indexing is combined with other operations. Exercises [6](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#6-create-a-null-vector-of-size-10-but-the-fifth-value-which-is-1-), [8](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#8-reverse-a-vector-first-element-becomes-last-), [10](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#10-find-indices-of-non-zero-elements-from-120040-), [15](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#15-create-a-2d-array-with-1-on-the-border-and-0-inside-), [16](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#16-how-to-add-a-border-filled-with-0s-around-an-existing-array-), [19](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#19-create-a-8x8-matrix-and-fill-it-with-a-checkerboard-pattern-), [20](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#20-consider-a-678-shape-array-what-is-the-index-xyz-of-the-100th-element-), [45](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#45-create-random-vector-of-size-10-and-replace-the-maximum-value-by-0-), [59](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#59-how-to-sort-an-array-by-the-nth-column-), [64](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#64-consider-a-given-vector-how-to-add-1-to-each-element-indexed-by-a-second-vector-be-careful-with-repeated-indices-), [65](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#65-how-to-accumulate-elements-of-a-vector-x-to-an-array-f-based-on-an-index-list-i-), [70](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#70-consider-the-vector-1-2-3-4-5-how-to-build-a-new-vector-with-3-consecutive-zeros-interleaved-between-each-value-), [71](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#71-consider-an-array-of-dimension-553-how-to-mulitply-it-by-an-array-with-dimensions-55-), [72](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#72-how-to-swap-two-rows-of-an-array-), [76](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#76-consider-a-one-dimensional-array-z-build-a-two-dimensional-array-whose-first-row-is-z0z1z2-and-each-subsequent-row-is--shifted-by-1-last-row-should-be-z-3z-2z-1-), [80](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#80-consider-an-arbitrary-array-write-a-function-that-extract-a-subpart-with-a-fixed-shape-and-centered-on-a-given-element-pad-with-a-fill-value-when-necessary-), [81](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#81-consider-an-array-z--1234567891011121314-how-to-generate-an-array-r--1234-2345-3456--11121314-), [84](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#84-extract-all-the-contiguous-3x3-blocks-from-a-random-10x10-matrix-), [87](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#87-consider-a-16x16-array-how-to-get-the-block-sum-block-size-is-4x4-), [90](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#90-given-an-arbitrary-number-of-vectors-build-the-cartesian-product-every-combinations-of-every-item-), [93](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#93-consider-two-arrays-a-and-b-of-shape-83-and-22-how-to-find-rows-of-a-that-contain-elements-of-each-row-of-b-regardless-of-the-order-of-the-elements-in-b-), [94](https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises_with_solutions.md#94-considering-a-10x3-matrix-extract-rows-with-unequal-values-eg-223-) are specially focused on indexing.

[ __ previous Reading and writing files ](how-to-io.html "previous page") [ next Verifying bugs and bug fixes in NumPy __](how-to-verify-bug.html "next page")

__On this page

  * [Access specific/arbitrary rows and columns](#access-specific-arbitrary-rows-and-columns)
    * [Index columns](#index-columns)
    * [Index along a specific axis](#index-along-a-specific-axis)
  * [Create subsets of larger matrices](#create-subsets-of-larger-matrices)
  * [Filter values](#filter-values)
    * [Non-zero elements](#non-zero-elements)
    * [Arbitrary conditions](#arbitrary-conditions)
    * [Replace values after filtering](#replace-values-after-filtering)
  * [Fetch indices of max/min values](#fetch-indices-of-max-min-values)
  * [Index the same ndarray multiple times efficiently](#index-the-same-ndarray-multiple-times-efficiently)
  * [Further reading](#further-reading)

---

## Verifying bugs and bug fixes in NumPy

**Source:** [https://numpy.org/devdocs/user/how-to-verify-bug.html](https://numpy.org/devdocs/user/how-to-verify-bug.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy how-tos](howtos_index.html)
  * Verifying bugs and bug fixes in NumPy



# Verifying bugs and bug fixes in NumPy[#](#verifying-bugs-and-bug-fixes-in-numpy "Link to this heading")

In this how-to you will learn how to:

  * Verify the existence of a bug in NumPy

  * Verify the fix, if any, made for the bug




While you walk through the verification process, you will learn how to:

  * Set up a Python virtual environment (using `virtualenv`)

  * Install appropriate versions of NumPy, first to see the bug in action, then to verify its fix




[Issue 16354](https://github.com/numpy/numpy/issues/16354) is used as an example.

This issue was:

> **Title** : _np.polymul return type is np.float64 or np.complex128 when given an all-zero argument_
> 
> _np.polymul returns an object with type np.float64 when one argument is all zero, and both arguments have type np.int64 or np.float32. Something similar happens with all zero np.complex64 giving result type np.complex128._
> 
> _This doesn’t happen with non-zero arguments; there the result is as expected._
> 
> _This bug isn’t present in np.convolve._
> 
> **Reproducing code example** :
>     
>     
>     >>> import numpy as np
>     >>> np.__version__
>     '1.18.4'
>     >>> a = np.array([1,2,3])
>     >>> z = np.array([0,0,0])
>     >>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
>     dtype('int64')
>     >>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
>     dtype('float64')
>     >>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
>     dtype('float64')
>     >>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
>     dtype('complex128')
>     Numpy/Python version information:
>     >>> import sys, numpy; print(numpy.__version__, sys.version)
>     1.18.4 3.7.5 (default, Nov  7 2019, 10:50:52) [GCC 8.3.0]
>     

## 1\. Set up a virtual environment[#](#set-up-a-virtual-environment "Link to this heading")

Create a new directory, enter into it, and set up a virtual environment using your preferred method. For example, this is how to do it using `virtualenv` on linux or macOS:
    
    
    virtualenv venv_np_bug
    source venv_np_bug/bin/activate
    

This ensures the system/global/default Python/NumPy installation will not be altered.

## 2\. Install the NumPy version in which the bug was reported[#](#install-the-numpy-version-in-which-the-bug-was-reported "Link to this heading")

The report references NumPy version 1.18.4, so that is the version you need to install in this case.

Since this bug is tied to a release and not a specific commit, a pre-built wheel installed in your virtual environment via `pip` will suffice:
    
    
    pip install numpy==1.18.4
    

Some bugs may require you to build the NumPy version referenced in the issue report. To learn how to do that, visit [Building from source](../building/index.html#building-from-source).

## 3\. Reproduce the bug[#](#reproduce-the-bug "Link to this heading")

The issue reported in [#16354](https://github.com/numpy/numpy/issues/16354) is that the wrong `dtype` is returned if one of the inputs of the method [`numpy.polymul`](../reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul") is a zero array.

To reproduce the bug, start a Python terminal, enter the code snippet shown in the bug report, and ensure that the results match those in the issue:
    
    
    >>> import numpy as np
    >>> np.__version__
    '...' # 1.18.4
    >>> a = np.array([1,2,3])
    >>> z = np.array([0,0,0])
    >>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
    dtype('int64')
    >>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
    dtype('...') # float64
    >>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
    dtype('...') # float64
    >>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
    dtype('...') # complex128
    

As reported, whenever the zero array, `z` in the example above, is one of the arguments to [`numpy.polymul`](../reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul"), an incorrect `dtype` is returned.

## 4\. Check for fixes in the latest version of NumPy[#](#check-for-fixes-in-the-latest-version-of-numpy "Link to this heading")

If the issue report for your bug has not yet been resolved, further action or patches need to be submitted.

In this case, however, the issue was resolved by [PR 17577](https://github.com/numpy/numpy/pull/17577) and is now closed. So you can try to verify the fix.

To verify the fix:

  1. Uninstall the version of NumPy in which the bug still exists:
         
         pip uninstall numpy
         

  2. Install the latest version of NumPy:
         
         pip install numpy
         

  3. In your Python terminal, run the reported code snippet you used to verify the existence of the bug and confirm that the issue has been resolved:
         
         >>> import numpy as np
         >>> np.__version__
         '...' # 1.18.4
         >>> a = np.array([1,2,3])
         >>> z = np.array([0,0,0])
         >>> np.polymul(a.astype(np.int64), a.astype(np.int64)).dtype
         dtype('int64')
         >>> np.polymul(a.astype(np.int64), z.astype(np.int64)).dtype
         dtype('int64')
         >>> np.polymul(a.astype(np.float32), z.astype(np.float32)).dtype
         dtype('float32')
         >>> np.polymul(a.astype(np.complex64), z.astype(np.complex64)).dtype
         dtype('complex64')
         




Note that the correct `dtype` is now returned even when a zero array is one of the arguments to [`numpy.polymul`](../reference/generated/numpy.polymul.html#numpy.polymul "numpy.polymul").

## 5\. Support NumPy development by verifying and fixing bugs[#](#support-numpy-development-by-verifying-and-fixing-bugs "Link to this heading")

Go to the [NumPy GitHub issues page](https://github.com/numpy/numpy/issues) and see if you can confirm the existence of any other bugs which have not been confirmed yet. In particular, it is useful for the developers to know if a bug can be reproduced on a newer version of NumPy.

Comments verifying the existence of bugs alert the NumPy developers that more than one user can reproduce the issue.

[ __ previous How to index `ndarrays` ](how-to-index.html "previous page") [ next How to create arrays with regularly-spaced values __](how-to-partition.html "next page")

__On this page

  * [1\. Set up a virtual environment](#set-up-a-virtual-environment)
  * [2\. Install the NumPy version in which the bug was reported](#install-the-numpy-version-in-which-the-bug-was-reported)
  * [3\. Reproduce the bug](#reproduce-the-bug)
  * [4\. Check for fixes in the latest version of NumPy](#check-for-fixes-in-the-latest-version-of-numpy)
  * [5\. Support NumPy development by verifying and fixing bugs](#support-numpy-development-by-verifying-and-fixing-bugs)

---

## How to create arrays with regularly-spaced values

**Source:** [https://numpy.org/devdocs/user/how-to-partition.html](https://numpy.org/devdocs/user/how-to-partition.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy how-tos](howtos_index.html)
  * How to create arrays with regularly-spaced values



# How to create arrays with regularly-spaced values[#](#how-to-create-arrays-with-regularly-spaced-values "Link to this heading")

There are a few NumPy functions that are similar in application, but which provide slightly different results, which may cause confusion if one is not sure when and how to use them. The following guide aims to list these functions and describe their recommended usage.

The functions mentioned here are

  * [`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace")

  * [`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange")

  * [`numpy.geomspace`](../reference/generated/numpy.geomspace.html#numpy.geomspace "numpy.geomspace")

  * [`numpy.logspace`](../reference/generated/numpy.logspace.html#numpy.logspace "numpy.logspace")

  * [`numpy.meshgrid`](../reference/generated/numpy.meshgrid.html#numpy.meshgrid "numpy.meshgrid")

  * [`numpy.mgrid`](../reference/generated/numpy.mgrid.html#numpy.mgrid "numpy.mgrid")

  * [`numpy.ogrid`](../reference/generated/numpy.ogrid.html#numpy.ogrid "numpy.ogrid")




## 1D domains (intervals)[#](#d-domains-intervals "Link to this heading")

### `linspace` vs. `arange`[#](#linspace-vs-arange "Link to this heading")

Both [`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") and [`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") provide ways to partition an interval (a 1D domain) into equal-length subintervals. These partitions will vary depending on the chosen starting and ending points, and the **step** (the length of the subintervals).

  * **Use** [`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") **if you want integer steps.**

[`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") relies on step size to determine how many elements are in the returned array, which excludes the endpoint. This is determined through the `step` argument to `arange`.

Example:
        
        >>> np.arange(0, 10, 2)  # np.arange(start, stop, step)
        array([0, 2, 4, 6, 8])
        

The arguments `start` and `stop` should be integer or real, but not complex numbers. [`numpy.arange`](../reference/generated/numpy.arange.html#numpy.arange "numpy.arange") is similar to the Python built-in [`range`](https://docs.python.org/3/library/stdtypes.html#range "\(in Python v3.14\)").

Floating-point inaccuracies can make `arange` results with floating-point numbers confusing. In this case, you should use [`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") instead.

  * **Use** [`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") **if you want the endpoint to be included in the result, or if you are using a non-integer step size.**

[`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") _can_ include the endpoint and determines step size from the _num_ argument, which specifies the number of elements in the returned array.

The inclusion of the endpoint is determined by an optional boolean argument `endpoint`, which defaults to `True`. Note that selecting `endpoint=False` will change the step size computation, and the subsequent output for the function.

Example:
        
        >>> np.linspace(0.1, 0.2, num=5)  # np.linspace(start, stop, num)
        array([0.1  , 0.125, 0.15 , 0.175, 0.2  ])
        >>> np.linspace(0.1, 0.2, num=5, endpoint=False)
        array([0.1, 0.12, 0.14, 0.16, 0.18])
        

[`numpy.linspace`](../reference/generated/numpy.linspace.html#numpy.linspace "numpy.linspace") can also be used with complex arguments:
        
        >>> np.linspace(1+1.j, 4, 5, dtype=np.complex64)
        array([1.  +1.j  , 1.75+0.75j, 2.5 +0.5j , 3.25+0.25j, 4.  +0.j  ],
              dtype=complex64)
        




### Other examples[#](#other-examples "Link to this heading")

  1. Unexpected results may happen if floating point values are used as `step` in `numpy.arange`. To avoid this, make sure all floating point conversion happens after the computation of results. For example, replace
         
         >>> list(np.arange(0.1,0.4,0.1).round(1))
         [0.1, 0.2, 0.3, 0.4]  # endpoint should not be included!
         

with
         
         >>> list(np.arange(1, 4, 1) / 10.0)
         [0.1, 0.2, 0.3]  # expected result
         

  2. Note that
         
         >>> np.arange(0, 1.12, 0.04)
         array([0.  , 0.04, 0.08, 0.12, 0.16, 0.2 , 0.24, 0.28, 0.32, 0.36, 0.4 ,
                0.44, 0.48, 0.52, 0.56, 0.6 , 0.64, 0.68, 0.72, 0.76, 0.8 , 0.84,
                0.88, 0.92, 0.96, 1.  , 1.04, 1.08, 1.12])
         

and
         
         >>> np.arange(0, 1.08, 0.04)
         array([0.  , 0.04, 0.08, 0.12, 0.16, 0.2 , 0.24, 0.28, 0.32, 0.36, 0.4 ,
                0.44, 0.48, 0.52, 0.56, 0.6 , 0.64, 0.68, 0.72, 0.76, 0.8 , 0.84,
                0.88, 0.92, 0.96, 1.  , 1.04])
         

These differ because of numeric noise. When using floating point values, it is possible that `0 + 0.04 * 28 < 1.12`, and so `1.12` is in the interval. In fact, this is exactly the case:
         
         >>> 1.12/0.04
         28.000000000000004
         

But `0 + 0.04 * 27 >= 1.08` so that 1.08 is excluded:
         
         >>> 1.08/0.04
         27.0
         

Alternatively, you could use `np.arange(0, 28)*0.04` which would always give you precise control of the end point since it is integral:
         
         >>> np.arange(0, 28)*0.04
         array([0.  , 0.04, 0.08, 0.12, 0.16, 0.2 , 0.24, 0.28, 0.32, 0.36, 0.4 ,
                0.44, 0.48, 0.52, 0.56, 0.6 , 0.64, 0.68, 0.72, 0.76, 0.8 , 0.84,
                0.88, 0.92, 0.96, 1.  , 1.04, 1.08])
         




### `geomspace` and `logspace`[#](#geomspace-and-logspace "Link to this heading")

`numpy.geomspace` is similar to `numpy.linspace`, but with numbers spaced evenly on a log scale (a geometric progression). The endpoint is included in the result.

Example:
    
    
    >>> np.geomspace(2, 3, num=5)
    array([2.        , 2.21336384, 2.44948974, 2.71080601, 3.        ])
    

`numpy.logspace` is similar to `numpy.geomspace`, but with the start and end points specified as logarithms (with base 10 as default):
    
    
    >>> np.logspace(2, 3, num=5)
    array([ 100.        ,  177.827941  ,  316.22776602,  562.34132519, 1000.        ])
    

In linear space, the sequence starts at `base ** start` (`base` to the power of `start`) and ends with `base ** stop`:
    
    
    >>> np.logspace(2, 3, num=5, base=2)
    array([4.        , 4.75682846, 5.65685425, 6.72717132, 8.        ])
    

## N-D domains[#](#n-d-domains "Link to this heading")

N-D domains can be partitioned into _grids_. This can be done using one of the following functions.

### `meshgrid`[#](#meshgrid "Link to this heading")

The purpose of `numpy.meshgrid` is to create a rectangular grid out of a set of one-dimensional coordinate arrays.

Given arrays:
    
    
    >>> x = np.array([0, 1, 2, 3])
    >>> y = np.array([0, 1, 2, 3, 4, 5])
    

`meshgrid` will create two coordinate arrays, which can be used to generate the coordinate pairs determining this grid.:
    
    
    >>> xx, yy = np.meshgrid(x, y)
    >>> xx
    array([[0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3],
           [0, 1, 2, 3]])
    >>> yy
    array([[0, 0, 0, 0],
           [1, 1, 1, 1],
           [2, 2, 2, 2],
           [3, 3, 3, 3],
           [4, 4, 4, 4],
           [5, 5, 5, 5]])
    
    >>> import matplotlib.pyplot as plt
    >>> plt.plot(xx, yy, marker='.', color='k', linestyle='none')
    

![../_images/meshgrid_plot.png](../_images/meshgrid_plot.png)

### `mgrid`[#](#mgrid "Link to this heading")

`numpy.mgrid` can be used as a shortcut for creating meshgrids. It is not a function, but when indexed, returns a multidimensional meshgrid.
    
    
    >>> xx, yy = np.meshgrid(np.array([0, 1, 2, 3]), np.array([0, 1, 2, 3, 4, 5]))
    >>> xx.T, yy.T
    (array([[0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3]]),
     array([[0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5]]))
    
    >>> np.mgrid[0:4, 0:6]
    array([[[0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3, 3]],
    
           [[0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5],
            [0, 1, 2, 3, 4, 5]]])
    

### `ogrid`[#](#ogrid "Link to this heading")

Similar to `numpy.mgrid`, `numpy.ogrid` returns an _open_ multidimensional meshgrid. This means that when it is indexed, only one dimension of each returned array is greater than 1. This avoids repeating the data and thus saves memory, which is often desirable.

These sparse coordinate grids are intended to be used with [Broadcasting](https://scipy-lectures.org/intro/numpy/operations.html#broadcasting "\(in Scipy lecture notes v2022.1\)"). When all coordinates are used in an expression, broadcasting still leads to a fully-dimensional result array.
    
    
    >>> np.ogrid[0:4, 0:6]
    (array([[0],
            [1],
            [2],
            [3]]), array([[0, 1, 2, 3, 4, 5]]))
    

All three methods described here can be used to evaluate function values on a grid.
    
    
    >>> g = np.ogrid[0:4, 0:6]
    >>> zg = np.sqrt(g[0]**2 + g[1]**2)
    >>> g[0].shape, g[1].shape, zg.shape
    ((4, 1), (1, 6), (4, 6))
    >>> m = np.mgrid[0:4, 0:6]
    >>> zm = np.sqrt(m[0]**2 + m[1]**2)
    >>> np.array_equal(zm, zg)
    True
    

[ __ previous Verifying bugs and bug fixes in NumPy ](how-to-verify-bug.html "previous page") [ next Printing NumPy Arrays __](how-to-print.html "next page")

__On this page

  * [1D domains (intervals)](#d-domains-intervals)
    * [`linspace` vs. `arange`](#linspace-vs-arange)
    * [Other examples](#other-examples)
    * [`geomspace` and `logspace`](#geomspace-and-logspace)
  * [N-D domains](#n-d-domains)
    * [`meshgrid`](#meshgrid)
    * [`mgrid`](#mgrid)
    * [`ogrid`](#ogrid)

---

## Printing NumPy Arrays

**Source:** [https://numpy.org/devdocs/user/how-to-print.html](https://numpy.org/devdocs/user/how-to-print.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [NumPy how-tos](howtos_index.html)
  * Printing NumPy Arrays



# Printing NumPy Arrays[#](#printing-numpy-arrays "Link to this heading")

This page explains how to control the formatting of printed NumPy arrays. Note that these printing options apply only to arrays, not to scalars.

## Defining printing options[#](#defining-printing-options "Link to this heading")

### Applying settings globally[#](#applying-settings-globally "Link to this heading")

Use [`numpy.set_printoptions`](../reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions") to change printing options for the entire runtime session. To inspect current print settings, use [`numpy.get_printoptions`](../reference/generated/numpy.get_printoptions.html#numpy.get_printoptions "numpy.get_printoptions"):
    
    
    >>> np.set_printoptions(precision=2)
    >>> np.get_printoptions()
    {'edgeitems': 3, 'threshold': 1000, 'floatmode': 'maxprec', 'precision': 2, 'suppress': False, 'linewidth': 75, 'nanstr': 'nan', 'infstr': 'inf', 'sign': '-', 'formatter': None, 'legacy': False, 'override_repr': None}
    

To restore the default settings, use:
    
    
    >>> np.set_printoptions(edgeitems=3, infstr='inf',
    ... linewidth=75, nanstr='nan', precision=8,
    ... suppress=False, threshold=1000, formatter=None)
    

### Applying settings temporarily[#](#applying-settings-temporarily "Link to this heading")

Use [`numpy.printoptions`](../reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions") as a context manager to temporarily override print settings within a specific scope:
    
    
    >>> arr = np.array([0.155, 0.184, 0.173])
    >>> with np.printoptions(precision=2):
    ...     print(arr)
    [0.15 0.18 0.17]
    

All keywords that apply to [`numpy.set_printoptions`](../reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions") also apply to [`numpy.printoptions`](../reference/generated/numpy.printoptions.html#numpy.printoptions "numpy.printoptions").

## Changing the number of digits of precision[#](#changing-the-number-of-digits-of-precision "Link to this heading")

The default number of fractional digits displayed is 8. You can change this number using `precision` keyword.
    
    
    >>> arr = np.array([0.1, 0.184, 0.17322])
    >>> with np.printoptions(precision=2):
    ...     print(arr)
    [0.1 0.18 0.17]
    

The `floatmode` option determines how the `precision` setting is interpreted. By default, `floatmode=maxprec_equal` displays values with the minimal number of digits needed to uniquely represent them, using the same number of digits across all elements. If you want to show exactly the same number of digits specified by `precision`, use `floatmode=fixed`:
    
    
    >>> arr = np.array([0.1, 0.184, 0.173], dtype=np.float32)
    >>> with np.printoptions(precision=2, floatmode="fixed"):
    ...     print(arr)
    [0.10 0.18 0.17]
    

## Changing how _nan_ and _inf_ are displayed[#](#changing-how-nan-and-inf-are-displayed "Link to this heading")

By default, [`numpy.nan`](../reference/constants.html#numpy.nan "numpy.nan") is displayed as _nan_ and [`numpy.inf`](../reference/constants.html#numpy.inf "numpy.inf") is displayed as _inf_. You can override these representations using the `nanstr` and `infstr` options:
    
    
    >>> arr = np.array([np.inf, np.nan, 0])
    >>> with np.printoptions(nanstr="NAN", infstr="INF"):
    ...     print(arr)
    [INF NAN  0.]
    

## Controlling scientific notations[#](#controlling-scientific-notations "Link to this heading")

By default, NumPy uses scientific notation when:

  * The absolute value of the smallest number is less than `1e-4`, or

  * The ratio of the largest to the smallest absolute value is greater than `1e3`
        
        >>> arr = np.array([0.00002, 210000.0, 3.14])
        >>> print(arr)
        [2.00e-05 2.10e+05 3.14e+00]
        




To suppress scientific notation and always use fixed-point notation, set `suppress=True`:
    
    
    >>> arr = np.array([0.00002, 210000.0, 3.14])
    >>> with np.printoptions(suppress=True):
    ...     print(arr)
    [     0.00002 210000.           3.14   ]
    

## Applying custom formatting functions[#](#applying-custom-formatting-functions "Link to this heading")

You can apply custom formatting functions to specific or all data types using `formatter` keyword. See [`numpy.set_printoptions`](../reference/generated/numpy.set_printoptions.html#numpy.set_printoptions "numpy.set_printoptions") for more details on supported format keys.

For example, to format _datetime64_ values with a custom function:
    
    
    >>> arr = np.array([np.datetime64("2025-01-01"), np.datetime64("2024-01-01")])
    >>> with np.printoptions(formatter={"datetime":lambda x: f"(Year: {x.item().year}, Month: {x.item().month})"}):
    ...     print(arr)
    [(Year: 2025, Month: 1) (Year: 2024, Month: 1)]
    

[ __ previous How to create arrays with regularly-spaced values ](how-to-partition.html "previous page") [ next Using NumPy C-API __](c-info.html "next page")

__On this page

  * [Defining printing options](#defining-printing-options)
    * [Applying settings globally](#applying-settings-globally)
    * [Applying settings temporarily](#applying-settings-temporarily)
  * [Changing the number of digits of precision](#changing-the-number-of-digits-of-precision)
  * [Changing how _nan_ and _inf_ are displayed](#changing-how-nan-and-inf-are-displayed)
  * [Controlling scientific notations](#controlling-scientific-notations)
  * [Applying custom formatting functions](#applying-custom-formatting-functions)

---

## How to extend NumPy

**Source:** [https://numpy.org/devdocs/user/c-info.how-to-extend.html](https://numpy.org/devdocs/user/c-info.how-to-extend.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Using NumPy C-API](c-info.html)
  * How to extend NumPy



# How to extend NumPy[#](#how-to-extend-numpy "Link to this heading")

That which is static and repetitive is boring. That which is dynamic

and random is confusing. In between lies art.

— _John A. Locke_

Science is a differential equation. Religion is a boundary condition.

— _Alan Turing_

## Writing an extension module[#](#writing-an-extension-module "Link to this heading")

While the ndarray object is designed to allow rapid computation in Python, it is also designed to be general-purpose and satisfy a wide- variety of computational needs. As a result, if absolute speed is essential, there is no replacement for a well-crafted, compiled loop specific to your application and hardware. This is one of the reasons that numpy includes f2py so that an easy-to-use mechanisms for linking (simple) C/C++ and (arbitrary) Fortran code directly into Python are available. You are encouraged to use and improve this mechanism. The purpose of this section is not to document this tool but to document the more basic steps to writing an extension module that this tool depends on.

When an extension module is written, compiled, and installed to somewhere in the Python path (sys.path), the code can then be imported into Python as if it were a standard python file. It will contain objects and methods that have been defined and compiled in C code. The basic steps for doing this in Python are well-documented and you can find more information in the documentation for Python itself available online at [www.python.org](https://www.python.org) .

In addition to the Python C-API, there is a full and rich C-API for NumPy allowing sophisticated manipulations on a C-level. However, for most applications, only a few API calls will typically be used. For example, if you need to just extract a pointer to memory along with some shape information to pass to another calculation routine, then you will use very different calls than if you are trying to create a new array-like type or add a new data type for ndarrays. This chapter documents the API calls and macros that are most commonly used.

## Required subroutine[#](#required-subroutine "Link to this heading")

There is exactly one function that must be defined in your C-code in order for Python to use it as an extension module. The function must be called init{name} where {name} is the name of the module from Python. This function must be declared so that it is visible to code outside of the routine. Besides adding the methods and constants you desire, this subroutine must also contain calls like `import_array()` and/or `import_ufunc()` depending on which C-API is needed. Forgetting to place these commands will show itself as an ugly segmentation fault (crash) as soon as any C-API subroutine is actually called. It is actually possible to have multiple init{name} functions in a single file in which case multiple modules will be defined by that file. However, there are some tricks to get that to work correctly and it is not covered here.

A minimal `init{name}` method looks like:
    
    
    PyMODINIT_FUNC
    init{name}(void)
    {
       (void)Py_InitModule({name}, mymethods);
       import_array();
    }
    

The mymethods must be an array (usually statically declared) of PyMethodDef structures which contain method names, actual C-functions, a variable indicating whether the method uses keyword arguments or not, and docstrings. These are explained in the next section. If you want to add constants to the module, then you store the returned value from Py_InitModule which is a module object. The most general way to add items to the module is to get the module dictionary using PyModule_GetDict(module). With the module dictionary, you can add whatever you like to the module manually. An easier way to add objects to the module is to use one of three additional Python C-API calls that do not require a separate extraction of the module dictionary. These are documented in the Python documentation, but repeated here for convenience:

int PyModule_AddObject([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)") *module, char *name, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)") *value)[#](#c.PyModule_AddObject "Link to this definition")  

    

int PyModule_AddIntConstant([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)") *module, char *name, long value)[#](#c.PyModule_AddIntConstant "Link to this definition")  

    

int PyModule_AddStringConstant([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)") *module, char *name, char *value)[#](#c.PyModule_AddStringConstant "Link to this definition")  

    

All three of these functions require the _module_ object (the return value of Py_InitModule). The _name_ is a string that labels the value in the module. Depending on which function is called, the _value_ argument is either a general object ([`PyModule_AddObject`](#c.PyModule_AddObject "PyModule_AddObject") steals a reference to it), an integer constant, or a string constant.

## Defining functions[#](#defining-functions "Link to this heading")

The second argument passed in to the Py_InitModule function is a structure that makes it easy to define functions in the module. In the example given above, the mymethods structure would have been defined earlier in the file (usually right before the init{name} subroutine) to:
    
    
    static PyMethodDef mymethods[] = {
        { nokeywordfunc,nokeyword_cfunc,
          METH_VARARGS,
          Doc string},
        { keywordfunc, keyword_cfunc,
          METH_VARARGS|METH_KEYWORDS,
          Doc string},
        {NULL, NULL, 0, NULL} /* Sentinel */
    }
    

Each entry in the mymethods array is a [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "\(in Python v3.14\)") structure containing 1) the Python name, 2) the C-function that implements the function, 3) flags indicating whether or not keywords are accepted for this function, and 4) The docstring for the function. Any number of functions may be defined for a single module by adding more entries to this table. The last entry must be all NULL as shown to act as a sentinel. Python looks for this entry to know that all of the functions for the module have been defined.

The last thing that must be done to finish the extension module is to actually write the code that performs the desired functions. There are two kinds of functions: those that don’t accept keyword arguments, and those that do.

### Functions without keyword arguments[#](#functions-without-keyword-arguments "Link to this heading")

Functions that don’t accept keyword arguments should be written as:
    
    
    static PyObject*
    nokeyword_cfunc (PyObject *dummy, PyObject *args)
    {
        /* convert Python arguments */
        /* do function */
        /* return something */
    }
    

The dummy argument is not used in this context and can be safely ignored. The _args_ argument contains all of the arguments passed in to the function as a tuple. You can do anything you want at this point, but usually the easiest way to manage the input arguments is to call [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "\(in Python v3.14\)") (args, format_string, addresses_to_C_variables…) or [`PyArg_UnpackTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple "\(in Python v3.14\)") (tuple, “name”, min, max, …). A good description of how to use the first function is contained in the Python C-API reference manual under section 5.5 (Parsing arguments and building values). You should pay particular attention to the “O&” format which uses converter functions to go between the Python object and the C object. All of the other format functions can be (mostly) thought of as special cases of this general rule. There are several converter functions defined in the NumPy C-API that may be of use. In particular, the [`PyArray_DescrConverter`](../reference/c-api/array.html#c.PyArray_DescrConverter "PyArray_DescrConverter") function is very useful to support arbitrary data-type specification. This function transforms any valid data-type Python object into a [PyArray_Descr](../reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")* object. Remember to pass in the address of the C-variables that should be filled in.

There are lots of examples of how to use [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "\(in Python v3.14\)") throughout the NumPy source code. The standard usage is like this:
    
    
    PyObject *input;
    PyArray_Descr *dtype;
    if (!PyArg_ParseTuple(args, "OO&", &input,
                          PyArray_DescrConverter,
                          &dtype)) return NULL;
    

It is important to keep in mind that you get a _borrowed_ reference to the object when using the “O” format string. However, the converter functions usually require some form of memory handling. In this example, if the conversion is successful, _dtype_ will hold a new reference to a [PyArray_Descr](../reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr")* object, while _input_ will hold a borrowed reference. Therefore, if this conversion were mixed with another conversion (say to an integer) and the data-type conversion was successful but the integer conversion failed, then you would need to release the reference count to the data-type object before returning. A typical way to do this is to set _dtype_ to `NULL` before calling [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "\(in Python v3.14\)") and then use [`Py_XDECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XDECREF "\(in Python v3.14\)") on _dtype_ before returning.

After the input arguments are processed, the code that actually does the work is written (likely calling other functions as needed). The final step of the C-function is to return something. If an error is encountered then `NULL` should be returned (making sure an error has actually been set). If nothing should be returned then increment [`Py_None`](https://docs.python.org/3/c-api/none.html#c.Py_None "\(in Python v3.14\)") and return it. If a single object should be returned then it is returned (ensuring that you own a reference to it first). If multiple objects should be returned then you need to return a tuple. The [`Py_BuildValue`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "\(in Python v3.14\)") (format_string, c_variables…) function makes it easy to build tuples of Python objects from C variables. Pay special attention to the difference between ‘N’ and ‘O’ in the format string or you can easily create memory leaks. The ‘O’ format string increments the reference count of the [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)")* C-variable it corresponds to, while the ‘N’ format string steals a reference to the corresponding [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)")* C-variable. You should use ‘N’ if you have already created a reference for the object and just want to give that reference to the tuple. You should use ‘O’ if you only have a borrowed reference to an object and need to create one to provide for the tuple.

### Functions with keyword arguments[#](#functions-with-keyword-arguments "Link to this heading")

These functions are very similar to functions without keyword arguments. The only difference is that the function signature is:
    
    
    static PyObject*
    keyword_cfunc (PyObject *dummy, PyObject *args, PyObject *kwds)
    {
    ...
    }
    

The kwds argument holds a Python dictionary whose keys are the names of the keyword arguments and whose values are the corresponding keyword-argument values. This dictionary can be processed however you see fit. The easiest way to handle it, however, is to replace the [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "\(in Python v3.14\)") (args, format_string, addresses…) function with a call to [`PyArg_ParseTupleAndKeywords`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTupleAndKeywords "\(in Python v3.14\)") (args, kwds, format_string, char *kwlist[], addresses…). The kwlist parameter to this function is a `NULL` -terminated array of strings providing the expected keyword arguments. There should be one string for each entry in the format_string. Using this function will raise a TypeError if invalid keyword arguments are passed in.

For more help on this function please see section 1.8 (Keyword Parameters for Extension Functions) of the Extending and Embedding tutorial in the Python documentation.

### Reference counting[#](#reference-counting "Link to this heading")

The biggest difficulty when writing extension modules is reference counting. It is an important reason for the popularity of f2py, weave, Cython, ctypes, etc…. If you mis-handle reference counts you can get problems from memory-leaks to segmentation faults. The only strategy I know of to handle reference counts correctly is blood, sweat, and tears. First, you force it into your head that every Python variable has a reference count. Then, you understand exactly what each function does to the reference count of your objects, so that you can properly use DECREF and INCREF when you need them. Reference counting can really test the amount of patience and diligence you have towards your programming craft. Despite the grim depiction, most cases of reference counting are quite straightforward with the most common difficulty being not using DECREF on objects before exiting early from a routine due to some error. In second place, is the common error of not owning the reference on an object that is passed to a function or macro that is going to steal the reference ( _e.g._ [`PyTuple_SET_ITEM`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SET_ITEM "\(in Python v3.14\)"), and most functions that take [`PyArray_Descr`](../reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr") objects).

Typically you get a new reference to a variable when it is created or is the return value of some function (there are some prominent exceptions, however — such as getting an item out of a tuple or a dictionary). When you own the reference, you are responsible to make sure that [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "\(in Python v3.14\)") (var) is called when the variable is no longer necessary (and no other function has “stolen” its reference). Also, if you are passing a Python object to a function that will “steal” the reference, then you need to make sure you own it (or use [`Py_INCREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "\(in Python v3.14\)") to get your own reference). You will also encounter the notion of borrowing a reference. A function that borrows a reference does not alter the reference count of the object and does not expect to “hold on “to the reference. It’s just going to use the object temporarily. When you use [`PyArg_ParseTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "\(in Python v3.14\)") or [`PyArg_UnpackTuple`](https://docs.python.org/3/c-api/arg.html#c.PyArg_UnpackTuple "\(in Python v3.14\)") you receive a borrowed reference to the objects in the tuple and should not alter their reference count inside your function. With practice, you can learn to get reference counting right, but it can be frustrating at first.

One common source of reference-count errors is the [`Py_BuildValue`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "\(in Python v3.14\)") function. Pay careful attention to the difference between the ‘N’ format character and the ‘O’ format character. If you create a new object in your subroutine (such as an output array), and you are passing it back in a tuple of return values, then you should most- likely use the ‘N’ format character in [`Py_BuildValue`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "\(in Python v3.14\)"). The ‘O’ character will increase the reference count by one. This will leave the caller with two reference counts for a brand-new array. When the variable is deleted and the reference count decremented by one, there will still be that extra reference count, and the array will never be deallocated. You will have a reference-counting induced memory leak. Using the ‘N’ character will avoid this situation as it will return to the caller an object (inside the tuple) with a single reference count.

## Dealing with array objects[#](#dealing-with-array-objects "Link to this heading")

Most extension modules for NumPy will need to access the memory for an ndarray object (or one of it’s sub-classes). The easiest way to do this doesn’t require you to know much about the internals of NumPy. The method is to

  1. Ensure you are dealing with a well-behaved array (aligned, in machine byte-order and single-segment) of the correct type and number of dimensions.

     1. By converting it from some Python object using [`PyArray_FromAny`](../reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny") or a macro built on it.

     2. By constructing a new ndarray of your desired shape and type using [`PyArray_NewFromDescr`](../reference/c-api/array.html#c.PyArray_NewFromDescr "PyArray_NewFromDescr") or a simpler macro or function based on it.

  2. Get the shape of the array and a pointer to its actual data.

  3. Pass the data and shape information on to a subroutine or other section of code that actually performs the computation.

  4. If you are writing the algorithm, then I recommend that you use the stride information contained in the array to access the elements of the array (the [`PyArray_GetPtr`](../reference/c-api/array.html#c.PyArray_GetPtr "PyArray_GetPtr") macros make this painless). Then, you can relax your requirements so as not to force a single-segment array and the data-copying that might result.




Each of these sub-topics is covered in the following sub-sections.

### Converting an arbitrary sequence object[#](#converting-an-arbitrary-sequence-object "Link to this heading")

The main routine for obtaining an array from any Python object that can be converted to an array is [`PyArray_FromAny`](../reference/c-api/array.html#c.PyArray_FromAny "PyArray_FromAny"). This function is very flexible with many input arguments. Several macros make it easier to use the basic function. [`PyArray_FROM_OTF`](../reference/c-api/array.html#c.PyArray_FROM_OTF "PyArray_FROM_OTF") is arguably the most useful of these macros for the most common uses. It allows you to convert an arbitrary Python object to an array of a specific builtin data-type ( _e.g._ float), while specifying a particular set of requirements ( _e.g._ contiguous, aligned, and writeable). The syntax is

[`PyArray_FROM_OTF`](../reference/c-api/array.html#c.PyArray_FROM_OTF "PyArray_FROM_OTF")
    

Return an ndarray from any Python object, _obj_ , that can be converted to an array. The number of dimensions in the returned array is determined by the object. The desired data-type of the returned array is provided in _typenum_ which should be one of the enumerated types. The _requirements_ for the returned array can be any combination of standard array flags. Each of these arguments is explained in more detail below. You receive a new reference to the array on success. On failure, `NULL` is returned and an exception is set.

_obj_
    

The object can be any Python object convertible to an ndarray. If the object is already (a subclass of) the ndarray that satisfies the requirements then a new reference is returned. Otherwise, a new array is constructed. The contents of _obj_ are copied to the new array unless the array interface is used so that data does not have to be copied. Objects that can be converted to an array include: 1) any nested sequence object, 2) any object exposing the array interface, 3) any object with an [`__array__`](../reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__") method (which should return an ndarray), and 4) any scalar object (becomes a zero-dimensional array). Sub-classes of the ndarray that otherwise fit the requirements will be passed through. If you want to ensure a base-class ndarray, then use [`NPY_ARRAY_ENSUREARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "NPY_ARRAY_ENSUREARRAY") in the requirements flag. A copy is made only if necessary. If you want to guarantee a copy, then pass in [`NPY_ARRAY_ENSURECOPY`](../reference/c-api/array.html#c.NPY_ARRAY_ENSURECOPY "NPY_ARRAY_ENSURECOPY") to the requirements flag.

_typenum_
    

One of the enumerated types or [`NPY_NOTYPE`](../reference/c-api/dtype.html#c.NPY_NOTYPE "NPY_NOTYPE") if the data-type should be determined from the object itself. The C-based names can be used:

> [`NPY_BOOL`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_BOOL "NPY_BOOL"), [`NPY_BYTE`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_BYTE "NPY_BYTE"), [`NPY_UBYTE`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_UBYTE "NPY_UBYTE"), [`NPY_SHORT`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_SHORT "NPY_SHORT"), [`NPY_USHORT`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_USHORT "NPY_USHORT"), [`NPY_INT`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT "NPY_INT"), [`NPY_UINT`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT "NPY_UINT"), [`NPY_LONG`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONG "NPY_LONG"), [`NPY_ULONG`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_ULONG "NPY_ULONG"), [`NPY_LONGLONG`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONGLONG "NPY_LONGLONG"), [`NPY_ULONGLONG`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_ULONGLONG "NPY_ULONGLONG"), [`NPY_DOUBLE`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_DOUBLE "NPY_DOUBLE"), [`NPY_LONGDOUBLE`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_LONGDOUBLE "NPY_LONGDOUBLE"), [`NPY_CFLOAT`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_CFLOAT "NPY_CFLOAT"), [`NPY_CDOUBLE`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_CDOUBLE "NPY_CDOUBLE"), [`NPY_CLONGDOUBLE`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_CLONGDOUBLE "NPY_CLONGDOUBLE"), [`NPY_OBJECT`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_OBJECT "NPY_OBJECT").

Alternatively, the bit-width names can be used as supported on the platform. For example:

> [`NPY_INT8`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT8 "NPY_INT8"), [`NPY_INT16`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT16 "NPY_INT16"), [`NPY_INT32`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT32 "NPY_INT32"), [`NPY_INT64`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_INT64 "NPY_INT64"), [`NPY_UINT8`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT8 "NPY_UINT8"), [`NPY_UINT16`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT16 "NPY_UINT16"), [`NPY_UINT32`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT32 "NPY_UINT32"), [`NPY_UINT64`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_UINT64 "NPY_UINT64"), [`NPY_FLOAT32`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT32 "NPY_FLOAT32"), [`NPY_FLOAT64`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_FLOAT64 "NPY_FLOAT64"), [`NPY_COMPLEX64`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_COMPLEX64 "NPY_COMPLEX64"), [`NPY_COMPLEX128`](../reference/c-api/dtype.html#c.NPY_TYPES.NPY_COMPLEX128 "NPY_COMPLEX128").

The object will be converted to the desired type only if it can be done without losing precision. Otherwise `NULL` will be returned and an error raised. Use [`NPY_ARRAY_FORCECAST`](../reference/c-api/array.html#c.NPY_ARRAY_FORCECAST "NPY_ARRAY_FORCECAST") in the requirements flag to override this behavior.

_requirements_
    

The memory model for an ndarray admits arbitrary strides in each dimension to advance to the next element of the array. Often, however, you need to interface with code that expects a C-contiguous or a Fortran-contiguous memory layout. In addition, an ndarray can be misaligned (the address of an element is not at an integral multiple of the size of the element) which can cause your program to crash (or at least work more slowly) if you try and dereference a pointer into the array data. Both of these problems can be solved by converting the Python object into an array that is more “well-behaved” for your specific usage.

The requirements flag allows specification of what kind of array is acceptable. If the object passed in does not satisfy this requirements then a copy is made so that the returned object will satisfy the requirements. these ndarray can use a very generic pointer to memory. This flag allows specification of the desired properties of the returned array object. All of the flags are explained in the detailed API chapter. The flags most commonly needed are [`NPY_ARRAY_IN_ARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_IN_ARRAY "NPY_ARRAY_IN_ARRAY"), [`NPY_ARRAY_OUT_ARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_OUT_ARRAY "NPY_ARRAY_OUT_ARRAY"), and [`NPY_ARRAY_INOUT_ARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_INOUT_ARRAY "NPY_ARRAY_INOUT_ARRAY"):

[`NPY_ARRAY_IN_ARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_IN_ARRAY "NPY_ARRAY_IN_ARRAY")
    

This flag is useful for arrays that must be in C-contiguous order and aligned. These kinds of arrays are usually input arrays for some algorithm.

[`NPY_ARRAY_OUT_ARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_OUT_ARRAY "NPY_ARRAY_OUT_ARRAY")
    

This flag is useful to specify an array that is in C-contiguous order, is aligned, and can be written to as well. Such an array is usually returned as output (although normally such output arrays are created from scratch).

[`NPY_ARRAY_INOUT_ARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_INOUT_ARRAY "NPY_ARRAY_INOUT_ARRAY")
    

This flag is useful to specify an array that will be used for both input and output. [`PyArray_ResolveWritebackIfCopy`](../reference/c-api/array.html#c.PyArray_ResolveWritebackIfCopy "PyArray_ResolveWritebackIfCopy") must be called before [`Py_DECREF`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "\(in Python v3.14\)") at the end of the interface routine to write back the temporary data into the original array passed in. Use of the [`NPY_ARRAY_WRITEBACKIFCOPY`](../reference/c-api/array.html#c.NPY_ARRAY_WRITEBACKIFCOPY "NPY_ARRAY_WRITEBACKIFCOPY") flag requires that the input object is already an array (because other objects cannot be automatically updated in this fashion). If an error occurs use [`PyArray_DiscardWritebackIfCopy`](../reference/c-api/array.html#c.PyArray_DiscardWritebackIfCopy "PyArray_DiscardWritebackIfCopy") (obj) on an array with these flags set. This will set the underlying base array writable without causing the contents to be copied back into the original array.

Other useful flags that can be OR’d as additional requirements are:

[`NPY_ARRAY_FORCECAST`](../reference/c-api/array.html#c.NPY_ARRAY_FORCECAST "NPY_ARRAY_FORCECAST")
    

Cast to the desired type, even if it can’t be done without losing information.

[`NPY_ARRAY_ENSURECOPY`](../reference/c-api/array.html#c.NPY_ARRAY_ENSURECOPY "NPY_ARRAY_ENSURECOPY")
    

Make sure the resulting array is a copy of the original.

[`NPY_ARRAY_ENSUREARRAY`](../reference/c-api/array.html#c.NPY_ARRAY_ENSUREARRAY "NPY_ARRAY_ENSUREARRAY")
    

Make sure the resulting object is an actual ndarray and not a sub- class.

Note

Whether or not an array is byte-swapped is determined by the data-type of the array. Native byte-order arrays are always requested by [`PyArray_FROM_OTF`](../reference/c-api/array.html#c.PyArray_FROM_OTF "PyArray_FROM_OTF") and so there is no need for a [`NPY_ARRAY_NOTSWAPPED`](../reference/c-api/array.html#c.NPY_ARRAY_NOTSWAPPED "NPY_ARRAY_NOTSWAPPED") flag in the requirements argument. There is also no way to get a byte-swapped array from this routine.

### Creating a brand-new ndarray[#](#creating-a-brand-new-ndarray "Link to this heading")

Quite often, new arrays must be created from within extension-module code. Perhaps an output array is needed and you don’t want the caller to have to supply it. Perhaps only a temporary array is needed to hold an intermediate calculation. Whatever the need there are simple ways to get an ndarray object of whatever data-type is needed. The most general function for doing this is [`PyArray_NewFromDescr`](../reference/c-api/array.html#c.PyArray_NewFromDescr "PyArray_NewFromDescr"). All array creation functions go through this heavily re-used code. Because of its flexibility, it can be somewhat confusing to use. As a result, simpler forms exist that are easier to use. These forms are part of the [`PyArray_SimpleNew`](../reference/c-api/array.html#c.PyArray_SimpleNew "PyArray_SimpleNew") family of functions, which simplify the interface by providing default values for common use cases.

### Getting at ndarray memory and accessing elements of the ndarray[#](#getting-at-ndarray-memory-and-accessing-elements-of-the-ndarray "Link to this heading")

If obj is an ndarray ([PyArrayObject](../reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")*), then the data-area of the ndarray is pointed to by the void* pointer [`PyArray_DATA`](../reference/c-api/array.html#c.PyArray_DATA "PyArray_DATA") (obj) or the char* pointer [`PyArray_BYTES`](../reference/c-api/array.html#c.PyArray_BYTES "PyArray_BYTES") (obj). Remember that (in general) this data-area may not be aligned according to the data-type, it may represent byte-swapped data, and/or it may not be writeable. If the data area is aligned and in native byte-order, then how to get at a specific element of the array is determined only by the array of npy_intp variables, [`PyArray_STRIDES`](../reference/c-api/array.html#c.PyArray_STRIDES "PyArray_STRIDES") (obj). In particular, this c-array of integers shows how many **bytes** must be added to the current element pointer to get to the next element in each dimension. For arrays less than 4-dimensions there are `PyArray_GETPTR{k}` (obj, …) macros where {k} is the integer 1, 2, 3, or 4 that make using the array strides easier. The arguments …. represent {k} non- negative integer indices into the array. For example, suppose `E` is a 3-dimensional ndarray. A (void*) pointer to the element `E[i,j,k]` is obtained as [`PyArray_GETPTR3`](../reference/c-api/array.html#c.PyArray_GETPTR3 "PyArray_GETPTR3") (E, i, j, k).

As explained previously, C-style contiguous arrays and Fortran-style contiguous arrays have particular striding patterns. Two array flags ([`NPY_ARRAY_C_CONTIGUOUS`](../reference/c-api/array.html#c.NPY_ARRAY_C_CONTIGUOUS "NPY_ARRAY_C_CONTIGUOUS") and [`NPY_ARRAY_F_CONTIGUOUS`](../reference/c-api/array.html#c.NPY_ARRAY_F_CONTIGUOUS "NPY_ARRAY_F_CONTIGUOUS")) indicate whether or not the striding pattern of a particular array matches the C-style contiguous or Fortran-style contiguous or neither. Whether or not the striding pattern matches a standard C or Fortran one can be tested Using [`PyArray_IS_C_CONTIGUOUS`](../reference/c-api/array.html#c.PyArray_IS_C_CONTIGUOUS "PyArray_IS_C_CONTIGUOUS") (obj) and [`PyArray_ISFORTRAN`](../reference/c-api/array.html#c.PyArray_ISFORTRAN "PyArray_ISFORTRAN") (obj) respectively. Most third-party libraries expect contiguous arrays. But, often it is not difficult to support general-purpose striding. I encourage you to use the striding information in your own code whenever possible, and reserve single-segment requirements for wrapping third-party code. Using the striding information provided with the ndarray rather than requiring a contiguous striding reduces copying that otherwise must be made.

## Example[#](#example "Link to this heading")

The following example shows how you might write a wrapper that accepts two input arguments (that will be converted to an array) and an output argument (that must be an array). The function returns None and updates the output array. Note the updated use of WRITEBACKIFCOPY semantics for NumPy v1.14 and above
    
    
    static PyObject *
    example_wrapper(PyObject *dummy, PyObject *args)
    {
        PyObject *arg1=NULL, *arg2=NULL, *out=NULL;
        PyObject *arr1=NULL, *arr2=NULL, *oarr=NULL;
    
        if (!PyArg_ParseTuple(args, "OOO!", &arg1, &arg2,
            &PyArray_Type, &out)) return NULL;
    
        arr1 = PyArray_FROM_OTF(arg1, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY);
        if (arr1 == NULL) return NULL;
        arr2 = PyArray_FROM_OTF(arg2, NPY_DOUBLE, NPY_ARRAY_IN_ARRAY);
        if (arr2 == NULL) goto fail;
    #if NPY_API_VERSION >= 0x0000000c
        oarr = PyArray_FROM_OTF(out, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2);
    #else
        oarr = PyArray_FROM_OTF(out, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY);
    #endif
        if (oarr == NULL) goto fail;
    
        /* code that makes use of arguments */
        /* You will probably need at least
           nd = PyArray_NDIM(<..>)    -- number of dimensions
           dims = PyArray_DIMS(<..>)  -- npy_intp array of length nd
                                         showing length in each dim.
           dptr = (double *)PyArray_DATA(<..>) -- pointer to data.
    
           If an error occurs goto fail.
         */
    
        Py_DECREF(arr1);
        Py_DECREF(arr2);
    #if NPY_API_VERSION >= 0x0000000c
        PyArray_ResolveWritebackIfCopy(oarr);
    #endif
        Py_DECREF(oarr);
        Py_INCREF(Py_None);
        return Py_None;
    
     fail:
        Py_XDECREF(arr1);
        Py_XDECREF(arr2);
    #if NPY_API_VERSION >= 0x0000000c
        PyArray_DiscardWritebackIfCopy(oarr);
    #endif
        Py_XDECREF(oarr);
        return NULL;
    }
    

[ __ previous Using NumPy C-API ](c-info.html "previous page") [ next Using Python as glue __](c-info.python-as-glue.html "next page")

__On this page

  * [Writing an extension module](#writing-an-extension-module)
  * [Required subroutine](#required-subroutine)
  * [Defining functions](#defining-functions)
    * [Functions without keyword arguments](#functions-without-keyword-arguments)
    * [Functions with keyword arguments](#functions-with-keyword-arguments)
    * [Reference counting](#reference-counting)
  * [Dealing with array objects](#dealing-with-array-objects)
    * [Converting an arbitrary sequence object](#converting-an-arbitrary-sequence-object)
    * [Creating a brand-new ndarray](#creating-a-brand-new-ndarray)
    * [Getting at ndarray memory and accessing elements of the ndarray](#getting-at-ndarray-memory-and-accessing-elements-of-the-ndarray)
  * [Example](#example)

---

## Using Python as glue

**Source:** [https://numpy.org/devdocs/user/c-info.python-as-glue.html](https://numpy.org/devdocs/user/c-info.python-as-glue.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Using NumPy C-API](c-info.html)
  * Using Python as glue



# Using Python as glue[#](#using-python-as-glue "Link to this heading")

Warning

This was written in 2008 as part of the original [Guide to NumPy](https://archive.org/details/NumPyBook) book by Travis E. Oliphant and is out of date.

There is no conversation more boring than the one where everybody

agrees.

— _Michel de Montaigne_

Duct tape is like the force. It has a light side, and a dark side, and

it holds the universe together.

— _Carl Zwanzig_

Many people like to say that Python is a fantastic glue language. Hopefully, this Chapter will convince you that this is true. The first adopters of Python for science were typically people who used it to glue together large application codes running on super-computers. Not only was it much nicer to code in Python than in a shell script or Perl, in addition, the ability to easily extend Python made it relatively easy to create new classes and types specifically adapted to the problems being solved. From the interactions of these early contributors, Numeric emerged as an array-like object that could be used to pass data between these applications.

As Numeric has matured and developed into NumPy, people have been able to write more code directly in NumPy. Often this code is fast-enough for production use, but there are still times that there is a need to access compiled code. Either to get that last bit of efficiency out of the algorithm or to make it easier to access widely-available codes written in C/C++ or Fortran.

This chapter will review many of the tools that are available for the purpose of accessing code written in other compiled languages. There are many resources available for learning to call other compiled libraries from Python and the purpose of this Chapter is not to make you an expert. The main goal is to make you aware of some of the possibilities so that you will know what to “Google” in order to learn more.

## Calling other compiled libraries from Python[#](#calling-other-compiled-libraries-from-python "Link to this heading")

While Python is a great language and a pleasure to code in, its dynamic nature results in overhead that can cause some code ( _i.e._ raw computations inside of for loops) to be up 10-100 times slower than equivalent code written in a static compiled language. In addition, it can cause memory usage to be larger than necessary as temporary arrays are created and destroyed during computation. For many types of computing needs, the extra slow-down and memory consumption can often not be spared (at least for time- or memory- critical portions of your code). Therefore one of the most common needs is to call out from Python code to a fast, machine-code routine (e.g. compiled using C/C++ or Fortran). The fact that this is relatively easy to do is a big reason why Python is such an excellent high-level language for scientific and engineering programming.

There are two basic approaches to calling compiled code: writing an extension module that is then imported to Python using the import command, or calling a shared-library subroutine directly from Python using the [ctypes](https://docs.python.org/3/library/ctypes.html) module. Writing an extension module is the most common method.

Warning

Calling C-code from Python can result in Python crashes if you are not careful. None of the approaches in this chapter are immune. You have to know something about the way data is handled by both NumPy and by the third-party library being used.

## Hand-generated wrappers[#](#hand-generated-wrappers "Link to this heading")

Extension modules were discussed in [Writing an extension module](c-info.how-to-extend.html#writing-an-extension). The most basic way to interface with compiled code is to write an extension module and construct a module method that calls the compiled code. For improved readability, your method should take advantage of the `PyArg_ParseTuple` call to convert between Python objects and C data-types. For standard C data-types there is probably already a built-in converter. For others you may need to write your own converter and use the `"O&"` format string which allows you to specify a function that will be used to perform the conversion from the Python object to whatever C-structures are needed.

Once the conversions to the appropriate C-structures and C data-types have been performed, the next step in the wrapper is to call the underlying function. This is straightforward if the underlying function is in C or C++. However, in order to call Fortran code you must be familiar with how Fortran subroutines are called from C/C++ using your compiler and platform. This can vary somewhat platforms and compilers (which is another reason f2py makes life much simpler for interfacing Fortran code) but generally involves underscore mangling of the name and the fact that all variables are passed by reference (i.e. all arguments are pointers).

The advantage of the hand-generated wrapper is that you have complete control over how the C-library gets used and called which can lead to a lean and tight interface with minimal over-head. The disadvantage is that you have to write, debug, and maintain C-code, although most of it can be adapted using the time-honored technique of “cutting-pasting-and-modifying” from other extension modules. Because the procedure of calling out to additional C-code is fairly regimented, code-generation procedures have been developed to make this process easier. One of these code-generation techniques is distributed with NumPy and allows easy integration with Fortran and (simple) C code. This package, f2py, will be covered briefly in the next section.

## F2PY[#](#f2py "Link to this heading")

F2PY allows you to automatically construct an extension module that interfaces to routines in Fortran 77/90/95 code. It has the ability to parse Fortran 77/90/95 code and automatically generate Python signatures for the subroutines it encounters, or you can guide how the subroutine interfaces with Python by constructing an interface-definition-file (or modifying the f2py-produced one).

See the [F2PY documentation](../f2py/index.html#f2py) for more information and examples.

The f2py method of linking compiled code is currently the most sophisticated and integrated approach. It allows clean separation of Python with compiled code while still allowing for separate distribution of the extension module. The only draw-back is that it requires the existence of a Fortran compiler in order for a user to install the code. However, with the existence of the free-compilers g77, gfortran, and g95, as well as high-quality commercial compilers, this restriction is not particularly onerous. In our opinion, Fortran is still the easiest way to write fast and clear code for scientific computing. It handles complex numbers, and multi-dimensional indexing in the most straightforward way. Be aware, however, that some Fortran compilers will not be able to optimize code as well as good hand- written C-code.

## Cython[#](#cython "Link to this heading")

[Cython](https://cython.org) is a compiler for a Python dialect that adds (optional) static typing for speed, and allows mixing C or C++ code into your modules. It produces C or C++ extensions that can be compiled and imported in Python code.

If you are writing an extension module that will include quite a bit of your own algorithmic code as well, then Cython is a good match. Among its features is the ability to easily and quickly work with multidimensional arrays.

Notice that Cython is an extension-module generator only. Unlike f2py, it includes no automatic facility for compiling and linking the extension module. However, many Python build tools have support for Cython.

Here is an example of how to set up a Python project that contains a Cython extension. The example uses the [meson-python Python build backend](https://mesonbuild.com/meson-python/) and [the meson build system](https://mesonbuild.com). This is the same build system NumPy itself uses. .

First, create a file named `my_extension.pyx`.
    
    
    cimport numpy as np
    
    def say_hello():
        print("Hello!")
    

This file lives next to a `__init__.py` file with the following content:
    
    
    from .my_extension import say_hello
    

Now you need to create two more files to set up the build system. First, a `meson.build` file:
    
    
    project(
       'module_with_extension',
       'c', 'cython',
       version: '0.0.1',
       license: 'MIT',
    )
    
    cython = find_program('cython')
    py = import('python').find_installation(pure: false)
    
    numpy_nodepr_api = ['-DNPY_NO_DEPRECATED_API=NPY_2_0_API_VERSION']
    
    np_dep = declare_dependency(dependencies: dependency('numpy'),
                                compile_args: numpy_nodepr_api)
    
    py.extension_module(
      'my_extension',
      'my_extension.pyx',
      dependencies: [np_dep],
      install: true,
      subdir: 'my_module_with_extension',
    )
    
    py.install_sources(
      '__init__.py',
      subdir: 'my_module_with_extension',
    )
    

And a `pyproject.toml` file with the following content:
    
    
    [build-system]
    build-backend = "mesonpy"
    requires = [
        "meson-python",
        "Cython>=3.0.0",
        "numpy",
    ]
    
    [project]
    name = "my_module_with_extension"
    version = "0.0.1"
    license = "MIT"
    dependencies = ["numpy"]
    

You should then be able to do the following command to build, install, and call the function defined in the extension from Python:
    
    
    $ pip install .
    $ python -c "from my_module_with_extension import say_hello; say_hello()"
    "Hello!"
    

Adding a NumPy dependency to your Meson configuration is only necessary if you are using the NumPy C API in the extension module via `cimport numpy` (which is what we assume you are using Cython for). If you just use Cython to compile a standard Python module, then you will get a C extension module that typically runs a bit faster than the equivalent Python module. Further speed increases can be gained by using the `cdef` keyword to statically define C variables.

See the meson and meson-python documentation for more details on how to build more complicated extensions.

Let’s look at two examples we’ve seen before to see how they might be implemented using Cython.

### Complex addition in Cython[#](#complex-addition-in-cython "Link to this heading")

Here is part of a Cython module named `add.pyx` which implements the complex addition functions we previously implemented using f2py:
    
    
    cimport cython
    cimport numpy as np
    import numpy as np
    
    # We need to initialize NumPy.
    np.import_array()
    
    #@cython.boundscheck(False)
    def zadd(in1, in2):
        cdef double complex[:] a = in1.ravel()
        cdef double complex[:] b = in2.ravel()
    
        out = np.empty(a.shape[0], np.complex64)
        cdef double complex[:] c = out.ravel()
    
        for i in range(c.shape[0]):
            c[i].real = a[i].real + b[i].real
            c[i].imag = a[i].imag + b[i].imag
    
        return out
    

This module shows use of the `cimport` statement to load the definitions from the `numpy.pxd` header that ships with Cython. It looks like NumPy is imported twice; `cimport` only makes the NumPy C-API available, while the regular `import` causes a Python-style import at runtime and makes it possible to call into the familiar NumPy Python API.

The example also demonstrates Cython’s “typed memoryviews”, which are like NumPy arrays at the C level, in the sense that they are shaped and strided arrays that know their own extent (unlike a C array addressed through a bare pointer). The syntax `double complex[:]` denotes a one-dimensional array (vector) of doubles, with arbitrary strides. A contiguous array of ints would be `int[::1]`, while a matrix of floats would be `float[:, :]`.

Shown commented is the `cython.boundscheck` decorator, which turns bounds-checking for memory view accesses on or off on a per-function basis. We can use this to further speed up our code, at the expense of safety (or a manual check prior to entering the loop).

Other than the view syntax, the function is immediately readable to a Python programmer. Static typing of the variable `i` is implicit. Instead of the view syntax, we could also have used Cython’s special NumPy array syntax, but the view syntax is preferred.

### Image filter in Cython[#](#image-filter-in-cython "Link to this heading")

The two-dimensional example we created using Fortran is just as easy to write in Cython:
    
    
    cimport numpy as np
    import numpy as np
    
    np.import_array()
    
    def filter(img):
        cdef double[:, :] a = np.asarray(img, dtype=np.double)
        out = np.zeros(img.shape, dtype=np.double)
        cdef double[:, ::1] b = out
    
        cdef np.npy_intp i, j
    
        for i in range(1, a.shape[0] - 1):
            for j in range(1, a.shape[1] - 1):
                b[i, j] = (a[i, j]
                           + .5 * (  a[i-1, j] + a[i+1, j]
                                   + a[i, j-1] + a[i, j+1])
                           + .25 * (  a[i-1, j-1] + a[i-1, j+1]
                                    + a[i+1, j-1] + a[i+1, j+1]))
    
        return out
    

This 2-d averaging filter runs quickly because the loop is in C and the pointer computations are done only as needed. If the code above is compiled as a module `image`, then a 2-d image, `img`, can be filtered using this code very quickly using:
    
    
    import image
    out = image.filter(img)
    

Regarding the code, two things are of note: firstly, it is impossible to return a memory view to Python. Instead, a NumPy array `out` is first created, and then a view `b` onto this array is used for the computation. Secondly, the view `b` is typed `double[:, ::1]`. This means 2-d array with contiguous rows, i.e., C matrix order. Specifying the order explicitly can speed up some algorithms since they can skip stride computations.

### Conclusion[#](#conclusion "Link to this heading")

Cython is the extension mechanism of choice for several scientific Python libraries, including Scipy, Pandas, SAGE, scikit-image and scikit-learn, as well as the XML processing library LXML. The language and compiler are well-maintained.

There are several disadvantages of using Cython:

  1. When coding custom algorithms, and sometimes when wrapping existing C libraries, some familiarity with C is required. In particular, when using C memory management (`malloc` and friends), it’s easy to introduce memory leaks. However, just compiling a Python module renamed to `.pyx` can already speed it up, and adding a few type declarations can give dramatic speedups in some code.

  2. It is easy to lose a clean separation between Python and C which makes re-using your C-code for other non-Python-related projects more difficult.

  3. The C-code generated by Cython is hard to read and modify (and typically compiles with annoying but harmless warnings).




One big advantage of Cython-generated extension modules is that they are easy to distribute. In summary, Cython is a very capable tool for either gluing C code or generating an extension module quickly and should not be over-looked. It is especially useful for people that can’t or won’t write C or Fortran code.

## ctypes[#](#index-2 "Link to this heading")

[ctypes](https://docs.python.org/3/library/ctypes.html) is a Python extension module, included in the stdlib, that allows you to call an arbitrary function in a shared library directly from Python. This approach allows you to interface with C-code directly from Python. This opens up an enormous number of libraries for use from Python. The drawback, however, is that coding mistakes can lead to ugly program crashes very easily (just as can happen in C) because there is little type or bounds checking done on the parameters. This is especially true when array data is passed in as a pointer to a raw memory location. The responsibility is then on you that the subroutine will not access memory outside the actual array area. But, if you don’t mind living a little dangerously ctypes can be an effective tool for quickly taking advantage of a large shared library (or writing extended functionality in your own shared library).

Because the ctypes approach exposes a raw interface to the compiled code it is not always tolerant of user mistakes. Robust use of the ctypes module typically involves an additional layer of Python code in order to check the data types and array bounds of objects passed to the underlying subroutine. This additional layer of checking (not to mention the conversion from ctypes objects to C-data-types that ctypes itself performs), will make the interface slower than a hand-written extension-module interface. However, this overhead should be negligible if the C-routine being called is doing any significant amount of work. If you are a great Python programmer with weak C skills, ctypes is an easy way to write a useful interface to a (shared) library of compiled code.

To use ctypes you must

  1. Have a shared library.

  2. Load the shared library.

  3. Convert the Python objects to ctypes-understood arguments.

  4. Call the function from the library with the ctypes arguments.




### Having a shared library[#](#having-a-shared-library "Link to this heading")

There are several requirements for a shared library that can be used with ctypes that are platform specific. This guide assumes you have some familiarity with making a shared library on your system (or simply have a shared library available to you). Items to remember are:

  * A shared library must be compiled in a special way ( _e.g._ using the `-shared` flag with gcc).

  * On some platforms (_e.g._ Windows), a shared library requires a .def file that specifies the functions to be exported. For example a mylib.def file might contain:
        
        LIBRARY mylib.dll
        EXPORTS
        cool_function1
        cool_function2
        

Alternatively, you may be able to use the storage-class specifier `__declspec(dllexport)` in the C-definition of the function to avoid the need for this `.def` file.




There is no standard way in Python distutils to create a standard shared library (an extension module is a “special” shared library Python understands) in a cross-platform manner. Thus, a big disadvantage of ctypes at the time of writing this book is that it is difficult to distribute in a cross-platform manner a Python extension that uses ctypes and includes your own code which should be compiled as a shared library on the users system.

### Loading the shared library[#](#loading-the-shared-library "Link to this heading")

A simple, but robust way to load the shared library is to get the absolute path name and load it using the cdll object of ctypes:
    
    
    lib = ctypes.cdll[<full_path_name>]
    

However, on Windows accessing an attribute of the `cdll` method will load the first DLL by that name found in the current directory or on the PATH. Loading the absolute path name requires a little finesse for cross-platform work since the extension of shared libraries varies. There is a `ctypes.util.find_library` utility available that can simplify the process of finding the library to load but it is not foolproof. Complicating matters, different platforms have different default extensions used by shared libraries (e.g. .dll – Windows, .so – Linux, .dylib – Mac OS X). This must also be taken into account if you are using ctypes to wrap code that needs to work on several platforms.

NumPy provides a convenience function called `ctypeslib.load_library` (name, path). This function takes the name of the shared library (including any prefix like ‘lib’ but excluding the extension) and a path where the shared library can be located. It returns a ctypes library object or raises an `OSError` if the library cannot be found or raises an `ImportError` if the ctypes module is not available. (Windows users: the ctypes library object loaded using `load_library` is always loaded assuming cdecl calling convention. See the ctypes documentation under `ctypes.windll` and/or `ctypes.oledll` for ways to load libraries under other calling conventions).

The functions in the shared library are available as attributes of the ctypes library object (returned from `ctypeslib.load_library`) or as items using `lib['func_name']` syntax. The latter method for retrieving a function name is particularly useful if the function name contains characters that are not allowable in Python variable names.

### Converting arguments[#](#converting-arguments "Link to this heading")

Python ints/longs, strings, and unicode objects are automatically converted as needed to equivalent ctypes arguments The None object is also converted automatically to a NULL pointer. All other Python objects must be converted to ctypes-specific types. There are two ways around this restriction that allow ctypes to integrate with other objects.

  1. Don’t set the argtypes attribute of the function object and define an `_as_parameter_` method for the object you want to pass in. The `_as_parameter_` method must return a Python int which will be passed directly to the function.

  2. Set the argtypes attribute to a list whose entries contain objects with a classmethod named from_param that knows how to convert your object to an object that ctypes can understand (an int/long, string, unicode, or object with the `_as_parameter_` attribute).




NumPy uses both methods with a preference for the second method because it can be safer. The ctypes attribute of the ndarray returns an object that has an `_as_parameter_` attribute which returns an integer representing the address of the ndarray to which it is associated. As a result, one can pass this ctypes attribute object directly to a function expecting a pointer to the data in your ndarray. The caller must be sure that the ndarray object is of the correct type, shape, and has the correct flags set or risk nasty crashes if the data-pointer to inappropriate arrays are passed in.

To implement the second method, NumPy provides the class-factory function [`ndpointer`](#ndpointer "ndpointer") in the [`numpy.ctypeslib`](../reference/routines.ctypeslib.html#module-numpy.ctypeslib "numpy.ctypeslib") module. This class-factory function produces an appropriate class that can be placed in an argtypes attribute entry of a ctypes function. The class will contain a from_param method which ctypes will use to convert any ndarray passed in to the function to a ctypes-recognized object. In the process, the conversion will perform checking on any properties of the ndarray that were specified by the user in the call to [`ndpointer`](#ndpointer "ndpointer"). Aspects of the ndarray that can be checked include the data-type, the number-of-dimensions, the shape, and/or the state of the flags on any array passed. The return value of the from_param method is the ctypes attribute of the array which (because it contains the `_as_parameter_` attribute pointing to the array data area) can be used by ctypes directly.

The ctypes attribute of an ndarray is also endowed with additional attributes that may be convenient when passing additional information about the array into a ctypes function. The attributes **data** , **shape** , and **strides** can provide ctypes compatible types corresponding to the data-area, the shape, and the strides of the array. The data attribute returns a `c_void_p` representing a pointer to the data area. The shape and strides attributes each return an array of ctypes integers (or None representing a NULL pointer, if a 0-d array). The base ctype of the array is a ctype integer of the same size as a pointer on the platform. There are also methods `data_as({ctype})`, `shape_as(<base ctype>)`, and `strides_as(<base ctype>)`. These return the data as a ctype object of your choice and the shape/strides arrays using an underlying base type of your choice. For convenience, the `ctypeslib` module also contains `c_intp` as a ctypes integer data-type whose size is the same as the size of `c_void_p` on the platform (its value is None if ctypes is not installed).

### Calling the function[#](#calling-the-function "Link to this heading")

The function is accessed as an attribute of or an item from the loaded shared-library. Thus, if `./mylib.so` has a function named `cool_function1`, it may be accessed either as:
    
    
    lib = numpy.ctypeslib.load_library('mylib','.')
    func1 = lib.cool_function1  # or equivalently
    func1 = lib['cool_function1']
    

In ctypes, the return-value of a function is set to be ‘int’ by default. This behavior can be changed by setting the restype attribute of the function. Use None for the restype if the function has no return value (‘void’):
    
    
    func1.restype = None
    

As previously discussed, you can also set the argtypes attribute of the function in order to have ctypes check the types of the input arguments when the function is called. Use the [`ndpointer`](#ndpointer "ndpointer") factory function to generate a ready-made class for data-type, shape, and flags checking on your new function. The [`ndpointer`](#ndpointer "ndpointer") function has the signature

ndpointer(_dtype =None_, _ndim =None_, _shape =None_, _flags =None_)[#](#ndpointer "Link to this definition")
    

Keyword arguments with the value `None` are not checked. Specifying a keyword enforces checking of that aspect of the ndarray on conversion to a ctypes-compatible object. The dtype keyword can be any object understood as a data-type object. The ndim keyword should be an integer, and the shape keyword should be an integer or a sequence of integers. The flags keyword specifies the minimal flags that are required on any array passed in. This can be specified as a string of comma separated requirements, an integer indicating the requirement bits OR’d together, or a flags object returned from the flags attribute of an array with the necessary requirements.

Using an ndpointer class in the argtypes method can make it significantly safer to call a C function using ctypes and the data- area of an ndarray. You may still want to wrap the function in an additional Python wrapper to make it user-friendly (hiding some obvious arguments and making some arguments output arguments). In this process, the `requires` function in NumPy may be useful to return the right kind of array from a given input.

### Complete example[#](#complete-example "Link to this heading")

In this example, we will demonstrate how the addition function and the filter function implemented previously using the other approaches can be implemented using ctypes. First, the C code which implements the algorithms contains the functions `zadd`, `dadd`, `sadd`, `cadd`, and `dfilter2d`. The `zadd` function is:
    
    
    /* Add arrays of contiguous data */
    typedef struct {double real; double imag;} cdouble;
    typedef struct {float real; float imag;} cfloat;
    void zadd(cdouble *a, cdouble *b, cdouble *c, long n)
    {
        while (n--) {
            c->real = a->real + b->real;
            c->imag = a->imag + b->imag;
            a++; b++; c++;
        }
    }
    

with similar code for `cadd`, `dadd`, and `sadd` that handles complex float, double, and float data-types, respectively:
    
    
    void cadd(cfloat *a, cfloat *b, cfloat *c, long n)
    {
            while (n--) {
                    c->real = a->real + b->real;
                    c->imag = a->imag + b->imag;
                    a++; b++; c++;
            }
    }
    void dadd(double *a, double *b, double *c, long n)
    {
            while (n--) {
                    *c++ = *a++ + *b++;
            }
    }
    void sadd(float *a, float *b, float *c, long n)
    {
            while (n--) {
                    *c++ = *a++ + *b++;
            }
    }
    

The `code.c` file also contains the function `dfilter2d`:
    
    
    /*
     * Assumes b is contiguous and has strides that are multiples of
     * sizeof(double)
     */
    void
    dfilter2d(double *a, double *b, ssize_t *astrides, ssize_t *dims)
    {
        ssize_t i, j, M, N, S0, S1;
        ssize_t r, c, rm1, rp1, cp1, cm1;
    
        M = dims[0]; N = dims[1];
        S0 = astrides[0]/sizeof(double);
        S1 = astrides[1]/sizeof(double);
        for (i = 1; i < M - 1; i++) {
            r = i*S0;
            rp1 = r + S0;
            rm1 = r - S0;
            for (j = 1; j < N - 1; j++) {
                c = j*S1;
                cp1 = j + S1;
                cm1 = j - S1;
                b[i*N + j] = a[r + c] +
                    (a[rp1 + c] + a[rm1 + c] +
                     a[r + cp1] + a[r + cm1])*0.5 +
                    (a[rp1 + cp1] + a[rp1 + cm1] +
                     a[rm1 + cp1] + a[rm1 + cp1])*0.25;
            }
        }
    }
    

A possible advantage this code has over the Fortran-equivalent code is that it takes arbitrarily strided (i.e. non-contiguous arrays) and may also run faster depending on the optimization capability of your compiler. But, it is an obviously more complicated than the simple code in `filter.f`. This code must be compiled into a shared library. On my Linux system this is accomplished using:
    
    
    gcc -o code.so -shared code.c
    

Which creates a shared_library named code.so in the current directory. On Windows don’t forget to either add `__declspec(dllexport)` in front of void on the line preceding each function definition, or write a `code.def` file that lists the names of the functions to be exported.

A suitable Python interface to this shared library should be constructed. To do this create a file named interface.py with the following lines at the top:
    
    
    __all__ = ['add', 'filter2d']
    
    import numpy as np
    import os
    
    _path = os.path.dirname('__file__')
    lib = np.ctypeslib.load_library('code', _path)
    _typedict = {'zadd' : complex, 'sadd' : np.single,
                 'cadd' : np.csingle, 'dadd' : float}
    for name in _typedict.keys():
        val = getattr(lib, name)
        val.restype = None
        _type = _typedict[name]
        val.argtypes = [np.ctypeslib.ndpointer(_type,
                          flags='aligned, contiguous'),
                        np.ctypeslib.ndpointer(_type,
                          flags='aligned, contiguous'),
                        np.ctypeslib.ndpointer(_type,
                          flags='aligned, contiguous,'\
                                'writeable'),
                        np.ctypeslib.c_intp]
    

This code loads the shared library named `code.{ext}` located in the same path as this file. It then adds a return type of void to the functions contained in the library. It also adds argument checking to the functions in the library so that ndarrays can be passed as the first three arguments along with an integer (large enough to hold a pointer on the platform) as the fourth argument.

Setting up the filtering function is similar and allows the filtering function to be called with ndarray arguments as the first two arguments and with pointers to integers (large enough to handle the strides and shape of an ndarray) as the last two arguments.:
    
    
    lib.dfilter2d.restype=None
    lib.dfilter2d.argtypes = [np.ctypeslib.ndpointer(float, ndim=2,
                                           flags='aligned'),
                              np.ctypeslib.ndpointer(float, ndim=2,
                                     flags='aligned, contiguous,'\
                                           'writeable'),
                              ctypes.POINTER(np.ctypeslib.c_intp),
                              ctypes.POINTER(np.ctypeslib.c_intp)]
    

Next, define a simple selection function that chooses which addition function to call in the shared library based on the data-type:
    
    
    def select(dtype):
        if dtype.char in ['?bBhHf']:
            return lib.sadd, single
        elif dtype.char in ['F']:
            return lib.cadd, csingle
        elif dtype.char in ['DG']:
            return lib.zadd, complex
        else:
            return lib.dadd, float
        return func, ntype
    

Finally, the two functions to be exported by the interface can be written simply as:
    
    
    def add(a, b):
        requires = ['CONTIGUOUS', 'ALIGNED']
        a = np.asanyarray(a)
        func, dtype = select(a.dtype)
        a = np.require(a, dtype, requires)
        b = np.require(b, dtype, requires)
        c = np.empty_like(a)
        func(a,b,c,a.size)
        return c
    

and:
    
    
    def filter2d(a):
        a = np.require(a, float, ['ALIGNED'])
        b = np.zeros_like(a)
        lib.dfilter2d(a, b, a.ctypes.strides, a.ctypes.shape)
        return b
    

### Conclusion[#](#id4 "Link to this heading")

Using ctypes is a powerful way to connect Python with arbitrary C-code. Its advantages for extending Python include

  * clean separation of C code from Python code

  * no need to learn a new syntax except Python and C

  * allows reuse of C code

  * functionality in shared libraries written for other purposes can be obtained with a simple Python wrapper and search for the library.

  * easy integration with NumPy through the ctypes attribute

  * full argument checking with the ndpointer class factory




Its disadvantages include

  * It is difficult to distribute an extension module made using ctypes because of a lack of support for building shared libraries in distutils.

  * You must have shared-libraries of your code (no static libraries).

  * Very little support for C++ code and its different library-calling conventions. You will probably need a C wrapper around C++ code to use with ctypes (or just use Boost.Python instead).




Because of the difficulty in distributing an extension module made using ctypes, f2py and Cython are still the easiest ways to extend Python for package creation. However, ctypes is in some cases a useful alternative. This should bring more features to ctypes that should eliminate the difficulty in extending Python and distributing the extension using ctypes.

## Additional tools you may find useful[#](#additional-tools-you-may-find-useful "Link to this heading")

These tools have been found useful by others using Python and so are included here. They are discussed separately because they are either older ways to do things now handled by f2py, Cython, or ctypes (SWIG, PyFort) or because of a lack of reasonable documentation (SIP, Boost). Links to these methods are not included since the most relevant can be found using Google or some other search engine, and any links provided here would be quickly dated. Do not assume that inclusion in this list means that the package deserves attention. Information about these packages are collected here because many people have found them useful and we’d like to give you as many options as possible for tackling the problem of easily integrating your code.

### SWIG[#](#swig "Link to this heading")

Simplified Wrapper and Interface Generator (SWIG) is an old and fairly stable method for wrapping C/C++-libraries to a large variety of other languages. It does not specifically understand NumPy arrays but can be made usable with NumPy through the use of typemaps. There are some sample typemaps in the numpy/tools/swig directory under numpy.i together with an example module that makes use of them. SWIG excels at wrapping large C/C++ libraries because it can (almost) parse their headers and auto-produce an interface. Technically, you need to generate a `.i` file that defines the interface. Often, however, this `.i` file can be parts of the header itself. The interface usually needs a bit of tweaking to be very useful. This ability to parse C/C++ headers and auto-generate the interface still makes SWIG a useful approach to adding functionality from C/C++ into Python, despite the other methods that have emerged that are more targeted to Python. SWIG can actually target extensions for several languages, but the typemaps usually have to be language-specific. Nonetheless, with modifications to the Python-specific typemaps, SWIG can be used to interface a library with other languages such as Perl, Tcl, and Ruby.

My experience with SWIG has been generally positive in that it is relatively easy to use and quite powerful. It has been used often before becoming more proficient at writing C-extensions. However, writing custom interfaces with SWIG is often troublesome because it must be done using the concept of typemaps which are not Python specific and are written in a C-like syntax. Therefore, other gluing strategies are preferred and SWIG would be probably considered only to wrap a very-large C/C++ library. Nonetheless, there are others who use SWIG quite happily.

### SIP[#](#sip "Link to this heading")

SIP is another tool for wrapping C/C++ libraries that is Python specific and appears to have very good support for C++. Riverbank Computing developed SIP in order to create Python bindings to the QT library. An interface file must be written to generate the binding, but the interface file looks a lot like a C/C++ header file. While SIP is not a full C++ parser, it understands quite a bit of C++ syntax as well as its own special directives that allow modification of how the Python binding is accomplished. It also allows the user to define mappings between Python types and C/C++ structures and classes.

### Boost Python[#](#boost-python "Link to this heading")

Boost is a repository of C++ libraries and Boost.Python is one of those libraries which provides a concise interface for binding C++ classes and functions to Python. The amazing part of the Boost.Python approach is that it works entirely in pure C++ without introducing a new syntax. Many users of C++ report that Boost.Python makes it possible to combine the best of both worlds in a seamless fashion. Using Boost to wrap simple C-subroutines is usually over-kill. Its primary purpose is to make C++ classes available in Python. So, if you have a set of C++ classes that need to be integrated cleanly into Python, consider learning about and using Boost.Python.

### Pyfort[#](#pyfort "Link to this heading")

Pyfort is a nice tool for wrapping Fortran and Fortran-like C-code into Python with support for Numeric arrays. It was written by Paul Dubois, a distinguished computer scientist and the very first maintainer of Numeric (now retired). It is worth mentioning in the hopes that somebody will update PyFort to work with NumPy arrays as well which now support either Fortran or C-style contiguous arrays.

[ __ previous How to extend NumPy ](c-info.how-to-extend.html "previous page") [ next Writing your own ufunc __](c-info.ufunc-tutorial.html "next page")

__On this page

  * [Calling other compiled libraries from Python](#calling-other-compiled-libraries-from-python)
  * [Hand-generated wrappers](#hand-generated-wrappers)
  * [F2PY](#f2py)
  * [Cython](#cython)
    * [Complex addition in Cython](#complex-addition-in-cython)
    * [Image filter in Cython](#image-filter-in-cython)
    * [Conclusion](#conclusion)
  * [ctypes](#index-2)
    * [Having a shared library](#having-a-shared-library)
    * [Loading the shared library](#loading-the-shared-library)
    * [Converting arguments](#converting-arguments)
    * [Calling the function](#calling-the-function)
      * [`ndpointer`](#ndpointer)
    * [Complete example](#complete-example)
    * [Conclusion](#id4)
  * [Additional tools you may find useful](#additional-tools-you-may-find-useful)
    * [SWIG](#swig)
    * [SIP](#sip)
    * [Boost Python](#boost-python)
    * [Pyfort](#pyfort)

---

## Writing your own ufunc

**Source:** [https://numpy.org/devdocs/user/c-info.ufunc-tutorial.html](https://numpy.org/devdocs/user/c-info.ufunc-tutorial.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Using NumPy C-API](c-info.html)
  * Writing your own ufunc



# Writing your own ufunc[#](#writing-your-own-ufunc "Link to this heading")

I have the Power!

— _He-Man_

## Creating a new universal function[#](#creating-a-new-universal-function "Link to this heading")

Before reading this, it may help to familiarize yourself with the basics of C extensions for Python by reading/skimming the tutorials in Section 1 of [Extending and Embedding the Python Interpreter](https://docs.python.org/extending/index.html) and in [How to extend NumPy](c-info.how-to-extend.html)

The umath module is a computer-generated C-module that creates many ufuncs. It provides a great many examples of how to create a universal function. Creating your own ufunc that will make use of the ufunc machinery is not difficult either. Suppose you have a function that you want to operate element-by-element over its inputs. By creating a new ufunc you will obtain a function that handles

  * broadcasting

  * N-dimensional looping

  * automatic type-conversions with minimal memory usage

  * optional output arrays




It is not difficult to create your own ufunc. All that is required is a 1-d loop for each data-type you want to support. Each 1-d loop must have a specific signature, and only ufuncs for fixed-size data-types can be used. The function call used to create a new ufunc to work on built-in data-types is given below. A different mechanism is used to register ufuncs for user-defined data-types.

In the next several sections we give example code that can be easily modified to create your own ufuncs. The examples are successively more complete or complicated versions of the logit function, a common function in statistical modeling. Logit is also interesting because, due to the magic of IEEE standards (specifically IEEE 754), all of the logit functions created below automatically have the following behavior.
    
    
    >>> logit(0)
    -inf
    >>> logit(1)
    inf
    >>> logit(2)
    nan
    >>> logit(-2)
    nan
    

This is wonderful because the function writer doesn’t have to manually propagate infs or nans.

## Example non-ufunc extension[#](#example-non-ufunc-extension "Link to this heading")

For comparison and general edification of the reader we provide a simple implementation of a C extension of `logit` that uses no numpy.

To do this we need three files. The first is the C file which contains the actual code, and the others are two project files that describe how to create the module.

> 
>     #define PY_SSIZE_T_CLEAN
>     #include <Python.h>
>     #include <math.h>
>     
>     /*
>      * spammodule.c
>      * This is the C code for a non-numpy Python extension to
>      * define the logit function, where logit(p) = log(p/(1-p)).
>      * This function will not work on numpy arrays automatically.
>      * numpy.vectorize must be called in python to generate
>      * a numpy-friendly function.
>      *
>      * Details explaining the Python-C API can be found under
>      * 'Extending and Embedding' and 'Python/C API' at
>      * docs.python.org .
>      */
>     
>     
>     /* This declares the logit function */
>     static PyObject *spam_logit(PyObject *self, PyObject *args);
>     
>     /*
>      * This tells Python what methods this module has.
>      * See the Python-C API for more information.
>      */
>     static PyMethodDef SpamMethods[] = {
>         {"logit",
>             spam_logit,
>             METH_VARARGS, "compute logit"},
>         {NULL, NULL, 0, NULL}
>     };
>     
>     /*
>      * This actually defines the logit function for
>      * input args from Python.
>      */
>     
>     static PyObject *spam_logit(PyObject *self, PyObject *args)
>     {
>         double p;
>     
>         /* This parses the Python argument into a double */
>         if(!PyArg_ParseTuple(args, "d", &p)) {
>             return NULL;
>         }
>     
>         /* THE ACTUAL LOGIT FUNCTION */
>         p = p/(1-p);
>         p = log(p);
>     
>         /*This builds the answer back into a python object */
>         return Py_BuildValue("d", p);
>     }
>     
>     /* This initiates the module using the above definitions. */
>     static struct PyModuleDef moduledef = {
>         PyModuleDef_HEAD_INIT,
>         "spam",
>         NULL,
>         -1,
>         SpamMethods,
>         NULL,
>         NULL,
>         NULL,
>         NULL
>     };
>     
>     PyMODINIT_FUNC PyInit_spam(void)
>     {
>         PyObject *m;
>         m = PyModule_Create(&moduledef);
>         if (!m) {
>             return NULL;
>         }
>         return m;
>     }
>     

To create the module, one proceeds as one would for a Python package, creating a `pyproject.toml` file, which defines a build back-end, and then another file for that backend which describes how to compile the code. For the backend, we recommend `meson-python`, as we use it for numpy itself, but below we also show how to use the older `setuptools`.

meson

Sample `pyproject.toml` and `meson.build`.
    
    
    [project]
    name = "spam"
    version = "0.1"
    
    [build-system]
    requires = ["meson-python"]
    build-backend = "mesonpy"
    
    
    
    project('spam', 'c')
    
    py = import('python').find_installation()
    
    sources = files('spammodule.c')
    
    extension_module = py.extension_module(
      'spam',
      sources,
      install: true,
    )
    

setuptools

Sample `pyproject.toml` and `setup.py`.
    
    
    [project]
    name = "spam"
    version = "0.1"
    
    [build-system]
    requires = ["setuptools"]
    build-backend = "setuptools.build_meta"
    
    
    
    from setuptools import setup, Extension
    
    spammodule = Extension('spam', sources=['spammodule.c'])
    
    setup(name='spam', version='1.0',
          ext_modules=[spammodule])
    

With either of the above, one can build and install the `spam` package with,
    
    
    pip install .
    

Once the `spam` module is imported into python, you can call logit via `spam.logit`. Note that the function used above cannot be applied as-is to numpy arrays. To do so we must call [`numpy.vectorize`](../reference/generated/numpy.vectorize.html#numpy.vectorize "numpy.vectorize") on it. For example:
    
    
    >>> import numpy as np
    >>> import spam
    >>> spam.logit(0)
    -inf
    >>> spam.logit(1)
    inf
    >>> spam.logit(0.5)
    0.0
    >>> x = np.linspace(0,1,10)
    >>> spam.logit(x)
    TypeError: only length-1 arrays can be converted to Python scalars
    >>> f = np.vectorize(spam.logit)
    >>> f(x)
    array([       -inf, -2.07944154, -1.25276297, -0.69314718, -0.22314355,
        0.22314355,  0.69314718,  1.25276297,  2.07944154,         inf])
    

THE RESULTING LOGIT FUNCTION IS NOT FAST! `numpy.vectorize` simply loops over `spam.logit`. The loop is done at the C level, but the numpy array is constantly being parsed and build back up. This is expensive. When the author compared `numpy.vectorize(spam.logit)` against the logit ufuncs constructed below, the logit ufuncs were almost exactly 4 times faster. Larger or smaller speedups are, of course, possible depending on the nature of the function.

## Example NumPy ufunc for one dtype[#](#example-numpy-ufunc-for-one-dtype "Link to this heading")

For simplicity we give a ufunc for a single dtype, the `'f8'` `double`. As in the previous section, we first give the `.c` file and then the files used to create a `npufunc` module containing the ufunc.

The place in the code corresponding to the actual computations for the ufunc are marked with `/* BEGIN main ufunc computation */` and `/* END main ufunc computation */`. The code in between those lines is the primary thing that must be changed to create your own ufunc.

> 
>     #define PY_SSIZE_T_CLEAN
>     #include <Python.h>
>     #include "numpy/ndarraytypes.h"
>     #include "numpy/ufuncobject.h"
>     #include "numpy/npy_3kcompat.h"
>     #include <math.h>
>     
>     /*
>      * single_type_logit.c
>      * This is the C code for creating your own
>      * NumPy ufunc for a logit function.
>      *
>      * In this code we only define the ufunc for
>      * a single dtype. The computations that must
>      * be replaced to create a ufunc for
>      * a different function are marked with BEGIN
>      * and END.
>      *
>      * Details explaining the Python-C API can be found under
>      * 'Extending and Embedding' and 'Python/C API' at
>      * docs.python.org .
>      */
>     
>     static PyMethodDef LogitMethods[] = {
>         {NULL, NULL, 0, NULL}
>     };
>     
>     /* The loop definition must precede the PyMODINIT_FUNC. */
>     
>     static void double_logit(char **args, const npy_intp *dimensions,
>                              const npy_intp *steps, void *data)
>     {
>         npy_intp i;
>         npy_intp n = dimensions[0];
>         char *in = args[0], *out = args[1];
>         npy_intp in_step = steps[0], out_step = steps[1];
>     
>         double tmp;
>     
>         for (i = 0; i < n; i++) {
>             /* BEGIN main ufunc computation */
>             tmp = *(double *)in;
>             tmp /= 1 - tmp;
>             *((double *)out) = log(tmp);
>             /* END main ufunc computation */
>     
>             in += in_step;
>             out += out_step;
>         }
>     }
>     
>     /* This a pointer to the above function */
>     PyUFuncGenericFunction funcs[1] = {&double_logit};
>     
>     /* These are the input and return dtypes of logit.*/
>     static const char types[2] = {NPY_DOUBLE, NPY_DOUBLE};
>     
>     static struct PyModuleDef moduledef = {
>         PyModuleDef_HEAD_INIT,
>         "npufunc",
>         NULL,
>         -1,
>         LogitMethods,
>         NULL,
>         NULL,
>         NULL,
>         NULL
>     };
>     
>     PyMODINIT_FUNC PyInit_npufunc(void)
>     {
>         PyObject *m, *logit, *d;
>     
>         import_array();
>         import_umath();
>     
>         m = PyModule_Create(&moduledef);
>         if (!m) {
>             return NULL;
>         }
>     
>         logit = PyUFunc_FromFuncAndData(funcs, NULL, types, 1, 1, 1,
>                                         PyUFunc_None, "logit",
>                                         "logit_docstring", 0);
>     
>         d = PyModule_GetDict(m);
>     
>         PyDict_SetItemString(d, "logit", logit);
>         Py_DECREF(logit);
>     
>         return m;
>     }
>     

For the files needed to create the module, the main difference from our previous example is that we now need to declare dependencies on numpy.

meson

Sample `pyproject.toml` and `meson.build`.
    
    
    [project]
    name = "npufunc"
    dependencies = ["numpy"]
    version = "0.1"
    
    [build-system]
    requires = ["meson-python", "numpy"]
    build-backend = "mesonpy"
    
    
    
    project('npufunc', 'c')
    
    py = import('python').find_installation()
    np_dep = dependency('numpy')
    
    sources = files('single_type_logit.c')
    
    extension_module = py.extension_module(
      'npufunc',
      sources,
      dependencies: [np_dep],
      install: true,
    )
    

setuptools

Sample `pyproject.toml` and `setup.py`.
    
    
    [project]
    name = "npufunc"
    dependencies = ["numpy"]
    version = "0.1"
    
    [build-system]
    requires = ["setuptools", "numpy"]
    build-backend = "setuptools.build_meta"
    
    
    
    from setuptools import setup, Extension
    from numpy import get_include
    
    npufunc = Extension('npufunc',
                        sources=['single_type_logit.c'],
                        include_dirs=[get_include()])
    
    setup(name='npufunc', version='1.0', ext_modules=[npufunc])
    

After the above has been installed, it can be imported and used as follows:
    
    
    >>> import numpy as np
    >>> import npufunc
    >>> npufunc.logit(0.5)
    np.float64(0.0)
    >>> a = np.linspace(0, 1, 5)
    >>> npufunc.logit(a)
    array([       -inf, -1.09861229,  0.        ,  1.09861229,         inf])
    

## Example NumPy ufunc with multiple dtypes[#](#example-numpy-ufunc-with-multiple-dtypes "Link to this heading")

We now extend the above to a full `logit` ufunc, with inner loops for floats, doubles, and long doubles. Here, we can use the same build files as above, except we need to change the source file from `single_type_logit.c` to `multi_type_logit.c`.

The places in the code corresponding to the actual computations for the ufunc are marked with `/* BEGIN main ufunc computation */` and `/* END main ufunc computation */`. The code in between those lines is the primary thing that must be changed to create your own ufunc.

> 
>     #define PY_SSIZE_T_CLEAN
>     #include <Python.h>
>     #include "numpy/ndarraytypes.h"
>     #include "numpy/ufuncobject.h"
>     #include <math.h>
>     
>     /*
>      * multi_type_logit.c
>      * This is the C code for creating your own
>      * NumPy ufunc for a logit function.
>      *
>      * Each function of the form type_logit defines the
>      * logit function for a different numpy dtype. Each
>      * of these functions must be modified when you
>      * create your own ufunc. The computations that must
>      * be replaced to create a ufunc for
>      * a different function are marked with BEGIN
>      * and END.
>      *
>      * Details explaining the Python-C API can be found under
>      * 'Extending and Embedding' and 'Python/C API' at
>      * docs.python.org .
>      *
>      */
>     
>     static PyMethodDef LogitMethods[] = {
>         {NULL, NULL, 0, NULL}
>     };
>     
>     /* The loop definitions must precede the PyMODINIT_FUNC. */
>     
>     static void long_double_logit(char **args, const npy_intp *dimensions,
>                                   const npy_intp *steps, void *data)
>     {
>         npy_intp i;
>         npy_intp n = dimensions[0];
>         char *in = args[0], *out = args[1];
>         npy_intp in_step = steps[0], out_step = steps[1];
>     
>         long double tmp;
>     
>         for (i = 0; i < n; i++) {
>             /* BEGIN main ufunc computation */
>             tmp = *(long double *)in;
>             tmp /= 1 - tmp;
>             *((long double *)out) = logl(tmp);
>             /* END main ufunc computation */
>     
>             in += in_step;
>             out += out_step;
>         }
>     }
>     
>     static void double_logit(char **args, const npy_intp *dimensions,
>                              const npy_intp *steps, void *data)
>     {
>         npy_intp i;
>         npy_intp n = dimensions[0];
>         char *in = args[0], *out = args[1];
>         npy_intp in_step = steps[0], out_step = steps[1];
>     
>         double tmp;
>     
>         for (i = 0; i < n; i++) {
>             /* BEGIN main ufunc computation */
>             tmp = *(double *)in;
>             tmp /= 1 - tmp;
>             *((double *)out) = log(tmp);
>             /* END main ufunc computation */
>     
>             in += in_step;
>             out += out_step;
>         }
>     }
>     
>     static void float_logit(char **args, const npy_intp *dimensions,
>                            const npy_intp *steps, void *data)
>     {
>         npy_intp i;
>         npy_intp n = dimensions[0];
>         char *in = args[0], *out = args[1];
>         npy_intp in_step = steps[0], out_step = steps[1];
>     
>         float tmp;
>     
>         for (i = 0; i < n; i++) {
>             /* BEGIN main ufunc computation */
>             tmp = *(float *)in;
>             tmp /= 1 - tmp;
>             *((float *)out) = logf(tmp);
>             /* END main ufunc computation */
>     
>             in += in_step;
>             out += out_step;
>         }
>     }
>     
>     
>     
>     /*This gives pointers to the above functions*/
>     PyUFuncGenericFunction funcs[3] = {&float_logit,
>                                        &double_logit,
>                                        &long_double_logit};
>     
>     static const char types[6] = {NPY_FLOAT, NPY_FLOAT,
>                                   NPY_DOUBLE, NPY_DOUBLE,
>                                   NPY_LONGDOUBLE, NPY_LONGDOUBLE};
>     
>     static struct PyModuleDef moduledef = {
>         PyModuleDef_HEAD_INIT,
>         "npufunc",
>         NULL,
>         -1,
>         LogitMethods,
>         NULL,
>         NULL,
>         NULL,
>         NULL
>     };
>     
>     PyMODINIT_FUNC PyInit_npufunc(void)
>     {
>         PyObject *m, *logit, *d;
>     
>         import_array();
>         import_umath();
>     
>         m = PyModule_Create(&moduledef);
>         if (!m) {
>             return NULL;
>         }
>     
>         logit = PyUFunc_FromFuncAndData(funcs, NULL, types, 4, 1, 1,
>                                         PyUFunc_None, "logit",
>                                         "logit_docstring", 0);
>     
>         d = PyModule_GetDict(m);
>     
>         PyDict_SetItemString(d, "logit", logit);
>         Py_DECREF(logit);
>     
>         return m;
>     }
>     

After the above has been installed, it can be imported and used as follows.
    
    
    >>> import numpy as np
    >>> import npufunc
    >>> npufunc.logit(0.5)
    np.float64(0.0)
    >>> a = np.linspace(0, 1, 5, dtype=np.float32)
    >>> npufunc.logit(a)
    <python-input-4>:1: RuntimeWarning: divide by zero encountered in logit
    array([      -inf, -1.0986123,  0.       ,  1.0986123,        inf],
          dtype=float32)
    

Note

Supporting `float16` (half-precision) in custom ufuncs is more complex due to its non-standard C representation and conversion requirements. The above code can process `float16` input, but will do so by converting it to `float32`. The result will then be `float32` too, but one can convert it back to `float16` by passing in a suitable output, as in `npufunc.logit(a, out=np.empty_like(a))`. For examples of actual `float16` loops, see the numpy source code.

## Example NumPy ufunc with multiple arguments/return values[#](#example-numpy-ufunc-with-multiple-arguments-return-values "Link to this heading")

Creating a ufunc with multiple arguments is not difficult. Here, we make a modification of the code for a logit ufunc, where we compute `(A * B, logit(A * B))`. For simplicity, we only create a loop for doubles.

We again only give the C code as the files needed to create the module are the same as before, but with the source file name replaced by `multi_arg_logit.c`.

The C file is given below. The ufunc generated takes two arguments `A` and `B`. It returns a tuple whose first element is `A * B` and whose second element is `logit(A * B)`. Note that it automatically supports broadcasting, as well as all other properties of a ufunc.

> 
>     #define PY_SSIZE_T_CLEAN
>     #include <Python.h>
>     #include "numpy/ndarraytypes.h"
>     #include "numpy/ufuncobject.h"
>     #include <math.h>
>     
>     /*
>      * multi_arg_logit.c
>      * This is the C code for creating your own
>      * NumPy ufunc for a multiple argument, multiple
>      * return value ufunc. The places where the
>      * ufunc computation is carried out are marked
>      * with comments.
>      *
>      * Details explaining the Python-C API can be found under
>      * 'Extending and Embedding' and 'Python/C API' at
>      * docs.python.org.
>      */
>     
>     static PyMethodDef LogitMethods[] = {
>         {NULL, NULL, 0, NULL}
>     };
>     
>     /* The loop definition must precede the PyMODINIT_FUNC. */
>     
>     static void double_logitprod(char **args, const npy_intp *dimensions,
>                                  const npy_intp *steps, void *data)
>     {
>         npy_intp i;
>         npy_intp n = dimensions[0];
>         char *in1 = args[0], *in2 = args[1];
>         char *out1 = args[2], *out2 = args[3];
>         npy_intp in1_step = steps[0], in2_step = steps[1];
>         npy_intp out1_step = steps[2], out2_step = steps[3];
>     
>         double tmp;
>     
>         for (i = 0; i < n; i++) {
>             /* BEGIN main ufunc computation */
>             tmp = *(double *)in1;
>             tmp *= *(double *)in2;
>             *((double *)out1) = tmp;
>             *((double *)out2) = log(tmp / (1 - tmp));
>             /* END main ufunc computation */
>     
>             in1 += in1_step;
>             in2 += in2_step;
>             out1 += out1_step;
>             out2 += out2_step;
>         }
>     }
>     
>     /*This a pointer to the above function*/
>     PyUFuncGenericFunction funcs[1] = {&double_logitprod};
>     
>     /* These are the input and return dtypes of logit.*/
>     
>     static const char types[4] = {NPY_DOUBLE, NPY_DOUBLE,
>                                   NPY_DOUBLE, NPY_DOUBLE};
>     
>     static struct PyModuleDef moduledef = {
>         PyModuleDef_HEAD_INIT,
>         "npufunc",
>         NULL,
>         -1,
>         LogitMethods,
>         NULL,
>         NULL,
>         NULL,
>         NULL
>     };
>     
>     PyMODINIT_FUNC PyInit_npufunc(void)
>     {
>         PyObject *m, *logit, *d;
>     
>         import_array();
>         import_umath();
>     
>         m = PyModule_Create(&moduledef);
>         if (!m) {
>             return NULL;
>         }
>     
>         logit = PyUFunc_FromFuncAndData(funcs, NULL, types, 1, 2, 2,
>                                         PyUFunc_None, "logit",
>                                         "logit_docstring", 0);
>     
>         d = PyModule_GetDict(m);
>     
>         PyDict_SetItemString(d, "logit", logit);
>         Py_DECREF(logit);
>     
>         return m;
>     }
>     

## Example NumPy ufunc with structured array dtype arguments[#](#example-numpy-ufunc-with-structured-array-dtype-arguments "Link to this heading")

This example shows how to create a ufunc for a structured array dtype. For the example we show a trivial ufunc for adding two arrays with dtype `'u8,u8,u8'`. The process is a bit different from the other examples since a call to [`PyUFunc_FromFuncAndData`](../reference/c-api/ufunc.html#c.PyUFunc_FromFuncAndData "PyUFunc_FromFuncAndData") cannot register ufuncs for custom dtypes and structured array dtypes. We need to also call [`PyUFunc_RegisterLoopForDescr`](../reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForDescr "PyUFunc_RegisterLoopForDescr") to finish setting up the ufunc.

We only give the C code as the files needed to construct the module are again exactly the same as before, except that the source file is now `add_triplet.c`.

> 
>     #define PY_SSIZE_T_CLEAN
>     #include <Python.h>
>     #include "numpy/ndarraytypes.h"
>     #include "numpy/ufuncobject.h"
>     #include "numpy/npy_3kcompat.h"
>     #include <math.h>
>     
>     /*
>      * add_triplet.c
>      * This is the C code for creating your own
>      * NumPy ufunc for a structured array dtype.
>      *
>      * Details explaining the Python-C API can be found under
>      * 'Extending and Embedding' and 'Python/C API' at
>      * docs.python.org.
>      */
>     
>     static PyMethodDef StructUfuncTestMethods[] = {
>         {NULL, NULL, 0, NULL}
>     };
>     
>     /* The loop definition must precede the PyMODINIT_FUNC. */
>     
>     static void add_uint64_triplet(char **args, const npy_intp *dimensions,
>                                    const npy_intp *steps, void *data)
>     {
>         npy_intp i;
>         npy_intp is1 = steps[0];
>         npy_intp is2 = steps[1];
>         npy_intp os = steps[2];
>         npy_intp n = dimensions[0];
>         uint64_t *x, *y, *z;
>     
>         char *i1 = args[0];
>         char *i2 = args[1];
>         char *op = args[2];
>     
>         for (i = 0; i < n; i++) {
>     
>             x = (uint64_t *)i1;
>             y = (uint64_t *)i2;
>             z = (uint64_t *)op;
>     
>             z[0] = x[0] + y[0];
>             z[1] = x[1] + y[1];
>             z[2] = x[2] + y[2];
>     
>             i1 += is1;
>             i2 += is2;
>             op += os;
>         }
>     }
>     
>     static struct PyModuleDef moduledef = {
>         PyModuleDef_HEAD_INIT,
>         "npufunc",
>         NULL,
>         -1,
>         StructUfuncTestMethods,
>         NULL,
>         NULL,
>         NULL,
>         NULL
>     };
>     
>     PyMODINIT_FUNC PyInit_npufunc(void)
>     {
>         PyObject *m, *add_triplet, *d;
>         PyObject *dtype_dict;
>         PyArray_Descr *dtype;
>         PyArray_Descr *dtypes[3];
>     
>         import_array();
>         import_umath();
>     
>         m = PyModule_Create(&moduledef);
>         if (m == NULL) {
>             return NULL;
>         }
>     
>         /* Create a new ufunc object */
>         add_triplet = PyUFunc_FromFuncAndData(NULL, NULL, NULL, 0, 2, 1,
>                                               PyUFunc_None, "add_triplet",
>                                               "add_triplet_docstring", 0);
>     
>         dtype_dict = Py_BuildValue("[(s, s), (s, s), (s, s)]",
>                                    "f0", "u8", "f1", "u8", "f2", "u8");
>         PyArray_DescrConverter(dtype_dict, &dtype);
>         Py_DECREF(dtype_dict);
>     
>         dtypes[0] = dtype;
>         dtypes[1] = dtype;
>         dtypes[2] = dtype;
>     
>         /* Register ufunc for structured dtype */
>         PyUFunc_RegisterLoopForDescr((PyUFuncObject *)add_triplet,
>                                      dtype,
>                                      &add_uint64_triplet,
>                                      dtypes,
>                                      NULL);
>     
>         d = PyModule_GetDict(m);
>     
>         PyDict_SetItemString(d, "add_triplet", add_triplet);
>         Py_DECREF(add_triplet);
>         return m;
>     }
>     

Sample usage:
    
    
    >>> import npufunc
    >>> import numpy as np
    >>> a = np.array([(1, 2, 3), (4, 5, 6)], "u8,u8,u8")
    >>> npufunc.add_triplet(a, a)
    array([(2,  4,  6), (8, 10, 12)],
          dtype=[('f0', '<u8'), ('f1', '<u8'), ('f2', '<u8')])
    

[ __ previous Using Python as glue ](c-info.python-as-glue.html "previous page") [ next Beyond the basics __](c-info.beyond-basics.html "next page")

__On this page

  * [Creating a new universal function](#creating-a-new-universal-function)
  * [Example non-ufunc extension](#example-non-ufunc-extension)
  * [Example NumPy ufunc for one dtype](#example-numpy-ufunc-for-one-dtype)
  * [Example NumPy ufunc with multiple dtypes](#example-numpy-ufunc-with-multiple-dtypes)
  * [Example NumPy ufunc with multiple arguments/return values](#example-numpy-ufunc-with-multiple-arguments-return-values)
  * [Example NumPy ufunc with structured array dtype arguments](#example-numpy-ufunc-with-structured-array-dtype-arguments)

---

## Beyond the basics

**Source:** [https://numpy.org/devdocs/user/c-info.beyond-basics.html](https://numpy.org/devdocs/user/c-info.beyond-basics.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Using NumPy C-API](c-info.html)
  * Beyond the basics



# Beyond the basics[#](#beyond-the-basics "Link to this heading")

The voyage of discovery is not in seeking new landscapes but in having

new eyes.

— _Marcel Proust_

Discovery is seeing what everyone else has seen and thinking what no

one else has thought.

— _Albert Szent-Gyorgi_

## Iterating over elements in the array[#](#iterating-over-elements-in-the-array "Link to this heading")

### Basic iteration[#](#basic-iteration "Link to this heading")

One common algorithmic requirement is to be able to walk over all elements in a multidimensional array. The array iterator object makes this easy to do in a generic way that works for arrays of any dimension. Naturally, if you know the number of dimensions you will be using, then you can always write nested for loops to accomplish the iteration. If, however, you want to write code that works with any number of dimensions, then you can make use of the array iterator. An array iterator object is returned when accessing the .flat attribute of an array.

Basic usage is to call [`PyArray_IterNew`](../reference/c-api/array.html#c.PyArray_IterNew "PyArray_IterNew") ( `array` ) where array is an ndarray object (or one of its sub-classes). The returned object is an array-iterator object (the same object returned by the .flat attribute of the ndarray). This object is usually cast to PyArrayIterObject* so that its members can be accessed. The only members that are needed are `iter->size` which contains the total size of the array, `iter->index`, which contains the current 1-d index into the array, and `iter->dataptr` which is a pointer to the data for the current element of the array. Sometimes it is also useful to access `iter->ao` which is a pointer to the underlying ndarray object.

After processing data at the current element of the array, the next element of the array can be obtained using the macro [`PyArray_ITER_NEXT`](../reference/c-api/array.html#c.PyArray_ITER_NEXT "PyArray_ITER_NEXT") ( `iter` ). The iteration always proceeds in a C-style contiguous fashion (last index varying the fastest). The [`PyArray_ITER_GOTO`](../reference/c-api/array.html#c.PyArray_ITER_GOTO "PyArray_ITER_GOTO") ( `iter`, `destination` ) can be used to jump to a particular point in the array, where `destination` is an array of npy_intp data-type with space to handle at least the number of dimensions in the underlying array. Occasionally it is useful to use [`PyArray_ITER_GOTO1D`](../reference/c-api/array.html#c.PyArray_ITER_GOTO1D "PyArray_ITER_GOTO1D") ( `iter`, `index` ) which will jump to the 1-d index given by the value of `index`. The most common usage, however, is given in the following example.
    
    
    PyObject *obj; /* assumed to be some ndarray object */
    PyArrayIterObject *iter;
    ...
    iter = (PyArrayIterObject *)PyArray_IterNew(obj);
    if (iter == NULL) goto fail;   /* Assume fail has clean-up code */
    while (iter->index < iter->size) {
        /* do something with the data at it->dataptr */
        PyArray_ITER_NEXT(it);
    }
    ...
    

You can also use [`PyArrayIter_Check`](../reference/c-api/array.html#c.PyArrayIter_Check "PyArrayIter_Check") ( `obj` ) to ensure you have an iterator object and [`PyArray_ITER_RESET`](../reference/c-api/array.html#c.PyArray_ITER_RESET "PyArray_ITER_RESET") ( `iter` ) to reset an iterator object back to the beginning of the array.

It should be emphasized at this point that you may not need the array iterator if your array is already contiguous (using an array iterator will work but will be slower than the fastest code you could write). The major purpose of array iterators is to encapsulate iteration over N-dimensional arrays with arbitrary strides. They are used in many, many places in the NumPy source code itself. If you already know your array is contiguous (Fortran or C), then simply adding the element- size to a running pointer variable will step you through the array very efficiently. In other words, code like this will probably be faster for you in the contiguous case (assuming doubles).
    
    
    npy_intp size;
    double *dptr;  /* could make this any variable type */
    size = PyArray_SIZE(obj);
    dptr = PyArray_DATA(obj);
    while(size--) {
       /* do something with the data at dptr */
       dptr++;
    }
    

### Iterating over all but one axis[#](#iterating-over-all-but-one-axis "Link to this heading")

A common algorithm is to loop over all elements of an array and perform some function with each element by issuing a function call. As function calls can be time consuming, one way to speed up this kind of algorithm is to write the function so it takes a vector of data and then write the iteration so the function call is performed for an entire dimension of data at a time. This increases the amount of work done per function call, thereby reducing the function-call over-head to a small(er) fraction of the total time. Even if the interior of the loop is performed without a function call it can be advantageous to perform the inner loop over the dimension with the highest number of elements to take advantage of speed enhancements available on micro- processors that use pipelining to enhance fundamental operations.

The [`PyArray_IterAllButAxis`](../reference/c-api/array.html#c.PyArray_IterAllButAxis "PyArray_IterAllButAxis") ( `array`, `&dim` ) constructs an iterator object that is modified so that it will not iterate over the dimension indicated by dim. The only restriction on this iterator object, is that the [`PyArray_ITER_GOTO1D`](../reference/c-api/array.html#c.PyArray_ITER_GOTO1D "PyArray_ITER_GOTO1D") ( `it`, `ind` ) macro cannot be used (thus flat indexing won’t work either if you pass this object back to Python — so you shouldn’t do this). Note that the returned object from this routine is still usually cast to PyArrayIterObject *. All that’s been done is to modify the strides and dimensions of the returned iterator to simulate iterating over array[…,0,…] where 0 is placed on the \\(\textrm{dim}^{\textrm{th}}\\) dimension. If dim is negative, then the dimension with the largest axis is found and used.

### Iterating over multiple arrays[#](#iterating-over-multiple-arrays "Link to this heading")

Very often, it is desirable to iterate over several arrays at the same time. The universal functions are an example of this kind of behavior. If all you want to do is iterate over arrays with the same shape, then simply creating several iterator objects is the standard procedure. For example, the following code iterates over two arrays assumed to be the same shape and size (actually obj1 just has to have at least as many total elements as does obj2):
    
    
    /* It is already assumed that obj1 and obj2
       are ndarrays of the same shape and size.
    */
    iter1 = (PyArrayIterObject *)PyArray_IterNew(obj1);
    if (iter1 == NULL) goto fail;
    iter2 = (PyArrayIterObject *)PyArray_IterNew(obj2);
    if (iter2 == NULL) goto fail;  /* assume iter1 is DECREF'd at fail */
    while (iter2->index < iter2->size)  {
        /* process with iter1->dataptr and iter2->dataptr */
        PyArray_ITER_NEXT(iter1);
        PyArray_ITER_NEXT(iter2);
    }
    

### Broadcasting over multiple arrays[#](#broadcasting-over-multiple-arrays "Link to this heading")

When multiple arrays are involved in an operation, you may want to use the same broadcasting rules that the math operations (_i.e._ the ufuncs) use. This can be done easily using the [`PyArrayMultiIterObject`](../reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject"). This is the object returned from the Python command numpy.broadcast and it is almost as easy to use from C. The function [`PyArray_MultiIterNew`](../reference/c-api/array.html#c.PyArray_MultiIterNew "PyArray_MultiIterNew") ( `n`, `...` ) is used (with `n` input objects in place of `...` ). The input objects can be arrays or anything that can be converted into an array. A pointer to a PyArrayMultiIterObject is returned. Broadcasting has already been accomplished which adjusts the iterators so that all that needs to be done to advance to the next element in each array is for PyArray_ITER_NEXT to be called for each of the inputs. This incrementing is automatically performed by [`PyArray_MultiIter_NEXT`](../reference/c-api/array.html#c.PyArray_MultiIter_NEXT "PyArray_MultiIter_NEXT") ( `obj` ) macro (which can handle a multiterator `obj` as either a [PyArrayMultiIterObject](../reference/c-api/types-and-structures.html#c.PyArrayMultiIterObject "PyArrayMultiIterObject")* or a [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "\(in Python v3.14\)")*). The data from input number `i` is available using [`PyArray_MultiIter_DATA`](../reference/c-api/array.html#c.PyArray_MultiIter_DATA "PyArray_MultiIter_DATA") ( `obj`, `i` ). An example of using this feature follows.
    
    
    mobj = PyArray_MultiIterNew(2, obj1, obj2);
    size = mobj->size;
    while(size--) {
        ptr1 = PyArray_MultiIter_DATA(mobj, 0);
        ptr2 = PyArray_MultiIter_DATA(mobj, 1);
        /* code using contents of ptr1 and ptr2 */
        PyArray_MultiIter_NEXT(mobj);
    }
    

The function [`PyArray_RemoveSmallest`](../reference/c-api/array.html#c.PyArray_RemoveSmallest "PyArray_RemoveSmallest") ( `multi` ) can be used to take a multi-iterator object and adjust all the iterators so that iteration does not take place over the largest dimension (it makes that dimension of size 1). The code being looped over that makes use of the pointers will very-likely also need the strides data for each of the iterators. This information is stored in multi->iters[i]->strides.

There are several examples of using the multi-iterator in the NumPy source code as it makes N-dimensional broadcasting-code very simple to write. Browse the source for more examples.

## User-defined data-types[#](#user-defined-data-types "Link to this heading")

NumPy comes with 24 builtin data-types. While this covers a large majority of possible use cases, it is conceivable that a user may have a need for an additional data-type. There is some support for adding an additional data-type into the NumPy system. This additional data- type will behave much like a regular data-type except ufuncs must have 1-d loops registered to handle it separately. Also checking for whether or not other data-types can be cast “safely” to and from this new type or not will always return “can cast” unless you also register which types your new data-type can be cast to and from.

The NumPy source code includes an example of a custom data-type as part of its test suite. The file `_rational_tests.c.src` in the source code directory `numpy/_core/src/umath/` contains an implementation of a data-type that represents a rational number as the ratio of two 32 bit integers.

### Adding the new data-type[#](#adding-the-new-data-type "Link to this heading")

To begin to make use of the new data-type, you need to first define a new Python type to hold the scalars of your new data-type. It should be acceptable to inherit from one of the array scalars if your new type has a binary compatible layout. This will allow your new data type to have the methods and attributes of array scalars. New data- types must have a fixed memory size (if you want to define a data-type that needs a flexible representation, like a variable-precision number, then use a pointer to the object as the data-type). The memory layout of the object structure for the new Python type must be PyObject_HEAD followed by the fixed-size memory needed for the data- type. For example, a suitable structure for the new Python type is:
    
    
    typedef struct {
       PyObject_HEAD;
       some_data_type obval;
       /* the name can be whatever you want */
    } PySomeDataTypeObject;
    

After you have defined a new Python type object, you must then define a new [`PyArray_Descr`](../reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr") structure whose typeobject member will contain a pointer to the data-type you’ve just defined. In addition, the required functions in the “.f” member must be defined: nonzero, copyswap, copyswapn, setitem, getitem, and cast. The more functions in the “.f” member you define, however, the more useful the new data-type will be. It is very important to initialize unused functions to NULL. This can be achieved using [`PyArray_InitArrFuncs`](../reference/c-api/array.html#c.PyArray_InitArrFuncs "PyArray_InitArrFuncs") (f).

Once a new [`PyArray_Descr`](../reference/c-api/types-and-structures.html#c.PyArray_Descr "PyArray_Descr") structure is created and filled with the needed information and useful functions you call [`PyArray_RegisterDataType`](../reference/c-api/array.html#c.PyArray_RegisterDataType "PyArray_RegisterDataType") (new_descr). The return value from this call is an integer providing you with a unique type_number that specifies your data-type. This type number should be stored and made available by your module so that other modules can use it to recognize your data-type.

Note that this API is inherently thread-unsafe. See [Thread Safety](../reference/thread_safety.html#thread-safety) for more details about thread safety in NumPy.

### Registering a casting function[#](#registering-a-casting-function "Link to this heading")

You may want to allow builtin (and other user-defined) data-types to be cast automatically to your data-type. In order to make this possible, you must register a casting function with the data-type you want to be able to cast from. This requires writing low-level casting functions for each conversion you want to support and then registering these functions with the data-type descriptor. A low-level casting function has the signature.

void castfunc(void *from, void *to, [npy_intp](../reference/c-api/dtype.html#c.npy_intp "npy_intp") n, void *fromarr, void *toarr)[#](#c.castfunc "Link to this definition")  

    

Cast `n` elements `from` one type `to` another. The data to cast from is in a contiguous, correctly-swapped and aligned chunk of memory pointed to by from. The buffer to cast to is also contiguous, correctly-swapped and aligned. The fromarr and toarr arguments should only be used for flexible-element-sized arrays (string, unicode, void).

An example castfunc is:
    
    
    static void
    double_to_float(double *from, float* to, npy_intp n,
                    void* ignore1, void* ignore2) {
        while (n--) {
              (*to++) = (double) *(from++);
        }
    }
    

This could then be registered to convert doubles to floats using the code:
    
    
    doub = PyArray_DescrFromType(NPY_DOUBLE);
    PyArray_RegisterCastFunc(doub, NPY_FLOAT,
         (PyArray_VectorUnaryFunc *)double_to_float);
    Py_DECREF(doub);
    

### Registering coercion rules[#](#registering-coercion-rules "Link to this heading")

By default, all user-defined data-types are not presumed to be safely castable to any builtin data-types. In addition builtin data-types are not presumed to be safely castable to user-defined data-types. This situation limits the ability of user-defined data-types to participate in the coercion system used by ufuncs and other times when automatic coercion takes place in NumPy. This can be changed by registering data-types as safely castable from a particular data-type object. The function [`PyArray_RegisterCanCast`](../reference/c-api/array.html#c.PyArray_RegisterCanCast "PyArray_RegisterCanCast") (from_descr, totype_number, scalarkind) should be used to specify that the data-type object from_descr can be cast to the data-type with type number totype_number. If you are not trying to alter scalar coercion rules, then use [`NPY_NOSCALAR`](../reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "NPY_NOSCALAR") for the scalarkind argument.

If you want to allow your new data-type to also be able to share in the scalar coercion rules, then you need to specify the scalarkind function in the data-type object’s “.f” member to return the kind of scalar the new data-type should be seen as (the value of the scalar is available to that function). Then, you can register data-types that can be cast to separately for each scalar kind that may be returned from your user-defined data-type. If you don’t register scalar coercion handling, then all of your user-defined data-types will be seen as [`NPY_NOSCALAR`](../reference/c-api/array.html#c.NPY_SCALARKIND.NPY_NOSCALAR "NPY_NOSCALAR").

### Registering a ufunc loop[#](#registering-a-ufunc-loop "Link to this heading")

You may also want to register low-level ufunc loops for your data-type so that an ndarray of your data-type can have math applied to it seamlessly. Registering a new loop with exactly the same arg_types signature, silently replaces any previously registered loops for that data-type.

Before you can register a 1-d loop for a ufunc, the ufunc must be previously created. Then you call [`PyUFunc_RegisterLoopForType`](../reference/c-api/ufunc.html#c.PyUFunc_RegisterLoopForType "PyUFunc_RegisterLoopForType") (…) with the information needed for the loop. The return value of this function is `0` if the process was successful and `-1` with an error condition set if it was not successful.

## Subtyping the ndarray in C[#](#subtyping-the-ndarray-in-c "Link to this heading")

One of the lesser-used features that has been lurking in Python since 2.2 is the ability to sub-class types in C. This facility is one of the important reasons for basing NumPy off of the Numeric code-base which was already in C. A sub-type in C allows much more flexibility with regards to memory management. Sub-typing in C is not difficult even if you have only a rudimentary understanding of how to create new types for Python. While it is easiest to sub-type from a single parent type, sub-typing from multiple parent types is also possible. Multiple inheritance in C is generally less useful than it is in Python because a restriction on Python sub-types is that they have a binary compatible memory layout. Perhaps for this reason, it is somewhat easier to sub-type from a single parent type.

All C-structures corresponding to Python objects must begin with [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "\(in Python v3.14\)") (or [`PyObject_VAR_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_VAR_HEAD "\(in Python v3.14\)")). In the same way, any sub-type must have a C-structure that begins with exactly the same memory layout as the parent type (or all of the parent types in the case of multiple-inheritance). The reason for this is that Python may attempt to access a member of the sub-type structure as if it had the parent structure ( _i.e._ it will cast a given pointer to a pointer to the parent structure and then dereference one of it’s members). If the memory layouts are not compatible, then this attempt will cause unpredictable behavior (eventually leading to a memory violation and program crash).

One of the elements in [`PyObject_HEAD`](https://docs.python.org/3/c-api/structures.html#c.PyObject_HEAD "\(in Python v3.14\)") is a pointer to a type-object structure. A new Python type is created by creating a new type-object structure and populating it with functions and pointers to describe the desired behavior of the type. Typically, a new C-structure is also created to contain the instance-specific information needed for each object of the type as well. For example, [`&PyArray_Type`](../reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type") is a pointer to the type-object table for the ndarray while a [PyArrayObject](../reference/c-api/types-and-structures.html#c.PyArrayObject "PyArrayObject")* variable is a pointer to a particular instance of an ndarray (one of the members of the ndarray structure is, in turn, a pointer to the type- object table [`&PyArray_Type`](../reference/c-api/types-and-structures.html#c.PyArray_Type "PyArray_Type")). Finally [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "\(in Python v3.14\)") (<pointer_to_type_object>) must be called for every new Python type.

### Creating sub-types[#](#creating-sub-types "Link to this heading")

To create a sub-type, a similar procedure must be followed except only behaviors that are different require new entries in the type- object structure. All other entries can be NULL and will be filled in by [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "\(in Python v3.14\)") with appropriate functions from the parent type(s). In particular, to create a sub-type in C follow these steps:

  1. If needed create a new C-structure to handle each instance of your type. A typical C-structure would be:
         
         typedef _new_struct {
             PyArrayObject base;
             /* new things here */
         } NewArrayObject;
         

Notice that the full PyArrayObject is used as the first entry in order to ensure that the binary layout of instances of the new type is identical to the PyArrayObject.

  2. Fill in a new Python type-object structure with pointers to new functions that will over-ride the default behavior while leaving any function that should remain the same unfilled (or NULL). The tp_name element should be different.

  3. Fill in the tp_base member of the new type-object structure with a pointer to the (main) parent type object. For multiple-inheritance, also fill in the tp_bases member with a tuple containing all of the parent objects in the order they should be used to define inheritance. Remember, all parent-types must have the same C-structure for multiple inheritance to work properly.

  4. Call [`PyType_Ready`](https://docs.python.org/3/c-api/type.html#c.PyType_Ready "\(in Python v3.14\)") (<pointer_to_new_type>). If this function returns a negative number, a failure occurred and the type is not initialized. Otherwise, the type is ready to be used. It is generally important to place a reference to the new type into the module dictionary so it can be accessed from Python.




More information on creating sub-types in C can be learned by reading PEP 253 (available at <https://www.python.org/dev/peps/pep-0253>).

### Specific features of ndarray sub-typing[#](#specific-features-of-ndarray-sub-typing "Link to this heading")

Some special methods and attributes are used by arrays in order to facilitate the interoperation of sub-types with the base ndarray type.

#### The __array_finalize__ method[#](#the-array-finalize-method "Link to this heading")

ndarray.__array_finalize__[#](#ndarray.__array_finalize__ "Link to this definition")
    

Several array-creation functions of the ndarray allow specification of a particular sub-type to be created. This allows sub-types to be handled seamlessly in many routines. When a sub-type is created in such a fashion, however, neither the __new__ method nor the __init__ method gets called. Instead, the sub-type is allocated and the appropriate instance-structure members are filled in. Finally, the [`__array_finalize__`](../reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__") attribute is looked-up in the object dictionary. If it is present and not None, then it can be either a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "\(in Python v3.14\)") containing a pointer to a [`PyArray_FinalizeFunc`](../reference/c-api/array.html#c.PyArray_FinalizeFunc "PyArray_FinalizeFunc") or it can be a method taking a single argument (which could be None)

If the [`__array_finalize__`](../reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__") attribute is a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "\(in Python v3.14\)"), then the pointer must be a pointer to a function with the signature:
    
    
    (int) (PyArrayObject *, PyObject *)
    

The first argument is the newly created sub-type. The second argument (if not NULL) is the “parent” array (if the array was created using slicing or some other operation where a clearly-distinguishable parent is present). This routine can do anything it wants to. It should return a -1 on error and 0 otherwise.

If the [`__array_finalize__`](../reference/arrays.classes.html#numpy.class.__array_finalize__ "numpy.class.__array_finalize__") attribute is not None nor a [`PyCapsule`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule "\(in Python v3.14\)"), then it must be a Python method that takes the parent array as an argument (which could be None if there is no parent), and returns nothing. Errors in this method will be caught and handled.

#### The __array_priority__ attribute[#](#the-array-priority-attribute "Link to this heading")

ndarray.__array_priority__[#](#ndarray.__array_priority__ "Link to this definition")
    

This attribute allows simple but flexible determination of which sub- type should be considered “primary” when an operation involving two or more sub-types arises. In operations where different sub-types are being used, the sub-type with the largest [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") attribute will determine the sub-type of the output(s). If two sub- types have the same [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") then the sub-type of the first argument determines the output. The default [`__array_priority__`](../reference/arrays.classes.html#numpy.class.__array_priority__ "numpy.class.__array_priority__") attribute returns a value of 0.0 for the base ndarray type and 1.0 for a sub-type. This attribute can also be defined by objects that are not sub-types of the ndarray and can be used to determine which [`__array_wrap__`](../reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__") method should be called for the return output.

#### The __array_wrap__ method[#](#the-array-wrap-method "Link to this heading")

ndarray.__array_wrap__[#](#ndarray.__array_wrap__ "Link to this definition")
    

Any class or type can define this method which should take an ndarray argument and return an instance of the type. It can be seen as the opposite of the [`__array__`](../reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__") method. This method is used by the ufuncs (and other NumPy functions) to allow other objects to pass through. For Python >2.4, it can also be used to write a decorator that converts a function that works only with ndarrays to one that works with any type with [`__array__`](../reference/arrays.classes.html#numpy.class.__array__ "numpy.class.__array__") and [`__array_wrap__`](../reference/arrays.classes.html#numpy.class.__array_wrap__ "numpy.class.__array_wrap__") methods.

[ __ previous Writing your own ufunc ](c-info.ufunc-tutorial.html "previous page") [ next F2PY user guide and reference manual __](../f2py/index.html "next page")

__On this page

  * [Iterating over elements in the array](#iterating-over-elements-in-the-array)
    * [Basic iteration](#basic-iteration)
    * [Iterating over all but one axis](#iterating-over-all-but-one-axis)
    * [Iterating over multiple arrays](#iterating-over-multiple-arrays)
    * [Broadcasting over multiple arrays](#broadcasting-over-multiple-arrays)
  * [User-defined data-types](#user-defined-data-types)
    * [Adding the new data-type](#adding-the-new-data-type)
    * [Registering a casting function](#registering-a-casting-function)
    * [Registering coercion rules](#registering-coercion-rules)
    * [Registering a ufunc loop](#registering-a-ufunc-loop)
  * [Subtyping the ndarray in C](#subtyping-the-ndarray-in-c)
    * [Creating sub-types](#creating-sub-types)
    * [Specific features of ndarray sub-typing](#specific-features-of-ndarray-sub-typing)
      * [The __array_finalize__ method](#the-array-finalize-method)
        * [`ndarray.__array_finalize__`](#ndarray.__array_finalize__)
      * [The __array_priority__ attribute](#the-array-priority-attribute)
        * [`ndarray.__array_priority__`](#ndarray.__array_priority__)
      * [The __array_wrap__ method](#the-array-wrap-method)
        * [`ndarray.__array_wrap__`](#ndarray.__array_wrap__)

---

## Subclassing ndarray

**Source:** [https://numpy.org/devdocs/user/basics.subclassing.html](https://numpy.org/devdocs/user/basics.subclassing.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Under-the-hood documentation for developers](../dev/underthehood.html)
  * Subclassing ndarray



# Subclassing ndarray[#](#subclassing-ndarray "Link to this heading")

## Introduction[#](#introduction "Link to this heading")

Subclassing ndarray is relatively simple, but it has some complications compared to other Python objects. On this page we explain the machinery that allows you to subclass ndarray, and the implications for implementing a subclass.

### ndarrays and object creation[#](#ndarrays-and-object-creation "Link to this heading")

Subclassing ndarray is complicated by the fact that new instances of ndarray classes can come about in three different ways. These are:

  1. Explicit constructor call - as in `MySubClass(params)`. This is the usual route to Python instance creation.

  2. View casting - casting an existing ndarray as a given subclass

  3. New from template - creating a new instance from a template instance. Examples include returning slices from a subclassed array, creating return types from ufuncs, and copying arrays. See [Creating new from template](#new-from-template) for more details




The last two are characteristics of ndarrays - in order to support things like array slicing. The complications of subclassing ndarray are due to the mechanisms numpy has to support these latter two routes of instance creation.

### When to use subclassing[#](#when-to-use-subclassing "Link to this heading")

Besides the additional complexities of subclassing a NumPy array, subclasses can run into unexpected behaviour because some functions may convert the subclass to a baseclass and “forget” any additional information associated with the subclass. This can result in surprising behavior if you use NumPy methods or functions you have not explicitly tested.

On the other hand, compared to other interoperability approaches, subclassing can be useful because many things will “just work”.

This means that subclassing can be a convenient approach and for a long time it was also often the only available approach. However, NumPy now provides additional interoperability protocols described in “[Interoperability with NumPy](basics.interoperability.html#basics-interoperability)”. For many use-cases these interoperability protocols may now be a better fit or supplement the use of subclassing.

Subclassing can be a good fit if:

  * you are less worried about maintainability or users other than yourself: Subclass will be faster to implement and additional interoperability can be added “as-needed”. And with few users, possible surprises are not an issue.

  * you do not think it is problematic if the subclass information is ignored or lost silently. An example is `np.memmap` where “forgetting” about data being memory mapped cannot lead to a wrong result. An example of a subclass that sometimes confuses users are NumPy’s masked arrays. When they were introduced, subclassing was the only approach for implementation. However, today we would possibly try to avoid subclassing and rely only on interoperability protocols.




Note that also subclass authors may wish to study [Interoperability with NumPy](basics.interoperability.html#basics-interoperability) to support more complex use-cases or work around the surprising behavior.

`astropy.units.Quantity` and `xarray` are examples for array-like objects that interoperate well with NumPy. Astropy’s `Quantity` is an example which uses a dual approach of both subclassing and interoperability protocols.

## View casting[#](#view-casting "Link to this heading")

_View casting_ is the standard ndarray mechanism by which you take an ndarray of any subclass, and return a view of the array as another (specified) subclass:
    
    
    >>> import numpy as np
    >>> # create a completely useless ndarray subclass
    >>> class C(np.ndarray): pass
    >>> # create a standard ndarray
    >>> arr = np.zeros((3,))
    >>> # take a view of it, as our useless subclass
    >>> c_arr = arr.view(C)
    >>> type(c_arr)
    <class '__main__.C'>
    

## Creating new from template[#](#creating-new-from-template "Link to this heading")

New instances of an ndarray subclass can also come about by a very similar mechanism to [View casting](#view-casting), when numpy finds it needs to create a new instance from a template instance. The most obvious place this has to happen is when you are taking slices of subclassed arrays. For example:
    
    
    >>> v = c_arr[1:]
    >>> type(v) # the view is of type 'C'
    <class '__main__.C'>
    >>> v is c_arr # but it's a new instance
    False
    

The slice is a _view_ onto the original `c_arr` data. So, when we take a view from the ndarray, we return a new ndarray, of the same class, that points to the data in the original.

There are other points in the use of ndarrays where we need such views, such as copying arrays (`c_arr.copy()`), creating ufunc output arrays (see also [__array_wrap__ for ufuncs and other functions](#array-wrap)), and reducing methods (like `c_arr.mean()`).

## Relationship of view casting and new-from-template[#](#relationship-of-view-casting-and-new-from-template "Link to this heading")

These paths both use the same machinery. We make the distinction here, because they result in different input to your methods. Specifically, [View casting](#view-casting) means you have created a new instance of your array type from any potential subclass of ndarray. [Creating new from template](#new-from-template) means you have created a new instance of your class from a pre-existing instance, allowing you - for example - to copy across attributes that are particular to your subclass.

## Implications for subclassing[#](#implications-for-subclassing "Link to this heading")

If we subclass ndarray, we need to deal not only with explicit construction of our array type, but also [View casting](#view-casting) or [Creating new from template](#new-from-template). NumPy has the machinery to do this, and it is this machinery that makes subclassing slightly non-standard.

There are two aspects to the machinery that ndarray uses to support views and new-from-template in subclasses.

The first is the use of the `ndarray.__new__` method for the main work of object initialization, rather then the more usual `__init__` method. The second is the use of the `__array_finalize__` method to allow subclasses to clean up after the creation of views and new instances from templates.

### A brief Python primer on `__new__` and `__init__`[#](#a-brief-python-primer-on-new-and-init "Link to this heading")

`__new__` is a standard Python method, and, if present, is called before `__init__` when we create a class instance. See the [python __new__ documentation](https://docs.python.org/reference/datamodel.html#object.__new__) for more detail.

For example, consider the following Python code:
    
    
    >>> class C:
    ...     def __new__(cls, *args):
    ...         print('Cls in __new__:', cls)
    ...         print('Args in __new__:', args)
    ...         # The `object` type __new__ method takes a single argument.
    ...         return object.__new__(cls)
    ...     def __init__(self, *args):
    ...         print('type(self) in __init__:', type(self))
    ...         print('Args in __init__:', args)
    

meaning that we get:
    
    
    >>> c = C('hello')
    Cls in __new__: <class '__main__.C'>
    Args in __new__: ('hello',)
    type(self) in __init__: <class '__main__.C'>
    Args in __init__: ('hello',)
    

When we call `C('hello')`, the `__new__` method gets its own class as first argument, and the passed argument, which is the string `'hello'`. After python calls `__new__`, it usually (see below) calls our `__init__` method, with the output of `__new__` as the first argument (now a class instance), and the passed arguments following.

As you can see, the object can be initialized in the `__new__` method or the `__init__` method, or both, and in fact ndarray does not have an `__init__` method, because all the initialization is done in the `__new__` method.

Why use `__new__` rather than just the usual `__init__`? Because in some cases, as for ndarray, we want to be able to return an object of some other class. Consider the following:
    
    
    class D(C):
        def __new__(cls, *args):
            print('D cls is:', cls)
            print('D args in __new__:', args)
            return C.__new__(C, *args)
    
        def __init__(self, *args):
            # we never get here
            print('In D __init__')
    

meaning that:
    
    
    >>> obj = D('hello')
    D cls is: <class 'D'>
    D args in __new__: ('hello',)
    Cls in __new__: <class 'C'>
    Args in __new__: ('hello',)
    >>> type(obj)
    <class 'C'>
    

The definition of `C` is the same as before, but for `D`, the `__new__` method returns an instance of class `C` rather than `D`. Note that the `__init__` method of `D` does not get called. In general, when the `__new__` method returns an object of class other than the class in which it is defined, the `__init__` method of that class is not called.

This is how subclasses of the ndarray class are able to return views that preserve the class type. When taking a view, the standard ndarray machinery creates the new ndarray object with something like:
    
    
    obj = ndarray.__new__(subtype, shape, ...
    

where `subtype` is the subclass. Thus the returned view is of the same class as the subclass, rather than being of class `ndarray`.

That solves the problem of returning views of the same type, but now we have a new problem. The machinery of ndarray can set the class this way, in its standard methods for taking views, but the ndarray `__new__` method knows nothing of what we have done in our own `__new__` method in order to set attributes, and so on. (Aside - why not call `obj = subdtype.__new__(...` then? Because we may not have a `__new__` method with the same call signature).

### The role of `__array_finalize__`[#](#the-role-of-array-finalize "Link to this heading")

`__array_finalize__` is the mechanism that numpy provides to allow subclasses to handle the various ways that new instances get created.

Remember that subclass instances can come about in these three ways:

  1. explicit constructor call (`obj = MySubClass(params)`). This will call the usual sequence of `MySubClass.__new__` then (if it exists) `MySubClass.__init__`.

  2. [View casting](#view-casting)

  3. [Creating new from template](#new-from-template)




Our `MySubClass.__new__` method only gets called in the case of the explicit constructor call, so we can’t rely on `MySubClass.__new__` or `MySubClass.__init__` to deal with the view casting and new-from-template. It turns out that `MySubClass.__array_finalize__` _does_ get called for all three methods of object creation, so this is where our object creation housekeeping usually goes.

  * For the explicit constructor call, our subclass will need to create a new ndarray instance of its own class. In practice this means that we, the authors of the code, will need to make a call to `ndarray.__new__(MySubClass,...)`, a class-hierarchy prepared call to `super().__new__(cls, ...)`, or do view casting of an existing array (see below)

  * For view casting and new-from-template, the equivalent of `ndarray.__new__(MySubClass,...` is called, at the C level.




The arguments that `__array_finalize__` receives differ for the three methods of instance creation above.

The following code allows us to look at the call sequences and arguments:
    
    
    import numpy as np
    
    class C(np.ndarray):
        def __new__(cls, *args, **kwargs):
            print('In __new__ with class %s' % cls)
            return super().__new__(cls, *args, **kwargs)
    
        def __init__(self, *args, **kwargs):
            # in practice you probably will not need or want an __init__
            # method for your subclass
            print('In __init__ with class %s' % self.__class__)
    
        def __array_finalize__(self, obj):
            print('In array_finalize:')
            print('   self type is %s' % type(self))
            print('   obj type is %s' % type(obj))
    

Now:
    
    
    >>> # Explicit constructor
    >>> c = C((10,))
    In __new__ with class <class 'C'>
    In array_finalize:
       self type is <class 'C'>
       obj type is <type 'NoneType'>
    In __init__ with class <class 'C'>
    >>> # View casting
    >>> a = np.arange(10)
    >>> cast_a = a.view(C)
    In array_finalize:
       self type is <class 'C'>
       obj type is <type 'numpy.ndarray'>
    >>> # Slicing (example of new-from-template)
    >>> cv = c[:1]
    In array_finalize:
       self type is <class 'C'>
       obj type is <class 'C'>
    

The signature of `__array_finalize__` is:
    
    
    def __array_finalize__(self, obj):
    

One sees that the `super` call, which goes to `ndarray.__new__`, passes `__array_finalize__` the new object, of our own class (`self`) as well as the object from which the view has been taken (`obj`). As you can see from the output above, the `self` is always a newly created instance of our subclass, and the type of `obj` differs for the three instance creation methods:

  * When called from the explicit constructor, `obj` is `None`

  * When called from view casting, `obj` can be an instance of any subclass of ndarray, including our own.

  * When called in new-from-template, `obj` is another instance of our own subclass, that we might use to update the new `self` instance.




Because `__array_finalize__` is the only method that always sees new instances being created, it is the sensible place to fill in instance defaults for new object attributes, among other tasks.

This may be clearer with an example.

## Simple example - adding an extra attribute to ndarray[#](#simple-example-adding-an-extra-attribute-to-ndarray "Link to this heading")
    
    
    import numpy as np
    
    class InfoArray(np.ndarray):
    
        def __new__(subtype, shape, dtype=np.float64, buffer=None, offset=0,
                    strides=None, order=None, info=None):
            # Create the ndarray instance of our type, given the usual
            # ndarray input arguments.  This will call the standard
            # ndarray constructor, but return an object of our type.
            # It also triggers a call to InfoArray.__array_finalize__
            obj = super().__new__(subtype, shape, dtype,
                                  buffer, offset, strides, order)
            # set the new 'info' attribute to the value passed
            obj.info = info
            # Finally, we must return the newly created object:
            return obj
    
        def __array_finalize__(self, obj):
            # ``self`` is a new object resulting from
            # ndarray.__new__(InfoArray, ...), therefore it only has
            # attributes that the ndarray.__new__ constructor gave it -
            # i.e. those of a standard ndarray.
            #
            # We could have got to the ndarray.__new__ call in 3 ways:
            # From an explicit constructor - e.g. InfoArray():
            #    obj is None
            #    (we're in the middle of the InfoArray.__new__
            #    constructor, and self.info will be set when we return to
            #    InfoArray.__new__)
            if obj is None: return
            # From view casting - e.g arr.view(InfoArray):
            #    obj is arr
            #    (type(obj) can be InfoArray)
            # From new-from-template - e.g infoarr[:3]
            #    type(obj) is InfoArray
            #
            # Note that it is here, rather than in the __new__ method,
            # that we set the default value for 'info', because this
            # method sees all creation of default objects - with the
            # InfoArray.__new__ constructor, but also with
            # arr.view(InfoArray).
            self.info = getattr(obj, 'info', None)
            # We do not need to return anything
    

Using the object looks like this:
    
    
    >>> obj = InfoArray(shape=(3,)) # explicit constructor
    >>> type(obj)
    <class 'InfoArray'>
    >>> obj.info is None
    True
    >>> obj = InfoArray(shape=(3,), info='information')
    >>> obj.info
    'information'
    >>> v = obj[1:] # new-from-template - here - slicing
    >>> type(v)
    <class 'InfoArray'>
    >>> v.info
    'information'
    >>> arr = np.arange(10)
    >>> cast_arr = arr.view(InfoArray) # view casting
    >>> type(cast_arr)
    <class 'InfoArray'>
    >>> cast_arr.info is None
    True
    

This class isn’t very useful, because it has the same constructor as the bare ndarray object, including passing in buffers and shapes and so on. We would probably prefer the constructor to be able to take an already formed ndarray from the usual numpy calls to `np.array` and return an object.

## Slightly more realistic example - attribute added to existing array[#](#slightly-more-realistic-example-attribute-added-to-existing-array "Link to this heading")

Here is a class that takes a standard ndarray that already exists, casts as our type, and adds an extra attribute.
    
    
    import numpy as np
    
    class RealisticInfoArray(np.ndarray):
    
        def __new__(cls, input_array, info=None):
            # Input array is an already formed ndarray instance
            # We first cast to be our class type
            obj = np.asarray(input_array).view(cls)
            # add the new attribute to the created instance
            obj.info = info
            # Finally, we must return the newly created object:
            return obj
    
        def __array_finalize__(self, obj):
            # see InfoArray.__array_finalize__ for comments
            if obj is None: return
            self.info = getattr(obj, 'info', None)
    

So:
    
    
    >>> arr = np.arange(5)
    >>> obj = RealisticInfoArray(arr, info='information')
    >>> type(obj)
    <class 'RealisticInfoArray'>
    >>> obj.info
    'information'
    >>> v = obj[1:]
    >>> type(v)
    <class 'RealisticInfoArray'>
    >>> v.info
    'information'
    

## `__array_ufunc__` for ufuncs[#](#array-ufunc-for-ufuncs "Link to this heading")

A subclass can override what happens when executing numpy ufuncs on it by overriding the default `ndarray.__array_ufunc__` method. This method is executed _instead_ of the ufunc and should return either the result of the operation, or [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "\(in Python v3.14\)") if the operation requested is not implemented.

The signature of `__array_ufunc__` is:
    
    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
    

  * _ufunc_ is the ufunc object that was called.

  * _method_ is a string indicating how the Ufunc was called, either `"__call__"` to indicate it was called directly, or one of its [methods](../reference/ufuncs.html#ufuncs-methods): `"reduce"`, `"accumulate"`, `"reduceat"`, `"outer"`, or `"at"`.

  * _inputs_ is a tuple of the input arguments to the `ufunc`

  * _kwargs_ contains any optional or keyword arguments passed to the function. This includes any `out` arguments, which are always contained in a tuple.




A typical implementation would convert any inputs or outputs that are instances of one’s own class, pass everything on to a superclass using `super()`, and finally return the results after possible back-conversion. An example, taken from the test case `test_ufunc_override_with_super` in `_core/tests/test_umath.py`, is the following.
    
    
    input numpy as np
    
    class A(np.ndarray):
        def __array_ufunc__(self, ufunc, method, *inputs, out=None, **kwargs):
            args = []
            in_no = []
            for i, input_ in enumerate(inputs):
                if isinstance(input_, A):
                    in_no.append(i)
                    args.append(input_.view(np.ndarray))
                else:
                    args.append(input_)
    
            outputs = out
            out_no = []
            if outputs:
                out_args = []
                for j, output in enumerate(outputs):
                    if isinstance(output, A):
                        out_no.append(j)
                        out_args.append(output.view(np.ndarray))
                    else:
                        out_args.append(output)
                kwargs['out'] = tuple(out_args)
            else:
                outputs = (None,) * ufunc.nout
    
            info = {}
            if in_no:
                info['inputs'] = in_no
            if out_no:
                info['outputs'] = out_no
    
            results = super().__array_ufunc__(ufunc, method, *args, **kwargs)
            if results is NotImplemented:
                return NotImplemented
    
            if method == 'at':
                if isinstance(inputs[0], A):
                    inputs[0].info = info
                return
    
            if ufunc.nout == 1:
                results = (results,)
    
            results = tuple((np.asarray(result).view(A)
                             if output is None else output)
                            for result, output in zip(results, outputs))
            if results and isinstance(results[0], A):
                results[0].info = info
    
            return results[0] if len(results) == 1 else results
    

So, this class does not actually do anything interesting: it just converts any instances of its own to regular ndarray (otherwise, we’d get infinite recursion!), and adds an `info` dictionary that tells which inputs and outputs it converted. Hence, e.g.,
    
    
    >>> a = np.arange(5.).view(A)
    >>> b = np.sin(a)
    >>> b.info
    {'inputs': [0]}
    >>> b = np.sin(np.arange(5.), out=(a,))
    >>> b.info
    {'outputs': [0]}
    >>> a = np.arange(5.).view(A)
    >>> b = np.ones(1).view(A)
    >>> c = a + b
    >>> c.info
    {'inputs': [0, 1]}
    >>> a += b
    >>> a.info
    {'inputs': [0, 1], 'outputs': [0]}
    

Note that another approach would be to use `getattr(ufunc, methods)(*inputs, **kwargs)` instead of the `super` call. For this example, the result would be identical, but there is a difference if another operand also defines `__array_ufunc__`. E.g., let’s assume that we evaluate `np.add(a, b)`, where `b` is an instance of another class `B` that has an override. If you use `super` as in the example, `ndarray.__array_ufunc__` will notice that `b` has an override, which means it cannot evaluate the result itself. Thus, it will return _NotImplemented_ and so will our class `A`. Then, control will be passed over to `b`, which either knows how to deal with us and produces a result, or does not and returns _NotImplemented_ , raising a `TypeError`.

If instead, we replace our `super` call with `getattr(ufunc, method)`, we effectively do `np.add(a.view(np.ndarray), b)`. Again, `B.__array_ufunc__` will be called, but now it sees an `ndarray` as the other argument. Likely, it will know how to handle this, and return a new instance of the `B` class to us. Our example class is not set up to handle this, but it might well be the best approach if, e.g., one were to re-implement `MaskedArray` using `__array_ufunc__`.

As a final note: if the `super` route is suited to a given class, an advantage of using it is that it helps in constructing class hierarchies. E.g., suppose that our other class `B` also used the `super` in its `__array_ufunc__` implementation, and we created a class `C` that depended on both, i.e., `class C(A, B)` (with, for simplicity, not another `__array_ufunc__` override). Then any ufunc on an instance of `C` would pass on to `A.__array_ufunc__`, the `super` call in `A` would go to `B.__array_ufunc__`, and the `super` call in `B` would go to `ndarray.__array_ufunc__`, thus allowing `A` and `B` to collaborate.

## `__array_wrap__` for ufuncs and other functions[#](#array-wrap-for-ufuncs-and-other-functions "Link to this heading")

Prior to numpy 1.13, the behaviour of ufuncs could only be tuned using `__array_wrap__` and `__array_prepare__` (the latter is now removed). These two allowed one to change the output type of a ufunc, but, in contrast to `__array_ufunc__`, did not allow one to make any changes to the inputs. It is hoped to eventually deprecate these, but `__array_wrap__` is also used by other numpy functions and methods, such as `squeeze`, so at the present time is still needed for full functionality.

Conceptually, `__array_wrap__` “wraps up the action” in the sense of allowing a subclass to set the type of the return value and update attributes and metadata. Let’s show how this works with an example. First we return to the simpler example subclass, but with a different name and some print statements:
    
    
    import numpy as np
    
    class MySubClass(np.ndarray):
    
        def __new__(cls, input_array, info=None):
            obj = np.asarray(input_array).view(cls)
            obj.info = info
            return obj
    
        def __array_finalize__(self, obj):
            print('In __array_finalize__:')
            print('   self is %s' % repr(self))
            print('   obj is %s' % repr(obj))
            if obj is None: return
            self.info = getattr(obj, 'info', None)
    
        def __array_wrap__(self, out_arr, context=None, return_scalar=False):
            print('In __array_wrap__:')
            print('   self is %s' % repr(self))
            print('   arr is %s' % repr(out_arr))
            # then just call the parent
            return super().__array_wrap__(self, out_arr, context, return_scalar)
    

We run a ufunc on an instance of our new array:
    
    
    >>> obj = MySubClass(np.arange(5), info='spam')
    In __array_finalize__:
       self is MySubClass([0, 1, 2, 3, 4])
       obj is array([0, 1, 2, 3, 4])
    >>> arr2 = np.arange(5)+1
    >>> ret = np.add(arr2, obj)
    In __array_wrap__:
       self is MySubClass([0, 1, 2, 3, 4])
       arr is array([1, 3, 5, 7, 9])
    In __array_finalize__:
       self is MySubClass([1, 3, 5, 7, 9])
       obj is MySubClass([0, 1, 2, 3, 4])
    >>> ret
    MySubClass([1, 3, 5, 7, 9])
    >>> ret.info
    'spam'
    

Note that the ufunc (`np.add`) has called the `__array_wrap__` method with arguments `self` as `obj`, and `out_arr` as the (ndarray) result of the addition. In turn, the default `__array_wrap__` (`ndarray.__array_wrap__`) has cast the result to class `MySubClass`, and called `__array_finalize__` \- hence the copying of the `info` attribute. This has all happened at the C level.

But, we could do anything we wanted:
    
    
    class SillySubClass(np.ndarray):
    
        def __array_wrap__(self, arr, context=None, return_scalar=False):
            return 'I lost your data'
    
    
    
    >>> arr1 = np.arange(5)
    >>> obj = arr1.view(SillySubClass)
    >>> arr2 = np.arange(5)
    >>> ret = np.multiply(obj, arr2)
    >>> ret
    'I lost your data'
    

So, by defining a specific `__array_wrap__` method for our subclass, we can tweak the output from ufuncs. The `__array_wrap__` method requires `self`, then an argument - which is the result of the ufunc or another NumPy function - and an optional parameter _context_. This parameter is passed by ufuncs as a 3-element tuple: (name of the ufunc, arguments of the ufunc, domain of the ufunc), but is not passed by other numpy functions. Though, as seen above, it is possible to do otherwise, `__array_wrap__` should return an instance of its containing class. See the masked array subclass for an implementation. `__array_wrap__` is always passed a NumPy array which may or may not be a subclass (usually of the caller).

## Extra gotchas - custom `__del__` methods and ndarray.base[#](#extra-gotchas-custom-del-methods-and-ndarray-base "Link to this heading")

One of the problems that ndarray solves is keeping track of memory ownership of ndarrays and their views. Consider the case where we have created an ndarray, `arr` and have taken a slice with `v = arr[1:]`. The two objects are looking at the same memory. NumPy keeps track of where the data came from for a particular array or view, with the `base` attribute:
    
    
    >>> # A normal ndarray, that owns its own data
    >>> arr = np.zeros((4,))
    >>> # In this case, base is None
    >>> arr.base is None
    True
    >>> # We take a view
    >>> v1 = arr[1:]
    >>> # base now points to the array that it derived from
    >>> v1.base is arr
    True
    >>> # Take a view of a view
    >>> v2 = v1[1:]
    >>> # base points to the original array that it was derived from
    >>> v2.base is arr
    True
    

In general, if the array owns its own memory, as for `arr` in this case, then `arr.base` will be None - there are some exceptions to this \- see the numpy book for more details.

The `base` attribute is useful in being able to tell whether we have a view or the original array. This in turn can be useful if we need to know whether or not to do some specific cleanup when the subclassed array is deleted. For example, we may only want to do the cleanup if the original array is deleted, but not the views. For an example of how this can work, have a look at the `memmap` class in `numpy._core`.

## Subclassing and downstream compatibility[#](#subclassing-and-downstream-compatibility "Link to this heading")

When sub-classing `ndarray` or creating duck-types that mimic the `ndarray` interface, it is your responsibility to decide how aligned your APIs will be with those of numpy. For convenience, many numpy functions that have a corresponding `ndarray` method (e.g., `sum`, `mean`, `take`, `reshape`) work by checking if the first argument to a function has a method of the same name. If it exists, the method is called instead of coercing the arguments to a numpy array.

For example, if you want your sub-class or duck-type to be compatible with numpy’s `sum` function, the method signature for this object’s `sum` method should be the following:
    
    
    def sum(self, axis=None, dtype=None, out=None, keepdims=False):
    ...
    

This is the exact same method signature for `np.sum`, so now if a user calls `np.sum` on this object, numpy will call the object’s own `sum` method and pass in these arguments enumerated above in the signature, and no errors will be raised because the signatures are completely compatible with each other.

If, however, you decide to deviate from this signature and do something like this:
    
    
    def sum(self, axis=None, dtype=None):
    ...
    

This object is no longer compatible with `np.sum` because if you call `np.sum`, it will pass in unexpected arguments `out` and `keepdims`, causing a TypeError to be raised.

If you wish to maintain compatibility with numpy and its subsequent versions (which might add new keyword arguments) but do not want to surface all of numpy’s arguments, your function’s signature should accept `**kwargs`. For example:
    
    
    def sum(self, axis=None, dtype=None, **unused_kwargs):
    ...
    

This object is now compatible with `np.sum` again because any extraneous arguments (i.e. keywords that are not `axis` or `dtype`) will be hidden away in the `**unused_kwargs` parameter.

[ __ previous Writing custom array containers ](basics.dispatch.html "previous page") [ next Interoperability with NumPy __](basics.interoperability.html "next page")

__On this page

  * [Introduction](#introduction)
    * [ndarrays and object creation](#ndarrays-and-object-creation)
    * [When to use subclassing](#when-to-use-subclassing)
  * [View casting](#view-casting)
  * [Creating new from template](#creating-new-from-template)
  * [Relationship of view casting and new-from-template](#relationship-of-view-casting-and-new-from-template)
  * [Implications for subclassing](#implications-for-subclassing)
    * [A brief Python primer on `__new__` and `__init__`](#a-brief-python-primer-on-new-and-init)
    * [The role of `__array_finalize__`](#the-role-of-array-finalize)
  * [Simple example - adding an extra attribute to ndarray](#simple-example-adding-an-extra-attribute-to-ndarray)
  * [Slightly more realistic example - attribute added to existing array](#slightly-more-realistic-example-attribute-added-to-existing-array)
  * [`__array_ufunc__` for ufuncs](#array-ufunc-for-ufuncs)
  * [`__array_wrap__` for ufuncs and other functions](#array-wrap-for-ufuncs-and-other-functions)
  * [Extra gotchas - custom `__del__` methods and ndarray.base](#extra-gotchas-custom-del-methods-and-ndarray-base)
  * [Subclassing and downstream compatibility](#subclassing-and-downstream-compatibility)

---

## Writing custom array containers

**Source:** [https://numpy.org/devdocs/user/basics.dispatch.html](https://numpy.org/devdocs/user/basics.dispatch.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Under-the-hood documentation for developers](../dev/underthehood.html)
  * Writing custom array containers



# Writing custom array containers[#](#writing-custom-array-containers "Link to this heading")

Numpy’s dispatch mechanism, introduced in numpy version v1.16 is the recommended approach for writing custom N-dimensional array containers that are compatible with the numpy API and provide custom implementations of numpy functionality. Applications include [dask](https://docs.dask.org/en/stable/) arrays, an N-dimensional array distributed across multiple nodes, and [cupy](https://docs-cupy.chainer.org/en/stable/) arrays, an N-dimensional array on a GPU.

For comprehensive documentation on writing custom array containers, please see:

  * [Interoperability with NumPy](basics.interoperability.html#basics-interoperability) \- the main guide covering `__array_ufunc__` and `__array_function__` protocols

  * [Special attributes and methods](../reference/arrays.classes.html#special-attributes-and-methods) \- see `class.__array__()` for documentation and example implementing the `__array__()` method




Numpy provides some utilities to aid testing of custom array containers that implement the `__array_ufunc__` and `__array_function__` protocols in the `numpy.testing.overrides` namespace.

To check if a Numpy function can be overridden via `__array_ufunc__`, you can use [`allows_array_ufunc_override`](../reference/generated/numpy.testing.overrides.allows_array_ufunc_override.html#numpy.testing.overrides.allows_array_ufunc_override "numpy.testing.overrides.allows_array_ufunc_override"):
    
    
    >>> from numpy.testing.overrides import allows_array_ufunc_override
    >>> allows_array_ufunc_override(np.add)
    True
    

Similarly, you can check if a function can be overridden via `__array_function__` using [`allows_array_function_override`](../reference/generated/numpy.testing.overrides.allows_array_function_override.html#numpy.testing.overrides.allows_array_function_override "numpy.testing.overrides.allows_array_function_override").

Lists of every overridable function in the Numpy API are also available via [`get_overridable_numpy_array_functions`](../reference/generated/numpy.testing.overrides.get_overridable_numpy_array_functions.html#numpy.testing.overrides.get_overridable_numpy_array_functions "numpy.testing.overrides.get_overridable_numpy_array_functions") for functions that support the `__array_function__` protocol and [`get_overridable_numpy_ufuncs`](../reference/generated/numpy.testing.overrides.get_overridable_numpy_ufuncs.html#numpy.testing.overrides.get_overridable_numpy_ufuncs "numpy.testing.overrides.get_overridable_numpy_ufuncs") for functions that support the `__array_ufunc__` protocol. Both functions return sets of functions that are present in the Numpy public API. User-defined ufuncs or ufuncs defined in other libraries that depend on Numpy are not present in these sets.

Refer to the [dask source code](https://github.com/dask/dask) and [cupy source code](https://github.com/cupy/cupy) for more fully-worked examples of custom array containers.

See also [NEP 18](https://numpy.org/neps/nep-0018-array-function-protocol.html "\(in NumPy Enhancement Proposals\)").

[ __ previous Byte-swapping ](byteswapping.html "previous page") [ next Subclassing ndarray __](basics.subclassing.html "next page")

---

## Byte-swapping

**Source:** [https://numpy.org/devdocs/user/byteswapping.html](https://numpy.org/devdocs/user/byteswapping.html)

* [ __](../index.html)
  * [NumPy user guide](index.html)
  * [Under-the-hood documentation for developers](../dev/underthehood.html)
  * Byte-swapping



# Byte-swapping[#](#byte-swapping "Link to this heading")

## Introduction to byte ordering and ndarrays[#](#introduction-to-byte-ordering-and-ndarrays "Link to this heading")

The `ndarray` is an object that provides a python array interface to data in memory.

It often happens that the memory that you want to view with an array is not of the same byte ordering as the computer on which you are running Python.

For example, I might be working on a computer with a little-endian CPU - such as an Intel Pentium, but I have loaded some data from a file written by a computer that is big-endian. Let’s say I have loaded 4 bytes from a file written by a Sun (big-endian) computer. I know that these 4 bytes represent two 16-bit integers. On a big-endian machine, a two-byte integer is stored with the Most Significant Byte (MSB) first, and then the Least Significant Byte (LSB). Thus the bytes are, in memory order:

  1. MSB integer 1

  2. LSB integer 1

  3. MSB integer 2

  4. LSB integer 2




Let’s say the two integers were in fact 1 and 770. Because 770 = 256 * 3 + 2, the 4 bytes in memory would contain respectively: 0, 1, 3, 2. The bytes I have loaded from the file would have these contents:
    
    
    >>> big_end_buffer = bytearray([0,1,3,2])
    >>> big_end_buffer
    bytearray(b'\x00\x01\x03\x02')
    

We might want to use an `ndarray` to access these integers. In that case, we can create an array around this memory, and tell numpy that there are two integers, and that they are 16 bit and big-endian:
    
    
    >>> import numpy as np
    >>> big_end_arr = np.ndarray(shape=(2,),dtype='>i2', buffer=big_end_buffer)
    >>> big_end_arr[0]
    np.int16(1)
    >>> big_end_arr[1]
    np.int16(770)
    

Note the array `dtype` above of `>i2`. The `>` means ‘big-endian’ (`<` is little-endian) and `i2` means ‘signed 2-byte integer’. For example, if our data represented a single unsigned 4-byte little-endian integer, the dtype string would be `<u4`.

In fact, why don’t we try that?
    
    
    >>> little_end_u4 = np.ndarray(shape=(1,),dtype='<u4', buffer=big_end_buffer)
    >>> little_end_u4[0] == 1 * 256**1 + 3 * 256**2 + 2 * 256**3
    True
    

Returning to our `big_end_arr` \- in this case our underlying data is big-endian (data endianness) and we’ve set the dtype to match (the dtype is also big-endian). However, sometimes you need to flip these around.

Warning

Scalars do not include byte order information, so extracting a scalar from an array will return an integer in native byte order. Hence:
    
    
    >>> big_end_arr[0].dtype.byteorder == little_end_u4[0].dtype.byteorder
    True
    

NumPy intentionally does not attempt to always preserve byte-order and for example converts to native byte-order in [`numpy.concatenate`](../reference/generated/numpy.concatenate.html#numpy.concatenate "numpy.concatenate").

## Changing byte ordering[#](#changing-byte-ordering "Link to this heading")

As you can imagine from the introduction, there are two ways you can affect the relationship between the byte ordering of the array and the underlying memory it is looking at:

  * Change the byte-ordering information in the array dtype so that it interprets the underlying data as being in a different byte order. This is the role of `arr.view(arr.dtype.newbyteorder())`

  * Change the byte-ordering of the underlying data, leaving the dtype interpretation as it was. This is what `arr.byteswap()` does.




The common situations in which you need to change byte ordering are:

  1. Your data and dtype endianness don’t match, and you want to change the dtype so that it matches the data.

  2. Your data and dtype endianness don’t match, and you want to swap the data so that they match the dtype

  3. Your data and dtype endianness match, but you want the data swapped and the dtype to reflect this




### Data and dtype endianness don’t match, change dtype to match data[#](#data-and-dtype-endianness-don-t-match-change-dtype-to-match-data "Link to this heading")

We make something where they don’t match:
    
    
    >>> wrong_end_dtype_arr = np.ndarray(shape=(2,),dtype='<i2', buffer=big_end_buffer)
    >>> wrong_end_dtype_arr[0]
    np.int16(256)
    

The obvious fix for this situation is to change the dtype so it gives the correct endianness:
    
    
    >>> fixed_end_dtype_arr = wrong_end_dtype_arr.view(np.dtype('<i2').newbyteorder())
    >>> fixed_end_dtype_arr[0]
    np.int16(1)
    

Note the array has not changed in memory:
    
    
    >>> fixed_end_dtype_arr.tobytes() == big_end_buffer
    True
    

### Data and type endianness don’t match, change data to match dtype[#](#data-and-type-endianness-don-t-match-change-data-to-match-dtype "Link to this heading")

You might want to do this if you need the data in memory to be a certain ordering. For example you might be writing the memory out to a file that needs a certain byte ordering.
    
    
    >>> fixed_end_mem_arr = wrong_end_dtype_arr.byteswap()
    >>> fixed_end_mem_arr[0]
    np.int16(1)
    

Now the array _has_ changed in memory:
    
    
    >>> fixed_end_mem_arr.tobytes() == big_end_buffer
    False
    

### Data and dtype endianness match, swap data and dtype[#](#data-and-dtype-endianness-match-swap-data-and-dtype "Link to this heading")

You may have a correctly specified array dtype, but you need the array to have the opposite byte order in memory, and you want the dtype to match so the array values make sense. In this case you just do both of the previous operations:
    
    
    >>> swapped_end_arr = big_end_arr.byteswap()
    >>> swapped_end_arr = swapped_end_arr.view(swapped_end_arr.dtype.newbyteorder())
    >>> swapped_end_arr[0]
    np.int16(1)
    >>> swapped_end_arr.tobytes() == big_end_buffer
    False
    

An easier way of casting the data to a specific dtype and byte ordering can be achieved with the ndarray astype method:
    
    
    >>> swapped_end_arr = big_end_arr.astype('<i2')
    >>> swapped_end_arr[0]
    np.int16(1)
    >>> swapped_end_arr.tobytes() == big_end_buffer
    False
    

[ __ previous Memory alignment ](../dev/alignment.html "previous page") [ next Writing custom array containers __](basics.dispatch.html "next page")

__On this page

  * [Introduction to byte ordering and ndarrays](#introduction-to-byte-ordering-and-ndarrays)
  * [Changing byte ordering](#changing-byte-ordering)
    * [Data and dtype endianness don’t match, change dtype to match data](#data-and-dtype-endianness-don-t-match-change-dtype-to-match-data)
    * [Data and type endianness don’t match, change data to match dtype](#data-and-type-endianness-don-t-match-change-data-to-match-dtype)
    * [Data and dtype endianness match, swap data and dtype](#data-and-dtype-endianness-match-swap-data-and-dtype)

---

