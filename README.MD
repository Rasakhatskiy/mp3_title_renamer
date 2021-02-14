# Replace MP3 song title with file name, excluding number and extention  

#### Usage sample  
| Filename       | Title             | Result title|
| -------------- | ----------------- | -----       |
| 01. Song 2.mp3 | japanese teext    | Song 2      |
| Break.mp3      | pirated_music.com | Break       |

#### Dependencies  
[eyed3](https://eyed3.readthedocs.io/en/latest/)  
`python -m pip install eyed3`  

#### Run  
Script renames files recurcively through given directory  
`python main.py "D:\Music\Another dir"`