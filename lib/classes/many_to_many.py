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
    def title(self, title_value):
        if hasattr(title_value, '_title'):
            return
        elif not isinstance(title_value, str):
            return
        elif not (5 <= len(title_value) <= 50):
            return
        else:
            self._title = title_value


    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_value):
        if isinstance(author_value, Author):
            self._author = author_value


    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine_value):
        if isinstance(magazine_value, Magazine):
            self._magazine = magazine_value



class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_value):
        if hasattr(self, '_name'):
            return
        elif not isinstance(name_value, str):
            return
        elif len(name_value) == 0:
            return
        else:
            self._name = name_value



    def articles(self):
        return list(set([article for article in Article.all if article.author == self]))


    def magazines(self):
        return list(set([article.magazine for article in Article.all if article.author == self]))


    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article


    def topic_areas(self):
        author_articles = [article for article in Article.all if article.author == self]
        if not author_articles:
            return None

        return list(set(article.magazine.category for article in author_articles))



class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_value):
        if not isinstance(name_value, str):
            return
        elif len(name_value) > 16 or len(name_value) < 2 :
            return
        else:
            self._name = name_value


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category_value):
        if not isinstance(category_value, str):
            return
        elif not len(category_value) > 0 :
            return
        else:
            self._category = category_value



    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set([authors.author for authors in Article.all if authors.magazine == self]))

    def article_titles(self):

        magazine_articles = [article for article in Article.all if article.magazine == self]

        if not magazine_articles:
            return None

        return [article.title for article in magazine_articles]


    def contributing_authors(self):
        magazine_articles = [article for article in Article.all if article.magazine == self]

        author_counts = {}
        for article in magazine_articles:
            if article.author in author_counts:
                author_counts[article.author] += 1
            else:
                author_counts[article.author] = 1

        contributing_authors = [author for author, count in author_counts.items() if count > 2]

        return contributing_authors if contributing_authors else None