<style type="text/css">
    ol { list-style-type: lower-alpha; }
    ol>li>ol { list-style-type: numeric; }
</style>

# Pauta Examen 2017-2

## Indicaciones

- El examen dura **3 horas**. 
- El examen tiene **120 puntos**.
- Podrá hacer preguntas cada 30 minutos, en voz alta. Sólo se responderán preguntas que ayuden a mejorar la comprensión del enunciado. 
- Conteste cada pregunta en hojas separadas; es decir, no puede haber dos (o más) preguntas en una misma hoja. Las hojas de respuesta están incluidas con el enunciado. Puede, además, solicitar hojas adicionales a los ayudantes, en caso de que fuese necesario. 
- Si decide no responder una pregunta, deberá entregar una hoja en blanco con su nombre, número de alumno, usuario de GitHub y número de la pregunta.
- Una declaración de clases y métodos corresponde a 
    ```python
    class A:
        def __init__(self, param1):
            self.param1 = param1

        def metodo_1(self, param2):
            # param2: corresponde a Y
            # return: el resultado de hacer multiplicar self.param1 y param2
            # Entrega la multiplicacion entre self.param1 y param2
            pass
    ```

- La descripción del flujo de un método es una explicación detallada de lo que hace el método. Por ejemplo, para el siguiente método:

    ```python
    def multiplicar(a, b, c):
        aux = a * b
        aux = aux * c
        return aux
    ```

    Una buena descripción sería: _"Se multiplican a y b, se guardan en una variable, luego esta se multiplica por c y se retorna ese resultado."_. Una mala descripción sería: _"Se multiplican a, b y c."_.


## Pregunta 1 (40 pts)

El excéntrico _chef_ irlandés, Neville McKawas, es dueño del famoso restorán de comida alternativa, _La lechuga mágica_. En este último año, las ventas de _La lechuga mágica_ han disfrutado de un notable éxito.
La notoriedad de este restorán puede explicarse tanto por aceptar _nevcoins_ como medio de pago, como por los diversos tipos de menús ofrecidos, asociado a un tipo de dieta. Existen cinco de ellas: pescetarianismo, vegetarianismo, veganismo, crudiveganismo, frugivorismo.

Cada pedido (que ocurren a una tasa de 15 pedidos por hora) realizado a este restorán consiste en uno o más menús, que contiene un plato de fondo, una bebida y un postre. Cada uno de estos ítems tiene un costo por los ingredientes y un precio de venta. Además, cada ítem puede ser pedido por separado; sin embargo, comprar el menú completo entrega un descuento de tres _nevcoins_.
Este incentivo hace que, en la práctica, el 80% de los clientes prefiera comprar los tres ítems juntos como un menú.
Notemos, además, que los pedidos pueden ser buscados directamente en el local por los clientes, o pagar cinco _nevcoins_ adicionales para recibirlos a domicilio.
De estadísticas anteriores, los pedidos a domicilio ocurren un 65% de las veces. Y, en estos casos, para saber cuánta bencina se utiliza (un gasto relevante para _La lechuga mágica_), cada pedido almacena su distancia en kilómetros. 

Para satisfacer esta demanda, _La lechuga mágica_ dispone de empleados que realizan diferentes funciones, y que reciben distintos sueldos (en _nevcoins_) de forma mensual.
Por temas de contabilidad, _La lechuga mágica_ cuenta con un registro ---que guarda el nombre, la fecha de nacimiento y el RUT--- de sus trabajadores _full-time_: hay cajeros, repartidores de comida, y cocineros.
De estos últimos, se contratan según sus años de experiencia, por lo que se dividen en _chef_ de cocina, _sous-chef_ de cocina, ayudante de cocina, y lavador de utensilios. Todos ellos saben cocinar, pero el _chef_ de cocina es quien se encarga de organizar al resto.
Además, el _chef_, en sus ataques de furia culinaria, decide despedir de forma aleatoria a un _sous-chef_ una vez a la semana, quien recibe, como indemnización, un salario equivalente a tres meses.

Este restorán atiende de martes a domingo, desde 13 horas hasta las 21 horas, a excepción del jueves que abre más tarde, a las 17 horas. Sin embargo, el horario punta ocurre, con un 80% de probabilidad, los viernes desde las 19 horas hasta que el local cierra. En el otro 20%, ese viernes se comporta de forma regular. A raíz de esto, cuando hay un horario punta (en donde la tasa alcanza los 25 pedidos por hora), se contratan más repartidores de forma interina. A ellos, a diferencia de los repartidores _full-time_, se les paga por pedido entregado.

Además, para conocer más a sus clientes, el restorán guarda algo de información de ellos: nombre completo, edad, y el número de pedidos en el último mes. Este último dato permite implementar una estrategia de _marketing_ que consiste en que los clientes frecuentes ---definido como más de cinco pedidos en este periodo--- reciben una rebaja del 10% en el precio de sus pedidos.


