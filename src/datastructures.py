
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
initials_members = [{
    "name": "John" ,
    "age": 33 ,
    "lucky_numbers":[7, 13, 22]
},{
    "name": "Jane" ,
    "age": 35 ,
    "lucky_numbers":[10, 14, 3]
},{
    "name": "Jimmy" ,
    "age": 5 ,
    "lucky_numbers":[1]
}]


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

        # example list of members
        for member in initials_members:
              self.add_member(member)
      
        print(self._members)
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        if 'id' not in member:
          member['id'] = self._generateId()
        
        self._members.append(member)
        return self._members

    def delete_member(self, id):
        # fill this method and update the return
        don_dic = { "done": False }
       
        for i in range(len(self._members)):
            if self._members[i]['id'] == id:
                del(self._members[i])
                don_dic = {'done':True}
                break
        return don_dic 

    def get_member(self, id):
        # fill this method and update the return
        my_member = {}
        for member in self._members:
            # if member.id == id: nofunciona en diccionarios
            if member['id'] == id:
                my_member = member

        print(my_member)
        return my_member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
