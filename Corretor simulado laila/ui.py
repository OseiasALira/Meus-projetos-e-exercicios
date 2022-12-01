""" Interface app"""

import tkinter as tk
from tkinter import ttk

class StudentFrame(ttk.Frame):
    """Frame que trata dos dados do estudante, inclusão e exclusão."""
    def __init__(self, conteiner):
        super().__init__(conteiner)

        # Label frame
        self.lb_frame = ttk.Labelframe(self, text='Estudantes', padding=5)
        self.lb_frame.grid(column=0, row=0, sticky='NW', padx=5, pady=5)

        self.bt_frame = ttk.Frame(self.lb_frame, padding=3)
        self.bt_frame.grid(column=0, row=1)

        self.student_listbox()
        self.student_button()
        self.grid(row=0, column=0, padx=3, pady=5) # Posiciona o frame na janela

    def student_listbox(self):
        """Lista de alunos na lateral esquerda"""
        variavel_de_controle_list_box = ('nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome', 'nome')

        student_name = tk.StringVar(value=variavel_de_controle_list_box)
        list_box = tk.Listbox(self.lb_frame,
                              listvariable=student_name,
                              border=1,
                              height=20,
                              width=24,
                              font="Arial 12",
                              selectmode="browse" # Limita seleção para um item da lista
                              )
        list_box.grid(row=0,column=0)

        #colorize list
        for i in range(1, len(variavel_de_controle_list_box), 2):
            list_box.itemconfigure(i, background='#f0f0ff')

    def student_button(self):
        """Botões do frame de estudante"""

        bt_add_student = ttk.Button(self.bt_frame, text='Novo')
        bt_add_student.grid(row=0, column=0)

        bt_update_student = ttk.Button(self.bt_frame, text='Alterar')
        bt_update_student.grid(row=0, column=1)

        bt_delete_student = ttk.Button(self.bt_frame, text='Excluir')
        bt_delete_student.grid(row=0, column=2)

class ExamFrame(ttk.Frame):
    """frame function exam stuffs"""

    def __init__(self, conteiner):
        super().__init__(conteiner)

        #Label frame

        self.lb_frame = ttk.Labelframe(self, text='Provas', padding=5)
        self.lb_frame.grid(column=0, row=0, sticky='N', pady=5)

        self.bt_frame = ttk.Frame(self.lb_frame, padding=3)
        self.bt_frame.grid(column=0, row=1)

        self.exam_treeview()
        self.exam_buttons()
        self.grid(column=0, row=1)

    def exam_treeview(self):
        """Treeview db"""

        columns = ('id_exam', 'school','date')

        tree = ttk.Treeview(self.lb_frame, columns=columns, show='headings', height=5)
        tree.grid(column=0, row=0, sticky='nswe')

        tree.heading('id_exam', text='Cod')
        tree.heading('school', text='Estilo')
        tree.heading('date', text='Data')

        tree.column('id_exam',width=30, anchor='center')
        tree.column('school',width=150, anchor='center')
        tree.column('date',width=50, anchor='center')


        tree.insert('', tk.END, values=('01', 'Aplicação', '2022'))

    def exam_buttons(self):
        """Buttons exams"""

        bt_add_exam = ttk.Button(self.bt_frame, text='Novo')
        bt_add_exam.grid(row=0, column=0)

        bt_update_exam = ttk.Button(self.bt_frame, text='Alterar')
        bt_update_exam.grid(row=0, column=1)

        bt_delete_exam = ttk.Button(self.bt_frame, text='Excluir')
        bt_delete_exam.grid(row=0, column=2)



class WindowApp(tk.Tk):
    """main app"""
    def __init__(self):
        super().__init__()

        #configurações
        self.title("Corretor de prova objetiva")


if __name__ == "__main__":
    app = WindowApp()
    student = StudentFrame(app)
    exam = ExamFrame(app)
    app.mainloop()
