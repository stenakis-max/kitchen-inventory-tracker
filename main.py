# Global inventory variables
available_eggs = 1
available_flour = 2
available_sugar = 3

def check_kitchen_stock():
    """Calculates and displays the current state of the kitchen inventory."""
    total_items = available_eggs + available_flour + available_sugar
    print(f'The kitchen has {total_items} total items:')
    print(f'- {available_eggs} eggs')
    print(f'- {available_flour} flour')
    print(f'- {available_sugar} sugar')

def use_eggs(available_eggs, eggs_to_use):
    """
    Validates egg availability. Returns the remaining eggs if successful,
    or the original count if there are not enough eggs.
    """
    if eggs_to_use > available_eggs:
        print('The kitchen does not have enough eggs.')
        return available_eggs
        
    print(f'{eggs_to_use} egg(s) used out of {available_eggs} available.')
    return available_eggs - eggs_to_use

def make_fried_egg(available_eggs):
    """Recipe function that checks inventory and triggers egg usage."""
    has_enough_eggs = available_eggs >= 1
    
    if has_enough_eggs:
        available_eggs = use_eggs(available_eggs, 1)
        print("Made a fried egg. Yummy!")
    else:
        print("Could not make a fried egg. Not enough eggs!")
        
    return available_eggs

# --- Execution ---

# 1. Initial inventory check
check_kitchen_stock()
print("-" * 30)

# 2. Cook breakfast and explicitly update the global inventory state
available_eggs = make_fried_egg(available_eggs)
print("-" * 30)

# 3. Final inventory check to confirm state reduction
check_kitchen_stock()
