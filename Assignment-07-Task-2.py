#                   Assignment-07 and Task 02
#                     Author: ADIL RAUF
#
#   Write a Python implementation of a possible collection of classes which can be used to
#   represent a music collection (for example, inside a music player), focusing on how they
#   would be related by composition . You should include classes for songs, artists,
#   albums and playlists..

# COMPOSITION RELATION between MUSIC_PLAYER and Songs, Albums, Playlists classes

from File1_for_Assignment_07_Task_2 import Songs
from File2_for_Assignment_07_Task_2 import Albums
from File3_for_Assignment_07_Task_2 import Play_Lists

# CHILD/DERIVED Class INHERITED from BASE/PARENT Classes Songs, Albums, Playlists

class Music_Player(Songs, Albums, Play_Lists):

  def Songs_Implementation(self):                                                #  This Method is PUBLIC
    if Artist_Name == 'George Michael':
       Artist_Type = "Rock"
       self.Artist_Type = Artist_Type

  def Play_Lists_Implementation(self):                                           #  This Method is PUBLIC
     if self.Type_of_Song == 'm':
        self.Song_List = Music_Player_Details.Song_List

  def Albums_Implementation(self):                                               #  This Method is PUBLIC
     self.Song_List = Music_Player_Details.Song_List

  def print_statement(self):                                                    # This method is PUBLIC
    print()
    print("========== Artist Attribute ==================")
    print("Artist Name =", self.Artist_Name)
    print("Artist Type =", self.Artist_Type)
    print("Artist Nationality =", self.Artist_Nationality)
    print("Born = ", self.Born)
    print("Died = ", self.Died)
    print("========== Artist Songs List =================")
    print("Songs Album of",Artist_Name," = ", Music_Player_Details.Song_List)
    print("========== PlayList of Songs =================")
    print(self.Song,"List = ", self.Mourning_Song_List)

# CREATING INSTANCE FROM THE INHERITED CHILD/DERIVED CLASS "Bank_Account"

Music_Player_Details = Music_Player()

# INPUT

Artist_Name_1 = input("Name of Artist: <g=George Michael> : ")
if Artist_Name_1 == "g":
  Artist_Name = "George Michael"
  Music_Player_Details.A(Artist_Name)

Type_of_Song = input("Type of Song: <r=Rock, f=Folk, m=Mourning> : ")
if Type_of_Song == "m":
  Music_Player_Details.P(Type_of_Song)

# OUTPUT

Music_Player_Details.Songs_Implementation()
Music_Player_Details.Albums_Implementation()
Music_Player_Details.print_statement()


