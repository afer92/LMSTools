try:
    import urllib.parse
    urlmodule = urllib.parse
except ImportError:
    import urllib.request
    import urllib.parse
    import urllib.error
    urlmodule = urllib


class LMSUtils(object):

        @staticmethod
        def quote(text):
            return urlmodule.quote(text)

        @staticmethod
        def unquote(text):
            return urlmodule.unquote(text)
