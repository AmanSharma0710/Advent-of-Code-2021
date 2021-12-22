numbers = list(map(int, input().split(",")))
tickets = []

already_empty = False
while True:
    line = input()
    if line=="" and already_empty:
        break
    elif line=="":
        already_empty=True
        continue
    already_empty=False
    curr_ticket = []
    curr_ticket.append(list(map(int, line.split())))
    for i in range(4):
        curr_ticket.append(list(map(int, input().split())))
    tickets.append(curr_ticket)

numberOfTickets = len(tickets)

called = []
for ticket in range(numberOfTickets):
    called.append([0 for i in range(10)])

marked = [[[0 for i in range(5)] for j in range(5)]for k in range(numberOfTickets)]
won = [False for i in range(numberOfTickets)]
tickets_done=0
last_number = 0
winning_ticket = -1
for current_number in numbers:
    for ticket_no in range(numberOfTickets):
        if won[ticket_no]:
            continue
        for i in range(5):
            for j in range(5):
                if tickets[ticket_no][i][j]==current_number:
                    marked[ticket_no][i][j]=1
                    called[ticket_no][i]+=1
                    called[ticket_no][5+j]+=1
                    if (called[ticket_no][i]==5 or called[ticket_no][5+j]==5) and not won[ticket_no]:
                        won[ticket_no]=True
                        tickets_done += 1
                        winning_ticket = ticket_no
                        last_number = current_number
score = 0;
for i in range(5):
    for j in range(5):
        if marked[winning_ticket][i][j]==0:
            score+=tickets[winning_ticket][i][j]

print(score*last_number)

