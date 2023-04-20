from pprint import pprint
class RWA3:
    """
    A class to represent the functionality of pick-and-place of blocks using a robotic arm.

    ...

    Attributes
    ----------
    bottom : str
        block to be placed on the table
    middle : str
        block to be placed on the bottom block
    top : str
        block to be placed on the middle block, on top of the stack

    Methods
    -------
    config():
        returns the initial configuration
    stack(str,str):
        for stacking one block on top of  another
    unstack(str):
        for unstacking the block which is currently at the top of the stack
    put(str):
        for placing the block that was picked up by the gripper
    pick_up(str):
        for picking up the top block 
    print_configuration():
    move()
        for manipulating the configuration of blocks on the table using a gripper 

    """
    blocks = {
    'red': {
    'top': 'blue',
    'bottom': 'table'
    },
    'blue': {
    'top': 'green',
    'bottom': 'red'
    },
    'green': {
    'top': None,
    'bottom': 'blue'
        }
        }
    def __init__(self,bottom,middle,top) -> None:
        """ fucntion to initialise member variables

        Args:
            bottom (_type_): bottom block
            middle (_type_): middle block
            top (_type_): top block
        """
        self.bottom = bottom
        self.middle = middle
        self.top = top  
    

    def config(self):
        """ Function to return the initial configuration

        Returns:
            [bottom,middle,top]: a list which contains the initial configuration  
        """
        bottom= None
        for block in RWA3.blocks:
            if RWA3.blocks[block]['bottom'] == 'table':
                bottom = block
                break

        middle = RWA3.blocks[bottom]['top']

        top = RWA3.blocks[middle]['top']

        return [bottom,middle,top]

  
    def stack(self,b1:str,b2:str):
        """ function to perform the operation of stacking a block on top of another block

        Args:
            b1 (str): block to be stacked
            b2 (str): block on which another block is stacked 
        """
        if RWA3.blocks[b1]['top'] == 'gripper' and RWA3.blocks[b1]['bottom'] ==  None:
            RWA3.blocks[b1]['top']=None
            RWA3.blocks[b1]['bottom'] = b2
            RWA3.blocks[b2]['top'] = b1
            print(f'stacked {b1} on top of {b2}')


    def unstack(self,b1:str,b2:str):
        """ funtion to perform the operation of unstacking a block from another block

        Args:
            b1 (str): block to be unstacked
            b2 (str): block from which another block is unstacked
        """
        if RWA3.blocks[b1]['top'] == None and RWA3.blocks[b1]['bottom']==b2:
            RWA3.blocks[b1]['top'] = 'gripper' 
            RWA3.blocks[b1]['bottom'] = None
            RWA3.blocks[b2]['top']=None
            print(f'unstacked {b1} from {b2}')

    def put(self,b:str):
        """ function that performs the operation of using the gripper to place a block on the table

        Args:
            b (str): block which is on the gripper to be placed on the table
        """
        if RWA3.blocks[b]['top']== 'gripper' and RWA3.blocks[b]['bottom']==None:
            RWA3.blocks[b]['top'] = None
            RWA3.blocks[b]['bottom'] = 'table'
            print(f'put {b} on table')

    def pick_up(self,b:str):
        """ fucntion that performs the operation of picking up a block from the table 

        Args:
            b (str): block to be picked up from the table 
        """
        if RWA3.blocks[b]['top']== None and RWA3.blocks[b]['bottom'] == 'table':
            RWA3.blocks[b]['top'] = 'gripper'
            RWA3.blocks[b]['bottom'] = None
            print(f'picked up {b}')

    def print_configuration(self):
        """ function to return the current configuration
        """
        bottom= None
        for block in RWA3.blocks:
            if RWA3.blocks[block]['bottom'] == 'table':
                bottom = block
                break

        middle = RWA3.blocks[bottom]['top']

        top = RWA3.blocks[middle]['top']

        print(f'{bottom} block is on the table\n{middle} is on the {bottom} block\n{top} is on the {middle} block')

        
    
    def move(self,initial_bottom, initial_middle, initial_top):
        """ function that calls various functions to performs the operations of stacking,unstacking ,picking and placing the RWA3.blocks using the robotic arm

        Args:
            initial_bottom (_type_): bottom block in the initial configuration 
            initial_middle (_type_): middle block in the initial configuration
            initial_top (_type_): top block in the initial configuration
            final_bottom (_type_): bottom block in the final configuration
            final_middle (_type_): middle block in the final configuration
            final_top (_type_):  top block in the final configuration
        """
        print('\n---- unstacking blocks ----\n')
        self.unstack(initial_top,initial_middle)
        self.put(initial_top) 
        self.unstack(initial_middle,initial_bottom)
        self.put(initial_middle)
        # print('\n---- intermediate configuration ----\n')
        # pprint(blocks)
        print('\n---- stacking blocks ----\n')
        self.pick_up(self.middle)
        self.stack(self.middle,self.bottom)
        self.pick_up(self.top)
        self.stack(self.top,self.middle)
        # print('\n---- final configuration ----\n')
        # print(f'{final_bottom} block is on the table\n{final_middle} is on the {final_bottom} block\n{final_top} is on the {final_middle} block')
