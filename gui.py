import tkinter as tk
from tkinter import ttk

def init_window():
    window = tk.Tk()
    window.title("FeedMeGood!")
    window.geometry("500x950")
    window.resizable(0, 0)
    return window

def first_screen_init(window):
    
    #PONIEDZIAŁEK
    label_poniedzialek = tk.Label(window, text = "Poniedziałek")
    
    combobox_poniedzialek_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_poniedzialek_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_poniedzialek_obiad = ttk.Combobox(window, height = 15) 
    combobox_poniedzialek_deser = ttk.Combobox(window, height = 15) 
    combobox_poniedzialek_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_poniedzialek = tk.Checkbutton(window, var=False)
    checkbox_poniedzialek_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_poniedzialek_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_poniedzialek_obiad = tk.Checkbutton(window, var=False)
    checkbox_poniedzialek_deser = tk.Checkbutton(window, var=False)
    checkbox_poniedzialek_kolacja = tk.Checkbutton(window, var=False)
    
    label_poniedzialek.place(x=10, y=20) 
    combobox_poniedzialek_sniadanie.place(x=20, y=40)
    combobox_poniedzialek_2sniadanie.place(x=20, y=60)
    combobox_poniedzialek_obiad.place(x=20, y=80)
    combobox_poniedzialek_deser.place(x=20, y=100)
    combobox_poniedzialek_kolacja.place(x=20, y=120)
    checkbox_poniedzialek.place(x=200, y=20)
    checkbox_poniedzialek_sniadanie.place(x=200, y=40)
    checkbox_poniedzialek_2sniadanie.place(x=200, y=60)
    checkbox_poniedzialek_obiad.place(x=200, y=80)
    checkbox_poniedzialek_deser.place(x=200, y=100)
    checkbox_poniedzialek_kolacja.place(x=200, y=120)
    
   
    #WTOREK
    label_wtorek = tk.Label(window, text = "Wtorek")
    
    combobox_wtorek_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_wtorek_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_wtorek_obiad = ttk.Combobox(window, height = 15) 
    combobox_wtorek_deser = ttk.Combobox(window, height = 15) 
    combobox_wtorek_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_wtorek = tk.Checkbutton(window, var=False)
    checkbox_wtorek_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_wtorek_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_wtorek_obiad = tk.Checkbutton(window, var=False)
    checkbox_wtorek_deser = tk.Checkbutton(window, var=False)
    checkbox_wtorek_kolacja = tk.Checkbutton(window, var=False)
    
    label_wtorek.place(x=10, y=150) 
    combobox_wtorek_sniadanie.place(x=20, y=170)
    combobox_wtorek_2sniadanie.place(x=20, y=190)
    combobox_wtorek_obiad.place(x=20, y=210)
    combobox_wtorek_deser.place(x=20, y=230)
    combobox_wtorek_kolacja.place(x=20, y=250)
    checkbox_wtorek.place(x=200, y=150)
    checkbox_wtorek_sniadanie.place(x=200, y=170)
    checkbox_wtorek_2sniadanie.place(x=200, y=190)
    checkbox_wtorek_obiad.place(x=200, y=210)
    checkbox_wtorek_deser.place(x=200, y=230)
    checkbox_wtorek_kolacja.place(x=200, y=250)


   #ŚRODA
    label_sroda = tk.Label(window, text = "Środa")
    
    combobox_sroda_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_sroda_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_sroda_obiad = ttk.Combobox(window, height = 15) 
    combobox_sroda_deser = ttk.Combobox(window, height = 15) 
    combobox_sroda_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_sroda = tk.Checkbutton(window, var=False)
    checkbox_sroda_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_sroda_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_sroda_obiad = tk.Checkbutton(window, var=False)
    checkbox_sroda_deser = tk.Checkbutton(window, var=False)
    checkbox_sroda_kolacja = tk.Checkbutton(window, var=False)
    
    label_sroda.place(x=10, y=280) 
    combobox_sroda_sniadanie.place(x=20, y=300)
    combobox_sroda_2sniadanie.place(x=20, y=320)
    combobox_sroda_obiad.place(x=20, y=340)
    combobox_sroda_deser.place(x=20, y=360)
    combobox_sroda_kolacja.place(x=20, y=380)
    checkbox_sroda.place(x=200, y=280)
    checkbox_sroda_sniadanie.place(x=200, y=300)
    checkbox_sroda_2sniadanie.place(x=200, y=320)
    checkbox_sroda_obiad.place(x=200, y=340)
    checkbox_sroda_deser.place(x=200, y=360)
    checkbox_sroda_kolacja.place(x=200, y=380)


   #CZWARTEK
    label_czwartek = tk.Label(window, text = "Czwartek")
    
    combobox_czwartek_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_czwartek_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_czwartek_obiad = ttk.Combobox(window, height = 15) 
    combobox_czwartek_deser = ttk.Combobox(window, height = 15) 
    combobox_czwartek_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_czwartek = tk.Checkbutton(window, var=False)
    checkbox_czwartek_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_czwartek_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_czwartek_obiad = tk.Checkbutton(window, var=False)
    checkbox_czwartek_deser = tk.Checkbutton(window, var=False)
    checkbox_czwartek_kolacja = tk.Checkbutton(window, var=False)
    
    label_czwartek.place(x=10, y=410) 
    combobox_czwartek_sniadanie.place(x=20, y=430)
    combobox_czwartek_2sniadanie.place(x=20, y=450)
    combobox_czwartek_obiad.place(x=20, y=470)
    combobox_czwartek_deser.place(x=20, y=490)
    combobox_czwartek_kolacja.place(x=20, y=510)
    checkbox_czwartek.place(x=200, y=410)
    checkbox_czwartek_sniadanie.place(x=200, y=430)
    checkbox_czwartek_2sniadanie.place(x=200, y=450)
    checkbox_czwartek_obiad.place(x=200, y=470)
    checkbox_czwartek_deser.place(x=200, y=490)
    checkbox_czwartek_kolacja.place(x=200, y=510)


   #PIĄTEK
    label_piatek = tk.Label(window, text = "Piątek")
    
    combobox_piatek_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_piatek_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_piatek_obiad = ttk.Combobox(window, height = 15) 
    combobox_piatek_deser = ttk.Combobox(window, height = 15) 
    combobox_piatek_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_piatek = tk.Checkbutton(window, var=False)
    checkbox_piatek_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_piatek_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_piatek_obiad = tk.Checkbutton(window, var=False)
    checkbox_piatek_deser = tk.Checkbutton(window, var=False)
    checkbox_piatek_kolacja = tk.Checkbutton(window, var=False)
    
    label_piatek.place(x=10, y=540) 
    combobox_piatek_sniadanie.place(x=20, y=560)
    combobox_piatek_2sniadanie.place(x=20, y=580)
    combobox_piatek_obiad.place(x=20, y=600)
    combobox_piatek_deser.place(x=20, y=620)
    combobox_piatek_kolacja.place(x=20, y=640)
    checkbox_piatek.place(x=200, y=540)
    checkbox_piatek_sniadanie.place(x=200, y=560)
    checkbox_piatek_2sniadanie.place(x=200, y=680)
    checkbox_piatek_obiad.place(x=200, y=600)
    checkbox_piatek_deser.place(x=200, y=620)
    checkbox_piatek_kolacja.place(x=200, y=640)


   #SOBOTA
    label_sobota = tk.Label(window, text = "Sobota")
    
    combobox_sobota_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_sobota_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_sobota_obiad = ttk.Combobox(window, height = 15) 
    combobox_sobota_deser = ttk.Combobox(window, height = 15) 
    combobox_sobota_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_sobota = tk.Checkbutton(window, var=False)
    checkbox_sobota_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_sobota_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_sobota_obiad = tk.Checkbutton(window, var=False)
    checkbox_sobota_deser = tk.Checkbutton(window, var=False)
    checkbox_sobota_kolacja = tk.Checkbutton(window, var=False)
    
    label_sobota.place(x=10, y=670) 
    combobox_sobota_sniadanie.place(x=20, y=690)
    combobox_sobota_2sniadanie.place(x=20, y=710)
    combobox_sobota_obiad.place(x=20, y=730)
    combobox_sobota_deser.place(x=20, y=750)
    combobox_sobota_kolacja.place(x=20, y=770)
    checkbox_sobota.place(x=200, y=670)
    checkbox_sobota_sniadanie.place(x=200, y=690)
    checkbox_sobota_2sniadanie.place(x=200, y=710)
    checkbox_sobota_obiad.place(x=200, y=730)
    checkbox_sobota_deser.place(x=200, y=750)
    checkbox_sobota_kolacja.place(x=200, y=770)


   #NIEDZIELA
    label_niedziela = tk.Label(window, text = "Niedziela")
    
    combobox_niedziela_sniadanie = ttk.Combobox(window, height = 15) 
    combobox_niedziela_2sniadanie = ttk.Combobox(window, height = 15) 
    combobox_niedziela_obiad = ttk.Combobox(window, height = 15) 
    combobox_niedziela_deser = ttk.Combobox(window, height = 15) 
    combobox_niedziela_kolacja = ttk.Combobox(window, height = 15) 
    
    checkbox_niedziela = tk.Checkbutton(window, var=False)
    checkbox_niedziela_sniadanie = tk.Checkbutton(window, var=False)
    checkbox_niedziela_2sniadanie = tk.Checkbutton(window, var=False)
    checkbox_niedziela_obiad = tk.Checkbutton(window, var=False)
    checkbox_niedziela_deser = tk.Checkbutton(window, var=False)
    checkbox_niedziela_kolacja = tk.Checkbutton(window, var=False)
    
    label_niedziela.place(x=10, y=800) 
    combobox_niedziela_sniadanie.place(x=20, y=820)
    combobox_niedziela_2sniadanie.place(x=20, y=840)
    combobox_niedziela_obiad.place(x=20, y=860)
    combobox_niedziela_deser.place(x=20, y=880)
    combobox_niedziela_kolacja.place(x=20, y=900)
    checkbox_niedziela.place(x=200, y=800)
    checkbox_niedziela_sniadanie.place(x=200, y=820)
    checkbox_niedziela_2sniadanie.place(x=200, y=840)
    checkbox_niedziela_obiad.place(x=200, y=860)
    checkbox_niedziela_deser.place(x=200, y=880)
    checkbox_niedziela_kolacja.place(x=200, y=900)

    #PRZYCISKI

    #generate_week_button
    #generate_choosen_button
    #clear_comboboxes_button

    #SEPARATORY

    vertical_separator = ttk.Separator(window, orient="vertical")
    vertical_separator.place(x= 400, y=100, z=100)

def __main__():
    window = init_window()
    first_screen_init(window)
    window.mainloop()


__main__()


