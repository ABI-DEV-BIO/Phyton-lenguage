def time_seg(day=0, hour=0, min=0, seg=0):
    final_time = 0
    
    final_time += day * 24 * 3600
    final_time += hour * 3600
    final_time += min * 60
    final_time += seg
   
    total_milisegundos = final_time * 1000
    print(f"Total en milisegundos: {total_milisegundos}")

time_seg(2, 33, 23, 12)