Con el propósito de expandirse a una nueva sucursal en el barrio Lastarria, Neville decide aplicar los conceptos aprendidos en su paso por IIC2233 para realizar una simulación durante un mes de su flamante local.
Esta herramienta tiene como objetivo obtener estadísticas para tomar una decisión informada acerca de cómo organizar esta sucursal.
Por ejemplo, se intentará estimar cuánto dinero se recaudará por ventas, cuántos empleados contratar, cómo manejar la demanda en horarios punta, cuánto se tendrá que pagar en gastos, y cuántos menús en promedio se entregarán por día.

1.  **(15 pts)** Diseñe el diagrama de clases (en formato UML) que modela este problema. Indique claramente las clases, las relaciones entre estas (composición, agregación y herencia), y los métodos y atributos que estime conveniente. En caso que no fuese claro cuál de las relaciones existe entre dos clases, justifique su respuesta ---en una línea es suficiente. Realice los supuestos que considere necesarios. 
    Y, además, recuerde que los símbolos en UML son:
    
    ![Relaciones_UML](https://i.imgur.com/HbUnH55.png)


    
    ### Solución
    
    El diagrama se muestra a continuación.
    
    ![Diagrama](https://i.imgur.com/IbgLE9k.png)

    Este diagrama contempla las clases mínimas que deben existir en la modelación. En sus modelaciones pueden existir clases extras, las cuales no suman puntaje.
        
    Pueden haber distintas formas de modelar el problema, pero debe tener consistencia con lo indicado en el enunciado.
    
    #### Distribución de Puntaje
    
    **(8 pts)** Se tienen bien todas las clases mínimas. Si no crea las clases SousChef, Ayudante y Lavador son **6 pts**
    
    **(2 pts)** Los tipos de dieta son tratados como un atributo de la clase Menu y no como especializaciones.
    
    **(4 pts)** Las relaciones están bien hechas.
    
    **(1 pto)** Las relaciones están bien dirigidas.

1. **(10 pts)** Escriba la declaración de clases y métodos según el diagrama realizado en **(a)**. Los atributos de cada clase deben estar declarados en el método `__init__` de la clase. No olvide ser consistente con el diagrama de clases que realizó en **(a)**.

    ### Solución
    
    ```python
    class Item:
    
        def __init__(self, precio, costo, tipo):
            # Puede tener un nombre
            self.precio = precio
            self.costo = costo
            self.tipo = tipo
            # Puede ser: 'plato de fondo', 'bebida', 'postre'.
            # O cualquier identificador que esté asociado a eso.
    
    class Menu:
        def __init__(self, tipo, items):
            self.items = items # Una lista de instancias de Item.
                
            self.tipo = tipo 
            # Puede ser: 'pescetarianismo', 'vegetarianismo', 
            #  'veganismo', 'crudiveganismo', 'frugivorismo'.
                
        @property
        def precio(self):
            '''
            Este property encapsula los precios de sus ítems.
            Retorna la suma de sus precios, restándole 3 nevcoins.
            '''
            pass
                    
        @property
        def costo(self):
            '''
            Este property encapsula los costos de sus ítems.
            Retorna la suma de sus costos.
            '''
            pass
        
    class Pedido:
        
        def __init__(self, menus, items, cliente, entrega):
            self.menus = menus
            self.items = items
            self.cliente = cliente 
                        
            # Se debe ver si se va a ir a dejar a domicilio o no.
            self.entrega = entrega
                        
            # Se agregan los kilómetros que recorre en caso de
            # ser repartido a domicilio.
            self.kilometros = 0
        
        @property
        def precio(self):
            '''
            Esta property encapsula los precios de sus menus e ítems.
            Retorna la suma de los precios y debe considerar si el cliente
            tiene o no descuento de cliente frecuente.
            '''
            pass
        
        @property
        def costo(self):
            '''
            Esta property encapsula los costos de sus menus e ítems.
            Retorna la suma de los costos.
            '''
            pass
    
    class Cliente:
        def __init__(self, nombre, edad):
                                
            self.nombre = nombre
            self.edad = edad
                                
            # Guarda el número de pedidos por lo que al crearse comienza en 0.
            self.pedidos = 0 
            # Otra opción sería que al crearse se le agreguen de inmediato los
            # pedidos realizados.
                                
        @property
        def frecuente(self):
            '''
            Esta property permite permite saber si el cliente es frecuente.
            Retorna True si los pedidos son más que 5, o False en caso contrario.
            '''
            pass
                                
    class Empleado:
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo)
            # Puede tener nombre, edad, etc
            self.nombre = nombre
            self.rut = rut
            self.fecha_de_nacimiento = fecha_de_nacimiento
            self.sueldo = sueldo
                                    
    class Repartidor(Empleado):
                                        
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo, tipo):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo)
            self.tipo = tipo
              
            # Debe llevar registro del número pedidos que realiza
            self.pedidos_realizados = 0
            
            # Debe tener la referencia al pedido que lleva
            self.pedido = None
        
        def repartir(self, pedido):
            '''
            Este método hace que el Repartidor vaya a dejar un pedido.
            Además, guarda en el pedido el kilometraje.
            '''
    
    class Cajero(Empleado):
                                                
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo)                      
                         
        def cobrar(self, pedido):                     
            '''
            Este método se encarga de cobrar el pedido.
            '''                
    
    class Cocinero(Empleado):
        
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo)
            self.anos_experiencia = anos_experiencia
             
        def cocinar(self):
            '''
            Este método se encarga de cocinar los pedidos.
            '''
        
    class Chef(Cocinero):

        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia)
        
        def despedir(self, souschef):
            '''
            Este método toma a una instancia de souschef y la
            despide del Restorán.
            Debe guardar el costo de indemnización.
            '''
                                                                    
        def organizar(self, *cocineros):
            '''
            Este método toma instancias de cocineros y los organiza
            '''   
    
    class SousChef(Cocinero):
                        
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia)           
        
    class Ayudante(Cocinero):
                                   
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia)
    
        def ayudar(self):
            '''
            Este método hace que el ayudante ayude en la cocina
            o en lo que se necesite.
            '''
            
    class Lavador(Cocinero):
                                           
        def __init__(self, nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia):
            super().__init__(nombre, rut, fecha_de_nacimiento, sueldo, anos_experiencia)
      
        def lavar(self):
            '''
            Este método hace que el Lavador lave.
            '''
                      
    class Restoran:
        '''
        Se debe recordar que esta es la clase encargada
        de realizar la simulación.
        '''
        
        def __init__(self, clientes, cajeros, chefs, souschefs, ayudantes,
                     lavadores, menus, items, p_hora_punta = 0.8,
                     dias_totales = 30, tasa_pedidos = 15, tasa_punta = 25):
            
            self.clientes = clientes   # Lista con instancias de Cliente
            self.cajeros = cajeros     # Lista con instancias de Cajero
            self.chef = chefs          # Lista con instancias de Chef
            self.souschefs = souschefs # Lista con instancias de SousChef
            self.ayudantes = ayudantes # Lista con instancias de Ayudante
            self.lavadores = lavadores # Lista con instancias de Lavador
            self.menus = menus         # Lista con los Menus disponibles
            self.items = items         # Lista con los Items disponibles
            self.pedidos = []          # Lista con Pedidos realizados
            
            # -----------------------------------------------------------------
            # Los siguientes atributos apuntan a la simulación:
             
            self.ingresos = 0                # Ingresos totales por ventas
            self.costos_ingredientes = 0     # Costos totales por ingredientes
            self.costos_bencina = 0          # Costos totales por bencina
            self.costos_indemnizacion = 0    # Costos totales por indemnizaciones
            self.costos_sueldos = 0          # Costos totales por sueldos
            self.p_hora_punta = p_hora_punta # Float con la probabilidad
            self.dia_actual = 1              # Número de día actual
            self.dias_totales = dias_totales # Número de días a simular
            self.tasa_pedidos = tasa_pedidos # Pedidos por hora normales
            self.tasa_punta = tasa_punta     # Pedidos por hora en Horario Punta
            self.horario_punta = False       # True si está en horario punta
                        
            # Para manejar los eventos
            
            self.__proxima_llegada_pedido = None
            self.__proximo_furia_culinaria = None
            self.__proximo_horario_punta = None
            self.__proximo_fin_horario_punta = float('Inf')
            self.__proxima_entrega_pedido = float('Inf')
            

        def pagar_sueldos(self):
            '''
            Este método se encarga de pagar los sueldos de todos los empleados.
            Debe considerar que a los repartidores interinos les debe pagar
            por pedido entregado.
            '''
        
        def recibir_pedido(self, pedido):
            '''
            Este método se encarga de preparar el pedido que se crea.
            Además, debe guardar las estadísticas relacionadas: ingreso,
            costos por ingredientes.
            '''
        
        def entregar_pedido(self, pedido):
            '''
            Este método se encarga de la entrega del pedido.
            Si se debe entregar a domicilio, debe contabilizar los
            kilómetros recorridos.
            '''
                         
        def contratar_interino(self, repartidor):
            '''
            Este método se encarga del contrato de nuevos interinos para el
            horario punta.
            Los repartidores que se agreguen deben tener el atributo de interino
            '''
                    
        # ---------------------------------------------------------------------
        # Métodos relacionados con la simulación
        
        @property 
        def tasa_llegada_pedidos(self):
            '''
            Esta property se encarga de retornar la tasa correspondiente a la
            situación.
            Si está en horario punta, retorna la tasa de horario punta; si no,
            entonces retorna la tasa de pedidos normal
            '''
        
        def proximo_evento(self):
            '''
            Este método se encarga de decidir cuál es el próximo
            evento en la simulación según los tiempos.
            Debe considerar que el tiempo no puede superar el tiempo
            máximo de simulación.
            '''
        
        def run(self)
            '''
            En este método se realiza la simulación.
            Debe inicializar los eventos como la primera llegada, la
            primera furia culinaria y el primer horario punta.
            
            Debe ejecutar toda la lógica del Restorán
            '''
        
    ```
    #### Distribución de Puntaje
    
    **(4 pts)** Los atributos y métodos bien declarados y especificados, siguiendo el esquema presentado del enunciado
    **(2 pts)** Implementar método `run()` o similar, junto con respectivos atributos para estadísticas de la simulación.
    **(2 pts)** Resolver de forma concordante con la modelación la paga de los trabajadores (incluir un método para esto)
    **(2 pts)** Las declaraciones de clases son consistentes con lo entregado en la parte a)

1.  **(5 pts)** ¿Cuáles son las estadísticas que necesitará calcular?

    ### Solución
    
    Estadísticas explícitas en el enunciado:
    
    - Monto de ventas diario
    - Monto de costos diarios
    - Cantidad de pedidos diarios

    Para poder estimar los costos, se podría tomar:
    
    - Litros de bencina utilizados diarios (o kilómetros recorridos)
    - Costos de indemnización

    Para poder tomar la eficiencia del personal:
    - Cantidad de pedidos atendidos por empleado

    Se espera que los alumnos tengan al menos 3 de estas estadísticas, la distribución de puntaje quedará de la siguiente forma: 
    - 1 estadística: **2 ptos**
    - 2 estadísticas: **4 ptos**
    - 3 estadísticas o más: **5 ptos**


1.  **(10 pts)** Seleccione **cuatro** eventos, al menos uno relacionado con cada entidad, y escriba para cada uno: nombre descriptivo, cuándo ocurre o se gatilla, qué consecuencias tiene, y cómo afecta a las estadísticas que describió en la pregunta **\(c\)**.

    ### Solución
    
    *   Llegada pedido
        *   Entidades: Item, Menu, Pedido
        *   Cuándo ocurre: 15 pedidos por hora (25 en hora punta)
        *   Consecuencias: El pedido se procesa
        *   Estadísticas: Registra las ganancias por ventas, los costos de producción, y registra el pedido en el día.

    * Contratar Repartidor interino
        * Entidades: Restaurant, Repartidor Part-Time
        * Cuándo ocurre: Se excede la cantidad de pedidos que pueden manejar los repartidores de planta en horario punta. 
        * Consecuencias: Se contratan nuevos trabajadores, dando pedidos a estos trabajadores para que vayan a dejarlos
        * Estadísticas: Aumentan los costos tanto de bencina como por sueldos

    * Pagar el suedo (dependerá de la forma en que se modeló el problema)
        * Entidades: Trabajadores, Restorán
        * Cuándo ocurre: Dependerá de cómo se modele, al no estar especificado, puede ser en cualquier parte de la simulación, normalmente al final del mes.
        * Consecuencias: Los empleados obtienen su sueldo, siendo descontado de las utilidades del Restorán
        * Estadísticas: Se ven afectadas las utilidades del Restorán.
    
    * Entrega **^1^**
        *  Entidades: Repartidores, Pedido
        *  Cuándo ocurre: Una vez por cada pedido
        *  Consecuencias: En el 65% de las veces, el repartidor debe ir a dejarlo. En el resto, se va a buscar al local
        *  Estadísticas: En el caso de ir a dejarlo, se almacenan los kilómetros que debe recorrer el repartidor.
    
    * Chef se enoja
        * Entidades: Chef, Cocinero
        * Cuándo ocurre: 1 vez a la semana
        * Consecuencias: Pagarle el sueldo de tres meses al sous - chef y que éste deje de ser trabajador
        * Estadísticas: Agrega costo de pagarle al cocinero despedido.
    
    * Horario punta
        * Entidades: Pedidos
        * Cuándo ocurre: 80% de los viernes a las 19:00
        * Consecuencias: Cambia la tasa de llegada de pedidos
        * Estadísticas: Como van a llegar más pedidos, afecta la cantidad de pedidos diarias

    **1**: Se aceptan distintas formas de representar la entrega; es decir,  podría ser el evento de 'Entrega a Domicilio' o similares.

## Pregunta 2 (35 pts)

Neville McKawas quiere ofrecer un servicio de entrega de almuerzos a empresas que tienen convenio con su restorán _La lechuga mágica_. Neville tiene ciertas nociones de programación, por lo que ha puesto como requisito técnico que la aplicación sea escrita en Python con una arquitectura cliente-servidor. 

Cada empresa asociada al convenio, tiene un computador en el que se ejecuta una aplicación desde la cuál se pueden hacer pedidos _La lechuga mágica_. Cada uno de estos computadores mantiene una conexión TCP activa con una aplicación que se ejecuta en un computador ubicado en la sede central del restorán.

En las empresas, cada persona es responsable de pedir su propio almuerzo. Para hacer esto, la persona debe acudir al computador de su empresa donde se está ejecutando la aplicación y hacer el pedido desde ahí. Cuando se realiza el pedido, el _back-end_ de la aplicación envía un mensaje que es recibido por el computador de la sede central del restorán. El mensaje contiene el nombre de la empresa desde donde se realizó el pedido, el nombre de la persona lo hizo, el contenido el pedido y un _timestamp_ que indica la hora exacta en que se realizó. Es importante recalcar que desde cada empresa, se pueden hacer varios pedidos en un día.

Por asuntos de logística, todos los pedidos deben ser realizados el mismo día de la entrega y sólo se reciben pedidos hasta las 11:00 am. Una vez llegada esta hora, _La lechuga mágica_ deja de recibir pedidos y se comienzan a preparar para su entrega **en el mismo orden** que fueron recibidos, sin considerar desde qué empresa fueron enviados.

Dado este contexto, responda las siguientes preguntas:


1. **(3 pts)** Dibuje un esquema que indique el/los servidores y el/los clientes involucrados. Debe indicar el rol de cada cliente y/o servidor de acuerdo al contexto explicado anteriormente. Debe indicar específicamente entre qué computadores existirá paso de mensajes. 

    ### Solución
    
    El servidor es único y está en la empresa _La Lechuga Mágica_
    
    Los clientes son las aplicaciones ubicadas en las distintas empresas.
    
    **IMAGEN**
    
    La distribución del puntaje es así:
    
    - **1 punto** por el esquema, donde quede explícito que existe un servidor y varios clientes.
    - **1 punto** por indicar que el servidor corresponde a _La Lechuga Mágica_ y que se encarga de recibir, almacenar y procesar los pedidos (no envía mensajes a los clientes).
    - **1 punto** por indicar que los clientes corresponden a las empresas y que estas solo envían mensajes al servidor (no los reciben).

1. **(5 pts)** Explique por qué es recomendable usar _multithreading_ en esta aplicación. Indique qué cosas dejaría en el _thread_ principal, para qué cosas usaría un _thread_ especialmente dedicado y cuántos _threads_ usaría.

    ### Solución
    
    Se utiliza _multithreading_ para solucionar la concurrencia de múltiples pedidos desde distintos clientes en el servidor.
    
    
    El thread principal se encarga de administrar los recursos del servidor.
    
    Se utiliza, además, un thread para escuchar las solicitudes a cada cliente.
    
    La distribución del puntaje es así:
    
    - **2 punto** por justificar el uso con el problema de concurrencia en la llegada de mensajes.
    - **1 punto** por indicar el uso del thread principal.
    - **2 puntos** por indicar el uso de threads por cliente.

1. **(7 pts)** Explique cómo representaría los pedidos que están esperando ser atendidos. Para esto, debe especificar cómo se representaría cada mensaje y qué estructura(s) de datos(s) debe usar para representar el conjunto de mensajes.
Especifique cuántas estructuras de datos y qué tipo(s) de estructura(s) de dato(s) usaría. Considere que los pedidos deben ser atendidos en orden de llegada y, por motivos de eficiencia, no se pueden usar algoritmos de ordenamiento, ni funciones que implementen estos algoritmos, como `sort` o `sorted`. 


    ### Solución
    
    En las preguntas c) y d) debe haber consistencia y se obtiene el puntaje completo si cumplen con los requerimientos. Una forma de abrodarlo es la siguiente:
    
    La estructura utilizada para almacenar los pedidos de cada empresa es una cola. En otras palabras, existe una cola por empresa. Por otro lado, la estructura para almacenar las distintas colas será un diccionario. Este diccionario tendrá de _key_'s a las empresas y de _value_'s a las colas.
    
    Por cada thread que escucha a un cliente, existe una cola de pedidos independiente.
    
    La estructura para guardar el contenido de los pedidos queda a criterio del alumno. Puede ser una clase que contenga los siguientes atributos: nombre de la empresa, nombre de la persona, contenido del pedido, timestamp. Puede también ser una named tuple o un diccionario, pero debe contener toda la información relevante.
    
    La distribución del puntaje es así:
    
    - **2 puntos** por definir la representación de un pedido.
    - **2 puntos** por definir que se debe(n) usar cola(s).
    - **3 puntos** por proponer una solución sin problemas de concurrencia. Aquí lo ideal es que hayan usado colas independientes por cada empresa. 
        - Si pusieron solo una cola e identifican el problema de concurrencia, tienen **1 de los 3 puntos**. 
        - Si pusieron una cola y no identificaron problemas de concurrencia tienen **0 de los 3 puntos**.
        - Si pusieron una cola y **solucionaron** el problema de concurrencia (pueden mirar la d. para eso) **tienen el puntaje completo**. Es poco probable que esto ocurra, ya que para solucionar el problema de concurrencia en este caso, no basta con un lock. Se necesita un semáforo, que no se ve en este curso.
    

