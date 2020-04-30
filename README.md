# Learn Computer Vision Basics with OpenCV in Python

OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library. It was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

The library has more than 2500 optimised algorithms, which includes a comprehensive set of both classic and state-of-the-art computer vision and machine learning algorithms. These algorithms can be used to detect and recognise faces, identify objects, classify human actions in videos, track camera movements, track moving objects, extract 3D models of objects, produce 3D point clouds from stereo cameras, stitch images together to produce a high resolution image of an entire scene, find similar images from an image database, remove red eyes from images taken using flash, follow eye movements, recognise scenery and establish markers to overlay it with augmented reality, etc.

## What will I learn during this workshop?

In this hands-on Beginners Machine Learning online workshop, you will develop your data processing skills to images. These workshop series will gradually develop to include video processing, deep learning and more advanced applications in computer vision.

During the workshop we will analyse and process images in a Jupyter notebook. We first will look at the properties of images and explore the different image processing commands. After we have learned the basics, we will go through some exercises identifying objects in images using simple edge detection techniques and contours.

## Questions you will answer in this workshop

## Learning Objectives

- How are images stored in computers and what colour channels are
- How to read in and save images for processing using command line options
- How to perform basic image operations such as cropping, masking and transformations
- How to detect objects in images
- How to perform image analysis

## Steps

This workshop consists of 6 lessons and 5 projects:

**LESSONS**
1. Basic Image Operations (Parsing Commands, Loading and Showing images)
2. Basic Image Processing Techniques (Cropping, Masking, Geometric Transformations, Morphological Transformations)
3. Kernels, Smoothing and Blurring Images 
4. Image Gradients, Thresholding, Edge Detection 
5. Identifying Contours of objects in Images 
6. Histograms and Image Enhancements by Equalising

**PROJECTS**
1. Data Augmentation for a flower detection machine learning classifier
2. Detecting Xs and Os for a Tic Tac Toe mobile game app
3. Classifying Shapes in an image
4. Identifying portraits for a mobile portrait scanner app
5. Detecting dimly lit images of licence plates taken at night


## Prerequisites

While you won't need prior experience in computer vision, we will assume basic programming experience with Python and package/environment managers such as pip, conda or pipenv.
1. Conda installed locally (https://docs.anaconda.com/anaconda/install/)
2. Jupyter Notebook installed locally (https://jupyter.readthedocs.io/en/latest/install.html) 

For referesher on python programming we recommend the following free course:
- Python programming language: See [Udacity - Intro to Python](https://eu.udacity.com/course/introduction-to-python--ud1110)


## Setup
Use the following guides to setup your development environment

1. Create your local environment (see prerequisite No. 1): `conda create --name ${environment_name}`
2. Activate the env: `conda activate ${environment_name}`
3. **[Install OpenCV with Conda](https://anaconda.org/conda-forge/opencv)** - We recommend you install OpenCV via distributed packages and package managers like Conda to avoid unnecessary hassle
`conda install -c conda-forge opencv`
4. Install matplotlib and numpy using `conda install matplotlib numpy`
3. Add virtual env to jupyter notebook kernel
    `pip install --user ipykernel`
    `python -m ipykernel install --user --name=${environment_name}` (this should print "Installed kernelspec ${environment_name} in ${dir})
3. Make sure you have jupyter notebook installed (see prerequisite No. 2) and run `jupyter notebook` from the root of this project. This will start a local notebook server and open a new window
4. Go to /notebooks/Lesson 1 - Basic Image Operations and select the kernel that is attached to the environment you've just created 
5. You're ready to go!

## Flow

1. Clone this git repository using `git clone https://github.com/beginners-machine-learning-london/computer_vision_basics.git` or download the repo as a zip file to get started
2. Setup your development environment using conda or pipenv using the `requirements.txt` file.
3. Listen to lectures then work your way through the notebooks in `notebooks` folder.
4. Complete the project sections in the notebooks after the workshop.
5. Join our [slack group](http://tiny.cc/joinbmlslack) to get access to this workshop's private channel so that you can ask questions and connect with your classmates
6. Submit the github repo link to your completed projects on our [website](https://beginnersmachinelearning.com) for grading and a chance to earn a course certificate 

> **IMPORTANT NOTE**: Attempt to complete the projects by yourself using openCV documentation and googling online. If you get stuck and cannot progress any further, then take a look at the solutions in the `solutions` folder

## Primary Tools:

- [Python](https://www.python.org/): Python is a programming language that lets you work more quickly and integrate your systems more effectively.
- [OpenCV](https://opencv.org): OpenCV (Open Source Computer Vision Library) is an open source computer vision and machine learning software library containing 2500 computer vision algorithms. It was built to provide a common infrastructure for computer vision applications and to accelerate the use of machine perception in the commercial products.

## Learn More:

- **[OpenCV Python Documentation](https://opencv-python-tutroals.readthedocs.io/en/latest/)** - Use this resource as the main resource for this class.
- **[Official OpenCV Website](https://opencv.org)** - Check out this resource to learn more about OpenCV and read the official documentation. The documentation provides further information on CV algorithms and concepts utilised in each function.
- **[pyimagesearch Computer Vision Blog](https://www.pyimagesearch.com)** - A great resource to dive deeper into computer vision topics.

## Collaboration, Questions and Discussions

- [**BML Slack Channel**](http://tiny.cc/joinbmlslack) - Join our slack workspace to collaborate with others, discuss ideas and post any questions you have about our group or the workshops

## Workshop Feedback

- How was this workshop? Please provide us with some feedback [**here**](http://tiny.cc/BMLfeedback) so that we can improve the content and delivery of future workshops.

