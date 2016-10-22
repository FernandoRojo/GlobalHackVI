from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from .models import Item

class ShelterFeed(Feed):
   feed_type = Rss201rev2Feed
   title = "Homeless Shelter Updates"
   link = "/index/"
   description = "Updates for resources available/needed in St Louis"

   def items(self):
      return Item.objects.all().order_by("-pub_date")[:5]
    
   def item_title(self, item):
      return item.Title
    
   def item_description(self, item):
      return item.description
    
   def item_link(self, item):
      return reverse('rssitem', kwargs = {'postid':item.id})
