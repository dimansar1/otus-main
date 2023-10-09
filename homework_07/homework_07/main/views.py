from django.shortcuts import render
from main.models import Video
# from django.views.generic import FormView

# class VideoForm(FormView):
#     name = StringField(
#         label="Video name:",
#         validators=[
#             DataRequired(),
#             Length(min=3),
#         ],
#     )
#     link = StringField(
#         label="Video link:",
#         validators=[
#             DataRequired(),
#             Length(min=3),
#         ],
#     )

# Create your views here.
def index(request):
    return render(request, "index.html")

def get_videos_list(request):
    videos = Video.objects.all()
        
    context = {
        'videos': videos,
    }
    return render(request, 'videos/list.html', context=context)

def get_video_details(request, video_id):
    video = Video.objects.get(pk=video_id)

    context = {
        'video': video,
    }
    return render(request, "videos/details.html", context)

################################################################
def create_new_video(request):
    return render(request, "videos/add.html")
    # form = VideoForm()
    # if request.method == "GET":
    #     return render_template("videos/add.html", form=form)

    # if not form.validate_on_submit():
    #     return render_template("videos/add.html", form=form), 400

    # watch=form.data["link"].split("=")[1]
    # video = Video(name=form.data["name"], link=form.data["link"], watch=watch)
    # db.session.add(video)
    # db.session.commit()
    # url = url_for("videos_app.details", video_id=video.id)
    # flash(f"Created video {video.name!r}", category="primary")
    # return redirect(url)


# def confirm_delete_video(request, video_id: int):
#     video = get_video_by_id(video_id=video_id)
#     if request.method == "GET":
#         return render_template("videos/confirm-delete.html", video=video)

#     video_name = video.name
#     db.session.delete(video)
#     db.session.commit()
#     flash(f"Deleted video {video_name!r}", category="warning")
#     url = url_for("videos_app.list")
#     return redirect(url)
