class CreateStatics < ActiveRecord::Migration
  def self.up
    create_table :statics do |t|
      t.string :title
      t.text :content
      t.string :slug_name

      t.timestamps
    end
  end

  def self.down
    drop_table :statics
  end
end
