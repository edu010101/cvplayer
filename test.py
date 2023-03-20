import cv2
import queue
import threading
import time
import multiprocessing as mp




video_capture = cv2.VideoCapture('/media/eduardo/HD 2tb/Downloads/HD Simulado/MS-112/MS-112_C_01_R0/MS-112_C_01_R0.mp4')
encoded_frames = queue.Queue(10000)

#populate encoded frames queue
start = time.time()
while not encoded_frames.full():    
    encoded_frame = video_capture.grab()
    frame_id = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
    encoded_frames.put([encoded_frame, frame_id])

# print(time.time() - start)
# print('encoded_frames queue size: ', encoded_frames.qsize())

def decode_frame(encoded_frame, frame_id):
    video_capture.retrieve(encoded_frame)
    #print('frame_id: ', frame_id)

def process_video_chunk(encoded_frames):
    start = time.time()
    for encoded_frame, frame_id in encoded_frames:
        decode_frame(encoded_frame, frame_id)
    print('process_video_chunk',time.time() - start)
    # while not encoded_frames.empty():
    #     encoded_frame, frame_id = encoded_frames.get()
    #     decode_frame(encoded_frame, frame_id)

chunk_size = encoded_frames.qsize() // 3
print('chunk_size: ', chunk_size)

while not encoded_frames.empty():
    print(encoded_frames.get())



start = time.time()
while not encoded_frames.qsize() < chunk_size:
    chunk_list = [encoded_frames.get() for _ in range(chunk_size)]
    mp.Process(target=process_video_chunk, args=(chunk_list,)).start()

print('multiprocessing',time.time() - start)




# print('terminou mult')

# while not encoded_frames.full():    
#     encoded_frame = video_capture.grab()
#     frame_id = video_capture.get(cv2.CAP_PROP_POS_FRAMES)
#     encoded_frames.put([encoded_frame, frame_id])
# print('terminou mult')
# start = time.time()
# while not encoded_frames.empty():
#     encoded_frame, frame_id = encoded_frames.get()
#     decode_frame(encoded_frame, frame_id)

# print('normal',time.time() - start)


