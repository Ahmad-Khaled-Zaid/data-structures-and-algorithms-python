class Node:
    def __init__(self, name, pref):
        self.name = name
        self.pref = pref
        self.next = None


class AnimalShelter:
    def __init__(self):
        self.front = None
        self.rear = None

    #############################################
    def enqueue(self, name, pref):
        node = Node(name, pref)
        if not self.front:
            self.rear = node
            self.front = self.rear
        else:
            self.rear.next = node
            self.rear = node

    #############################################

    def dequeue(self, pref):
        if pref != "cat" and pref != "dog":
            return None

        curr = self.front
        flag = True
        while curr:
            if curr.pref == pref and flag:
                self.front = self.front.next
                return curr.name

            elif curr.next is not None and curr.next.pref == pref:
                temp = curr.next.name
                curr.next = curr.next.next
                return temp
            curr = curr.next
            flag = False
        print(f"{pref} not found in the queue")

    #############################################

    def __str__(self):
        text = ""
        curr = self.front
        while curr:
            text = f'[{curr.name} {curr.pref}] ->' + text
            curr = curr.next
        return text
    #############################################


if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("sherry", "dog")
    shelter.enqueue("Rex", "dog")
    shelter.enqueue("Sugar", "cat")
    shelter.enqueue("slim", "cat")
    shelter.enqueue("Candy", "dog")
    shelter.enqueue("Tac", "cat")
    print(shelter)
    shelter.dequeue("cat")
    print("<-------- Remove Cat -------->")
    print(shelter)



