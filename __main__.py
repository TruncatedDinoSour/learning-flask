from website import create_app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
# debug=True means that if we change any of the code
# it will rerun our web server
