class ApplicationController < ActionController::Base
  protect_from_forgery
  before_filter :load_sponsors
  
  private
  def load_sponsors
    @sponsors = Sponsor.visible
  end
end
