from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.cache import cache
import qrcode
import StringIO


def qrcode_view(request, key, size=4):
    # size can be only between 1 and 10
    size = int(size)
    if size < 1 or size > 10:
        return HttpResponseRedirect(reverse('qrcode', args=(key, 4)))

    cache_key = "qrcode:" + key + str(size)
    c = cache.get(cache_key)
    if not c:
        img = qrcode.make(key, box_size=size)
        output = StringIO.StringIO()
        img.save(output, "PNG")
        c = output.getvalue()
        cache.set(cache_key, c, 60*60)
    return HttpResponse(c, mimetype="image/png")
