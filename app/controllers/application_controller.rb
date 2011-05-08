class ApplicationController < ActionController::Base
  protect_from_forgery
  before_filter :load_sponsors
  
  rescue_from CanCan::AccessDenied do |exception|
    redirect_to root_url, :notice => exception.message
  end
  
  private
  def load_sponsors
    @sponsors = Sponsor.visible
  end
end
