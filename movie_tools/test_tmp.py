def check_sxxx(class_pred_list, sxxx_count, sxxx_flag, ir_class):
	
	if 'person_sxxx' in class_pred_list:
		sxxx_count+=1
		
		if sxxx_count > 10:
			sxxx_flag=True
			
			for i,c in enumerate(class_pred_list):
				if c=='person_sxxx':
					ir_class[i]='person_sxxx'
			#ir_class=[c if c=='person_sxxx' else None for c in class_pred_list]
			
	else:
		sxxx_flag=False
		sxxx_count=0
		
	return sxxx_count, sxxx_flag, ir_class
	
	
def check_mxxx(class_pred_list, mxxx_count, mxxx_flag, ir_class):
	
	# 筐ある & 人がいない
	if ('mxxx' in class_pred_list) & (len([c for c in class_pred_list if 'person' in c])==0):
		mxxx_count+=1
		
		if mxxx_count > 50:
			mxxx_flag=True
			
			for i,c in enumerate(class_pred_list):
				if c=='mxxx':
					ir_class[i]='mxxx'
			#ir_class=[c if c=='person_sxxx' else None for c in class_pred_list]
			
	else:
		mxxx_flag=False
		mxxx_count=0
		
	return mxxx_count, mxxx_flag, ir_class
	
	
def check_invasion(class_pred_list, ixxx_count, ixxx_flag, ir_class,
				   r, top_xy, bottom_xy):
				   
	ixxx_flag_tmp=False
	for j, c in enumerate(class_pred_list):
		if 'person' in c:
			if (top_xy[0] <= r[j][2][0]) and (r[j][2][0] <= bottom_xy[0]) and (top_xy[1] <= r[j][2][1]) and (r[j][2][1] <= bottom_xy[1]):
				ixxx_flag_tmp=True
				break

	
	if ixxx_flag_tmp:
		ixxx_count+=1
		if ixxx_count > 10:
			mxxx_flag=True
			
			for i,c in enumerate(class_pred_list):
				if c=='ixxx':
					ir_class[i]='ixxx'
			
	else:
		ixxx_flag=False
			
			for i,c in enumerate(class_pred_list):
				if c=='ixxx':
					ir_class[i]='ixxx'
			#ir_class=[c if c=='person_sxxx' else None for c in class_pred_list]
			
	else:
		ixxx_flag=False
		ixxx_count=0
		
	return ixxx_count, ixxx_flag, ir_class