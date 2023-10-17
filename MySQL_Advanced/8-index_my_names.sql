-- ever have a really giant sql file that takes forever? well, in this
-- script we will create an index for a file names.sql that is so big
-- I can't even upload it to github
CREATE INDEX idx_name_first ON names(name(1));
