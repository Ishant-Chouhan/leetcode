class Solution:
    def countDays(self, days, meetings):
        meetings.sort()
        ans = max(0,meetings[0][0]-1)
        newMeetings = []
        
        for m in meetings:
            if newMeetings and newMeetings[-1][-1]>m[0]:
                newMeetings[-1] = [min(newMeetings[-1][0],m[0]),max(newMeetings[-1][-1],m[-1])]
            else:
                newMeetings.append(m)
            
        for i in range(len(newMeetings)-1):
            ans += max(0,newMeetings[i+1][0]-newMeetings[i][-1]-1)
            
        ans += max(0,days-newMeetings[-1][-1])
        return ans