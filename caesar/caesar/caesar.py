#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
# caesar.py

ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def alphabet_position(letter):
    alphabet = ALPHABET_LOWERCASE if letter.islower() else ALPHABET_UPPERCASE
    return alphabet.index(letter)

def rotate_char(char, rotation):
    if not char.isalpha():
        return char

    alphabet = ALPHABET_LOWERCASE if char.islower() else ALPHABET_UPPERCASE
    new_pos = (alphabet_position(char) + rotation) % 26
    return alphabet[new_pos]

def encrypt(text1, rotation):
    answer = ""
    for char in text1:
        answer += rotate_char(char, rotation)
    return answer





class MainHandler(webapp2.RequestHandler):


    def get(self, rotationnumber="0"):

        form="""
        <html><head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
        </head>
        <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="%(rotationnumber)s">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text"></textarea>
            <br>
            <input type="submit">
        </form>

        </body>
        </html>
                """


        self.response.out.write(form % {"rotationnumber": rotationnumber})





    def post(self, rotated="", rotationnumber=""):

        form1="""
        <html><head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
        </head>
        <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="rot" value="%(rotationnumber)s">
                <p class="error"></p>
            </div>
            <input type="text" name="text" value="%(rotated)s"></input>
            <br>
            <input type="submit">
        </form>

        </body>
        </html>
                """



        text = str(self.request.get('text'))

        rot = int(self.request.get('rot'))
        rotated = encrypt(text, rot)
        #    % {"answer": answer}
        self.response.out.write(form1 % {"rotated": rotated, "rotationnumber": rot})


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
