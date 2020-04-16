import numpy as np
import os.path
import os
import itertools
import copy


###################
# DataEntry CLASS #
###################

class DataEntry:

    def __init__(self, 
                 ndim                   = None,  
                 description            = None,  
                 reference              = None,    
                 dimensions_descriptors = None,  
                 axes                   = None,  
                 values                 = None,  
                 err_up                 = None,  
                 err_down               = None,  
                 err_up2                = None,  
                 err_down2              = None,  
                 upper_lim              = None,  
                 lower_lim              = None):
        
        self.ndim                   = ndim                  
        self.description            = description           
        self.reference              = reference             
        self.dimensions_descriptors = dimensions_descriptors
        self.axes                   = axes                  
        self.values                 = values                
        self.err_up                 = err_up                
        self.err_down               = err_down              
        self.err_up2                = err_up2               
        self.err_down2              = err_down2             
        self.upper_lim              = upper_lim             
        self.lower_lim              = lower_lim             
    
    def __repr__(self):
        """string describing the class"""
        return "corecon DataEntry class"

    def __str__(self):
        """output of print"""

        ostr=""
        ostr += "ndim                   = %i\n"%self.ndim                  
        ostr += "description            = %s\n"%_insert_blank_spaces(self.description, 25)
        ostr += "reference              = %s\n"%self.reference             
        ostr += _get_str_from_array1d("dimensions_descriptors = ", self.dimensions_descriptors)
        ostr += _get_str_from_array("axes                   = ", self.axes                  )
        ostr += _get_str_from_array("values                 = ", self.values                )
        ostr += _get_str_from_array("err_up                 = ", self.err_up                )
        ostr += _get_str_from_array("err_down               = ", self.err_down              )
        ostr += _get_str_from_array("err_up2                = ", self.err_up2               )
        ostr += _get_str_from_array("err_down2              = ", self.err_down2             )
        ostr += _get_str_from_array("upper_lim              = ", self.upper_lim             )
        ostr += _get_str_from_array("lower_lim              = ", self.lower_lim             )
        return ostr

    def __eq__(self,other):
        """custom equality"""

        return(
                               (self.ndim                 == other.ndim                   ) & \
                               (self.description          == other.description            ) & \
                               (self.reference            == other.reference              ) & \
                _compare_arrays(self.dimensions_descriptors, other.dimensions_descriptors ) & \
                _compare_arrays(self.axes                  , other.axes                   ) & \
                _compare_arrays(self.values                , other.values                 ) & \
                _compare_arrays(self.err_up                , other.err_up                 ) & \
                _compare_arrays(self.err_down              , other.err_down               ) & \
                _compare_arrays(self.err_up2               , other.err_up2                ) & \
                _compare_arrays(self.err_down2             , other.err_down2              ) & \
                _compare_arrays(self.upper_lim             , other.upper_lim              ) & \
                _compare_arrays(self.lower_lim             , other.lower_lim              ) )
