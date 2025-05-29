#Day 18-02-2024
#Meeting Rooms 3
'''
You are given an integer n. There are n rooms numbered from 0 to n - 1.

You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held during the half-closed time interval [starti, endi). All the values of starti are unique.

Meetings are allocated to rooms in the following manner:

Each meeting will take place in the unused room with the lowest number.
If there are no available rooms, the meeting will be delayed until a room becomes free. The delayed meeting should have the same duration as the original meeting.
When a room becomes unused, meetings that have an earlier original start time should be given the room.
Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

A half-closed interval [a, b) is the interval between a and b including a and not including b.

 

Example 1:

Input: n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]
Output: 0
Explanation:
- At time 0, both rooms are not being used. The first meeting starts in room 0.
- At time 1, only room 1 is not being used. The second meeting starts in room 1.
- At time 2, both rooms are being used. The third meeting is delayed.
- At time 3, both rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 1 finishes. The third meeting starts in room 1 for the time period [5,10).
- At time 10, the meetings in both rooms finish. The fourth meeting starts in room 0 for the time period [10,11).
Both rooms 0 and 1 held 2 meetings, so we return 0. 

Example 2:

Input: n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
Output: 1
Explanation:
- At time 1, all three rooms are not being used. The first meeting starts in room 0.
- At time 2, rooms 1 and 2 are not being used. The second meeting starts in room 1.
- At time 3, only room 2 is not being used. The third meeting starts in room 2.
- At time 4, all three rooms are being used. The fourth meeting is delayed.
- At time 5, the meeting in room 2 finishes. The fourth meeting starts in room 2 for the time period [5,10).
- At time 6, all three rooms are being used. The fifth meeting is delayed.
- At time 10, the meetings in rooms 1 and 2 finish. The fifth meeting starts in room 1 for the time period [10,12).
Room 0 held 1 meeting while rooms 1 and 2 each held 2 meetings, so we return 1. 

'''

#We have to make a count of meeting held at each room at return than max meetings held 
#as well as if we encounter same meeting count at any rooms  just return the minimum index(least meeting room number)

#Algorithm
'''
Step 1: create  list for taking the count of meeting at each room 
        meeting_count=[]*(n-->number of rooms)
        create a taking the list for noting the endtime for each meeting 
        And in the same list we will update the the meetings which is delayed at same index
        
Step 2:Outer Loop: we iterate through 2D list 
        step-1:   start=list[0]
                  end=list[1]
                  
Inner: step-2:    initilaze status(var) set the status-->false(To keep track of whether meeting is delayed or schedule at room)
 loop             a variable to keep note of end time of each meeting but we will initialze it to max value 
                  minIndex=0(keep note at hich index we hve to delay the meeting and at which index we have to incrmenet the count of meeting held at each room)
                  
        step-3:   iterate loop in the range of 0-n(meeting rooms) i<n
                  if time[i]<val
                    we will update the val ---> in wjhich time[i](contains the end time of each meeting )
                    minIndex=i
                    
                  if time<=start
                    update meeting count to 1 at ith index
                    update time at ith index with =end
                    if the condition holds tur means the meeting is scheduled at ith room 
                    then uodate status to true
                    break the loop (cause meeting as scheduled)
                    
        step 4: Out of inner loop
                is status is false 
                   we have to delay the meeting 
                   we have index (meeting room-->minIndex) where the meeting is actually to take place 
                   we will increment it by one at that index 
                   and calculating the time[minIndex]+=(end-start)
        
'''

import sys
def meetingRoom(n,nums):
    nums.sort()
    #meeting count  for each room
    meeting_count=[0]*n
    #time list to keep track of end time to schedule next meeting
    
    time=[0]*1000000
    
    #iterate through 2D matrix
    for list1 in nums:
       
        start_time=list1[0]
        end_time=list1[1]
        #status to keep track of room 
        status=False
        #val to keep th end time of each room (usefule when the meeting is dealyed we can update)
        val=sys.maxsize
        #index to keep track where actually the meeting to take place
        index=0
        
        #iterate through 0-->n
        for i in range(n):
            #checking if the end time is just less  the previous meeting 
            if time[i]<val:
                val=time[i]
                index=i
            #checking if the metting is scheduled
            if time[i]<=start_time:
                #update at ith index meeting count 
                meeting_count[i]+=1
                #end time at ith index
                time[i]=end_time
                #change the status to true (meeting as schduled)
                status=True
                break#inner loop
        #meeting is delayed
        if not status:
            meeting_count[index]+=1
            #time
            time[index]+=(end_time-start_time)
            
    
    maxMeetingCount=index=0
    for i in range(len(meeting_count)):
        if meeting_count[i]>maxMeetingCount:
            maxMeetingCount=meeting_count[i]
            index=i
    return index

nums=[[1,20],[2,10],[3,5],[4,9],[6,8]]
n=3
print(meetingRoom(n,nums))