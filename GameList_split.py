# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:06:45 2024

@author: shender
"""

games_e = [
    [
        ('2023-05-06','KEM', 81, 'TIL', 197),
        ('2023-05-06','SWS', 66, 'TIL', 250),
        ('2023-05-06','CTB', 109, 'SWS', 108),
        ('2023-05-06','CTB', 107, 'KEM', 210),
        ('2023-05-07','CTB', 70, 'TIL', 279),
        ('2023-05-07','KEM', 224, 'SWS', 128)
    ],
    [
        ('2023-06-24','MRD', 274, 'TNF', 261)
    ],
    
    [
        ('2023-07-22','TIL', 217, 'TNF', 299)
    ],
    
    [
        ('2023-07-29','MRD', 300, 'TNF', 147)
    ],
    [
        ('2023-09-09','TIL', 193, 'KEM', 106)
    ],
    [   #ACE Autumn Clash
        ('2023-11-18','DHR', 82, 'BOR', 256),
        ('2023-11-18','PAN', 111, 'BOR', 193),
        ('2023-11-18','DHR', 103, 'PAN', 158)
    ],
    [
        ('2023-11-25','TIL', 91, 'MRD', 219)
    ],
#2024
    [
        ('2024-02-10','BOR', 197, 'TIL', 193),
        ('2024-02-10','TNF', 484, 'KEM', 103),
    ],
    [
        ('2024-02-24','SWS', 257, 'TNF(B)', 165),
        ('2024-02-24','MRD(B)', 129, 'SWS', 219),
        ('2024-02-25','MRD', 239, 'TNF', 249),
        ('2024-02-25','TNF', 291, 'TIL', 246)
    ],
    [
        ('2024-03-16','CTB', 300, 'TNF(B)', 246),
#        ('2024-03-16','CTB', 0, 'MRD(B)', 0),
    ],
    [
        ('2024-04-13','BOR', 521, 'KEM', 66),
        ('2024-04-13','MRD', 264, 'TIL', 116),
    ],
    [
        ('2024-04-20','CTB', 262, 'SWS', 158),
        ('2024-04-20','MRD(B)', 299, 'TNF(B)', 181),
    ],
    [
        ('2024-05-19','BOR', 213, 'TNF', 253),
        ('2024-05-19','KEM', 21, 'MRD', 308)
    ],
    [
        ('2024-06-23','TIL', 338, 'KEM', 117),
        ('2024-06-23','BOR', 271, 'MRD', 101)
    ],
    [
        ('2024-07-06','TNF', 429, 'TIL', 203),
    ],
    #[
        #('2024-07-07','CTB', 100, 'MRD(B)', 0),
    #],
]

games_w = [
    [
        ('2023-04-22', 'PHH', 152, 'PIT', 172),
    ],
    [
        ('2023-05-12','TOM', 168, 'CHK', 176),
    ],
    [
        ('2023-05-13','CHK', 148, 'TOM', 173),
        #('2023-05-13','RCR', 100, 'SLG', 0), #forfeit
        ('2023-05-13','TRD', 66, 'PIT', 533),
    ],
    [
        ('2023-05-14','TRD', 169, 'CLG', 115),
    ],
    [
        ('2023-05-20','CAB', 353, 'DEM', 56),
        ('2023-05-20','CAB', 334, 'CLG', 46),
        ('2023-05-20','CLG', 137, 'DEM', 206),
    ],
    [
        ('2023-06-03','CLG', 37, 'PHH', 208),
        ('2023-06-03','PHH', 96, 'TOM', 91),
        ('2023-06-04','CLG', 51, 'TOM', 364),
    ],
    [
        ('2023-06-10','DEM', 59, 'RCR', 339),
    ],
    [   #Sibling Rivalry
        ('2023-06-16','CAB', 113, 'SDA', 236),
        ('2023-06-17','DGC', 230, 'SDA', 120),
        ('2023-06-17','DGC', 113, 'SLG', 168),
        ('2023-06-17','SLG', 284, 'CAB', 77),
        ('2023-06-18','CAB', 55, 'DGC', 413),
        ('2023-06-18','SDA', 75, 'SLG', 290),
    ],
    [   #DOTD
        ('2023-06-24','AUA', 135, 'PIT', 121),
        ('2023-06-24','AUA', 43, 'CBB', 173),
        ('2023-06-24','CWB', 172, 'DIS', 175),
        ('2023-06-24','CWB', 147, 'CRD', 136),
        ('2023-06-24','CBB', 124, 'PIT', 135),
        ('2023-06-24','DIS', 180, 'CRD', 96),
        ('2023-06-25','CWB', 232, 'AUA', 91),
        ('2023-06-25','CBB', 102, 'DIS', 142),
        ('2023-06-25','PIT', 122, 'CRD', 115),
    ],
    [
        ('2023-07-08','CWB', 386, 'CLG', 85),
        ('2023-07-08','CWB', 200, 'PHH', 147),
        ('2023-07-09','CLG', 72, 'PHH', 252),
    ],
    [
        ('2023-07-15','CHK', 173, 'PSO', 163),
        ('2023-07-15','CHK', 81, 'CRD', 208),
        ('2023-07-15','CRD', 176, 'PSO', 175),
        ('2023-07-15','RCR', 145, 'CBB', 132),
    ],
    [
        ('2023-07-29','CLG', 35, 'RCR', 313),
    ],
    [   #WHC
        ('2023-10-21','CWB', 167, 'RCR', 134),
        ('2023-10-21','CBB', 154, 'PHH', 44),
        ('2023-10-21','CBB', 49, 'SLG', 278),
        ('2023-10-21','DGC', 228, 'CRD', 118),
        ('2023-10-21','DIS', 130, 'SDA', 169),
        ('2023-10-21','CRD', 201, 'PIT', 79),
        ('2023-10-22','DIS', 162, 'PHH', 92),
        ('2023-10-22','CWB', 123, 'SDA', 279),
        ('2023-10-22','CWB', 43, 'SLG', 291),
        ('2023-10-22','DGC', 151, 'SLG', 130),
        ('2023-10-22','DGC', 243, 'SDA', 128),
        ('2023-10-22','PIT', 115, 'RCR', 191),
    ],
    #2024
    [   #Dumpster Fire
        ('2024-02-24','CWB', 213, 'PIT', 132),
        ('2024-02-24','CWB', 97, 'MCM', 230),
        ('2024-02-24','CRD', 202, 'PSO', 106),
        ('2024-02-24','CRD', 120, 'MCM', 197),
        ('2024-02-24','PIT', 169, 'PSO', 175),
        ('2024-02-25','CWB', 171, 'PSO', 239),
        ('2024-02-25','CWB', 149, 'CRD', 161),
        ('2024-02-25','CRD', 228, 'PIT', 77),
        #('2024-02-25','MCM', 100, 'PIT', 0), #forfeit
        ('2024-02-25','MCM', 331, 'PSO', 85),
    ],
    [
        ('2024-03-02','CLG', 287, 'PIT(B)', 73),
    ],
    [
        ('2024-03-16','CLG', 125, 'DEM', 226),
        ('2024-03-16','CLG', 123, 'TRD', 208),
        ('2024-03-16','DEM', 192, 'TRD', 160),
    ],
    [
        ('2024-03-23','FLC', 53, 'TOM', 234)
    ],
    [
        ('2024-04-06','CLG', 161, 'PIT(B)', 175)
    ],
    [   #BoBH
        ('2024-04-13','PHH', 130, 'CAB', 156),
        ('2024-04-13','CAB', 162, 'AUA', 106),
        ('2024-04-14','PHH', 166, 'TOM', 173),
        ('2024-04-14','TOM', 138, 'AUA', 107),
        ('2024-04-14','CAB', 133, 'TOM', 118),
        ('2024-04-14','PHH', 195, 'AUA', 104),
    ],
    [
        ('2024-04-20','CAB(B)', 124, 'FLC', 227)
    ],
    [   #Salem Slam
        ('2024-04-26','CRD', 135, 'SDA', 110),
        ('2024-04-27','PSO', 133, 'SDA', 176),
        ('2024-04-27','CRD', 334, 'CHK', 101),
        ('2024-04-27','CHK', 105, 'PSO', 241),
        ('2024-04-28','CRD', 187, 'PSO', 111),
        ('2024-04-28','SDA', 312, 'CHK', 95),
    ],
    
    [   #Flat Track Fever
        ('2024-05-10','CHK', 187, 'TOM', 183),
        ('2024-05-11','CHK', 257, 'PSO', 113),
        ('2024-05-12','TOM', 265, 'PSO', 161),        
        ('2024-05-12','CHK', 204, 'TOM', 171),      
    ],
    [   #DOTD
        ('2024-05-11','RCR', 204, 'CBB', 87),
        ('2024-05-11','CWB', 210, 'PIT', 82),
        ('2024-05-11','MCM', 399, 'CBB', 3),
        ('2024-05-11','PIT', 116, 'PHH', 101),
        ('2024-05-11','MCM', 237, 'RCR', 45),
        ('2024-05-11','CWB', 273, 'PHH', 64),
        ('2024-05-12','MCM', 242, 'CWB', 85),
        ('2024-05-12','RCR', 160, 'PIT', 87),
        ('2024-05-12','CBB', 131, 'PHH', 114),
    ],  
    [
        ('2024-06-01','CLG', 159, 'CBB(B)', 152)
    ],
    [   #IHOD-Pt2
        ('2024-06-07','SLG(B)', 212, 'SDA(B)', 159),
        #('2024-06-07','DGC', 100, 'DIS', 0), #forfeit
        ('2024-06-07','SLG', 214, 'SDA', 65),
        
        ('2024-06-08','SLG(B)', 149, 'CAB', 233),
        ('2024-06-08','RCR', 120, 'SDA', 240),
        ('2024-06-08','SLG', 179, 'DGC', 115),
        ('2024-06-08','SDA(B)', 110, 'CAB', 266),
        ('2024-06-08','RCR', 169, 'DIS', 151),        
        
        ('2024-06-09','CAB', 122, 'RCR', 233),
        ('2024-06-09','SLG', 323, 'DIS', 57),
        ('2024-06-09','DGC', 287, 'SDA', 88),
    ],
    [
        ('2024-06-15','FLC', 233, 'CLG', 79)
    ],
    [
        ('2024-06-15','RCR', 49, 'SLG', 277)
    ],
    [
        ('2024-06-29','PHH(B)', 186, 'FLC', 124)
    ],
    [
        ('2024-07-06','TRD', 165, 'CLG', 123)
    ],
    [
        ('2024-07-13','RCR', 218, 'SLG(B)', 84)
    ],
    [   #Roller Derby Tournament 2024
        ('2024-07-20','CLG', 103, 'PHH(B)', 245),
        ('2024-07-20','FLC', 255, 'DEM', 110),
        ('2024-07-20','AUA', 454, 'TRD', 68),
        ('2024-07-20','DEM', 157, 'PIT(B)', 205),
        #('2024-07-20','FLC', 100, 'TRD', 0), #forfeit
        ('2024-07-21','DEM', 205, 'CLG', 213),
        ('2024-07-21','PIT(B)', 112, 'PHH(B)', 177),
        ('2024-07-21','AUA', 254, 'FLC', 140),
        ('2024-07-21','TRD', 117, 'PIT(B)', 256),
    ],
    [
        ('2024-07-27','RCR', 137, 'CBB', 84)
    ],

]
