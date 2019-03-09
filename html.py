import logging
import premailer
from io import StringIO
mylog = StringIO()
myhandler = logging.StreamHandler(mylog)
p = premailer.Premailer("""
    <html>
    <style type="text/css">
    @keyframes foo { from { opacity: 0; } to { opacity: 1; } }
    </style>
    <p>Hej</p>
    </html>""",
cssutils_logging_handler=myhandler,
cssutils_logging_level=logging.INFO)
result = p.transform()
mylog.getvalue()
        