'''

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3
 

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
Domain names must contain at least one character before ".com" suffix.

'''

class Solution:
      def numUniqueEmails(self, emails: list[str]) -> int:
            hash_map={}
            for email in emails:
                arr=email.split("@")
                mail=arr[0].split("+")[0].replace(".","")
                if mail in hash_map:
                   hash_map[mail].append(arr[1])
                else:
                    hash_map[mail]=[arr[1]]
            count=0 
            for key,value in hash_map.items():
                count+=len(set(value))
          
            return count

Solution().numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])

class TestApp:
      def testing_case_one(self):
          assert Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])==2
      def testing_Case_two(self):
          assert Solution().numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])==3
  
              