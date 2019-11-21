class Matrix:
    def __init__(self, matrix_string):
        entrys=[]
        rows=matrix_string.split("\n")
        for r in range(len(rows)):
            entrys.append([int(entry) for entry in rows[r].split(" ")])
        self.entrys = entrys

    def row(self, index):
        return self.entrys[index-1]

    def column(self, index):
        return [row[index-1] for row in self.entrys] 
