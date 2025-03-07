class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if (type(value) is str) and (not hasattr(self, 'title')) and (5 <= len(value) <= 50):
            self._title = value


    @property
    def author_getter(self):
        return self.author

    @author_getter.setter
    def author(self, value):
        if type(value) == Author:
            self._author = value


    @property
    def magazine_getter(self):
        return self.magazine

    @magazine_getter.setter
    def magazine(self, value):
        if type(value) == Magazine:
            self._magazine = value



class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name_getter(self):
        return self._name

    @name_getter.setter
    def name(self, name_value):
        if (not hasattr(self, 'name')) and (type(name_value) == str) and (len(name_value) > 0):
            self._name = name_value


    def articles(self):
        return [article for article in Article.all if article.author is self]


    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))


    def add_article(self, magazine, title):
        return Article(self, magazine, title)



    def topic_areas(self):
        if not self.articles:
            return None
        categories = set(article.magazine.catergory for article in self._articles)
        return list(categories)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def magazine_name_getter(self):
        return self._name

    @magazine_name_getter.setter
    def name(self, name_value):
       if (type(name_value) == str) and (2 <= len(name_value) <= 16):
           self._name = name_value


    @property
    def category_getter(self):
        return self._category

    @category_getter.setter
    def category(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._category = value


    def articles(self):
        return [article for article in Article.all if article.magazine is self]


    def contributors(self):
       return list(set([article.author for article in self.articles()]))


    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self._articles]


    def contributing_authors(self):
        pass