1. **(10 pts)** Suponga que existen los siguientes métodos:
	- `agregar_elementos(empresa)` Se encarga de ir agregando pedidos de una empresa a la(s) estructura de datos(s) descrita(s) en **\(c\)**, a medida que se reciben los mensajes en el computador de la sede central.
    - `eliminar_elementos(empresas)` Se encarga de ir eliminando estos pedidos de la(s) estructura(s) de datos a medida los leídos por la persona encargada para ser preparados.
    
    Explique paso a paso lo que debe hacer cada uno de estos métodos. Su solución debe garantizar que los pedidos se atiendan en orden de llegada. **_Hint:_** Recuerde que el orden en el que se ejecutan sentencias de diferentes _threads_ no es predecible de antemano.

    ### Solución
    
    * **5 puntos** `agregar_elementos(empresa)`: Este método lo poseen las colas antes mencionadas. Se encarga de agregar elementos al final en la cola (`append`)


    * **5 puntos** `eliminar_elementos(empresas)`: Este método lo posee el diccionario antes mencionado. Para garantizar que el pedido extraído sea el que primero arribó, se revisan los primeros elementos de cada cola del diccionario y se extrae el elemento con el menor _timestamp_. Dicha extracción se realiza a través de un `popleft`.

    * Si en la c) propuso solo una cola, debe identificar los problemas de concurrencia para obtener algo de puntaje en la d). Para cada método, se asignan **2 puntos** si identifica el problema de concurrencia (por ejemplo, si intenta resolverlo con un lock). **Puntaje total** si resuelve el problema de concurrencia con una cola (cosa improbable, ya que necesitaría implementar un semáforo o equivalente)



