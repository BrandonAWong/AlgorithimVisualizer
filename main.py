import pygame
import random
import os
import time

class Sorts():
    def bubbleSort(self, nums: list) -> list:
        comps = la = 0
        drawRects(nums)
        for _ in range(len(nums)):
            for i in range(len(nums) - 1):
                comps += 1
                la += 2
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    la += 2
                    drawRects(nums, [i, i+1])
                #self.text(la, comps)
        self.submitSort(nums)
        return nums

    def insertionSort(self, nums: list) -> list:
        drawRects(nums)
        for i in range(len(nums) - 1):
                j = i
                while j >= 0 and nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1
                    drawRects(nums, [j-1, j])
        self.submitSort(nums)
        return nums
    
    def selectionSort(self, nums) -> list:
        for i in range(len(nums)):
            minIdx = i
            for j in range(i + 1, len(nums)):
                if nums[minIdx] > nums[j]:
                    minIdx = j
                    drawRects(nums, [i, j])
            nums[i], nums[minIdx] = nums[minIdx], nums[i]
            drawRects(nums, [j, minIdx])
        self.submitSort(nums)
        return nums
    
    def _drawMerge(self, nums: list, ir: list=None):
        pass
    
    def mergeSort(self, nums: list, dNums: list=None) -> list:
        if dNums is None:
            self._drawMerge(nums)
            dNums = nums
        if len(nums) > 1:
            midpoint = len(nums) // 2
            l = self.mergeSort(nums[:midpoint], dNums)
            dNums[:len(l)] = l
            #drawRects(dNums, [midpoint])
            r = self.mergeSort(nums[midpoint:], dNums)
            dNums[midpoint:] = r
            #drawRects(dNums, [midpoint])
            li = ri = i = 0
            while li < len(l) and ri < len(r):
                if l[li] <= r[ri]:
                    nums[i] = l[li]
                    li += 1
                else:
                    nums[i] = r[ri]
                    ri += 1
                drawRects(nums, [i])
                i += 1
            while li < len(l):
                nums[i] = l[li]
                li += 1
                i += 1
                drawRects(nums, [i])
            while ri < len(r):
                nums[i] = r[ri]
                ri += 1
                i += 1
                drawRects(nums, [i])
        self.submitSort(nums)
        return nums      
    
    def text(self, la: int, c: int):
        font.render_to(screen, (0, 10), f'List accesses: {la}  Comparrisons: {c}', (255, 255, 255))
        pygame.display.update()

    def submitSort(self, nums):
        for i, num in enumerate(nums):
            pygame.draw.rect(screen, (255,255,255), [8*i, 1000-num, 7, num], 0)
        pygame.display.flip()
        for i, num in enumerate(nums):
            pygame.draw.rect(screen, (127,255,0), [8*i, 1000-num, 7, num], 0)
            pygame.display.update()
        pygame.time.delay(2500)
        

class Searches():
    def linearSearch(self, nums: list, x: int) -> int:
        comps: int = 0
        drawRects(nums)
        for i in range(len(nums)):
            self.text(x, i+1, comps)
            drawRects(nums, [i])
            comps += 1
            if nums[i] == x:
                self.text(x, i+1, comps)
                self.submitSearch(i, x)
                return i
        return -1
    
    def binarySearch(self, nums: list, x: int) -> int:
        drawRects(nums)
        comps = la = 0
        l, r = 0, len(nums)
        while l <= r:
            midpoint = (r + l) // 2
            drawRects(nums, [midpoint])
            self.text(x, la, comps)
            if nums[midpoint] == x:
                self.submitSearch(midpoint, x)
                return midpoint
            elif nums[midpoint] < x:
                l = midpoint
            elif nums[midpoint] > x:
                r = midpoint
            comps += 1
            la += 1
        return -1

    def text(self, x: int, la: int, c: int):
        font.render_to(screen, (0, 10), f'Searching for: {int(x/4)}  List accesses: {la}  Comparrisons: {c}', (255, 255, 255))
        pygame.display.update()
    
    def submitSearch(self, i: int, x: int):
        pygame.draw.rect(screen, (127,255,0), [8*i, 1000-x, 7, x], 0)
        pygame.display.update()
        pygame.time.delay(2500)


def drawRects(nums: list, ir: list=None):
    rgb = (255, 255, 255)
    screen.fill((0, 0, 0))
    for i, el in enumerate(nums):
        if ir and i in ir:
            rgb = (255,0,0)
        # [x, y, width, height]
        pygame.draw.rect(screen, rgb, [8*i, 1000-el, 7, el], 0)
        rgb = (255, 255, 255)
    pygame.display.flip()
    #pygame.mixer.Sound.play(sound)

def makeList():
    arr = list(range(1,240))
    arr = [4*x for x in arr]
    random.shuffle(arr)
    return arr

def sort():
    algo = Sorts()
    search = Searches()
    #algo.bubbleSort(makeList())
    #algo.insertionSort(makeList())
    #algo.selectionSort(makeList())
    #print(algo.mergeSort(makeList()))
    #search.linearSearch(makeList(), random.choice([4*x for x in range(1,240)]))
    l = list(range(1,240))
    l = [4*x for x in l]
    search.binarySearch(l, random.choice(l))


pygame.init()
font = pygame.freetype.Font("Minecraft.ttf", 14)
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