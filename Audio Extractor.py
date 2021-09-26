from PyQt5 import QtCore, QtGui, QtWidgets
from moviepy import editor
import webbrowser
import sys

class AboutDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setupUi()
    
    def setupUi(self):        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("files/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setFixedSize(300, 100)
        self.setWindowTitle("About us")

        discription = QtWidgets.QLabel(self)
        discription.setGeometry(75, 10, 150, 30)
        discription.setAlignment(QtCore.Qt.AlignCenter)
        discription.setText("This program made by Sina.f")
        
        horizontalLayoutWidget = QtWidgets.QWidget(self)
        horizontalLayoutWidget.setGeometry(15, 50, 270, 40)
        horizontalLayout = QtWidgets.QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        horizontalLayout.setSpacing(12)
        
        btn_github = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_github.setText("GitHub")
        btn_github.clicked.connect(lambda: webbrowser.open('https://github.com/sina-programer'))
        
        btn_instagram = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_instagram.setText("Instagram")
        btn_instagram.clicked.connect(lambda: webbrowser.open('https://www.instagram.com/sina.programer'))
        
        btn_telegram = QtWidgets.QPushButton(horizontalLayoutWidget)
        btn_telegram.setText("Telegram")
        btn_telegram.clicked.connect(lambda: webbrowser.open('https://t.me/sina_programer'))
        
        horizontalLayout.addWidget(btn_github)
        horizontalLayout.addWidget(btn_instagram)
        horizontalLayout.addWidget(btn_telegram)


class Widget(QtWidgets.QMainWindow):
    def __init__(self):
        super(Widget, self).__init__()
        self.aboutDialog = AboutDialog()
        self.video = None
        self.setupUi()
        self.show()
        
    def setupUi(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"Files\icon.ico"))

        self.setGeometry(430, 270, 460, 90)
        self.setFixedSize(460, 90)
        self.setWindowIcon(icon)
        self.setWindowTitle("Audio Extractor")

        font = QtGui.QFont()
        font.setPointSize(9)
        self.video_path = QtWidgets.QLineEdit(self)
        self.video_path.setGeometry(130, 40, 220, 30)
        self.video_path.setFont(font)
        self.video_path.setReadOnly(True)
        self.video_path.setPlaceholderText("Video path")

        open_video_btn = QtWidgets.QPushButton(self)
        open_video_btn.setGeometry(360, 40, 75, 30)
        open_video_btn.setText("Open video")
        open_video_btn.clicked.connect(self.open_video)
        
        extract_btn = QtWidgets.QPushButton(self)
        extract_btn.setGeometry(25, 40, 90, 30)
        extract_btn.setText("Extract audio")
        extract_btn.clicked.connect(self.extract_audio)

        self.init_menu()
        
    def extract_audio(self):
        if self.video:
            save_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Audio File', '', "Audio Files (*.mp3)")
            if save_path:
                self.video.audio.write_audiofile(save_path)
                self.video.close()
                
        else:
            QtWidgets.QMessageBox.critical(self, 'ERROR', '\nPlease first open a video!\t\n') 
            
    def open_video(self):
        video_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open Video File', '', "Video Files (*.mp4)")
        if video_path:
            self.video = editor.VideoFileClip(video_path)
            self.video_path.setText(video_path)
            
    def init_menu(self):
        helpAction = QtWidgets.QAction('Help', self)
        helpAction.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, 'Help', help_msg))
        
        aboutAction =  QtWidgets.QAction('About us', self)
        aboutAction.triggered.connect(lambda: self.aboutDialog.exec_())
        
        menu = self.menuBar()
        menu.addAction(helpAction)
        menu.addAction(aboutAction)

help_msg = '''\n1_ Open a video for extract audio
2_ Click on extract button and choose audio name\t
3_ Done!\n'''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()

    sys.exit(app.exec_())
