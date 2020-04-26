# videosplit.py

## Description
This program is a very simple application that leverages ffmpeg to split a video file into multiple pieces.

## Requirement
This application requires Python 3.7 and above.

This also requires the ffmpeg to be installed on the computer.   If you have a Mac OSX, then you can use homebrew to install ffmpeg:

```
brew install ffmpeg
```

## Usage
Use the following command line:

```python videosplit.py {filename}```

You will need to pass the input filename to the application.   

## Input File Format
The input file contains the list of split points that the application will attempt to split the file.   It has a specific format.

### First Line
The first line of the file should specify the original video file that we want to split apart.

### Remaining Lines
The remaining lines should contain the beginning of the split point, the ending of the split point and an optional filename. In the following example, we want to create a newfile called 'filename.mp4' and the file should contain everything from 0:01 and 10:35 of the original file.     If you want to specify the end of the file in the line, specify a valid time larger than the length of the file.   The parameter has to be a valid time and can be greater than the length of the file.  For example 99:59:59 is valid but 99:99:99 is not.

```
00:01 10:35 filename
```
The filename field is an optional paramter that will specify the name of the new file. It will use the same extension as the original file. If you leave off this filename paramter, then the file will be named with the original filename with a "-part#" appended to it.

### Example of input file
This is a example of a simple file:

```bash
video.mp4
00:00:00 00:00:50 filename1
00:00:50 00:03:00 filename2
00:03:00 00:07:00
00:07:00 00:09:00
00:09:00 99:59:59
```

This file when passed to videosplit will use the ```video.mp4``` as the input file and then will be split up in the following five files:

* Between 00:00:00 and 00:00:50            => filename1.mp4
* Between 00:00:50 and 00:03:00            => filename2.mp4
* Between 00:03:00 and 00:07:00            => video-part1.mp4
* Between 00:07:00 and 00:09:00            => video-part2.mp4
* Between 00:09:00 and 99:59:59 (Ending)   => video-part3.mp4

The following is the directory after the application is run:

```bash
$ls -l
total 5846528
-rw-r--r--  1 nouser  none        1026 Jan 11 10:55:52 2019 README.md
-rw-r--r--  1 nouser  none         100 Jan 11 10:50:37 2019 test.file
-rw-r--r--  1 nouser  none   127193901 Jan 11 10:54:31 2019 filename1.mp4
-rw-r--r--  1 nouser  none   327671607 Jan 11 10:54:33 2019 filename2.mp4
-rw-r--r--  1 nouser  none   606393559 Jan 11 10:54:36 2019 video-part1.mp4
-rw-r--r--  1 nouser  none   302315567 Jan 11 10:54:40 2019 video-part2.mp4
-rw-r--r--  1 nouser  none   302315567 Jan 11 10:54:40 2019 video-part3.mp4
-rw-r--r--@ 1 nouser  none  1597161158 Dec  2 13:12:57 2015 video.mp4
-rw-r--r--  1 nouser  none        1231 Jan 11 10:53:44 2019 videosplit.py
$ 
```

