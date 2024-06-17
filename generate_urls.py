# Input data
input_data = """
S01:25
S02:2
S03:14
S04:40
S05:2
S06:26
S07:10
S08:4
S10:28
S11:20
S12:29
S13:48
S14:2
S15:2
S16:1
S17:1
S18:21
S19:13
S20:25
S21:1
S22:39
S23:2
S24:80
S25:42
S26:11
S27:14
S28:5
S29:17
U01:1
U02:1
U03:1
U05:7
U06:1
U07:1
U08:5
U09:1
"""

# Process the input data
lines = input_data.strip().split('\n')

# Generate the output
output = []
for line in lines:
    category, count = line.split(':')
    count = int(count)
    for i in range(1, count + 1):
#        output.append(f"{category}-{i:02}")
#        output.append(f"{category}-{i}")
        output.append(f"https://results.eci.gov.in/PcResultGenJune2024/Constituencywise{category}{i}.htm")

# Print the output
for item in output:
    print(item)
