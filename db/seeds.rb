# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rake db:seed (or created alongside the db with db:setup).
#
# Examples:
#
#   cities = City.create([{ :name => 'Chicago' }, { :name => 'Copenhagen' }])
#   Mayor.create(:name => 'Daley', :city => cities.first)

Static.create :title => "About CSESoc", :content => "About CSESoc.", :slug_name => "about"
Static.create :title => "A Brief History of CSESoc", :content => "History of CSESoc.", :slug_name => "history"
Static.create :title => "Constitution", :content => "CSESoc Constitution.", :slug_name => "constitution"
Static.create :title => "CSESoc Exec & Heads", :content => "Exec & Heads", :slug_name => "execheads"
Static.create :title => "Working Groups", :content => "Working groups.", :slug_name => "workinggroups"
Static.create :title => "Beta", :content => "Beta.", :slug_name => "workinggroupsbeta"
Static.create :title => "Publicity", :content => "Publicity.", :slug_name => "workinggroupspublicity"
Static.create :title => "Social", :content => "Social.", :slug_name => "workinggroupssocial"
Static.create :title => "Sysadmin", :content => "Sysadmin.", :slug_name => "workinggroupssysadmin"
Static.create :title => "Tech", :content => "Tech.", :slug_name => "workinggroupstech"
Static.create :title => "Volunteer!", :content => "Volunteer.", :slug_name => "workinggroupsvolunteer"
Static.create :title => "Students", :content => "Students.", :slug_name => "students"
Static.create :title => "Murder", :content => "Murder.", :slug_name => "murder"
Static.create :title => "Bling", :content => "Bling.", :slug_name => "bling"
Static.create :title => "Games", :content => "Games.", :slug_name => "games"
Static.create :title => "IRC", :content => "Irc.", :slug_name => "irc"
Static.create :title => "Contact Us", :content => "Contact us.", :slug_name => "contact"