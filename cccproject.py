import tkinter as tk
from tkinter import messagebox, font
from collections import deque


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if not self._data:
            return None
        return self._data.popleft()

    def front(self):
        if not self._data:
            return None
        return self._data[0]

    def to_list(self):
        return list(self._data)



class QueueApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Queue Visualizer")
        self.geometry("800x500")
        self.resizable(False, False)

        self.queue = Queue()

        # Header
        header = tk.Frame(self)
        header.pack(fill="x", pady=6)
        tk.Label(header, text="QUEUE VISUALIZER",
                 font=font.Font(size=16, weight="bold")).pack()

        # Controls
        control = tk.Frame(self)
        control.pack(fill="x", pady=4)

        tk.Label(control, text="Value:").grid(row=0, column=0, padx=5)
        self.entry = tk.Entry(control)
        self.entry.grid(row=0, column=1, padx=5)

        tk.Button(control, text="Enqueue", width=12,
                  command=self.enqueue).grid(row=0, column=2, padx=6)
        tk.Button(control, text="Dequeue", width=12,
                  command=self.dequeue).grid(row=0, column=3, padx=6)
        tk.Button(control, text="Front", width=12,
                  command=self.front).grid(row=0, column=4, padx=6)
        tk.Button(control, text="Clear", width=12,
                  command=self.clear).grid(row=0, column=5, padx=6)

        # Canvas for drawing
        self.canvas = tk.Canvas(self, width=760, height=330, bg="white")
        self.canvas.pack(pady=10)

        # Drawing constants
        self.start_x = 50
        self.start_y = 150
        self.node_w = 60
        self.node_h = 40
        self.gap = 30

        self.draw()

   
    def _get_input(self):
        v = self.entry.get().strip()
        if v == "":
            messagebox.showwarning("Input required", "Please enter a value.")
            return None
        return v

    def enqueue(self):
        v = self._get_input()
        if v is None:
            return
        self.queue.enqueue(v)
        self.draw()

    def dequeue(self):
        val = self.queue.dequeue()
        if val is None:
            messagebox.showinfo("Empty", "Queue is empty.")
        else:
            messagebox.showinfo("Dequeued", f"Dequeued value: {val}")
        self.draw()

    def front(self):
        val = self.queue.front()
        if val is None:
            messagebox.showinfo("Empty", "Queue is empty.")
        else:
            messagebox.showinfo("Front", f"Front value: {val}")

    def clear(self):
        self.queue = Queue()
        self.draw()

   
    def draw(self):
        self.canvas.delete("all")
        vals = self.queue.to_list()

        x = self.start_x
        y = self.start_y

        for i, val in enumerate(vals):
            
            self.canvas.create_rectangle(
                x, y,
                x + self.node_w, y + self.node_h,
                fill="#e6ffe6", outline="#009900", width=2
            )
            self.canvas.create_text(
                x + self.node_w / 2,
                y + self.node_h / 2,
                text=str(val)
            )

           
            if i < len(vals) - 1:
                self.canvas.create_line(
                    x + self.node_w, y + self.node_h / 2,
                    x + self.node_w + self.gap, y + self.node_h / 2,
                    arrow=tk.LAST, width=2
                )

            x += self.node_w + self.gap

        
        if vals:
            fx = self.start_x + self.node_w / 2
            fy = y - 20
            self.canvas.create_text(
                fx, fy, text="Front",
                fill="#333333", font=(None, 10, "bold")
            )

            rx = self.start_x + (self.node_w + self.gap) * (len(vals) - 1) + self.node_w / 2
            ry = y - 20
            self.canvas.create_text(
                rx, ry, text="Rear",
                fill="#333333", font=(None, 10, "bold")
            )



if __name__ == "__main__":
    QueueApp().mainloop()
