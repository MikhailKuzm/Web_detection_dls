from flask import Flask, render_template, Response

app = Flask(__name__)   

@app.route('/')
def index():
    print('works')
    return render_template('./index.html')

@app.route("/video_feed") 
def video_feed():
    from Face_detect.launch_face_detection import func
    return Response(func(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
   app.run(debug=False)
    
