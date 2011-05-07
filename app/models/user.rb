class User < ActiveRecord::Base
  devise :token_authenticatable, :rememberable, :trackable

  # Setup accessible (or protected) attributes for your model
  attr_accessible :remember_me
end
