-- this sql script creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
-- Note: An average score can be a decimal
-- requirements include:
-- - Procedure ComputeAverageScoreForUser is taking 1 input:
-- -- user_id, a users.id value
-- -- - (you can assume user_id is linked to an existing users)
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
    DECLARE assignments INT DEFAULT 0;
    DECLARE total_score INT DEFAULT 0;
    DECLARE avg_score FLOAT DEFAULT 0;
    SELECT COUNT(*), COALESCE(SUM(c.score), 0) INTO assignments, total_score
    FROM corrections AS c
    WHERE c.user_id = user_id;
    IF assignments > 0 THEN
        SET avg_score = total_score / assignments;
    END IF;
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;
//
DELIMITER ;
