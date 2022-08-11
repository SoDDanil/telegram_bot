import psycopg2

answer_id = []
question_text = []
answer_text = dict()

def collect_data():
    conn = psycopg2.connect(dbname='telegram_bot', user='postgres', password='0CLmtkoE65A', host='localhost')
    cursor = conn.cursor()

    cursor.execute('select answer_id,answer_text from answer;')
    records = cursor.fetchall()
    for row in records:
        answer_text[row[0]] = row[1] 

    cursor.execute('select question,answer_id from question;')
    records = cursor.fetchall()
    for row in records:
        answer_id.append(row[1])
        question_text.append(row[0])

    cursor.close()
    conn.close()

    print(answer_text)
    print(question_text)
    print(answer_id)

def main(question):
    collect_data()
    buf = question_text.index(question)
    number_answer = answer_id[buf]
    answer = answer_text[number_answer]
    return answer



