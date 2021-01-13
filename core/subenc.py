from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip

'''
def encodesub(a, b, c):
    # a, b, c : video, subtitle, video with subtitles
    #try:
    myvideo = VideoFileClip(a)
    generator = lambda txt: TextClip(txt, font='Xolonium-Bold', fontsize=12, color='orange')
    sub = SubtitlesClip(b, generator)
    w = myvideo.w
    h = myvideo.h
    sub.pos=lambda t:(w*0.15,h*0.9)
    final = CompositeVideoClip([myvideo, sub])
    final.write_videofile(c, fps=myvideo.fps)
    #except:
        #print("Could not encode subtitles... Perhaps try one of these video types: mp4, avi or mov")
'''
def encodesub(a, b, c):
    # a, b, c : video, subtitle, video with subtitles
    myvideo = VideoFileClip(a)
    w = myvideo.w
    h = myvideo.h
    generator = lambda txt: TextClip(txt,size=(0.8*w, None), font='Xolonium-Bold', fontsize=int(w/40), color='white', stroke_color='black', stroke_width=(w/1400), method = 'caption')
    print(w/60)
    sub = SubtitlesClip(b, generator)
    sub.pos=lambda t:(w*0.1,h*0.82)
    final = CompositeVideoClip([myvideo, sub])
    final.write_videofile(c, fps=myvideo.fps)
