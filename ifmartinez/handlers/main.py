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


class MainHandler(webapp2.RequestHandler):
    def post(self):
        km = str(self.request.get("edKm", "0"))
        tiempo = str(self.request.get("edTm", "0"))
        consumo = str(self.request.get("edCm", "0"))

        if len(km.strip()) == 0:
            km = -1
        if len(tiempo.strip()) == 0:
            tiempo = -1
        if len(consumo.strip()) == 0:
            consumo = -1

        if km != -1 and tiempo != -1 and consumo != -1 and km.isdigit() and tiempo.isdigit() and consumo.isdigit() and float(tiempo) != 0:
            velocidad = float(km) / float(tiempo)
            consumo_final = float(consumo) * float(km)
            self.response.write(
                "Velocidad (media): " + str(velocidad) + "\nConsumo total: " + str(consumo_final) + " L")
        else:
            self.response.write("Error: Datos incorrectos.")


app = webapp2.WSGIApplication([
    ('/hello', MainHandler)
], debug=True)
