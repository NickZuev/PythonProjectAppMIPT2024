from windows import App


if __name__ == "__main__":
    app = App()
    app.bind("<Escape>", lambda event: app.change_window("MenuWindow"))
    app.bind("<Left>", lambda event: app.apply("get_next_card", 0))
    app.bind("<Right>", lambda event: app.apply("get_next_card", 1))
    app.bind("<Up>", lambda event: app.apply("increment"))
    app.bind("<Down>", lambda event: app.apply("decrement"))
    app.bind("<space>", lambda event: app.apply("flip"))
    app.mainloop()
