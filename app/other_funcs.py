from random import choice
import math


def main(data):
    d = ['up', 'down', 'left', 'right']
    head_x = data["you"]["body"][0]["x"]
    head_y = data["you"]["body"][0]["y"]
    board_width = data["board"]["width"]
    board_height = data["board"]["width"]
    health = data["you"]["health"]
    food = []
    for item in data["board"]["food"]:
        temp_x = item["x"]
        temp_y = item["y"]

        food.append((temp_x,temp_y))

    bodys = []
    for snake in data["board"]["snakes"]:
        for coordinates in snake["body"]:
            temp_x = coordinates["x"]
            temp_y = coordinates["y"]

            bodys.append((temp_x,temp_y))

    '''print("head_x:",head_x)
    print("head_y:",head_y)
    print("board_width:",board_width)
    print("board_height:",board_height)
    print("food:",food)
    print("health:",health)'''
    #print("bodys:",bodys)

    #       ----------------------  LOGIC BEHIND DECIDING ON NEXT MOVE ------------------------------------------


    if (health <= 30):
        narest_food_coordinates = get_nearest_food(food, head_x, head_y)
        d = go_towards(bodys, board_width, board_height, head_x, head_y, narest_food_coordinates[0], narest_food_coordinates[1])
    else:
        safe_space(bodys,board_width,board_height,d,head_x,head_y)
        

    print("d in main:", d)

    if len(d)<=0:
        direction = "right"
    else:
        #direction = choice(d)
        direction = d[0]

    return direction


#               ---------------------------- ALL FUNCTIONS BELOW THIS LINE ------------------------------------------


def go_towards(bodys,board_width,board_height,head_x,head_y, goto_x, goto_y): # goes towards a given point (to get food for now)
    prioratized_directions = []

    if (head_x <= goto_x):
        prioratized_directions.insert(0, "right")
        prioratized_directions.append("left")
    if (head_x == goto_x):
        pass
    if (head_x > goto_x):
        prioratized_directions.insert(0, "left")
        prioratized_directions.append("right")

    if (head_y <= goto_y):
        prioratized_directions.insert(0, "down")
        prioratized_directions.append("up")
    if (head_y == goto_y):
        pass
    if (head_y > goto_y):
        prioratized_directions.insert(0, "up")
        prioratized_directions.append("down")

    safe_space(bodys,board_width,board_height,prioratized_directions,head_x,head_y)


    print("IN FUNCTION:", prioratized_directions)

    return prioratized_directions




def get_nearest_food(food ,head_x, head_y):
    if (len(food)==0):
        return(-1,-1)  # could be changed to the center of the board
    else:
        dist = []
        for item in food:
            x = head_x - item[0]
            y = head_y - item[1]
            distance = math.sqrt((x**2)+(y**2))
            temp = [distance,item]
            dist.append(temp)


        smallest_info = dist[0]
        for count in range(0,len(dist)):
            if (smallest_info[0]>dist[count][0]):
                smallest_info = dist[count]


        return smallest_info[1]



def is_safe_space(bodys,board_width,board_height,x,y): # checks if a single space is safe or not
    if is_snake_body(bodys,x,y) or is_wall(board_width,board_height,x,y):
        return False
    else:
        return True


def safe_space(bodys,board_width,board_height,d,x,y):#checks the four tiles around the space at x and y and modifies direction list
    if is_snake_body(bodys,x+1,y) or is_wall(board_width,board_height,x+1,y,"right"):#right
        d.remove("right")
    if is_snake_body(bodys,x-1,y) or is_wall(board_width,board_height,x-1,y,"left"):#left
        d.remove("left")
    if is_snake_body(bodys,x,y-1) or is_wall(board_width,board_height,x,y-1,"up"):#up was y+1, caused us to kill ourself
        d.remove("up")
    if is_snake_body(bodys,x,y+1) or is_wall(board_width,board_height,x,y+1,"down"):#down
        d.remove("down")
    #print("d:",d)


def is_snake_body(bodys,x,y):
    result = False
    for i in bodys:
        if i[0] == x and i[1] == y:
            result = True
            #print("is body")
    return result


def is_wall(board_width,board_height,x,y,way):  # if outside the room returns true, else returns false
    result = False
    if x >= board_width or x < 0:
        result = True
        #print("is wall",way)
    if y >= board_height or y < 0:
        result = True
        #print("is wall",way)
    #was an else, fixed
    return result

def d_is_1(d):
    if len(d)==1:
        return True
    else:
        return False
		
