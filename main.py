import pygame
import random
import os
import time

class Algorithims():
    def bubbleSort(self, nums):
        drawRect(nums, (255,255,255))
        for _ in range(len(nums)):
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    drawRect(nums, [i, i+1])
        return nums

    def insertionSort(self, nums):
        drawRect(nums, (255,255,255))
        for i in range(len(nums) - 1):
                j = i
                while j >= 0 and nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1
                    drawRect(nums, [j-1, j])
        return nums
    
    def selectionSort(self, nums):
        for i in range(len(nums)):
            minIdx = i
            for j in range(i + 1, len(nums)):
                if nums[minIdx] > nums[j]:
                    minIdx = j
                drawRect(nums, [i, j])
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
            drawRect(nums, [j, minIdx])
        return nums


    def _merge():
        pass

    def mergeSort():
        pass

def drawRect(nums, ir=None):
    rgb = (255, 255, 255)
    screen.fill((0, 0, 0))
    for i, el in enumerate(nums):
        if ir and i in ir:
            rgb = (255,0,0)
        el *= 2
        # [x, y, width, height]
        pygame.draw.rect(screen, rgb, [0+(4*i), 1000-el, 3, el], 0)
        rgb = (255, 255, 255)
    pygame.display.flip()
    #pygame.mixer.Sound.play(sound)

def submitSort(nums):
    for i, el in enumerate(nums):
        el *= 2
        pygame.draw.rect(screen, (255,255,255), [0+(8*i), 1000-el, 7, el], 0)
    pygame.display.flip()
    for i, el in enumerate(nums):
        el *= 2
        pygame.draw.rect(screen, (127,255,0), [0+(8*i), 1000-el, 7, el], 0)
        pygame.display.update()

def Algorithims():
    algo = Algorithims()
    arr = list(range(1,480))
    random.shuffle(arr)
    arr = algo.bubbleSort(arr)
    submitSort(arr)
    pygame.time.delay(2500)
    arr = list(range(1,240))
    random.shuffle(arr)
    arr = algo.insertionSort(arr)
    submitSort(arr)
    pygame.time.delay(2500)
    arr = list(range(1,240))
    random.shuffle(arr)
    arr = algo.selectionSort(arr)
    submitSort(arr)
    pygame.time.delay(2500)

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound(os.path.join('sound', 'low.wav'))
screen = pygame.display.set_mode((1920, 1000))
clock = pygame.time.Clock()
clock.tick(30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    sort()
    pygame.time.delay(2500)
pygame.quit()