from datetime import datetime,timedelta

last_id = 0

class TodoTask():
    '''Am atomic todotask to use with todolist app'''

    def __init__(self,desc,deadline=3,tag=''):
        '''Initializer'''
        global last_id
        last_id+=1
        self.id = last_id
        self.desc = desc
        self.tag = tag
        self.creation_date = datetime.now()
        self.deadline = datetime.now() + timedelta(days=deadline)
        self.is_completed = False

    def match(self, filter):
        '''Searches for input'''
        return filter in self.desc or filter in self.tag

    def deadline_check(self):
        '''Checking wheter deadline has been breached'''
        if datetime.today() >= self.deadline:
            print('Note with desc: ' + self.desc +' has breached a deadline!')
            return True
        else:
            return False

    def __str__(self):
        return 'Task_id: ' + str(self.id) + ' Desc: ' + str(self.desc) + ' Deadline: ' + str(self.deadline)

if __name__ == '__main__':
    pass