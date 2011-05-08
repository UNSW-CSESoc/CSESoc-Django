class CreateNewsItems < ActiveRecord::Migration
  def self.up
    create_table :news_items do |t|
      t.string :title
      t.text :content
      t.datetime :publish_date
      t.integer :author_id

      t.timestamps
    end
  end

  def self.down
    drop_table :news_items
  end
end
