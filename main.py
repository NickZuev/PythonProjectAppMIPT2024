from src.app import App


if __name__ == "__main__":
    app = App()
    app.bind("<Control-Key-BackSpace>", lambda event: app.exit(0))
    app.bind("<Escape>", lambda event: app.undo())
    app.bind("<Left>", lambda event: app.apply("get_next_card", 0))
    app.bind("<Right>", lambda event: app.apply("get_next_card", 1))
    app.bind("<Up>", lambda event: app.apply("increment"))
    app.bind("<Down>", lambda event: app.apply("decrement"))
    app.bind("<space>", lambda event: app.apply("flip"))
    # app.bind("<Enter>", lambda event: app.apply("do_action"))
    app.mainloop()