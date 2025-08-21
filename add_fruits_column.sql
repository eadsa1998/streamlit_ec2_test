-- Add 'fruits' column to the 'food' table
ALTER TABLE food
ADD COLUMN fruits VARCHAR NOT NULL;

-- Note: If the table already contains data, you might need to provide a default value:
-- ALTER TABLE food
-- ADD COLUMN fruits VARCHAR NOT NULL DEFAULT 'Unknown';