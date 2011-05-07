module ApplicationHelper
  # Link's to static content that may not exist
  def static_content_path(name)
    begin
      return Static.find(name)
    rescue
      return root_path
    end
  end
end
