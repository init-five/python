# try block
try:
    with open('filelog.text', 'r') as reader:
        reader.read()

# catch block with customized failure message
#except:
    #print("I reached this block because there is failur in try block")
# when you try to catch the error python is throwing
except Exception as e:
    print(e)

# finally
finally:
    print("cleaning up resources")