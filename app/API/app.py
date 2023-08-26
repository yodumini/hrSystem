from flask import Flask, request, jsonify
from utils import connect_DB

app = Flask(__name__)

@app.route('/clockinout', methods=['POST'])
def clock_in_out():
    try:
        name = request.values.get("name")

        engine, con = connect_DB()
        sql = f'''INSERT INTO employee.e_attend (name, clock_date, clock_in_time, clock_out_time, working_hours, update_time)
                    VALUES ('{name}', date(NOW()), NOW(), NULL, NULL, NOW())
                    ON DUPLICATE KEY UPDATE clock_out_time = NOW(), working_hours=TIMEDIFF(clock_out_time, clock_in_time), update_time=NOW();'''
        con.execute(sql)
        con.close()
        engine.dispose()
        return {
            'message': 'Clock-in/out recorded successfully',
            'name': name,
        }
    except:
        return {"message": "error"}

@app.route('/index', methods=['GET'])
def index():
    return {"message": "hello"}

if __name__ == '__main__':
    app.run('0.0.0.0')
