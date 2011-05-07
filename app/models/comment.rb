class Comment < ActiveRecord::Base
  belongs_to :suggestion
  belongs_to :user
  
  validates :suggestion_id, :presence => true
  validates :user, :presence => true
  validates :comment, :presence => true
end
