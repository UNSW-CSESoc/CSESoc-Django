class Ability
  include CanCan::Ability

  def initialize(user)
    can :read, :all
    
    # Rails Admin
    if user && user.admin?
      can :access, :rails_admin
      if user.role? :superadmin
        can :manage, :all
      end
    end
    
  end
end
