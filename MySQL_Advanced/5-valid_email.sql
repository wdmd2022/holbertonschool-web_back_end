-- this sql script creates a trigger that resets the attribute
-- `valid_email` only when `email` has been changed
DELIMITER //
CREATE TRIGGER invalidate_email BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
