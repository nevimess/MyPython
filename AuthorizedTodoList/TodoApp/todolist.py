from TodoApp import todotask
import sys
import json
from datetime import datetime,timedelta
import traceback
import os


class TodoList():
    '''Todo list for Todo app'''

    actions = ['1. View list', '2 Add task', '3 Remove task', '4. Mark complete', '5 Remove done', '6 Check overdued','7 Dump to JSON', '8 Load from JSON', '9 Quit']

    def __init__(self,username="default"):
        '''Initializer'''
        self.tasklist = []
        self.username = username
        self.filestring = str(username)+".json"

        #with open(self.filestring,'r') as file:
         #   jstmp = json.load(file)
          #  print(json)
           # file.close()
        try:
            self.tasklist = self.load_from_json_dump(self.filestring)
            print(self.tasklist.__class__)
            print(self.tasklist)
            # not isinstance(self.tasklist,list):
            #    sys.exit(666)
        except Exception as e:
            print(e.__class__)
            print(e.args)

    def add_task(self,tag=''):
        '''Adding task to tasklist'''
        try:
            desc = raw_input('Enter a description: \n')
            if  not isinstance(desc,str):
                raise ValueError
            deadline = raw_input('Provide a deadline: \n')
            if not isinstance(int(deadline),int):
                raise ValueError
            #print(self.tasklist.__class__)
            #print(self.tasklist)
            self.tasklist.append(todotask.TodoTask(str(desc), int(deadline), tag))
        except ValueError:
            print('Value error in add_task')
            return False


    def remove_task(self):
        '''Removing specified task'''
        try:
            desc = input('Select a desc to be removed \n')
            if not isinstance(desc,str):
                raise ValueError
            for task in self.tasklist:
                if (task.match(desc)):
                    print('Found and removed requested task!')
                    self.tasklist.remove(task)
                    return True
            print('None have been found')
            return False
        except ValueError:
            print('Value error in remove_task')
            return False

    def view_list(self):
        '''Viewing entire list'''
        if not self.tasklist:
            print('List is empty')
            return False
        else:
            for task in self.tasklist:
                print(task)
            return True

    def mark_complete(self):
        '''Marking desc task as completed'''
        try:
            desc = input('Input description of task to be marked as complete: \n')
            if isinstance(desc,str):
                for task in self.tasklist:
                    if (task.desc) == desc:
                        task.is_completed = True
                        print('Task has beed set on coplete.')
                        return True
                print('Task not found')
                return False
        except ValueError:
            print('ValueError in mark_complete function!')
            return False

    def remove_done(self):
        '''Remove completed task'''
        print('Removing completed objects')
        for task in self.tasklist:
            if(task.is_completed):
                self.tasklist.remove(task)
                return True
        else:
            print('No object specified found')
            return False

    def check_overdued(self):
        '''Checking for overdued tasks'''
        for task in self.tasklist:
            task.deadline_check()

    def dump_into_json(self,filename):
        '''Dumping file into JSON'''
        tmpDict = {}
        boolean = None
        for task in self.tasklist:
            tmpDict[str(task.id)] = [(str(task.desc)), (str(task.creation_date)), (str(task.deadline)), task.is_completed]
        try:
            with open(filename,'w') as f:
                json.dump(tmpDict,f)
            print('Dumping completed!')
            #self.tasklist = []
            boolean = True
        except Exception as dump_exception:
            print('Something is wrong with file.')
            print(dump_exception)
            boolean = False
        finally:
            f.close()
            return boolean

    def load_from_json_dump(self,filename):
        '''Loading dumped json data'''
        tasklist = []
        try:
            #with open(filename,'w') as f:
            #   f.close()
            with open(filename,'a+') as f:
                tmpDict = json.load(f)       ## ----> ERROR PLACE
                for key,value in tmpDict.items():
                    task = todotask.TodoTask(value[0])
                    task.id = int(key)
                    task.creation_date = datetime.strptime(str(value[1]),"%Y-%m-%d %X.%f")
                    task.deadline = datetime.strptime(str(value[2]),"%Y-%m-%d %X.%f")
                    if str(value[3]) == 'true':
                        task.is_completed = True
                    else:
                        task.is_completed = False
                    tasklist.append(task)
        except ValueError:
            pass
        except Exception as load_exception:
            print('Exception occurred in loading json file')
            print(load_exception.__class__)
            print(load_exception.args)
            tasklist = []
        finally:
            f.close()
            return tasklist

    def clean_json_file(self):
        '''Deleting json file'''
        os.remove(self.filestring)

    def change_username(self,username):
        self.username=username
        self.filestring = str(username) + ".json"
        self.tasklist = self.load_from_json_dump(self.filestring)

    def main(self):
        '''Main method for application'''
        for action in self.actions:
            print(action)
        while True:
            cmd = input('Choose a command')
            if int(cmd) == 1:
                self.view_list()
            elif int(cmd) == 2:
                self.add_task()
            elif int(cmd) == 3:
                self.remove_task()
            elif int(cmd) == 4:
                self.mark_complete()
            elif int(cmd) == 5:
                self.remove_done()
            elif int(cmd) == 6:
                self.check_overdued()
            elif int(cmd) == 7:
                self.dump_into_json(self.filestring)
            elif int(cmd) == 8:
                self.tasklist = self.load_from_json_dump(self.filestring)
            elif int(cmd) == 9:
                print('Terminating application')
                self.dump_into_json(self.filestring)
                sys.exit(-1)

if __name__ == '__main__':

    list = TodoList()
    list.main()
