# Love Calculator

print('''
    8                            8
     8      /```|     .@@@@@,     8
     8     |  66|_    @@@@@@@@,   8 (\/)
     8     C     _)   aa`@@@@@@   8  \/
     8(\/)  \ ._|    (_   ?@@@@   8
    |8:\/:~:~) /:~:~: =' @@@@~:~:~8
    |8::::::/\\/`\;_:::\ (__::::::8
    |8:::::| \ '|___/` \\// `\):::8
    |8::::|| | '|::/ /  ^^  \ \:::8
    |8::::|| | ' \:| \__/\__/ |:::8
    |8o:::|\ \  ' |:\_\    /_/::::8o
    |"8o:::=\ \===::/`\`%%`/'\::::"8o
    |\"8o~|  \_\  \|   `""`   |:~:~\8o
    \ \"8o\   )))  \           \::::"8o
     \ \"8o\`.  \   \           \::::"8o
      \|~~~~~| -|| -|mmmmmmmmmmmm~~~~~|
       `~~~~~|  ||  |~~|  |~|  |~~~~~~
             |  ||  |  |__| |__|
             |  ||  |  \  | \  |
             |__||__|  (~~^\(~~^\
             (   \   \  `-._)`-._)
              `-._)-._)

''')

print("True Love Calculator")
Male_name = input("Enter your name here: ")
Female_name = input("Enter your crush name here: ")

combined_name = (Male_name + Female_name).lower()

#true
t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
first = t + r + u + e

#love
l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
second = l + o + v + e

score =int(str(first) + str(second))
if (score < 30) or (score > 90):
  print(f"Hey {Male_name} {Female_name} Your score is {score}, you are like Tom and Jerry.")
elif (score >= 40) and (score <= 50):
  print(f"Hey {Male_name} {Female_name} Your score is {score}, you are like Vanila and Strawberry.")
else:
  print(f"Hey {Male_name} {Female_name} Your score is {score}. None to say Hahaa.......")
