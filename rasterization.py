import numpy as np

class Rasterization:
    # def rasterizate(self, lista_par_points):
    #     lista = []
    #     x1, y1, x2, y2 = 0, 0, 0, 0
    #     listapoints = lista_par_points

    #     for index in range(len(listapoints)):
    #         if index == len(listapoints) - 1:
    #             x1, y1 = listapoints[0][0], listapoints[0][1],
    #             x2, y2 = listapoints[index][0], listapoints[index][1]
    #         else:
    #             next_point_index = index + 1
    #             x1, y1 = listapoints[index][0], listapoints[index][1]
    #             x2, y2 = listapoints[next_point_index][0], listapoints[
    #                 next_point_index][1]
    #         dx = x2 - x1
    #         dy = y2 - y1

    #         if abs(dx) > abs(dy):
    #           start_point = min((x1, y1), (x2, y2))
    #           final_point = max((x1, y1), (x2, y2))
    #           points = self.rasteriza_reta(start_point[0], start_point[1],
    #                                        final_point[0], final_point[1])
    #         else:
    #           points_sort = np.array([(x1, y1), (x2, y2)])
    #           points_sort = points_sort[points_sort[:, 1].argsort()]

    #           points = self.rasteriza_reta(points_sort[0][0], points_sort[0][1],
    #                                        points_sort[1][0], points_sort[1][1])
    #         lista.append(points)

    #     return lista

    # def rasteriza_reta(self, x1, y1, x2, y2):
    #     dx = x2 - x1
    #     dy = y2 - y1

    #     if abs(dx) > abs(dy):
    #         return self.__rasteriza_dx(dx, dy, x1, y1, x2, y2)
    #     else:
    #         return self.__rasteriza_dy(dx, dy, x1, y1, x2, y2)

    
    # def __rasteriza_dx(self, dx, dy, x1, y1, x2, y2):
    #     ''' Pixel por linha '''
    #     lista = []
    #     m = dy / dx
    #     b = y2 - (m * x2)
    #     x = x1
    #     y = y1
    #     p = self.__produz_fragmento(x, y)
    #     lista.append(p)

    #     while (x < x2):
    #         x += 1
    #         y = (m * x) + b
    #         p = self.__produz_fragmento(x, y)
    #         lista.append(p)

    #     return lista

    # def __rasteriza_dy(self, dx, dy, x1, y1, x2, y2):
    #     ''' Pixel por coluna '''
    #     print("dx: {}, dy: {}, x1: {}, x2: {}, y1: {}, y2 {}".format(dx, dy, x1, x2, y1, y2))
    #     lista = []
    #     m = dx / dy
    #     b = x2 - (m * y2)
    #     x = x1
    #     y = y1
    #     p = self.__produz_fragmento(x, y)
    #     lista.append(p)

    #     while (y < y2):
    #         y += 1
    #         if dx == dy:
    #           x += 1
    #         else: 
    #           x = (m * y) + b
    #         print("m - {}, x - {}, b - {}, y - {}".format(m, x, b, y))
    #         p = self.__produz_fragmento(x, y)
    #         lista.append(p)

    #     return lista

    # def __produz_fragmento(self, x, y):
    #     xm = int(x)
    #     ym = int(y)
    #     p = [xm, ym]
    #     return p

        # def preenche_poligono(self, poligono):
    #     def checa_se_ponto_existe_no_poligono(ponto_test):
    #         for i in range(len(poligono)):
    #             for j in range(len(poligono[i])):
    #                 if poligono[i][j] == [ponto_test[0], ponto_test[1]]:
    #                     return (True, i)
    #         return (False, None)

    #     def gerar_points_internos(extremidades):
    #         internos = []
    #         for i in range(extremidades[0][1], extremidades[1][1], 1):
    #             if i != extremidades[0][1]:
    #                 internos.append([extremidades[0][0], i])
    #         return internos

    #     def achar_extremos():
    #         x_max = 0
    #         y_max = 0

    #         x_min = 0
    #         y_min = 0

    #         for lista_points in poligono:
    #             for ponto in lista_points:
    #                 if ponto[0] > x_max: x_max = ponto[0]
    #                 if ponto[1] > y_max: y_max = ponto[1]
    #                 if ponto[0] < x_min: x_min = ponto[0]
    #                 if ponto[1] < y_min: y_min = ponto[1] 

    #         return (x_min, y_min, x_max, y_max)

    #     extremos = achar_extremos()

    #     minX = extremos[0]
    #     minY = extremos[1]
    #     maxX = extremos[2]
    #     maxY = extremos[3]

    #     for i in range(minX, maxX + 1):
    #         points_extremidades = []
    #         for j in range(minY, maxY + 1):
    #             ponto_atual = [i, j]
    #             interseccao = checa_se_ponto_existe_no_poligono(ponto_atual)

    #             if interseccao[0]:
    #                 points_extremidades.append(ponto_atual)
                
    #                 if len(points_extremidades) >= 2:
    #                     if points_extremidades[1][1] == points_extremidades[0][1] + 1:
    #                       points_extremidades.remove(ponto_atual)
    #                       continue
                        
    #                     points_internos = gerar_points_internos(points_extremidades)
    #                     poligono[interseccao[1]].extend(points_internos)

    #                     points_extremidades = []
                
    #     return poligono

    def rasterizate(self, points_list):
        rasterization_list = []
        x1, y1, x2, y2 = 0, 0, 0, 0

        for index in range(len(points_list)):
            if index == len(points_list) - 1:
                x1, y1 = points_list[0][0], points_list[0][1],
                x2, y2 = points_list[index][0], points_list[index][1]
            else:
                next_point_index = index + 1
                x1, y1 = points_list[index][0], points_list[index][1]
                x2, y2 = points_list[next_point_index][0], points_list[
                    next_point_index][1]
            dx = x2 - x1
            dy = y2 - y1

            if abs(dx) > abs(dy):
              start_point = min((x1, y1), (x2, y2))
              final_point = max((x1, y1), (x2, y2))
              points = self.line_rasterizate(start_point[0], start_point[1],
                                           final_point[0], final_point[1])
            else:
              points_sort = np.array([(x1, y1), (x2, y2)])
              points_sort = points_sort[points_sort[:, 1].argsort()]

              points = self.line_rasterizate(points_sort[0][0], points_sort[0][1],
                                           points_sort[1][0], points_sort[1][1])
            rasterization_list.append(points)

        return rasterization_list

    def line_rasterizate(self, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1

        if abs(dx) > abs(dy):
            return self.__rasterizate_dx(dx, dy, x1, y1, x2, y2)
        else:
            return self.__rasterizate_dy(dx, dy, x1, y1, x2, y2)

    def fill_polygon(self, polygon_points):
        def check_if_polygon_contains_point(point):
            for i in range(len(polygon_points)):
                for j in range(len(polygon_points[i])):
                    if polygon_points[i][j] == [point[0], point[1]]:
                        return (True, i)
            return (False, None)

        def generate_intern_points(edges):
            intern_point_list = []
            for i in range(edges[0][1], edges[1][1], 1):
                if i != edges[0][1]:
                    intern_point_list.append([edges[0][0], i])
            return intern_point_list

        def find_edges():
            x_max = 0
            y_max = 0

            x_min = 0
            y_min = 0

            for point_list in polygon_points:
                for point in point_list:
                    if point[0] > x_max: x_max = point[0]
                    if point[1] > y_max: y_max = point[1]
                    if point[0] < x_min: x_min = point[0]
                    if point[1] < y_min: y_min = point[1] 

            return (x_min, y_min, x_max, y_max)

        edges = find_edges()

        minX = edges[0]
        minY = edges[1]
        maxX = edges[2]
        maxY = edges[3]

        for i in range(minX, maxX + 1):
            point_edges = []
            for j in range(minY, maxY + 1):
                current_point = [i, j]
                intersection = check_if_polygon_contains_point(current_point)

                if intersection[0]:
                    point_edges.append(current_point)
                
                    if len(point_edges) >= 2:
                        if point_edges[1][1] == point_edges[0][1] + 1:
                          point_edges.remove(current_point)
                          continue
                        
                        intern_points = generate_intern_points(point_edges)
                        polygon_points[intersection[1]].extend(intern_points)

                        point_edges = []
                
        return polygon_points

    def __rasterizate_dx(self, dx, dy, x1, y1, x2, y2):
        rasterizated_point_list = []
        m = dy / dx
        b = y2 - (m * x2)
        x = x1
        y = y1
        p = self.__make_fragment(x, y)
        rasterizated_point_list.append(p)

        while (x < x2):
            x += 1
            y = (m * x) + b
            p = self.__make_fragment(x, y)
            rasterizated_point_list.append(p)

        return rasterizated_point_list

    def __rasterizate_dy(self, dx, dy, x1, y1, x2, y2):
        rasterizated_point_list = []
        m = dx / dy
        b = x2 - (m * y2)
        x = x1
        y = y1
        p = self.__make_fragment(x, y)
        rasterizated_point_list.append(p)

        while (y < y2):
            y += 1
            if dx == dy:
              x += 1
            else: 
              x = (m * y) + b
            p = self.__make_fragment(x, y)
            rasterizated_point_list.append(p)

        return rasterizated_point_list

    def __make_fragment(self, x, y):
        xm = int(x)
        ym = int(y)
        p = [xm, ym]
        return p
