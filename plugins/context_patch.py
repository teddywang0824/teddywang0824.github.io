from pelican import signals

# Global storage for articles
_ARTICLES = []

def store_articles(generator):
    """Store articles from the ArticleGenerator."""
    global _ARTICLES
    _ARTICLES = generator.articles

def inject_articles(generators):
    """Inject stored articles into the About page context."""
    global _ARTICLES
    
    # generators is a list of generators
    for generator in generators:
        if hasattr(generator, 'pages'):
            for page in generator.pages:
                if getattr(page, 'template', None) == 'about':
                    page.articles = _ARTICLES

def register():
    signals.article_generator_finalized.connect(store_articles)
    signals.all_generators_finalized.connect(inject_articles)
