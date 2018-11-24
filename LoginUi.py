 # # # # # # # # # # # # # # #
 # @file   LoginUi           #
 # @email  642212607@qq.com  #
 # @date   2018-11-24        #
 # # # # # # # # # # # # # # #

from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit,
							 QCheckBox, QVBoxLayout, QHBoxLayout, QSizePolicy)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import pyqtSignal, Qt, QObject

class LoginUi(QWidget):

	def __init__(self):
		super(LoginUi, self).__init__()
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.factor = self.__width__ = QApplication.desktop().screenGeometry().width()/100
		self.resize(self.factor*25, self.factor*40)
		self.setupUi()

	def setupUi(self):
		self.setting_button = QPushButton()
		self.minimize_button = QPushButton()
		self.close_button = QPushButton()
		self.logo = QLabel()
		self.user_logo = QLabel()
		self.password_logo = QLabel()
		self.username_line = QLineEdit()
		self.password_line = QLineEdit()
		self.register_button = QPushButton()
		self.find_password_button = QPushButton()
		self.is_rember_checkbox = QCheckBox()
		self.is_autologin_checkbox = QCheckBox()
		self.login_button = QPushButton()

		self.logo.setAlignment(Qt.AlignHCenter)
		self.username_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		self.password_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
		self.login_button.setFixedHeight(self.factor*5)

		main_layout = QVBoxLayout()
		main_layout.setContentsMargins(0, 0, 0, self.factor*3)
		tools_layout = QHBoxLayout()
		tools_layout.setSpacing(0)
		tools_layout.addWidget(self.setting_button)
		tools_layout.addWidget(self.minimize_button)
		tools_layout.addWidget(self.close_button)
		tools_layout.setAlignment(Qt.AlignRight)
		main_layout.addLayout(tools_layout)
		main_layout.addWidget(self.logo)
		user_layout = QHBoxLayout()
		user_layout.addWidget(self.user_logo)
		user_layout.addWidget(self.username_line)
		user_layout.addWidget(self.register_button)		
		password_layout = QHBoxLayout()
		password_layout.addWidget(self.password_logo)
		password_layout.addWidget(self.password_line)
		password_layout.addWidget(self.find_password_button)
		checkbox_layout = QHBoxLayout()
		checkbox_layout.addWidget(self.is_rember_checkbox)
		checkbox_layout.addWidget(self.is_autologin_checkbox)
		v_layout = QVBoxLayout()
		v_layout.addLayout(user_layout)
		v_layout.addLayout(password_layout)
		v_layout.addStretch(1)
		v_layout.addLayout(checkbox_layout)
		v_layout.setContentsMargins(self.factor*3, self.factor*2, self.factor*3, self.factor)
		main_layout.addLayout(v_layout)
		h_layout = QHBoxLayout()
		h_layout.addWidget(self.login_button)
		h_layout.setContentsMargins(self.factor, self.factor, self.factor, self.factor)
		main_layout.addLayout(h_layout)
		self.set_text_and_picture()
		self.setLayout(main_layout)

		self.minimize_button.clicked.connect(self.showMinimized)
		self.close_button.clicked.connect(self.close)

	def set_text_and_picture(self):
		self.register_button.setText('注册账户')
		self.find_password_button.setText('找回密码')
		self.is_rember_checkbox.setText('记住密码')
		self.is_autologin_checkbox.setText('自动登录')
		self.login_button.setText('登录')
		self.setting_button.setIcon(QIcon(QPixmap('./source/pic/setting.png')\
			.scaled(self.factor, self.factor)))
		self.minimize_button.setIcon(QIcon(QPixmap('./source/pic/hide.png')\
			.scaled(self.factor, self.factor)))
		self.close_button.setIcon(QIcon(QPixmap('./source/pic/close.png')\
			.scaled(self.factor, self.factor)))
		self.logo.setPixmap(QPixmap('./source/pic/logo.png')\
			.scaled(self.factor*15, self.factor*15))
		self.user_logo.setPixmap(QPixmap('./source/pic/user.png')\
			.scaled(self.factor*2, self.factor*2))
		self.password_logo.setPixmap(QPixmap('./source/pic/password.png')\
			.scaled(self.factor*2, self.factor*2))

	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
			event.accept()

	def mouseMoveEvent(self, event):
		if event.buttons() == Qt.LeftButton:
			self.move(event.globalPos() - self.dragPosition)
			event.accept()



if __name__ == '__main__':
	import sys
	import qdarkstyle
	app = QApplication(sys.argv)
	app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
	login = LoginUi()
	login.setupUi()
	login.show()
	sys.exit(app.exec_())
