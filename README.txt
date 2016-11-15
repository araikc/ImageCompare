Implemented image comparison Python script which compares 2 images and prints comparison result: 
  'true'  in case of equal result 
  'false' in case of difference.

Used 'Structured Similarity Image Metric' and 'Mean Squared Error' algorithms.

Referals:
 SSID https://en.wikipedia.org/wiki/Structural_similarity
 MSE  https://en.wikipedia.org/wiki/Mean_squared_error

Usage:

isequal.py --img1 <path> --img2 <path> [options]

Compare 2 images and return boolean value
	-i1 <path>,   --img1 <path> Path to image 1
	-i2 <path>,   --img2 <path> Path to image 2

optional arguments:
	-h,           --help show this help message and exit
	-t1 <int>,    --threshold1 <int> Threshold for MSE. The smaller the value the strict is comparison: default is [25]
	-t2 <float>,  --threshold2 <float> Threshold for SSIM. The near to 1 the value the strict is comparison: default is [0.998]

compare.bat file is a wrap to python executable for help in usage for Windows users.

Usage:

compare.bat <path_to_image1> <path_to_image2> <options>

<options>:
	-t1 <int>,    --threshold1 <int> Threshold for MSE. The smaller the value the strict is comparison: default is [25]
	-t2 <float>,  --threshold2 <float> Threshold for SSIM. The near to 1 the value the strict is comparison: default is [0.998]

Requirements and installation sources:
  Python 2.7.* (last version)
  Python modules:
       scikit-image (http://scikit-image.org/docs/dev/install.html )
       numpy        (https://sourceforge.net/projects/numpy/ )
       cv2	    (http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html )
       argparse     (pip install argparse)

