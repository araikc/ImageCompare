# USAGE
# python isequal.py -i1 img1 -i2 img2 -t1 threshold1 -t2 threshold2
# Used 'Structured Similarity Image Metric' and 'Mean Squared Error' algorithms for comparison

# import the necessary packages
from skimage.measure import compare_ssim as ssim
import numpy as np
import cv2
import argparse


# MSE algorithms
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err


def compare_images(args):
	# compute the mean squared error and structural similarity
	# index for the images
	imageA = args.img1
	imageB = args.img2
	imageA = cv2.imread(imageA)
	imageB = cv2.imread(imageB)
	imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
	imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
	try:
		m = mse(imageA, imageB)
		s = ssim(imageA, imageB)
	except ValueError:
		return "false"
	if m > args.threshold1 or s < args.threshold2: 
		return 'false'
	return 'true'
	

def get_options():
    parser = argparse.ArgumentParser(
        description='Compare 2 images and return boolean value',
        usage='%(prog)s --img1 <path> --img2 <path> [options]')
    parser.add_argument('-i1', '--img1',
        help="Path to image 1",
        metavar='<path>',
        required=True,
        type=str,
        default=None,
        action='store')
    parser.add_argument('-i2', '--img2',
        help="Path to image 2",
        metavar='<path>',
        required=True,
        type=str,
        default=None,
        action='store')
    parser.add_argument('-t1', '--threshold1',
	help="Threshold for MSE. The smaller the value the strict is comparison: default is [25]",
        metavar='<int>',
        type=int,
        default=25,
        action='store')
    parser.add_argument('-t2', '--threshold2',
	help="Threshold for SSIM. The near to 1 the value the strict is comparison: default is [0.998]",
        metavar='<float>',
        type=float,
        default=0.998,
        action='store')
    args = parser.parse_args()
    return args


def main():
    args = get_options()
    print compare_images(args)

# Entry point
main()

