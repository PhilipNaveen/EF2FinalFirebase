-- Inserting into cameras table
INSERT INTO cameras (serial_no, location_short, location_long, created_at)
VALUES 

    ('ACCC8EF6B105', 'Science & Engineering', 'SEL Main Entry C120', '2023-10-16 13:08:26'),
    ('ACCC8EF8C88D', 'Science & Engineering', 'SEL Lower Level Stairwell C054', '2023-10-16 13:08:26'),
    ('ACCC8EF93563', 'Science & Engineering', 'SEL Lower Level Stairwell C059', '2023-10-16 13:08:26'),
    ('ACCC8EF93510', 'Science & Engineering', 'SEL Lower Level Stairwell C048', '2023-10-16 13:08:26'),
    ('B8A44F59727B', 'Clemons', '007 - 2nd Floor - West Exit', '2023-10-16 13:08:26'),
    ('B8A44F5972AC', 'Clemons', '006 - 2nd Floor - North Exit', '2023-10-16 13:08:26'),
    ('ACCC8EF00E27', 'Clemons', '001A- 4th Floor - Main Entrance Camera 1', '2023-10-16 13:08:26'),
    ('ACCC8EF03363', 'Clemons', '001D - 4th Floor - Main Entrance Camera 4', '2023-10-16 13:08:26'),
    ('ACCC8EF03315', 'Clemons', '003 - 3rd Floor - Stairwell Exit', '2023-10-16 13:08:26'),
    ('ACCC8EF02852', 'Clemons', '001B - 4th Fl - Main Entrance Camera 2', '2023-10-16 13:08:26'),
    ('ACCC8EF031BC', 'Clemons', '004 - 3rd Floor - Emergency Exit', '2023-10-16 13:08:26'),
    ('B8A44F10A1F7', 'Clemons', 'Axis-B8A44F10A1F7', '2023-10-16 13:08:26'),
    ('ACCC8EF032BF', 'Clemons', '002 - 3rd Floor - North Exit', '2023-10-16 13:08:26'),
    ('ACCC8EF00DA0', 'Clemons', '001C - 4th Fl - Main Entrance Camera 3', '2023-10-16 13:08:26'),
    ('B8A44F07125E', 'Clemons', 'Axis-B8A44F07125E', '2023-10-16 13:08:26'),
    ('ACCC8EF00E06', 'Clemons', 'Axis-ACCC8EF00E06', '2023-10-16 13:08:26'),
    ('ACCC8EF02A0E', 'Clemons', 'Axis-ACCC8EF02A0E', '2023-10-16 13:08:27'),
    ('B8A44F4F1939', 'Music', 'OldCabell-B8A44F4F1939', '2023-10-16 13:08:27'),
    ('B8A44F4F195D', 'Fine Arts', 'FiskeKimball-B8A44F4F195D', '2023-10-16 13:08:27');

-- Inserting into rawmetrics table
INSERT INTO rawmetrics (source, serial_no, occupancy, count_in, count_out, source_unixtime, created_at)
VALUES 
    ('sum', 'ACCC8EF02852', 0, 41, 24, 1684972824, '2023-10-16 14:16:48'),
    ('sum', 'ACCC8EF03315', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('sum', 'B8A44F4F1939', 0, 33, 31, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF6B105', 5, 206, 201, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'B8A44F4F195D', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF8C88D', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF93563', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF93510', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'B8A44F59727B', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'B8A44F5972AC', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF00E27', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF03363', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF031BC', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'B8A44F10A1F7', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF032BF', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF00DA0', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'B8A44F07125E', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF00E06', 0, 0, 0, 1684972824, '2023-10-16 14:16:48'),
    ('occupancy', 'ACCC8EF02A0E', 0, 0, 0, 1684972824, '2023-10-16 14:16:48');

-- Inserting into rawmetrics_occupancy table
INSERT INTO rawmetrics_occupancy (serial_no, occupancy, total_in, total_out, date, time, day, dow)
VALUES 
    ('ACCC8EF6B105', 5, 206, 201, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('B8A44F4F195D', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF8C88D', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF93563', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF93510', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('B8A44F59727B', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('B8A44F5972AC', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF00E27', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF03363', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF031BC', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('B8A44F10A1F7', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF032BF', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF00DA0', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('B8A44F07125E', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF00E06', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF02A0E', 0, 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3);

-- Inserting into rawmetrics_sum table
INSERT INTO rawmetrics_sum (serial_no, count_in, count_out, date, time, day, dow)
VALUES 
    ('ACCC8EF02852', 41, 24, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('ACCC8EF03315', 0, 0, '2023-05-24', '20:00:24', 'Wednesday', 3),
    ('B8A44F4F1939', 33, 31, '2023-05-24', '20:00:24', 'Wednesday', 3);
