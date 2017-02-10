'''
    Copyright (C) 2017  Mustafa Neguib. This project is an Open Source Artificial Intelligence
    Library.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    {project}  Copyright (C) {year}  {fullname}
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
'''

from Data import Node
from SearchAlgorithms import Search

def build_arad_network():
    '''
    This function builds a network of cities in
    Romania which are connected to each other via roads.
    After this function has completed its execution,
    the root node, in our case city of Arad is returned.
    :return: node
    '''
    arad = Node.Node(1, "Arad", None, 366, False)
    zerind = Node.Node(2, "Zerind", None, 374, False)
    oradea = Node.Node(3, "Oradea", None, 380, False)
    sibiu = Node.Node(4, "Sibiu", None, 253, False)
    rimnicu_vilcea = Node.Node(5, "Rimnicu Vilcea", None, 193, False)
    fagaras = Node.Node(6, "Fagaras", None, 178, False)
    pitesti = Node.Node(7, "Pitesti", None, 98, False)
    craiova = Node.Node(8, "Craiova", None, 160, False)
    timisoara = Node.Node(9, "Timisoara", None, 329, False)
    lugoj = Node.Node(10, "Lugoj", None, 244, False)
    mehadia = Node.Node(11, "Mehadia", None, 241, False)
    dobreta = Node.Node(12, "Dobreta", None, 242, False)
    bucharest = Node.Node(13, "Bucharest", None, 0, True)
    giurgiu = Node.Node(14, "Giurgiu", None, 77, False)
    urziceni = Node.Node(15, "Urziceni", None, 80, False)
    vaslui = Node.Node(16, "Vaslui", None, 199, False)
    lasi = Node.Node(17, "Lasi", None, 226, False)
    neamt = Node.Node(18, "Neamt", None, 234, False)
    hirsova = Node.Node(19, "Hirsova", None, 226, False)
    eforie = Node.Node(20, "Eforie", None, 161, False)

    arad.set_neighbours([(zerind, 75), (sibiu, 140), (timisoara, 118)])
    zerind.set_neighbours([(arad, 75), (oradea, 71)])
    oradea.set_neighbours([(zerind, 71), (sibiu, 151)])
    sibiu.set_neighbours([(arad, 140), (oradea, 151), (rimnicu_vilcea, 80)])
    rimnicu_vilcea.set_neighbours([(sibiu, 80), (craiova, 146), (pitesti, 97)])
    fagaras.set_neighbours([(sibiu, 99), (bucharest, 211)])
    pitesti.set_neighbours([(rimnicu_vilcea, 97), (craiova, 138), (bucharest, 101)])
    craiova.set_neighbours([(dobreta, 120), (pitesti, 138)])
    timisoara.set_neighbours([(arad, 118), (lugoj, 111)])
    lugoj.set_neighbours([(timisoara, 111), (mehadia, 70)])
    mehadia.set_neighbours([(lugoj, 70), (dobreta, 75)])
    dobreta.set_neighbours([(mehadia, 75), (craiova, 120)])
    bucharest.set_neighbours([(pitesti, 101), (giurgiu, 85), (fagaras, 211)])
    giurgiu.set_neighbours([(bucharest, 90)])
    urziceni.set_neighbours([(bucharest, 85), (vaslui, 142), (hirsova, 98)])
    vaslui.set_neighbours([(urziceni, 142), (lasi, 92)])
    lasi.set_neighbours([(vaslui, 92), (neamt, 87)])
    neamt.set_neighbours([(lasi, 87)])
    hirsova.set_neighbours([(urziceni, 98), (hirsova, 86)])
    eforie.set_neighbours([(hirsova, 86)])

    return arad


print("Open Source Artificial Intelligence Library Copyright (C) 2017 Mustafa Neguib")

search = Search.Search()
arad = build_arad_network()

print("Found Goal Node: " + search.bfs(arad).get_name())