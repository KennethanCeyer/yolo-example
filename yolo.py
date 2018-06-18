import argparse

from command import Command

parser = argparse.ArgumentParser(description='object detection with Yolo model')

parser.add_argument('install', 'i', action='store_true', default=False, help='install train image set')
parser.add_argument('--epoch', '-e', type=int, default=10, help='an epoch number to train model')

if __name__ == 'main':
    args = parser.parse_args()
    command = Command(args)
    command.parse()
