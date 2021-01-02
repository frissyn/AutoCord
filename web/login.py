from .models import User

from web import login_manager


@login_manager.user_loader
def load_user(user_id: int):
    try:
        result = User.query.filter_by(id=user_id).first()
        return result
    except Exception:
        return None
