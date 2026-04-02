-- procedures.sql

-- Upsert: вставка или обновление
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

-- Bulk insert с проверкой телефона
CREATE OR REPLACE PROCEDURE bulk_insert(users TEXT[][])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
    invalid_users TEXT[] := '{}';
BEGIN
    FOR i IN array_lower(users,1)..array_upper(users,1) LOOP
        IF users[i][2] ~ '^\d{10,15}$' THEN
            CALL upsert_user(users[i][1], users[i][2]);
        ELSE
            invalid_users := array_append(invalid_users, users[i][1] || ':' || users[i][2]);
        END IF;
    END LOOP;

    IF array_length(invalid_users,1) IS NOT NULL THEN
        RAISE NOTICE 'Invalid users: %', invalid_users;
    END IF;
END;
$$;

-- Удаление по имени или телефону
CREATE OR REPLACE PROCEDURE delete_user(value TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE name = value OR phone = value;
END;
$$;
