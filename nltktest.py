# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 12:57:35 2016

@author: charu
"""
import sys
sys.path.append("/usr/local/lib/python3.5/site-packages/")
import nltk


#playing with nltk

#COMMAND_DICT =
grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V | V NP | V NP PP | V PP NP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)
  
def find_verb(tree):
    VPs = list(tree.subtrees(filter=lambda x: x.label()=='VP'))   
    V_In_VPs = map(lambda x: list(x.subtrees(filter=lambda x: x.label()=='V')), VPs)
    vs = [verb.leaves()[0] for verbs in V_In_VPs for verb in verbs]
    return vs

def find_object_NP(tree):
    VPs = tree.subtrees(filter=lambda x: x.label()=='VP')
    #VPsl = list(VPs)    
    #print(VPsl)
    NP = [NPs for VP in VPs for NPs in VP if NPs.label()=='NP']
    print(NP)
    #OBJ = map(lambda x: list(x.subtrees(filter=lambda x: x.label()=='N')), NP)
    #objs = [obj.leaves()[0] for objects in OBJ for obj in objects]
    #print(objs)
    return NP

def find_object_and_params(tree_list):
    N = [Ns for tree in tree_list for Ns in tree if Ns.label=='N']
    obj = [Noun.leaves()[0] for noun in N]
    
    return zip(obj, params)
    
sr_parser = nltk.ChartParser(grammar1)
sent = 'John ate a dog on a cat'.split()
parsed = sr_parser.parse(sent)
for tree in sr_parser.parse(sent):
    print(tree)
    find_verb(tree)
    find_object_NP(tree)
    
def traverse_and_send_command(tree):
    sentence_start = False
    subject_found = False
    verb_found = False
    verb_recognized = False
    object_found = False
    object_recognized = False
    
    SUBJECT = 'S'
    VERB = 'VP'
    
    
    '''
    for subtree in tree:
        v = None
        command = None
        if type(subtree) is nltk.Tree:
            if subtree.label() == SUBJECT:
                sentence_start = True
                subject_found = True
            if subtree.label() == VERB:
                v = find_word('V', subtree)
                print(v)                
             f check_if_word('V', v):
                    command = v
                    parameters = parse_rest_of_vp(tree)
                
    '''

def find_word(part_of_speech, tree):
    for sub in tree:
        if sub.label == part_of_speech:
            return sub
            
def check_if_word(part_of_speech, command):
    if part_of_speech in WORD_DICT:
        if command in WORD_DICT[part_of_speech]:
            return True
        else:
            print("Command does not exist")
            return False
    else:
        print("POS doesn't exist")
        return False
            
    
    
                
            
                
                