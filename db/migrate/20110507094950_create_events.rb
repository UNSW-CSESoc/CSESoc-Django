class CreateEvents < ActiveRecord::Migration
  def self.up
    create_table :events do |t|
      t.string :name
      t.datetime :time
      t.string :location
      t.boolean :registration_required
      t.string :registration_email
      t.boolean :volunteers_required
      t.string :volunteers_email
      t.text :description
      t.datetime :publish_date
      t.integer :author_id

      t.timestamps
    end
  end

  def self.down
    drop_table :events
  end
end
