class SuggestionsController < ApplicationController
  def index
    @suggestions = Suggestion.all
  end

  def show
    @suggestion = Suggestion.find(params[:id])
  end

  def new
    @suggestion = Suggestion.new
  end

  def create
    @suggestion = Suggestion.new(params[:suggestion])
	@suggestion.user = current_user
	
    if @suggestion.save
      redirect_to(@suggestion, :notice => 'Thanks for your suggestion.') 
    else
      render :action => "new"
    end
  end

end
