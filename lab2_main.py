# Libraries
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from lab2_datafilecreation import create_mycsv, get_dict_from_csv
from lab2_SimpleGroupedColorFunc import SimpleGroupedColorFunc
import random

# creating CSV file
file_name = create_mycsv()
# creating dict from CSV file
dictionary_from_csv = get_dict_from_csv(file_name)

# additional list with medals one by one is created for Second Ring (Inside)
g_s_b_medals = []
for i in range(len(dictionary_from_csv['gold_medals'])):
        g_s_b_medals.append(dictionary_from_csv['gold_medals'][i])
        g_s_b_medals.append(dictionary_from_csv['silver_medals'][i])
        g_s_b_medals.append(dictionary_from_csv['bronze_medals'][i])
        
# START Donut plot with subgroups       
# Create colors
# colors that will b user for First Ring (outside)
a, b, c, d, e = [plt.cm.Reds, plt.cm.Greys, plt.cm.GnBu, plt.cm.YlGnBu, plt.cm.Wistia]
# colors that will b user for Second Ring (Inside)
g, s, br = [plt.cm.Wistia, plt.cm.Greys, plt.cm.copper]
 
# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(dictionary_from_csv['total_medals'], radius=1.35, labels=dictionary_from_csv['countries_abbr'], colors=[a(0.6), b(0.9), c(0.5), d(0.9), e(0.1)])
plt.setp(mypie, width=0.5, edgecolor='white')
 
# Second Ring (Inside)
mypie2, _ = ax.pie(g_s_b_medals, radius=1.35-0.5, labels=g_s_b_medals, labeldistance=0.7, colors=[g(0.5), s(0.5), br(0.3)])
plt.setp(mypie2, width=0.5, edgecolor='white')
plt.margins(0,0)
 
# show it
fig.canvas.set_window_title('Donut plot with subgroups')
plt.show()
# END Donut plot with subgroups

# START Word Cloud
# Creating str that will contain country name * number of medals
text = str()
for i in range(len(dictionary_from_csv['countries'])):
    text += (dictionary_from_csv['countries'][i] + " ") * dictionary_from_csv['total_medals'][i]
text = text[:-1]

temp_list = text.split(' ')
random.shuffle(temp_list)
text = ' '.join(temp_list)

# Create costum color by groups
color_to_words = {
    'red': ['Canada'],
    'black': ['Germany'],
    'aqua': ['UnitedStates'],
    'darkblue': ['Norway'],
    'yellow': ['SouthKorea']
}

default_color = 'grey'

grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)

# Create the wordcloud object
wordcloud = WordCloud(width=450, height=450, max_font_size=100, background_color="whitesmoke").generate(text)
# Apply color function
wordcloud.recolor(color_func=grouped_color_func)
# Display the generated image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
# END Word Cloud