1. **(10 pts)** A medida que van llegando los pedidos, el programa que se ejecuta en el restorán debe escribir un archivo de _log_ en el que se lleva registro de lo ocurrido durante el día. Cada vez que llega un pedido o se comienza a preparar un pedido, esto debe ser registrado en el _log_. Indique paso a paso, cómo se debe escribir este archivo, considerando el uso de _multithreading_.

    ### Solución
    
    Dado que el archivo _log_ es un recurso compatido todos los _threads_, el principal y los que escuchan a cada cliente, se debe utilizar un `Lock` para evitar problemas de concurrencia.
    
    El paso a paso sería como sigue:
    * **3 puntos** Primero el _thread_ pide el `Lock` común ante la llegada (en el caso de los que escuchan) o ante extracción (en el caso del principal) de un pedido.
    * **2 puntos** Espera hasta que lo obtiene
    * **3 puntos** Una vez con el `Lock`en mano, se agrega lo deseado en el archivo.
    * **2 puntos** Finalmente, libera el `Lock`


## Pregunta 3 (35 pts)

1. **(4 pts)** Indique qué imprime el siguiente código.

    ```python=
    from collections import namedtuple
    import os
    import pickle

    Street = namedtuple("Street", "district name id")
    names = ["Rue Montmartre", "Rue des Moulins", 
             "Pont Neuf", "Rue de l'Oculus",
             "Avenue de l'Opera", "Boulevard du Palais",
             "Place du Palais-Royal"]  
    districts = ['1er-arrondissement', '1er-arrondissement', 
                 '1er-arrondissement', '1er-arrondissement']

    def convert(file_name, obj):
        if os.path.exists(file_name):
            return False
        else:
            with open(file_name, "wb+") as f:
                pickle.dump(obj, f)
            return True

    successful = list(filter(lambda a: convert("{}.iic2233".format(a[1]),
                                        Street(*a[0], a[1])),
                            ((n, len(n[0])) for n in zip(names, districts))))

    print(successful)
    ```

    ### Solución

        ```
    - **(2 pts)** por filtrar correctamente el iterable de acuerdo a las `namedtuples` que se guardaron correctamente por no haber sido serializadas previamente.
    - **(2 pts)** por imprimir correctamente el resultado como lista (con cada tupla como corresponde):

    ```python
    >>> [(('Rue Montmartre', '1er-arrondissement'), 14),
         (('Rue des Moulins', '1er-arrondissement'), 15),
         (('Pont Neuf', '1er-arrondissement'), 9)]
    ```

1. **(6 pts)** De acuerdo al código, responda las preguntas.

    ```python=
    class A:
        @classmethod
        def save(self, file):
            print("Class A saving {}".format(file))
            super().save(file)

    class B:
        @classmethod
        def save(self, file):
            print("Class B saving {}".format(file))

    class C(A, B):
        @classmethod
        def save(self, file):
            print("Class C saving {}".format(file)) 
            super().save(file)

    obj_c = C()
    C.save("file")
    obj_c.save("file")
    ```

    1. **(2 pts)** Indique paso a paso qué ocurre cuando se ejecuta la línea 19.

        ### Solución
        
        - Se ejecuta el método de clase `save` de `C` que imprime
            
            ```
            Class C saving file
            ```
            
            **(1 pto)** hasta acá.
            
        - Luego, se llama (según el orden de la herencia) a `save` de `A` que imprime
            
            ```
            Class A saving file
            ```
            
        - Finalmente, se llama a `save` de `B` que también imprime
            
            ```
            >>> Class B saving file
            ```
            
            **(1 pto)** hasta acá.
            
        Se entregará solo **1 pto** si solo se indican los _outputs_ en consola.

    2. **(2 pts)** ¿Cuál es el tipo de objeto del parámetro `self` del método `save` de la clase `B`? ¿Es el mismo que el de la clase `A`?

        ### Solución

        El tipo del argumento `self` en los métodos `save` de las clases `A` y `B` es `type` **(1 pto)**. En consecuencia, el tipo de ambos argumentos `self` es el mismo **(1 pto)**.
        
        Se entregará un punto si se especifica que `self` al ejecutar `C.save("file")` es la clase `C`, pero no que su tipo era `type`.

    3. **(2 pts)** ¿Es posible ejecutar la línea 20? Si se pudiese, ¿qué se imprime en consola?

        ### Solución

        Es posible porque los métodos de clase se pueden llamar desde instancias de ésta **(1 pto)**. En consecuencia, se imprime **(1 pto)**
        
        ```
        Class C saving file
        Class A saving file
        Class B saving file
        ```


1. **(4 pts)** Indique qué imprime el siguiente código.

    **_Hint:_** el _built-in_ `any` es una función que recibe un iterable y devolverá `True` si es que cualquier (psst... _any_) elemento del iterable se evalúa como `True`. En caso contrario, retornará `False`. Además, si el iterable está vacío, también devolverá `False`.

    ```python=
    def apply_func(data, func, cond):
        for n in data:
            if cond(n):
                yield func(n)

    data = [3004, 89, 278, 1023, 47, 816, 21, 8055]
    cond = lambda x: any(map(lambda d: x % d == 0, (2, 3, 4, 5)))
    func = lambda x: "{:>5,}".format(x) # Este format solo vale 0.5 pts

    a = apply_func(data, func, cond)
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    ```
    
    ### Solución
    
    Se entregará **1 pto** por cada línea correcta. Se descontarán **0.125 pts** por línea con el formato incorrecto.
    
        ```    
        3,004
          278
        1,023
          816
        ```

1. **(6 pts)** Indique qué imprime el siguiente código.

    ```python=
    def dec(x, y):
        def _dec(f):
            def __dec(*args, **kwargs):
                index = None
                cond = x < f(*args, **kwargs) < y
                if len(kwargs) == 0 and cond:
                    index = -1
                elif cond:
                    index = 1
                else:
                    index = 0
                return f(*args, **kwargs) * index
            return __dec
        return _dec

    @dec(-6, 9)
    def foo(a, b, c):
        return a * b + c

    @dec(-2, 7)
    def bar(a, b, c=1):
        return a * b * c

    @dec(-1, 2)
    def qux(a, b, c=1):
        return a - b * c

    print(foo(2, 3, 1))
    print(bar(2, 3, c=1))
    print(qux(2, 3, c=1))
    ```

    ### Solución
    
    Dos puntos por cada línea:
    
    ```    
    -7
    6
    0
    ```  

1. **(1 pt)** ¿Cuál es el _output_ en consola?

    ```python=
    class A:
        def save(self, file):
            print("A saving {}".format(file))

    class B:
        def save(self, file):
            print("B saving {}".format(file))

    class C(A, B):
        pass

    class D(B, A):
        pass

    obj_c = C()
    obj_d = D()
    obj_c.save("file")
    obj_d.save("file")
    ```
    
    ### Solución
    
    ```
    A saving file
    B saving file
    ```

1. **(14 pts)** De acuerdo al siguiente código, responda las preguntas.

    ```python=
    from random import randint

    class A:
        last_id = 0
        def __init__(foo, d):
            foo._id = randint(1, 100) * d 
            A.last_id = foo._id

        @staticmethod
        def load(data):
            print("loading")
            a = A(data)
            return a

        @classmethod
        def operate(foo, d1, d2):
            a1 = foo.load(d1)
            a2 = foo.load(d2)
            return a1 + a2

        def __add__(foo, other):
            return foo._id + other._id

    obj1 = A(1)
    ```

    1. **(1 pto)** ¿Qué tipo de objeto es el parámetro `foo` del método `__add__`?

        ### Solución

        Es de clase `A`.

    1. **(1 pt)** ¿Qué tipo de objeto es el parámetro `foo` del método `operate`?

        ### Solución

        Como corresponde a la clase `A`, es de tipo `type`.

    1. **(4 pts)**  ¿Es posible ejecutar `obj1.operate(1, 3)` si se agrega `foo + foo` al inicio del método `operate`? ¿Por qué?

        ### Solución

        No **(2 pto)** (el programa se cae), porque la clases (objetos `type`) **(1 pto)** no tienen definido el operador `+` con `__add__` **(1 pto)**.

    1. **(4 pts)** Indique, paso a paso, qué ocurre cuando se ejecuta `obj2 = obj1.load(3)`

        ### Solución

        - **(1 pto)** Se llama al método estático `load` con `data = 3`.
        - **(1 pto)** Se imprime `loading`.
        - **(1 pto)** Se instancia un nuevo objeto `A` con `3` y se actualiza `A.last_id`.
        - **(1 pto)** Se asigna el nuevo objeto a la variable `obj2`.

    1. **(4 pts)** Si se elimina la línea 9. ¿Qué ocurrirá al ejecutar `A.load(3)`?

        ### Solución

        Funcionará normalmente **(4to)**, porque el método se llama desde la clase y no de una de sus instancias. En este caso, no se le entrega ningún argumento adicional a la función. Si se hubiese llamado desde una instancia de `A`, esa instancia también se hubiese entregado como argumento y se tendría un `TypeError` por exceso de argumentos.


## Pregunta 4 (10 pts)

En no más de tres líneas, responda sólo **DIEZ** de las siguientes preguntas (un punto por cada pregunta). En caso de que conteste más preguntas, **sólo serán corregidas las primeras 10 respuestas** que se encuentren en su hoja de respuesta. Sea breve y conciso.

1. Defina brevemente qué es _duck typing_.

    ### Solución
    
    Se aceptan definiciones de la forma:
    
    - Polimorfismo sin usar herencia
    - Cuando clases distintas sin relación de herencia comparten métodos con los mismos nombres. 
    - Si se confunde con polimorfismo está malo.

1. ¿Cuál es la diferencia entre un _iterador_ y un _iterable_?

    ### Solución
    
    Un iterable es un objeto que tiene definido el método `__iter__` que retorna un iterador. Un iterador es un objeto que permite recorrer un iterable a través de su método `__next__`.

1. Explique la diferencia entre `re.search` y `re.match`.

    ### Solución
    
    - `re.search` determina la presencia de la expresión entregada dentro del texto, mientras que `re.match` determina la presencia de la expresión, pero esta debe estar al comienzo del texto.

1. ¿Por qué es útil hacer la diferencia entre _back-end_ y _front-end_?

    ### Solución
    
    - Da mayor flexibilidad al programador a la hora de querer hacer cambios, pues puede hacer cambios en la lógica del programa sin intervenir elementos visuales, y viceversa.
    - Permite programar la lógica (interfaz) por separado, sin necesidad de preocuparse de lo que ocurre en la interfaz (lógica) del programa.

1. Mencione una ventaja y una desventaja de serializar con `pickle`. 

    ### Solución
    
    Una ventaja de pickle, es que permite serializar cualquier objeto de python. Una desventaja, es que la serialización no puede ser interpretada por otros lenguajes de programación.

1. En `unittest`, ¿cuál es la diferencia entre `setUp` y `tearDown`?

    ### Solución
    
    - El setUp es llamado antes de ejecutar cada test, mientras que el tearDown se ejecuta después de ejecutar cada test.
    - El setUp se utiliza para inicializar cualquier objeto necesario para desarrollar los test, mientras que el tearDown se utiliza para limpiar efectos colaterales de los tesst (ej: uso de archivos)

1. ¿Qué realiza el método `__call__` de una clase que hereda de `type`?

    ### Solución
    
     Es el encargado de crear la instancia, y se encarga de llamar al método `__init__` de la clase que posee como metaclase a la clase que hereda de `type`.

1. ¿Cuál es la diferencia entre un método de clase y un método estático?

    ### Solución
    
     El método de clase, recibe como primer argumento a la clase, mientras que el método estático no recibe la clase.

1. Explique para qué sirven las clases abstractas y dé un ejemplo de su uso.

    ### Solución
    
   Permiten representan mejor lo que son las clases realmente abstractas desde el punto de vista del modelamiento. Se acepta cualquier ejemplo que haga sentido (Clase Humano como base de alumno, profesor ayudante, clase Vehículo como base de Camión, deportivo, etc...)

1. Dé un ejemplo en el que sea recomendable escribir una _property_ con un _setter_.

    ### Solución
    
    - Cuando se quiere controlar la forma en que se modifica un atributo. Ej: Se tiene un atributo que no puede ser negativo.
    - Cuando se quiere notificar cada vez que se modifique el atributo (logging). Ej: Escribir en un archivo, cada vez que un usuario modifique un atributo
    - Cuando se quiere que al momento de setear un atributo, ocurren efectos colaterales. Ej: Si el valor seteado es menor a cierto valor, se debe lanzar un warning.

1. ¿Para qué sirve el atributo `cls` de los métodos `dump` y `dumps` del módulo `json`?

    ### Solución
    
    Para entregar una clase que herede de `json.JSONEncoder` que defina (en `default`) la intervención de la serialización del JSON.

1. Explique por qué no se recomienda capturar excepciones, sin explicitar el tipo de excepción.

    ### Solución
    
    - Se pueden capturar excepciones desconocidas y no actuar acorde a esa situación.
    - Se ocultan errores de código.
    - No se puede actuar de forma distinta de acuerdo a la excepción levantada.

1. ¿Para qué son utilizados los _context managers_ en Python? ¿Y de qué forma es posible personalizarlos en una clase cualquiera? 

    ### Solución
    
    Son utilizados para asegurarse que un objeto ejecute un código previo y posterior a su uso. Para personalizarlo, se deben sobreescribir los métodos `__enter__` y `__exit__`

1. Indique qué imprime el siguiente código.

    ```python=
    n = [3, 1, 5, 2, 9]
    print([x for x in enumerate(map(lambda x: x**2, n)) if x[1] > 20])
    ```
    
    ### Solución
    
    ```python=
    [(2, 25), (4, 81)]
    ```

    ñ. ¿Cuál es el \textit{output} del siguiente código?

    ```python=
    a = [[1, 2], [3, 4], [5, 6]]
    b = a[:]
    a[0].append(7)
    a.append([8, 9])
    b.append([10, 11])
    b[1].append(12)
    print(a)
    print(b)
    ```

    ### Solución
    ```python=
    [[1, 2, 7], [3, 4, 12], [5, 6], [8, 9]]
    [[1, 2, 7], [3, 4, 12], [5, 6], [10, 11]]
    ```