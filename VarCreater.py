def VarCreater(var_name, var_type, default_value, description):
  if var_type=='int+':
    while True:
      var=input(description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=int(var)
        except ValueError:
          print('\nError: Type an integer larger than 0\n')
        else:
          if var<=0:
            print('\nError: Type an integer larger than 0\n')
          else:
            return var
            break
  elif var_type=='int+-':
    while True:
      var=input(description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=int(var)
        except ValueError:
          print('\nError: Type a valid integer\n')
        else:
          return var
          break
  elif var_type=='float+':
    while True:
      var=input(description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=float(var)
        except ValueError:
          print('\nError: Type a valid number larger than 0\n')
        else:
          if var<=0:
            print('\nError: Type a valid number larger than 0\n')
          else:
            return var
            break
  elif var_type=='float+-':
    while True:
      var=input(description+' The default value is '+str(default_value)+'.\nValue: ')
      if var=='':
        var=default_value
        return var
        break
      else:
        try:
          var=float(var)
        except ValueError:
          print('\nError: Type a valid Number\n')
        else:
          return var
          break
  elif var_type=='str':
    var=input(description)
    return var
  else:
    raise TypeError('Data type not available. Check for errors in var_type argument\n')

# Usage: var=VarCreater(var_name, var_type, default_value, description)
# var_name, var_type, description must be type 'str'
# 5 types of var_type: 'int+' (integer larger than 0), 'int+-' (integer), 'float+' (floating point number larger than 0),
# 'float+-' (floating point number), 'str' (string)
# description will appear upon input
