class NewsItem < ActiveRecord::Base
  belongs_to :author, :class_name => "User"
  
  has_friendly_id :title, :use_slug => true
  
  validates :title, :presence => true
  validates :content, :presence => true
  validates :publish_date, :presence => true
  validates :author, :presence => true
  
  scope :published, lambda { where "news_items.publish_date <= ?", Time.now}
  
  # If this news item is visible yet
  def published?
    DateTime.now >= self.publish_date
  end
end
