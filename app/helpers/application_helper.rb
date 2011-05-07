module ApplicationHelper
  
  # A page's title
  def page_title(y)
    y = "#{y} - " unless y.empty?
    "#{y}CSESoc - UNSW Computer Science and Engineering Society"
  end
  
  # Link's to static content that may not exist
  def static_content_path(name)
    begin
      return Static.find(name)
    rescue
      return root_path
    end
  end
  
end
