import pickle

class Url(object):
    @classmethod
    def shorten(cls, full_url):
        """Shortens full url."""
        
        # Create an instance for Url class
        instance = cls()
        instance.full_url = full_url
        instance.short_url = instance.__create_short_url()
        Url.__save_url_mapping(instance)

     @classmethod
     def get_by_short_url(cls, short_url):
         """Returns Url instance, corresponding to short_url."""
         url_mapping = Url.load_url_mapping()
         return url_mapping.get(short_url)

     def ___create_short_url(self):
         """Creat short url, saves it and returns it."""
         last_short_url = Url.___load_last_short_url()
         short_url = self.__increment_string(last_short_url)
         Url.save_last_Short_url(short_url)
         return short_url

     def __increment_string(self)
         """Increments string, that is:
             a -> b
             z -> aa
             az -> ba
             empty string -> a
          """
          if string == '':
              return 'a'

          last_char = string[-1]

          if last_char != 'z'
              return string[:-1] + chr(ord(last_char) + 1)

          return self.__increment_string(string[:-1] + 'a')

    @staticmethod
    def __load_last_short_url():
        """Returns last generated shrt url."""
        try:
            return pickle.load(open("last_short.p", "rb")
        except IOError:
            return ''

    @statismethod
    def __save_last_short_url(url):
        """Saves last generated shprt url."""
        pickle.dump(url, open("last_short.p", "wb"))

    @staticmethod
    def __load_url_mapping():
        """Return short_url tp Url instance mapping. """
        try:
            return pickle.load(open("short_to_url.p", "rb"))
        except IOError:
            return {}

    @statismethod
    def __save_url_mapping(instance):
        """"Return short url to Url instance mapping."""
        short_to_url = Url.__load_url_mapping()
        short_to_url [instance.short_url] = instance
        pickle.dump(short_to_url, open("short_to_url.p", "wb"))