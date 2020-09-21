import cv2
import os,sys,re

def movie_separate(movie_file, start_sec_list, end_sec_list, offset_sec=0):
	
	if not os.path.isfile(movie_file):
		print(f'{movie_file} file not exist')
		
	if len(start_sec_list) != len(end_sec_list):
		print(f'Erorr sec_lint num, start_sec_list:{len(start_sec_list)}, end_sec_list:{len(end_sec_list)}')
	
	file_prefix = re.sub('.h264|.mp4|.MP4|.wmv|.avi','_',os.path.basename(movie_file))
	print(file_prefix)
	
	# Read　Movie　File
	font = cv2.FONT_HERSHEY_SIMPLEX
	cap = cv2.VideoCapture(movie_file)
	width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	fps = cap.get(cv2.CAP_PROP_FPS)
	count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	print('cap:', width, height, fps, count)
	cap.release()
	
	for stime, etime in zip(start_sec_list, end_sec_list):
		stime_f=stime*fps
		etime_f=etime*fps
		cap = cv2.VideoCapture(movie_file)
		cap.set(cv2.CAP_PROP_POS_FRAMES, stime_f)
		fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #mp4
		writer = cv2.VideoWriter(f'{file_prefix}_{stime}_{etime}.mp4', fmt, fps, (width,height)) # ライター作成

		frame_pos=stime_f
		while(frame_pos<etime_f):
			ret, frame = cap.read()
			if not ret:
				break
				
			writer.write(frame)
				
			frame_pos+=1
		writer.release()
	
	"""
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
	"""
	cv2.destroyAllWindows()

if __name__ == '__main__':
	movie_separate('data/mov_hts-samp009.mp4', [10,15], [12,18])