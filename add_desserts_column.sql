-- Add 'desserts' column to 'food' table
ALTER TABLE food
ADD COLUMN desserts VARCHAR NOT NULL DEFAULT 'Unknown';

-- Remove the default constraint after adding the column
ALTER TABLE food
ALTER COLUMN desserts DROP DEFAULT;

-- Comment explaining the change
COMMENT ON COLUMN food.desserts IS 'Stores information about desserts related to the food item';