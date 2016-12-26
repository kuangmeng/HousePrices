#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 22:32:11 2016

@author: 匡盟盟
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
from sklearn.linear_model import Lasso
import warnings
import seaborn as sns
from scipy.stats import skew
from scipy.stats.stats import pearsonr
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet, LassoCV, LassoLarsCV
from sklearn.model_selection import cross_val_score
from operator import itemgetter
import itertools
import xgboost as xgb
from sklearn.svm import SVC
from itertools import product, chain
