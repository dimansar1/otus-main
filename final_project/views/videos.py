from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask import flash

from models import db, Video
from .forms.videos import VideoForm


videos_app = Blueprint(
    "videos_app",
    __name__,
    url_prefix="/videos",
)


@videos_app.get("/", endpoint="list")
def get_videos_list():
    videos: list[Video] = Video.query.order_by(Video.id).all()
    return render_template("videos/list.html", videos=videos)


def get_video_by_id(video_id: int) -> Video:
    return Video.query.get_or_404(
        video_id,
        description=f"Video #{video_id} not found!",
    )


@videos_app.get("/<int:video_id>/", endpoint="details")
def get_video_details(video_id: int):
    video = get_video_by_id(video_id=video_id)
    return render_template("videos/details.html", video=video)


@videos_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_new_video():
    form = VideoForm()
    if request.method == "GET":
        return render_template("videos/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("videos/add.html", form=form), 400

    watch=form.data["link"].split("=")[1]
    video = Video(name=form.data["name"], link=form.data["link"], watch=watch)
    db.session.add(video)
    db.session.commit()
    url = url_for("videos_app.details", video_id=video.id)
    flash(f"Created video {video.name!r}", category="primary")
    return redirect(url)


@videos_app.route(
    "/<int:video_id>/confirm-delete/",
    methods=["GET", "POST"],
    endpoint="confirm-delete",
)
def confirm_delete_video(video_id: int):
    video = get_video_by_id(video_id=video_id)
    if request.method == "GET":
        return render_template("videos/confirm-delete.html", video=video)

    video_name = video.name
    db.session.delete(video)
    db.session.commit()
    flash(f"Deleted video {video_name!r}", category="warning")
    url = url_for("videos_app.list")
    return redirect(url)
