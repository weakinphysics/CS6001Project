import pyspiel 
import itertools
from typing import List, DefaultDict
from collections import defaultdict


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class GameTreeNode:
    def __init__(self, player, actions=None, cards=None, parent=None, children=None, information_set:int=0):
        self.player = player
        self.cards = cards
        self.actions = actions
        self.parent = parent
        self.children = children
        self.information_set = information_set

    def add_child(self, child_node):
        self.children.append(child_node) # this is assuming the parameter is passed by reference
        child_node.parent = self 


class GameTreePoker:
    def __init__(self, cards:list, rounds: int):
        self.information_sets = defaultdict()
        self.deck = cards

        return
    
    def construct_tree(self):
        cards = ['J', 'Q', 'K']
        possible_deals = list(itertools.permutations(cards, 2))
        
        for deal in possible_deals:
            deal_node = GameTreeNode(player=1, action=None, cards=deal, parent=self.root, information_set=)
            self.root.add_child(deal_node)
            self.create_decision_nodes(deal_node, player=1)
    
    def create_decision_nodes(self, current_node, player):
        if player == 1:
            for action in ['Bet', 'Pass']:
                p1_action_node = GameTreeNode(player=2, action=action, cards=current_node.cards, parent=current_node)
                current_node.add_child(p1_action_node)
                self.create_decision_nodes(p1_action_node, player=2)
        elif player == 2:
            for action in ['Bet', 'Pass', 'Fold', 'Call', 'Raise']:
                p2_action_node = GameTreeNode(player='Terminal', action=action, cards=current_node.cards, parent=current_node)
                current_node.add_child(p2_action_node)

    def print_tree(self, node=None, depth=0):
        if node is None:
            node = self.root
        indent = "    " * depth
        print(f"{indent}{node.player} {'-' if node.action else ''} {node.action or 'Root'} {node.cards or ''}")
        for child in node.children:
            self.print_tree(child, depth + 1)



class PokerGame:
    def __init__(num_players, num_rounds, limit, )