class Event < ActiveRecord::Base
  belongs_to :author, :class_name => "User", :foreign_key => "author_id"
  
  has_friendly_id :name, :use_slug => true
  
  validates :name, :presence => true
  validates :time, :presence => true
  validates :location, :presence => true
  validates :description, :presence => true
  validates :publish_date, :presence => true
  validates :author, :presence => true
  
  validates_format_of :registration_email, :with => /^([\w\.%\+\-]+)@([\w\-]+\.)+([\w]{2,})$/i, :unless => lambda {|event| event.registration_email.blank?}
  validates_format_of :volunteers_email, :with => /^([\w\.%\+\-]+)@([\w\-]+\.)+([\w]{2,})$/i, :unless => lambda {|event| event.volunteers_email.blank?}
  
  scope :published, lambda { where "events.publish_date <= ?", Time.now}
  
  # If this event is visible yet
  def published?
    self.publish_date <= DateTime.now
  end
end
