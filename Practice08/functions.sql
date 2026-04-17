-- -------------------------------------------------
-- Function: search_pattern
-- Returns all phonebook entries matching pattern
-- -------------------------------------------------
DROP FUNCTION IF EXISTS search_pattern(TEXT);

CREATE FUNCTION search_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR(100), phone VARCHAR(100)) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || pattern || '%'
       OR p.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


-- -------------------------------------------------
-- Function: get_paginated
-- Returns phonebook entries with pagination
-- -------------------------------------------------
DROP FUNCTION IF EXISTS get_paginated(INT, INT);

CREATE FUNCTION get_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(id INT, name VARCHAR(100), phone VARCHAR(100)) AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;
