from django import template

register = template.Library()

# Secs to mins:secs
@register.filter()
def secs_to_minsecs(s):
    try:
        mins = int(s / 60)
        secs = s - (mins * 60)
    except:
        mins = 99
        secs = 99
    return "%02d:%02d" % (mins, secs)

# Timedelta to mins:secs
@register.filter()
def td_to_minsecs(timedeltaobj):
    s = timedeltaobj.total_seconds()
    try:
        mins = int(s / 60)
        secs = s - (mins * 60)
    except:
        mins = 99
        secs = 99
    return "%02d:%02d" % (mins, secs)
