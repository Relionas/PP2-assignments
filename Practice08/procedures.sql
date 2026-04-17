-- -------------------------------------------------
-- Procedure: upsert_user
-- Insert new user or update phone if exists
-- -------------------------------------------------
DROP PROCEDURE IF EXISTS upsert_user(TEXT, TEXT);

CREATE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook
        SET phone = p_phone
        WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$;


-- -------------------------------------------------
-- Procedure: bulk_insert
-- Insert multiple users from arrays, validate phone
-- -------------------------------------------------
DROP PROCEDURE IF EXISTS bulk_insert(TEXT[], TEXT[]);

CREATE PROCEDURE bulk_insert(names TEXT[], phones TEXT[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    invalid_entries TEXT := '';
BEGIN
    FOR i IN 1 .. array_length(names, 1) LOOP
        -- Validate phone: must be digits only
        IF phones[i] ~ '^\d+$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = names[i]) THEN
                UPDATE phonebook
                SET phone = phones[i]
                WHERE name = names[i];
            ELSE
                INSERT INTO phonebook(name, phone)
                VALUES (names[i], phones[i]);
            END IF;
        ELSE
            invalid_entries := invalid_entries || names[i] || ': ' || phones[i] || '; ';
        END IF;
    END LOOP;

    IF invalid_entries <> '' THEN
        RAISE NOTICE 'Invalid entries: %', invalid_entries;
    END IF;
END;
$$;


-- -------------------------------------------------
-- Procedure: delete_contact
-- Delete user by name or phone
-- -------------------------------------------------
DROP PROCEDURE IF EXISTS delete_contact(TEXT);

CREATE PROCEDURE delete_contact(value TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = value OR phone = value;
END;
$$;
