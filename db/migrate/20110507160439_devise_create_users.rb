class DeviseCreateUsers < ActiveRecord::Migration
  def self.up
    create_table(:users) do |t|
      t.token_authenticatable
      t.rememberable
      t.trackable
      t.string :cse_username

      t.timestamps
    end

    add_index :users, :authentication_token, :unique => true
  end

  def self.down
    drop_table :users
  end
end
