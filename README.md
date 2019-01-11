# videosplit

## Description
This program is a very simple application that leverages ffmpeg to split a video file into multipl pieces.

## Usage
Use the following command line:

```python videosplit.py {filename}```

You will need to pass the input filename to the application.   The input filename specifies the name of the original video file and then the points on which to split it.

The new files will be named with the original filename with a "-part #" appended to it.

## Example of input file
This is a example of a simple file:

```bash
video.mp4
00:00:00 00:00:50
00:00:50 00:03:00
00:03:00 00:07:00
00:07:00 00:09:00
00:09:00 99:99:99
```

This file when passed to videosplit will use the ```video.mp4``` as the input file and then will be split up in the following five files:

* Between 00:00:00 and 00:00:50
* Between 00:00:50 and 00:03:00
* Between 00:03:00 and 00:07:00
* Between 00:07:00 and 00:09:00
* Between 00:09:00 and 99:99:99 (Ending)

The following is the directory after the application is run:

```bash
$ls -l
total 5846528
-rw-r--r--  1 nouser  none        1026 Jan 11 10:55:52 2019 README.md
-rw-r--r--  1 nouser  none         100 Jan 11 10:50:37 2019 test.file
-rw-r--r--  1 nouser  none   127193901 Jan 11 10:54:31 2019 video-part 1.mp4
-rw-r--r--  1 nouser  none   327671607 Jan 11 10:54:33 2019 video-part 2.mp4
-rw-r--r--  1 nouser  none   606393559 Jan 11 10:54:36 2019 video-part 3.mp4
-rw-r--r--  1 nouser  none   302315567 Jan 11 10:54:40 2019 video-part 4.mp4
-rw-r--r--@ 1 nouser  none  1597161158 Dec  2 13:12:57 2015 video.mp4
-rw-r--r--  1 nouser  none        1231 Jan 11 10:53:44 2019 videosplit.py
$ 
```

