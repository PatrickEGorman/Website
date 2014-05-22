__author__ = 'Patrick Gorman'

from flask import Flask, render_template
import system
import get_videos
import gdata.youtube
import gdata.youtube.service


#create instance of flask with name of python package
app = Flask(__name__)


@app.route('/<variable>')
def load_webpage(variable):
    if len(variable) == 11:
        video = "http://www.youtube.com/embed/" + variable
        if variable in video_ids:
            return render_template('template2.html', input=video_data, video_ids=video_ids, link=video,
                                   object=video_data[variable])
        else:
            try:
                yt_service = gdata.youtube.service.YouTubeService()
                yt_service.ssl = True
                entry = yt_service.GetYouTubeVideoEntry(video_id=variable)
                video_data[variable] = entry.media.title.text
                video_ids.append(variable)
                return render_template('template2.html', input=video_data, video_ids=video_ids, link=video,
                                       object=video_data[variable])
            except:
                return render_template('template1.html', input=video_data, video_ids=video_ids)


#default app route
@app.route('/')
def load_default():
    #load default template
    return render_template('template1.html', input=video_data, video_ids=video_ids)


#default app load
if __name__ == "__main__":
    #becomes true when server is reset
    startup = False
    video_data, video_ids = get_videos.load_videos()
    while not startup:
        try:
            #try to run app
            app.run(debug=True)
            #if app runs, loop breaks
            startup = True
        except:
            #resets server
            system.server_reset()