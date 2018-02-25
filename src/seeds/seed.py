from src.models import Messages
import model

def seed_initial_notes():
    note_1 = Messages()
    note_1.messageContent = "I have to be at the skytrain in 50 minutes"
    note_1.save()
    note_2 = Messages()
    note_2.messageContent = "Remember to buy milk and eggs"
    note_2.save()
    note_3 = Messages()
    note_3.messageContent = "Study for match exam tonight"
    note_3.save()




if __name__ == '__main__':
    model.Database.setup(
        host="localhost",
        database="voicenotes",
        user="root",
        password=""
    )
    seed_initial_notes()

    ## getting records

    data = Messages.query()
    for d in data:
        print("{}: {}".format(d.id, d.messageContent))