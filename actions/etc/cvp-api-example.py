import requests
import json

CVP_HOST = "10.132.0.6"
CVP_USER = "cvpadmin"
CVP_PWD = "siesta3"

auth_data = json.dumps({'userId':CVP_USER,'password':CVP_PWD})
auth_url = "https://%s/cvpservice/login/authenticate.do" % CVP_HOST
auth_response = requests.post(auth_url, data=auth_data, verify=False)
assert auth_response.ok
cookies = auth_response.cookies

tasks_params = {'startIndex':'0','endIndex':'0'}
tasks_url = "https://%s/cvpservice/task/getTasks.do?" % CVP_HOST
tasks_response = requests.get(tasks_url, cookies=cookies, params=tasks_params, verify=False)
assert tasks_response.ok
tasks_json = tasks_response.json()
print(tasks_json)

tasks_data = tasks_json['data']
max_task_id = 0
for task in tasks_data:
    task_id = int(task['workOrderId'])
    if task_id > max_task_id:
        max_task_id = task_id

note_string = 'This task currently has the highest numerical ID'
note_data = json.dumps({'workOrderId':str(max_task_id),'note':note_string})
note_url = "https://%s/cvpservice/task/addNoteToTask.do" % CVP_HOST
note_response = requests.post(note_url, cookies=cookies, data=note_data, verify=False)
assert note_response.ok
print(auth_response)
