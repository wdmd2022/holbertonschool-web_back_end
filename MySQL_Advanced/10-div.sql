-- for this task we are creating a general function that can be used
-- in mysql for dividing two numbers safely; that is, if the divisor
-- is 0, we'll just return 0 and not complain about it
DELIMITER hasta-la-vista
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT
BEGIN
    DECLARE quotient FLOAT;
    SET quotient = 0;
    IF b != 0 THEN
        SET quotient = a / b;
    END IF;
    RETURN quotient;
END;
hasta-la-vista
DELIMITER ;
