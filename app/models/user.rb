class User < ActiveRecord::Base
  ROLES = ['admin', 'superadmin']
  
  has_many :events
  has_many :comments
  has_many :news_items
  has_many :suggestions
  
  devise :token_authenticatable, :rememberable, :trackable

  validates :cse_username, :presence => true, :uniqueness => true
  # Setup accessible (or protected) attributes for your model
  attr_accessible :remember_me
  
  # Determine email from CSE Username
  def email
    "#{cse_username}@cse.unsw.edu.au"
  end
  
  # Checks if a user is an admin
  def admin?
    ROLES.include?(self.role)
  end
  
  def role?(role)
    self.role == role.to_s
  end
end
