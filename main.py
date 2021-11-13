import numpy as np
import random


class Game():
    def __init__(self):
        self.board=np.matrix([4*[0],4*[0],4*[0],4*[0]])
        self.income_brick()
        self.income_brick()
        self.flag = False

    def index_None_value(self):

        indexes=np.where(self.board==0)
        indexes=list(zip(indexes[0],indexes[1]))
        return indexes

    def income_brick(self):

        new_brick=random.choice([2,2,2,2,2,2,2,2,2,4])
        index=random.choice(self.index_None_value())
        self.board[index[0],index[1]]=new_brick

    def move(self,towards):

        if towards=='w':
            self.move_up()
        if towards == 'x':
            self.move_down()
        if towards == 'a':
            self.move_left()
        if towards == 'd':
            self.move_right()

    def move_up(self):

        for i in range(4):
            for j in range(3):
                if self.board[j,i]==0:
                    continue
                for k in range(j+1,4):
                    if self.board[k,i] == 0:
                        continue
                    if self.board[j,i]==self.board[k,i]:
                        self.board[j,i]*=2
                        self.board[k,i]=0
                        self.flag = True
                        break
                    if self.board[j,i]!=self.board[k,i]:
                        break

        for i in range(4):
            for j in range(3):
                if self.board[j,i]!=0:
                    continue
                for k in range(j+1,4):

                    if self.board[k,i] == 0:
                        continue
                    self.board[j,i]=self.board[k,i]
                    self.board[k,i]=0
                    self.flag = True
                    break

    def move_down(self):
        for i in range(3, -1, -1):
            for j in range(3, 0, -1):
                if self.board[j,i] == 0:
                    continue
                for k in range(j - 1, -1, -1):
                    if self.board[k,i] == 0:
                        continue
                    if self.board[j,i] == self.board[k,i]:
                        self.board[j,i] *= 2
                        self.board[k,i] = 0
                        self.flag = True
                        break
                    if self.board[j,i] != self.board[k,i]:
                        break

        for i in range(3, -1, -1):
            for j in range(3, 0, -1):
                if self.board[j,i] != 0:
                    continue
                for k in range(j - 1, -1, -1):
                    if self.board[k,i] == 0:
                        continue
                    self.board[j,i] = self.board[k,i]
                    self.board[k,i] = 0
                    self.flag = True
                    break

    def move_left(self):

        for i in range(4):
            for j in range(3):
                if self.board[i,j]==0:
                    continue
                for k in range(j+1,4):
                    if self.board[i, k] == 0:
                        continue
                    if self.board[i,j]==self.board[i,k]:
                        self.board[i,j]*=2
                        self.board[i,k]=0
                        self.flag = True
                        break
                    if self.board[i,j]!=self.board[i,k]:
                        break

        for i in range(4):
            for j in range(3):
                if self.board[i,j]!=0:
                    continue
                for k in range(j+1,4):
                    if self.board[i, k] == 0:
                        continue
                    self.board[i,j]=self.board[i,k]
                    self.board[i,k]=0
                    self.flag = True
                    break

    def move_right(self):

        for i in range(3,-1,-1):
            for j in range(3,0,-1):
                if self.board[i, j] == 0:
                    continue
                for k in range(j-1,-1,-1):
                    if self.board[i, k] == 0:
                        continue
                    if self.board[i, j] == self.board[i, k]:
                        self.board[i, j] *= 2
                        self.board[i, k] = 0
                        self.flag = True
                        break
                    if self.board[i, j] != self.board[i, k]:
                        break

        for i in range(3,-1,-1):
            for j in range(3,0,-1):
                if self.board[i, j] != 0:
                    continue
                for k in range(j-1,-1,-1):
                    if self.board[i, k] == 0:
                        continue
                    self.board[i, j] = self.board[i, k]
                    self.board[i, k]=0
                    self.flag = True
                    break

    def check_if_win(self):

        check=np.where(self.board==2048)

        if check[0].size!=0:
            return True
        return False

    def check_if_lose(self):

        check = np.where(self.board == 0)
        if check[0].size==0:
            self.move_up()
            if self.flag==True:
                return True
            self.move_down()
            if self.flag==True:
                return True
            self.move_left()
            if self.flag==True:
                return True
            self.move_right()
            if self.flag==True:
                return True
            return False
        return True



class general():
    def __init__(self):
        game=Game()
        print(game.board)
        while True:
            towards=input("Enter the direction:")
            game.move(towards)
            if game.flag==False:
                continue
            game.income_brick()
            if (win:=game.check_if_win())==True:
                print('your won')
                break
            print(game.board)
            check_game=game
            if (lose:=check_game.check_if_lose())==False:
                print('your lose')
                break
            game.flag=False

if __name__ == '__main__':
    general()
