"""Examples of set and dictionary syntax."""

pids: set[int] = {710000000, 712345678}
pids.add(730822638)
print(pids)
# added int to the set

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
ice_cream["vanilla"] += 110
print(ice_cream)
# added 110 to existing vanilla value

print(len(ice_cream))
# tells us the number of key-value pairs in dictionary

# use append for lists, add for sets

ice_cream["mint"] = 3
print(ice_cream)

# accessing a specific value
print(ice_cream["chocolate"])

# update values

ice_cream["vanilla"] = 10
print(ice_cream)

if "mint" in ice_cream:
    print(f"{ice_cream["mint"]} Orders of Mint!")
else:
    print("No Orders of Mint")

# removing a key-value pair from dictionary   (can store value for later)
ice_cream.pop("strawberry")
print(ice_cream)


for key in ice_cream:
    # print keys
    print(key)
    # print value of keys
    print(ice_cream[key])
