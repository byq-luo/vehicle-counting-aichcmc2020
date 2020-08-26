import os
import argparse

from detect import detect
from track import track
from count import count
from visualize import visualize

def parse_args():
    argparser = argparse.ArgumentParser(
        description='Data preparation for vehicle counting')
    argparser.add_argument('-j', '--json_dir', type=str,
                           default='data/json/', help='Json directory')
    argparser.add_argument('-v', '--video_dir', type=str,
                           default='data/video/', help='Video directory')
    argparser.add_argument('-d', '--detect_dir', type=str,
                           default='data/detect', help='Detection result directory')
    argparser.add_argument('-t', '--track_dir', type=str,
                           default='data/track', help='Tracking result directory')
    argparser.add_argument('-c', '--count_dir', type=str,
                           default='data/count', help='Counting result directory')
    argparser.add_argument('-s', '--visualize_dir', type=str,
                           default='data/visualize', help='Visualizing result directory')
    argparser.add_argument('-r', '--result_dir', type=str,
                           default='result/', help='Final result directory')
    args = vars(argparser.parse_args())
    return args

if __name__=='__main__':
    args = parse_args()

    json_dir = args['json_dir']
    video_dir = args['video_dir']
    detect_dir = args['detect_dir']
    track_dir = args['track_dir']
    count_dir = args['count_dir']
    visualize_dir = args['visualize_dir']
    result_dir = args['result_dir']

    detect(json_dir, video_dir, detect_dir)
    track(json_dir, video_dir, detect_dir, track_dir)
    count(json_dir, video_dir, track_dir, count_dir)
    if visualize_dir:
        visualize(json_dir, video_dir, detect_dir, track_dir, count_dir, visualize_dir)
