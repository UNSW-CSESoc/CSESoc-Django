class CommentsController < ApplicationController
  def create
    @comment = Comment.new(params[:comment])
    
    @comment.suggestion = Suggestion.find(params[:suggestion_id])
    @comment.user = current_user
    
    if @comment.save
      respond_to do |f|
        f.html {redirect_to @comment.suggestion, :notice => "Thanks for your comment!"}
        f.js # Renders RJS template
      end
    else
      respond_to do |f|
        f.html {redirect_to @comment.suggestion, :notice => "Sorry, your comment could not be saved."}
        f.js # Renders RJS template
      end
    end
    
  end
  
end