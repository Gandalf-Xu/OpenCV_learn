
import os
import cv2

if __name__ == '__main__':
    flv_paths = []
    dataset_path = r'D:/xxxx/datasets/'  # for videos path
    for filename in os.listdir(dataset_path):
        flv_paths.append(os.path.join(dataset_path, filename))  # ['str']

    print('reading video...')
    frame_skip = 25
    for flv in flv_paths[1:4]:
        cap = cv2.VideoCapture(flv)
        while True:
            ret, frame = cap.read()
            if not ret:
                cap.release()
                break

            print(frame.shape, flv)  # (240, 320, 3)
            cv2.imshow('frame', frame)
            # 处理视频帧...

            key = cv2.waitKey(1) & 0xFF  # 等候1ms 播放下一帧或按q键退出
            if key == ord("q"):
                break
            video_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 视频帧数

            next_frame_idx = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 'float' (start from 1.0)
            print('next_frame_idx:', next_frame_idx)
            if (next_frame_idx + frame_skip) < video_frames:
                read_frame = (next_frame_idx + frame_skip)
            else:
                break
            print('read_frame:', read_frame)
            cap.set(1, read_frame)  # 设置cv2.CAP_PROP_POS_FRAMES(1)的属性值

        cv2.destroyAllWindows()
