class person:
    def __init__(self):
        self.name = "Thiyan"
class do(person):
    def check(self):
        if self.name == "Thiyan":
            print("Thiyan")

p = person()
#print(p.x)
d = do()
d.check()

string = "[1,2,3]"
print(list(string))


for i, j in enumerate([3,4,5]):
    print(i,j)

class enemy:
    def print1(self):
        print("here")
        '''def enemy_on_surface(self, enemy_list, special_case):
        if len(enemy_list) == 0:
            return []
        for index, e in enumerate(enemy_list):
            not_in_surface = []
            for i in self.base_list:
                #print(2)
                #print(e[0][0].rect.x, i.rect.x - 25, (i.rect.x + i.width) - 20)
                if int(e[0][0].rect.x) in range(i.rect.x - 25, (i.rect.x + i.width) - 20):

                    if special_case:
                        if i == self.big_rock_1a:
                            if int(e[0][0].rect.y - self.velocity) < i.rect.y and int(e[0][0].rect.y +self.velocity) > i.rect.y:
                                self.velocity = e[0][0].rect.y - i.rect.top - 3
                                break
                        elif i in self.float_rock[1]:
                            if int(e[0][0].rect.bottom - self.velocity) < i.rect.top + 12 and int(e[0][0].rect.bottom +self.velocity) > i.rect.top + 12:
                                #print(vikram[0][0].rect.bottom, i.rect.top, self.velocity)
                                self.velocity = (e[0][0].rect.y - i.rect.top) + 10
                                break
                        elif i in self.float_rock[0]:
                            if int(e[0][0].rect.bottom - self.velocity) < i.rect.top and int(e[0][0].rect.bottom +self.velocity) > i.rect.top:
                                self.velocity = (e[0][0].rect.y - i.rect.top) + 10
                                break
                        elif i in self.float_rock[2]:
                            if int(e[0][0].rect.bottom - self.velocity) < i.rect.top and int(e[0][0].rect.bottom + self.velocity) > i.rect.top:
                                self.velocity = (e[0][0].rect.y - i.rect.top)
                                break
                        elif i == self.main_rock_1a:
                            if int(e[0][0].rect.bottom - self.velocity) < (i.rect.bottom - 54) and int(e[0][0].rect.bottom + self.velocity) > (i.rect.bottom - 54):
                                self.velocity = (e[0][0].rect.y - (i.rect.bottom-54))
                                break
                    else:
                        if i == self.big_rock_1a:
                            #print(2)
                            if int(e[0][0].rect.y) in range(i.rect.top - 6, i.rect.top + 6):
                                print(0)
                                break
                        elif i in self.float_rock[1]:
                            if int(e[0][0].rect.bottom) in range(i.rect.top + 8, i.rect.top + 16):
                                #print(vikram[0][0].rect.bottom, i.rect.top)
                                #print(0)
                                break
                        elif i in self.float_rock[0]:
                            if int(e[0][0].rect.bottom) in range(i.rect.top + 8, i.rect.top + 16):
                                #print(vikram[0][0].rect.bottom, i.rect.top)
                                #print(0)
                                break
                        elif i in self.float_rock[2]:
                            if int(e[0][0].rect.bottom) in range(i.rect.top +28, i.rect.top + 37):
                                #print("i am else")
                                break
                        elif i == self.main_rock_1a:
                            #print(vikram[0][0].rect.bottom, i.rect.bottom - 53)
                            if int(e[0][0].rect.bottom) in range(i.rect.bottom - 55, i.rect.bottom - 50):
                                #print("main")
                                break

                else:
                    #print(1)
                    not_in_surface.append(index)
                return not_in_surface

'''
enemy().print1()

def printh():
    print('h')

def hai(i):
    i()

hai(printh)


def generator():
    while True:
        print(1)
        yield 1
        print(2)

print(generator)
