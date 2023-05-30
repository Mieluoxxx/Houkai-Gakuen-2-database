import tkinter as tk


class MainPage:
    def __init__(self, master):
        self.root = master
        self.root.title('学生信息管理系统 v0.0.1')
        self.root.geometry('600x400')
        self.create_page()

    def create_page(self):
        self.about_frame = tk.Frame(self.root)
        tk.Label(self.about_frame, text='关于作品: 本作品由tkinter制作').pack()
        tk.Label(self.about_frame, text='关于作者: moguw').pack()
        tk.Label(self.about_frame, text='版权所有: 咕噜咕噜').pack()

        menubar = tk.Menu(self.root)
        menubar.add_command(label='录入')
        menubar.add_command(label='查询')
        menubar.add_command(label='删除')
        menubar.add_command(label='修改')
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    def show_about(self):
        self.about_frame.pack()


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
