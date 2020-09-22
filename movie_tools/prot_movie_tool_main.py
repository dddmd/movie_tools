import cv2
import os,sys,re

def movie_separate(movie_file, start_sec_list, end_sec_list, offset_sec=0, silent=False):
	"""
		in
			offset_sec:前後のオフセット時間(秒)
	"""
	
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
	
		#if type(stime)==str:
		stime_str = re.findall('\d+', stime)
		time_str = max(int(stime_str[0])*60 + int(stime_str[1]) - offset_sec, 0)
		stime_f=int(time_str*fps)
		etime_str = re.findall('\d+', etime)
		time_str = min(int(etime_str[0])*60 + int(etime_str[1]) + offset_sec, int(count/fps))
		etime_f=int(time_str*fps)
		write_file_name=f'{file_prefix}{stime_str[0]}{stime_str[1]}_{etime_str[0]}{etime_str[1]}.mp4'
		#elif type(stime)==int:
		#	stime_f=int(max(stime-offset_sec, 0)*fps)
		#	etime_f=int(min(etime+offset_sec, int(count/fps))*fps)
		#	write_file_name=f'{file_prefix}{stime}_{etime}.mp4'
		print(stime_f, etime_f)
		
		# Write Movie File Makes
		cap = cv2.VideoCapture(movie_file)
		cap.set(cv2.CAP_PROP_POS_FRAMES, stime_f)
		fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #mp4
		writer = cv2.VideoWriter(write_file_name, fmt, fps, (width,height)) # ライター作成

		frame_pos=stime_f
		while(frame_pos<etime_f):
			ret, frame = cap.read()
			if not ret:
				break
			
			if silent:
				cv2.imshow("frame", frame)
				key=cv2.waitKey(1) & 0xff
				if key == ord('q'):
					break
			
			writer.write(frame)	
			frame_pos+=1
		writer.release()
	
	cv2.destroyAllWindows()

if __name__ == '__main__':
	movie_separate('data/mov_hts-samp009.mp4', ['00:10','00:15'], ['00:12','00:18'], offset_sec=1)