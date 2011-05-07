class StaticsController < ApplicationController

  def show
    @static = Static.find(params[:id])
  end

end
