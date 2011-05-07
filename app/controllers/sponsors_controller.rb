class SponsorsController < ApplicationController
  def index
    @sponsors = Sponsor.visible
  end
end
