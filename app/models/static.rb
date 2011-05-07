class Static < ActiveRecord::Base
  has_friendly_id :slug, :use_slug => true
  
  validates :title, :presence => true
  validates :content, :presence => true
  validates :slug, :presence => true
end
