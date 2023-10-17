-- with one successful index under our belts, we now turn to a much
-- trickier problem: creating an index that indexes the first letter
-- of name, as well as the score.
CREATE INDEX idx_name_first_score ON names(name(1), score);
