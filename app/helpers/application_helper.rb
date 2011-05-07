module ApplicationHelper
  
  # A page's title
  def page_title(y)
    y = "#{y} - " unless y.empty?
    "#{y}CSESoc - UNSW Computer Science and Engineering Society"
  end
  
  # Link's to static content that may not exist
  def static_content_path(name)
    Static.find(name)
  end
  
end
