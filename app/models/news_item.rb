class NewsItem < ActiveRecord::Base
  has_friendly_id :title, :use_slug => true
  
  validates :title, :presence => true
  validates :content, :presence => true
  validates :publish_date, :presence => true
  validates :author, :presence => true
  
  scope :published, lambda { where "news_items.publish_date <= ?", Time.now}
  
  # If this post is visible yet
  def published?
    DateTime.now > self.publish_date
  end
end
