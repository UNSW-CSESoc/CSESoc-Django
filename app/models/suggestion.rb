class Suggestion < ActiveRecord::Base
  has_many :comments
  belongs_to :user
  
  validates :subject, :presence => true
  validates :message, :presence => true
  validates :user, :presence => true
end
