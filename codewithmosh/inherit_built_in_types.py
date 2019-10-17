class Text(str):
    def duplicate(self):
        return self + self


text = Text('Python')
print(text.duplicate())


class TrackableList(list):
    def append(self, object: object) -> None:
        print("Append called")
        super(TrackableList, self).append(object)
        # super().append()


tlist = TrackableList()
tlist.append('hello')
print(tlist)