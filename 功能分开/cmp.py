#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:32:11 2016

@author: 匡盟盟
"""
import pandas as pd
import numpy as np
import sys
train = pd.read_csv(sys.argv[1])
test = pd.read_csv(sys.argv[2])
train["SalePrice"]=train["SalePrice"]-test["SalePrice"]
def neg(x):
	if x<0:
		x=-1*x
	return x
train["SalePrice"]=train["SalePrice"].apply(neg)
train.to_csv("sol3.csv", index = False)
print (train["SalePrice"].sum())
