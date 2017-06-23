import pickle
from testxpaht import myPageStucture

thisclass=myPageStucture.pageStructure()

pickle1=pickle.dumps(thisclass)
print pickle1
pickle2=pickle.loads(pickle1)

print pickle2.name
print pickle2.num