mathpass={"Tom", "John","Mary", "Jimmy", "Sunny", "Amy"}
englishpass={"John", "Mary" , "Tony" , "Bob" , "Pony", "Tom", "Alice"}
both_no_pass={"Joe", "Donald", "Daniel", "Helen"}
allpass=mathpass&englishpass
print("數學及格但英⽂不及格: ",mathpass-allpass)
print("數學不及格但英⽂及格: ",englishpass-allpass)
print("兩科都及格: ",allpass)
allpeople=mathpass|englishpass|both_no_pass
print("全班總共有",len(allpeople),"個同學")