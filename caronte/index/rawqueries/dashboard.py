# Python
from datetime import datetime
# Project
from caronte.users.models import User


def select_current_status(user: User) -> str:
    return f"""
    
    SELECT * FROM details_detail det
    
    RIGHT JOIN dailies_daily day
    ON day.id = det.daily_id
    
    RIGHT JOIN periods_period per
    ON per.id = day.period_id
    
    """
