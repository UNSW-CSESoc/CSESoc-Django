class Sponsor < ActiveRecord::Base
  has_friendly_id :title, :use_slug => true
  has_attached_file :image, :styles => { :medium => "300x300>", :thumb => "100x100>" }
  
  validates :name, :presence => true
  validates :website, :presence => true
  validates :alt_text, :presence => true
  validates :start_date, :presence => true
  validates :expiry_date, :presence => true
  
  scope :visible, lambda { where "sponsors.expiry_date >= ?", Time.now}
  
  # If this sponsor is currently visible
  def visible?
    self.expiry_date >= DateTime.now
  end
end
