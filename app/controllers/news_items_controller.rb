class NewsItemsController < ApplicationController
  before_filter :public_post, :only => :show

  def index
    @news_items = NewsItem.all

    respond_to do |format|
      format.html
      # format.xml # TODO: Create builder feed, use as RSS + Feedburner
    end
  end

  def show
    @news_item = NewsItem.find(params[:id])
  end
  
  private
  
  def public_post
    @news_item = NewsItem.find(params[:id])
    unless @news_item.published?
      redirect_to(:action => :index, :notice => "Post not available yet.")
    end
  end
end
