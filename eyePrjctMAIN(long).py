from tkinter import*  
import webbrowser

class eye:
    def __init__ (self):
        self.spec=str(input("Укажите специализацию глаза: "))
        self.color=str(input("Укажите цвет глаза: "))
        self.tier=int(input("Укажите редкость глаза: "))
        print("=================================")

    def info(self):
        print("Специализация: ",self.spec,"\nЦвет глаза: ",self.color,"\nРедкость: ",self.tier)
        print("=================================")
    def search(self):
        print("Определяем вид вашего глаза...")
        if self.spec=="Гендзюцу" and self.color=="Красный" and self.tier==1:
            print("Ваш глаз Шаринган")
            window=Tk()
            window.geometry("400x400")
            window.title("Глаз Шаринган")
            tomoe=PhotoImage(file='c:\\Users\\user\\Desktop\\clique\\dcs\\cdSpcl\\pythonPrjcts\\eyesFndr\\shrngn.png')
            first_button=Button(window,image=tomoe)
            first_button.place(x=100,y=100,width=400,height=400)
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%A8%D0%B0%D1%80%D0%B8%D0%BD%D0%B3%D0%B0%D0%BD")
            window.mainloop()
        elif self.spec=="Гендзюцу" and self.color=="Красный" and self.tier==2:
            print("Ваш глаз Кецурьюган")
            window=Tk()
            window.geometry("400x400")
            window.title("Глаз Кецурьюган")
            ktsrygn=PhotoImage(file='c:\\Users\\user\\Desktop\\clique\\dcs\\cdSpcl\\pythonPrjcts\\eyesFndr\\ktsrygn.png')
            second_button=Button(window,image=ktsrygn)
            second_button.place(x=100,y=100,width=400,height=400)
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%9A%D0%B5%D1%86%D1%83%D1%80%D1%8C%D1%8E%D0%B3%D0%B0%D0%BD")
            window.mainloop()
        elif self.spec=="Техника Призыва" and self.color=="Фиолетовый" and self.tier==1:
            print("Ваш глаз Риннеган")
            window=Tk()
            window.geometry("400x400")
            window.title("Глаз Риннеган")
            rnngn=PhotoImage(file='c:\\Users\\user\\Desktop\\clique\\dcs\\cdSpcl\\pythonPrjcts\\eyesFndr\\rnngn.png')
            third_button=Button(window,image=rnngn)
            third_button.place(x=100,y=100,width=400,height=400)
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%A0%D0%B8%D0%BD%D0%BD%D0%B5%D0%B3%D0%B0%D0%BD")
            window.mainloop()
        elif self.spec=="Техника Призыва" and self.color=="Жёлтый" and self.tier==1:
            print("Ваш глаз Кокуган")
            window=Tk()
            window.geometry("400x400")
            window.title("Глаз Кокуган")
            kkgn=PhotoImage(file='c:\\Users\\user\\Desktop\\clique\\dcs\\cdSpcl\\pythonPrjcts\\eyesFndr\\kkgn.png')
            fourth_button=Button(window,image=kkgn)
            fourth_button.place(x=100,y=100,width=400,height=400)
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%9A%D0%BE%D0%BA%D1%83%D0%B3%D0%B0%D0%BD")
            window.mainloop()
        elif self.spec=="Тайдзюцу" and self.color=="Белый" and self.tier==1:
            print("Ваш глаз Бьякуган")
            window=Tk()
            window.geometry("400x400")
            window.title("Глаз Бьякуган")
            bykgn=PhotoImage(file='c:\\Users\\user\\Desktop\\clique\\dcs\\cdSpcl\\pythonPrjcts\\eyesFndr\\bykgn.png')
            fifth_button=Button(window,image=bykgn)
            fifth_button.place(x=100,y=100,width=400,height=400)
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%91%D1%8C%D1%8F%D0%BA%D1%83%D0%B3%D0%B0%D0%BD")
            window.mainloop()
        elif self.spec=="Тайдзюцу" and self.color=="Белый" and self.tier==2:
            print("Ваш глаз Тенсейган")
            window=Tk()
            window.geometry("400x400")
            window.title("Глаз Тенсейган")
            tnsgn=PhotoImage(file='c:\\Users\\user\\Desktop\\clique\\dcs\\cdSpcl\\pythonPrjcts\\eyesFndr\\tnsgn.png')
            sixth_button=Button(window,image=tnsgn)
            sixth_button.place(x=100,y=100,width=400,height=400)
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%A2%D0%B5%D0%BD%D1%81%D0%B5%D0%B9%D0%B3%D0%B0%D0%BD")
            window.mainloop()
        else:
            print("Вашего глаза нет в базе данных. *-*")
            webbrowser.open_new("https://naruto.fandom.com/ru/wiki/%D0%94%D0%BE%D1%83%D0%B4%D0%B7%D1%8E%D1%86%D1%83")


eye_first=eye()

eye_first.info()

eye_first.search()