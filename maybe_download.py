import os
import urllib.request
import sys

def _print_download_progress(count, block_size, total_size):
    
    pct_complete = float(count * block_size) / total_size

    msg = "\r- Download progress: {0:.1%}".format(pct_complete)

    sys.stdout.write(msg)
    sys.stdout.flush()

def maybe_extract():
	check_dirs = ['./ssd_inception_v2_coco_2017_11_17']
	if not (os.path.exists(check_dirs[0])):
		print('Extracting Files...')
		os.system('tar xf ./ssd_inception_v2_coco_2017_11_17.tar.gz -C ./')
		print('Extraction Complete')
	else:
		print('Files already extracted')


def maybe_download():
	files = ['ssd_inception_v2_coco_2017_11_17.tar.gz']
	url_train = 'http://download.tensorflow.org/models/object_detection/ssd_inception_v2_coco_2017_11_17.tar.gz'
	parent_dir = os.listdir('./')
	if files[0] not in parent_dir:
		print('Downloading Files...')
		file_path, _ = urllib.request.urlretrieve(url=url_train,
												  filename='./'+files[0],
												  reporthook=_print_download_progress)
		print()
		print('Test Dataset Download Finsihed')
	else:
		print('Files already downloaded')
	maybe_extract()





