#!/mnt/d/projects/separe-sounds/.env/bin/python
# -*- coding: utf-8 -*-

from spleeter.separator import Separator

separator = Separator('spleeter:2stems')

audio_file = 'music/input/music.mp3'
destination = 'music/output'

separator.separate_to_file(audio_file, destination)
