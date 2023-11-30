<h1>Данный репозиторий содержит проект по анализу городских данных</h1>
<h2>Авторы: Катынсус Александр, Жембровский Даниил, Шаповаленко Екатерина и Адрианова Екатерина</h2>
<h3>Содержание репозитория:</h3>
<ol><li>
В папке data находятся все данные по сервисам в городе Калининград
</li>
<li>
Файлы building.geojson, buildings.geojson содержат исходные данные о зданиях в городе Калининград
</li>
<li>
Файлы geocoded_buildings_partN.geojson содержат геокодированные точки (Координаты конвертировали в улицы латинскими буквами)
</li>
<li>Файл new_buildings содержит промежуточнные значения зданий</li>
<li>Файл full_data содержит финальный результат обработки данных</li>
<li>kaliningrad_buildings - DAG для геокодироваания зданий</li>
<li>Buildings_data_processing - ноутбук с выполненной предобработкой данных</li>
<li>yandex_parser - парсер для сбора данных о сервисах с яндекс карт</li>
<li>city_model - модель города Калининград</li>
</ol>

<h2>Визуализация города и зданий</h2>

![Screenshot 2023-11-12 173547.png](src%2FScreenshot%202023-11-12%20173547.png)

![Screenshot 2023-11-12 173702.png](src%2FScreenshot%202023-11-12%20173702.png)


<h2>Загрузка слоя со зданиями находится в папке notebooks в ноутбуке под названием Buildings_formatting</h2>

[Buildings_formatting.ipynb](notebooks%2FBuildings_formatting.ipynb)

<h2>Загрузка слоя с кварталами и их кластеризация находятся в папке notebooks в ноутбуке под названием blocks_clusterization</h2>
<h3>Пример визуализации кластеризации кварталов в Ленинском районе города Калининград:</h2>

[blocks_clusterization.ipynb](notebooks%2Fblocks_clusterization.ipynb)

![Screenshot1.JPG](src/Screenshot1.JPG)

<h2>Загрузка слоя с сервисами и их кластеризация находятся в папке notebooks в ноутбуке под названием services_clusterization</h2>
<h3>Пример визуализации кластеризации сервисов:</h2>

[services_clusterization.ipynb](notebooks%2Fservices_clusterization.ipynb)

![Screenshot2.png](src/Screenshot2.png)

<h2>Ноутбук с созданием графов города разного типа (walk, drive, public_transport) находится в папке notebooks</h2>

[Graphs.ipynb](notebooks%2FGraphs.ipynb)


<h2>Создание изохронов было выполнено в ноутбуке isochrones в папке notebooks</h2>
<p>Для постреония изохронов была выбрана точка с координатами [[54.722642, 20.514075]]</p>

[isochrones.ipynb](notebooks%2Fisochrones.ipynb)

<h2>Выделение зданий, которые находятся в каждом изохроне, сделано в ноутбуке Buildings_inside_isochrones</h2>

[Buildings_inside_isochrones.ipynb](notebooks%2FBuildings_inside_isochrones.ipynb)

<p>Визаулизации изохронов и зданий внутри изохронов представлены на следующих скриншотах</p>
<p>Drive изохрон</p>

![drive_iso.png](src%2Fdrive_iso.png)

<p>Walk изохрон</p>

![pedestrian_iso.png](src%2Fpedestrian_iso.png)

<p>Public transport изохрон</p>

![public_transport_iso.png](src%2Fpublic_transport_iso.png)
