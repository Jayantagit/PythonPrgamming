st=set({1,2,3,4,4,5,"Ashish",True,3+5j})
print(st)
st.add("Jayanta")
print(f"complete set is={st}")
for s in st:
    print(s,end="")

print(s,end="")
print("========================")
print(f"complete set pre update is={st}")
st.update([1,2,4,9,"python","Java","Selenium"])
print(f"complete set post update is={st}")

#del st
st.pop()
print(f"complete set is after pop={st}")
st.discard("Selenium")
print(f"complete set is={st}")
print("========================")
st.remove(9)
print(f"complete set after remove is={st}")
