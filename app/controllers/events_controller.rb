class EventsController < ApplicationController
  before_filter :public_post, :only => :show

  def index
    @events = Event.published

    respond_to do |format|
      format.html # index.html.erb
      # format.xml # TODO: Format as .ical
    end
  end

  def show
    @event = Event.find(params[:id])
  end
  
  private
  
  def public_post
    @event = Event.find(params[:id])
    unless @event.published?
      redirect_to(:action => :index, :notice => "Event not available yet.")
    end
  end
end
