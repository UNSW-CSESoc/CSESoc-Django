class Event < ActiveRecord::Base
  belongs_to :author, :class_name => "User"
  
  has_friendly_id :name, :use_slug => true
  
  validates :name, :presence => true
  validates :time, :presence => true
  validates :location, :presence => true
  validates :description, :presence => true
  validates :publish_date, :presence => true
  validates :author, :presence => true
  
  validates :registration_required, :presence => true
  validates :registration_email, 
    :format => {:with => /^([\w\.%\+\-]+)@([\w\-]+\.)+([\w]{2,})$/i}
  validates :volunteers_required, :presence => true
  validates :volunteers_email,
    :format => {:with => /^([\w\.%\+\-]+)@([\w\-]+\.)+([\w]{2,})$/i}
  
  scope :published, lambda { where "events.publish_date <= ?", Time.now}
  
  # If this event is visible yet
  def published?
    DateTime.now >= self.publish_date
  end
end
