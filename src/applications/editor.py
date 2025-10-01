

class Editor():
    def __init__(self):
        '''
        simple text editor class using two stacks, supporting: 
        - insert(str): insert string at cursor position
        - delete(n): delete up to n characters to the left of the cursor
        - move_left(n): move cursor left up to n positions
        - move_right(n): move cursor right up to n positions
        - get_text(): return the current text in the editor including cursor position as '|'
        '''

        self.left = []  # characters to the left of the cursor
        self.right = []  # characters to the right of the cursor

    def insert(self, string: str) -> None:
        for char in string:
            self.left.append(char)

    def delete(self, n: int) -> None:
        for _ in range(n):
            if self.left:
                self.left.pop()

    def move_left(self, n: int) -> None:
        for _ in range(n):
            if self.left:
                self.right.append(self.left.pop())

    def move_right(self, n: int) -> None:
        for _ in range(n):
            if self.right:
                self.left.append(self.right.pop())

    def get_text(self) -> str:
        return ''.join(self.left) + '|' + ''.join(reversed(self.right))
    
if __name__ == "__main__":
    editor = Editor()
    editor.insert("hello")
    editor.insert("world")
    editor.move_left(5)
    print( editor.get_text() )  # should return "hello|world"