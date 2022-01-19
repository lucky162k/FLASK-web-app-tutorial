from website import create_app

app = create_app()

if __name__ == '__main__':
    # Every-time the program is changed and saved the debugger will run automatically.
    # Not to leave it running when the application is live in production.
    app.run(debug=True)