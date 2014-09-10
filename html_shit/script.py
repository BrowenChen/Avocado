#!/usr/bin/python
import sys

def draw(content):
    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 707
    html_skeleton_start = "<!DOCTYPE HTML><html><head><title>Cheatify</title><link rel='stylesheet' href='style.css'></head><body><div id='container'>"
    html_skeleton_end = "</div></body></html>"
    html_output = ""
    for line in content:
        html_output += (line + "\n")
    html = html_skeleton_start + html_output + html_skeleton_end
    f = open('output.html', 'w')
    f.write(html)

def parse_input(filename):
    f = open(filename, 'r')
    strings = []
    for line in f.readlines():
        if line != '\n':
            for message in line.split('\n'):
                if message != '':
                    strings.append(message)
    return strings

def main():
    if len(sys.argv) < 2:
        print("Please specify text file name")
        exit()
    input_file = sys.argv[1]
    cheatsheet_content = parse_input(input_file)
    #print(str(cheatsheet_content))
    draw(cheatsheet_content)

if __name__ == '__main__': main()

