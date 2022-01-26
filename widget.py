
def main():
    for i in range(20):
        print(Widget())
    print(Widget.getNextId())

class Widget:

    nextId = 0

    def __init__(self):
        self.id = Widget.nextId
        Widget.nextId += 1

    def __str__(self):
        return(f"Widget#{self.id}")

    @staticmethod
    def getNextId():
        return Widget.nextId

if __name__ == "__main__":
    main()
