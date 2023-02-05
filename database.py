import psycopg2
import datetime

conn = psycopg2.connect(
                        host = "139.59.254.206",
                        port = 5432,
                        dbname = "jiande",
                        user = "postgres",
                        password = "password123"
                        )

def get_patient_detail():
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients")

    rows = cursor.fetchall()
    conn.commit()

    for row in rows:
        print(row)

    cursor.close()

    return rows

def get_patient_detail_expect(id):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE id != %s", id)

    rows = cursor.fetchall()
    conn.commit()

    for row in rows:
        print(row)

    cursor.close()

    return rows

def get_single_patient_detail(id):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE id = %s", id)

    rows = cursor.fetchall()
    conn.commit()

    print(rows)

    cursor.close()

    return rows

def get_single_patient_id(name):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE id = %s", name)

    rows = cursor.fetchall()
    conn.commit()

    print(rows)

    cursor.close()

    return rows  

def get_ecg_data(patient_id):
    cursor = conn.cursor()

    query = """
        SELECT * FROM ecg_data
        WHERE patient_id = %s
        ORDER BY timestamp DESC
        LIMIT 50;
    """
    cursor.execute(query, (patient_id,))
    rows = cursor.fetchall()

    ecg = []
    time = []
    i = 0
    for row in rows:
        i = i + 1
        ecg.append(row[2])
        timestamp = datetime.datetime.strptime(str(row[1]), "%Y-%m-%d %H:%M:%S.%f")
        formatted_date = timestamp.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        time.append(formatted_date)

    return ecg, time

def insert_ecg_data(patient_id, ecg):
    cursor = conn.cursor()

    query = """
        INSERT INTO ecg_data (patient_id, timestamp, ecg)
        VALUES (%s, %s, %s);
    """
    timestamp = datetime.datetime.now()
    cursor.execute(query, (patient_id, timestamp, ecg))
    conn.commit()

    print("Data inserted successfully")

def update_patient_location(patient_id, geolat, geolong):
    cursor = conn.cursor()

    query = """
        UPDATE patients SET  geolat = %s, geolong = %s WHERE id = %s;
    """
    cursor.execute(query, (geolat, geolong, patient_id))
    conn.commit()

    print("Location updated successfully")

    cursor.close()

def update_patient_data(patient_id, heartbeat, o2_saturation, bloodpressure):
    cursor = conn.cursor()

    query = """
        UPDATE patients SET  heartbeat = %s, o2_saturation = %s, bloodpressure = %s WHERE id = %s;
    """
    cursor.execute(query, (heartbeat, o2_saturation, bloodpressure, patient_id))
    conn.commit()

    print("Data updated successfully")

    cursor.close()

# update_patient_data(1, 1.53, 103.66)
# update_patient_data(2, 1.53, 103.62)
# update_patient_data(3, 1.52, 103.63)

a = [336, 324, 321, 348, 376, 392, 403, 417, 422, 414, 423, 440, 
    442, 438, 448, 460, 459, 454, 465, 478, 474, 469, 482, 493, 
    484, 480, 490, 498, 488, 486, 494, 488, 474, 474, 482, 477, 
    466, 470, 481, 481, 478, 489, 502, 499, 495, 506, 513, 502, 
    495, 504, 511, 507, 509, 520, 522, 518, 523, 540, 541, 531, 
    536, 546, 541, 531, 538, 547, 541, 535, 543, 547, 535, 523, 
    533, 538, 528, 519, 528, 532, 521, 519, 532, 535, 532, 537, 
    545, 535, 532, 560, 588, 582, 568, 566, 562, 552, 537, 542, 
    538, 517, 502, 510, 514, 506, 506, 512, 507, 488, 474, 498, 
    582, 763, 1024, 1024, 1024, 1024, 877, 548, 409, 379, 377, 
    376, 396, 436, 459, 453, 447, 459, 462, 457, 461, 474, 475, 
    469, 471, 481, 480, 474, 481, 494, 487, 476, 485, 495, 484, 
    474, 478, 481, 466, 456, 460, 459, 444, 437, 440, 440, 430, 
    437, 451, 451, 445, 450, 465, 461, 448, 451, 457, 448, 440, 
    449, 458, 449, 446, 456, 461, 454, 452, 464, 466, 456, 457, 
    464, 460, 449, 449, 456, 447, 433, 432, 438, 430, 415, 420,
    427, 417, 410, 415, 415, 402, 397, 405, 405, 397, 400, 415, 
    417, 404, 405, 427, 440, 442, 450, 451, 430, 406, 411, 415, 
    399, 378, 374, 369, 357, 356, 367, 368, 356, 353, 349, 331, 
    348, 457, 682, 978, 1024, 1024, 999, 613, 313, 258, 243, 213,
    217, 254, 284, 291, 294, 303, 302, 297, 306, 317, 310, 304,
    314, 324, 316, 312, 326, 331, 319, 316, 329, 330, 320, 321, 
    329, 328, 317, 317, 322, 312, 296, 296, 302, 291, 278, 286, 
    296, 293, 290, 303, 314, 306, 303, 314, 314, 304, 305, 315, 
    316, 307, 310, 325, 321, 316, 320, 330, 326, 318, 326, 332, 
    325, 318, 326, 332, 325, 318, 322, 327, 316, 312, 321, 321, 
    308, 304, 314, 312, 301, 300, 308, 306, 295, 296, 306, 303, 
    295, 307, 317, 306, 302, 331, 356, 350, 341, 342, 332, 316, 
    310, 317, 306, 282, 270, 276, 272, 264, 273, 282, 276, 262, 
    248, 248]
