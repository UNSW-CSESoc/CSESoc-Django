class Static < ActiveRecord::Base
  has_friendly_id :slug_name, :use_slug => true
  
  validates :title, :presence => true
  validates :content, :presence => true
  validates :slug_name, :presence => true
end
