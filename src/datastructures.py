
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []
        

        # example list of members
        self._members = [{"lucky_number":[7,13,22],"first_name": "Jhon","age":"33","last_name": self.last_name, "id" :self._generate_id()},
                        {"lucky_number":[10, 14, 3], "first_name":"Jane", "age":35, "last_name":self.last_name, "id":self._generate_id()},
                        {"lucky_number":1, "first_name":"Jimmy", "age":5, "last_name":self.last_name, "id":self._generate_id()}
                         ]

        
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
    def add_member(self, member):
        print(f"viene de family {member}")
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return True
        

    def delete_member(self, id):
       for member in self._members:
           if member.get("id") ==id:
               self._members.remove(member)
               return {"msg":"member deleted succesfully"}
    
    def get_member(self, id):
       members = [member for member in self._members if member["id"] == id]
       if member: 
           member = members[0]
           response= {
               "id" :member["id"],
               "first_name":member["first_name"],
               "last_name":member["last_name"],
               "lucky_number": member["lucky_number"]
           }
           return response
       else :
           return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
