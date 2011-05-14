UNSW CSESoc Website
===================

How To Setup
------------

    rvm install 1.9.2
    rvm use 1.9.2  --default

    bundle install
    rake db:migrate
    rake db:seed
    rails server

Auth Module
-----------

A script similar to this needs to run on the CSESoc account on
a CSE Server to authenticate users.

    # Find the user if it exists
    u = User.where(:cse_username => params[:cse_username])
    if u.any?
      u = u.first
    else
      u = User.new
      u.cse_username = params[:cse_username]
    end
    
    # Give them a new token
    token = User.authentication_token
    u.authentication_token = token
    u.save
    
    # Redirect them back with the new auth token
    redirect_to("http://csesoc.unsw.edu.au/callback?auth_token=#{token}")

Changes from Django
-------------------

This list may be incomplete.

### Models

- User Model
  - Added
  - Added user sessions
  - TODO: Facebook integration
- Static Model
  - Text is now Content
  - Removed creator
  - Removed updater
  - Now uses Markdown
- NewsItem Model
  - Headline is now Title
  - Text is now Content
  - pubdate is now publish_date
  - Now uses Markdown
  - TODO: RSS Feed
- Event Model
  - TODO: implement controller and views
  - TODO: iCal RSS feed
- Beta Model
  - Removed
- Sponsor Model
  - Added Attachment
  - TODO: Resize sizes and layouts
- Suggestion Model
  - Changed sender to user_id
  - TODO: Needs Comment nested controller and routes
- Comment Model
  - name is now user_id
  - suggestion to now suggestion_id

### Design

- Made titles of news posts links to articles
- Made Cal and Sponsors only show on home page
- Added a notice flash
- TODO: Javascript notice flash
- A lot of logic in views was removed
- Fixed murder players been different from CSE users
- Can now log out properly
- No passwords or emails, only cse auth

### Development

- Added Capistrano, anyone with ssh key can deploy
- Added migrations for DB
- Added DB seeds

### TODO

- Murder
- Scheduler
- Campleaders
- Campattendees
- rspec
- Music
- Game

License
-------

    UNSW CSESoc Website
    Copyright (C) 2011  UNSW CSESoc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.