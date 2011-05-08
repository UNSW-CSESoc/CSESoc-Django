class User < ActiveRecord::Base
  devise :token_authenticatable, :rememberable, :trackable

  validates :cse_username, :presence => true, :uniqueness => true
  # Setup accessible (or protected) attributes for your model
  attr_accessible :remember_me
end
