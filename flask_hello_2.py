from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("hello.html", title="Home Page")

@app.route("/first")
def first():
  return render_template("first.html", title="First Page")


@app.route("/second")
def second():
  return render_template("second.html", title="Second Page")

if __name__=="__main__":
  app.run(host="0.0.0.0")


# '''
#     <p>Hello, Flask!</p>
#     <a href="/first">Go first</a>
#     <a href="/second">Go Second</a>
#     '''
# '''
#     <p>First Page</p>
#     <a href="/">Go Home</a>
#   '''
# '''
#     <p>Second Page</p>
#     <a href="/">Go Home</a>
#   '''