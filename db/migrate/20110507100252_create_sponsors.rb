class CreateSponsors < ActiveRecord::Migration
  def self.up
    create_table :sponsors do |t|
      t.string :name
      t.text :description
      t.string :website
      t.string :alt_text
      t.integer :amount_paid
      t.datetime :start_date
      t.datetime :expiry_date
      t.text :html_override
      
      t.string :image_file_name
      t.string :image_content_type
      t.integer :image_file_size
      t.datetime :image_updated_at

      t.timestamps
    end
  end

  def self.down
    drop_table :sponsors
  end
end
