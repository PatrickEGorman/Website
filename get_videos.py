from models import Video


def load_videos():
    videos = Video.query.all()
    video_data = {}
    video_ids = []
    for x in videos:
        video_data[x.video_id] = x.video_name
        video_ids.append(x.video_id)
    return video_data, video_ids