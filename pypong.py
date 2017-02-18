#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author : mashixuan123123@sina.com
#version : Final
import pygame as py
import sys
class MyBallClass(py.sprite.Sprite):
	def __init__(self,image_file,speed,location):
		py.sprite.Sprite.__init__(self)       #call Sprite initializer
		self.image = py.image.load(image_file)
		self.rect = self.image.get_rect()
		self.rect.left,self.rect.top = location
		self.speed = speed
	def move(self):
		global points,score_text
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > screen.get_width():
			self.speed[0] = -self.speed[0]
			points = points + 1
		if self.rect.top <= 0:
			self.speed[1] = -self.speed[1]
			points = points + 2
			score_text = font.render(str(points),1,(0,0,0))
class MyPaddleClass(py.sprite.Sprite):
	def __init__(self,location = [0,0]):
		py.sprite.Sprite.__init__(self)
		image_surface = py.surface.Surface([85,20])
		image_surface.fill([236,157,160])
		self.image = image_surface.convert()
		self.rect = self.image.get_rect()
		self.rect.left,self.rect.top = location
py.init()
screen = py.display.set_mode([640,480])
clock = py.time.Clock()
ball_speed = [10,5]
myBall = MyBallClass('beach_ball.png',ball_speed,[50,50])
ballGroup = py.sprite.Group(myBall)
paddle = MyPaddleClass([270,400])
lives = 3
points = 0
font = py.font.Font(None,50)
score_text = font.render(str(points),1,(0,0,0))
textpos = [10,10]
done = False
while 1:
	clock.tick(30)
	screen.fill([32,250,78])
	for event in py.event.get():
		if event.type == py.QUIT:
			sys.exit()
		elif event.type == py.MOUSEMOTION:
			paddle.rect.centerx = event.pos[0]
	if py.sprite.spritecollide(paddle,ballGroup,False):
		myBall.speed[1] = -myBall.speed[1]
	myBall.move()
	if not done:
		screen.blit(myBall.image,myBall.rect)
		screen.blit(paddle.image,paddle.rect)
		screen.blit(score_text,textpos)
		for i in range (lives):
			width = screen.get_width()
			screen.blit(myBall.image,[width - 40 * i,20])
		py.display.flip()
		py.display.update()
	if myBall.rect.top >= screen.get_rect().bottom:
		lives = lives - 1
		if lives == 0:
			final_text1 = "GAME OVER"
			final_text2 = "Your Final Score is: " + str(points)
			ft1_font = py.font.Font(None,70)
			ft1_surf = font.render(final_text1,1,(0,0,0))
			ft2_font = py.font.Font(None,50)
			ft2_surf = font.render(final_text2,1,(0,0,0))
			screen.blit(ft1_surf,[screen.get_width() / 2 - ft1_surf.get_width() / 2,100])
			screen.blit(ft2_surf,[screen.get_width() / 2 - ft2_surf.get_width() / 2,200])
			py.display.flip()
			py.display.update()
			done = True
		else:
			py.time.delay(2000)
			myBall.rect.topleft = [50,50]