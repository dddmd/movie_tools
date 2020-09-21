import cv2
import os,sys,re

def movie_separate(movie_file, start_sec_list, end_sec_list, offset_sec=0):
	
	if not os.path.isfile(movie_file):
		print(f'{movie_file} file not exist')
	
	file_prefix = re.sub('.h264|.mp4|.MP4|.wmv|.avi','_',os.path.basename(movie_file))
	print(file_prefix)
	
	font = cv2.FONT_HERSHEY_SIMPLEX
	cap = cv2.VideoCapture(movie_file)
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	fps = cap.get(cv2.CAP_PROP_FPS)
	count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	print('cap:', width, height, fps, count)
	
	frame_pos=0
	while(cap.isOpened()):
		
		ret, frame = cap.read()
		if not ret:
			break
			
		cv2.imshow("frame", frame)
		key=cv2.waitKey(1) & 0xff
		if key == ord('q'):
			break
		
		frame_pos+=1
		
	cap.release()
	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	movie_separate('../data/mov_hts-samp009.mp4', [], [])