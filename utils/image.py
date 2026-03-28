import cv2
import numpy as np

from PIL import Image


def read_video_frames(video_path) -> list[cv2.typing.MatLike]:
    """
    Reads frames from an MP4 video and can optionally process or save them.

    Args:
        video_path (str): The path to the input MP4 video file.

    Returns:
        List of frames extracted from the video.
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    response: list[cv2.typing.MatLike] = []

    frame_count = 0
    while True:
        ret, frame = cap.read() # Read a frame

        if not ret: # Break the loop if no more frames are returned
            break

        frame_count += 1
        response.append(frame)
    
    cap.release() # Release the video capture object
    cv2.destroyAllWindows() # Close any OpenCV windows
    return response
