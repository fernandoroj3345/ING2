# TP9 Administración de proyectos (Planificación)

## 1) Asumiendo que el mantenimiento de un sistema es una tarea continua. ¿Puede ser considerado como un proyecto? ¿Qué características deben asignarse a las tareas de mantenimiento para poder ser, efectivamente, considerada un proyecto?

Pensándolo como un sistema un proyecto, según la gestión de proyectos (PMBOK, ISO), se define como un esfuerzo temporal con un inicio y un fin claro, que busca generar un producto, servicio o resultado único.

El mantenimiento, en cambio, es una actividad continua y repetitiva destinada a asegurar que el sistema siga funcionando correctamente.

**Características que deben asignarse para considerarlo proyecto:**

- Temporalidad: debe tener un plazo de ejecución definido (no ser indefinido).
- Objetivo claro y único: por ejemplo, “actualizar el sistema a la versión 2.0 en 3 meses”.
- Planificación de recursos y tareas: establecer responsables, cronograma y estimaciones de esfuerzo.
- Entregables concretos: documentaciones, versiones liberadas, manuales de usuario, etc.
- Evaluación de éxito: cumplimiento de calidad, costo y tiempo acordados.

## 2) ¿Cuál es el motivo conceptual por la cual ciertas iniciativas se estructuran como programas en vez de proyectos?

**Motivo conceptual principal:**

Un proyecto es un esfuerzo temporal con un objetivo único y definido.

Un programa, en cambio, es un conjunto de proyectos relacionados que se gestionan de forma coordinada para obtener beneficios que no podrían lograrse si cada proyecto se gestionara de manera independiente.

**Razón de estructurar iniciativas como programas:**

- Cuando los objetivos son demasiado amplios o estratégicos para alcanzarse con un único proyecto.
- Se busca alinear varios proyectos bajo una misma visión, asegurando coherencia en la asignación de recursos, plazos y resultados.
- Permite gestionar interdependencias y sinergias entre proyectos (ejemplo: compartir datos, infraestructura o personal especializado).

**Características diferenciales:**

- El programa se centra en los beneficios a largo plazo, no solo en la entrega de un producto puntual.
- Un programa integra y coordina varios proyectos que comparten un mismo propósito estratégico.
- Ofrece una visión global para que la organización logre ventajas competitivas o de negocio más amplias.

## 3) Asumiendo como válida la premisa que la definición de las características de un proyecto viene dada por las elecciones de los parámetros de Tiempo (Calendario), Recursos (Costo), Requerimientos (Funciones) y Calidad (Defectos). ¿Cuál cree pueda ser el efecto de fijar arbitrariamente Tiempo, Recursos y Requerimientos a valores de conveniencia para el proyecto?

La gestión de proyectos se apoya en (tiempo, costo/recursos, alcance/requerimientos), al que se suele agregar la calidad.

Si se fijan arbitrariamente tiempo, recursos y requerimientos sin un análisis realista, se limita la capacidad de maniobra del proyecto.

**Efecto inmediato:**

- La única variable flexible que queda es la calidad.
- Esto implica que, para cumplir con lo impuesto, se corre el riesgo de entregar un producto con defectos, incompleto o poco mantenible.

**Riesgos concretos:**

- Sobrecarga del equipo: aumenta el estrés, se extiende la jornada laboral, lo cual genera más errores.
- Incremento de defectos: al reducir tiempos de prueba o simplificar procesos, la calidad del software se degrada.
- Falsas estimaciones: se genera un plan “idealista” que probablemente no se cumpla, produciendo retrasos o sobrecostos ocultos.
- Insatisfacción del cliente: porque aunque se cumplan los tres parámetros fijados, el producto puede no cumplir las expectativas de usabilidad, confiabilidad o rendimiento.

**Ejemplo aplicado:**

Un proyecto de desarrollo de un sistema de mercado fija:

- Tiempo: 3 meses.
- Recursos: 3 desarrolladores.
- Requerimientos: módulo de transferencias, pagos y reportes.

**Conclusión:**

Fijar arbitrariamente tiempo, recursos y requerimientos lleva a que el proyecto solo pueda cumplir sacrificando la calidad.

Una buena práctica es negociar al menos una de las tres variables (ejemplo: reducir requerimientos o ampliar plazo) para mantener la calidad y viabilidad del proyecto.

## 5)
Si el equipo tiene una capacidad histórica de 5 story points por sprint y los sprints duran 2 semanas. Con un presupuesto para 6 semanas, el equipo puede realizar 3 sprints en total.

La capacidad total del equipo para el proyecto es:
3 sprints * 5 story points/sprint = 15 story points.

1. ¿Qué funciones recomendaría incluir dentro del alcance?
Considerando una capacidad total de 15 story points, la recomendación es incluir las funciones que aporten el mayor valor con el menor costo. El valor de negocio se puede estimar por la frecuencia de uso mensual ("Hits").

Se sugiere priorizar las funciones con mayor frecuencia de uso, siempre que sea posible. Se pueden incluir las siguientes combinaciones hasta alcanzar los 15 story points:

Función G (13 story points, 8030 hits): Es la función con más hits, por lo que proporciona el mayor valor.

Función C (8 story points, 6602 hits) + Función B (3 story points, 1762 hits) + Función A (2 story points, 1104 hits) + Función F (2 story points, 2179 hits) = 15 story points. Esta opción incluye varias funciones de alto valor.

Una tercera opción sería Función C (8 story points, 6602 hits) + Función D (5 story points, 1565 hits) + Función A (2 story points, 1104 hits) = 15 story points.

2. ¿Qué funciones eliminará si se le reduce el presupuesto a la mitad?
Si el presupuesto se reduce a la mitad (3 semanas), el equipo solo puede completar 1.5 sprints. La capacidad total se reduciría a 1.5 sprints * 5 story points/sprint = 7.5 story points.

Se deben priorizar las funciones que aporten el mayor valor en un menor tiempo. Si la Función C (8 story points) no se puede dividir, se tendría que excluir o se podría incluir la Función C (8 story points) y sacrificar las demás.

Si se excluye la Función C, se pueden incluir otras funciones que sumen menos de 7.5 story points, como:

Función B (3 story points) + Función D (5 story points) = 8 story points. Esta opción supera el límite de 7.5 story points.

Función F (2 story points) + Función A (2 story points) + Función B (3 story points) = 7 story points.

Función D (5 story points) + Función A (2 story points) = 7 story points.

Función F (2 story points) + Función B (3 story points) = 5 story points.

Función D (5 story points) + Función F (2 story points) = 7 story points.

Las funciones que se eliminarían son aquellas que excedan la capacidad total del equipo.

3. ¿Qué funciones incluirá si se puede tener al equipo por 7 semanas?
Si el presupuesto se extiende a 7 semanas, el equipo puede completar 3.5 sprints. La capacidad total sería 3.5 sprints * 5 story points/sprint = 17.5 story points.

Con esta capacidad, se podría incluir la Función G (13 story points) y aún quedaría una capacidad de 4.5 story points para otras funciones, como la Función A (2 story points) y la Función F (2 story points).

Otra opción sería incluir las funciones C (8), D (5), F (2) y A (2), lo que suma 17 story points. Esta combinación abarca más funciones que la anterior.

4. ¿Qué prioridad recomendará para la función "D"?
La Función D (5 story points) debe tener una prioridad muy alta porque, según el líder técnico, es la más importante desde el punto de vista de la arquitectura. Incluso si su frecuencia de uso no es la más alta, las funciones que aseguran la estabilidad, escalabilidad y la base técnica del proyecto deben ser consideradas como críticas. La no inclusión de esta función podría generar problemas a largo plazo, resultando en deuda técnica y mayores costos de mantenimiento.

5. ¿Cómo se modifica lo anterior si el equipo tiene una velocidad para deuda técnica de 1 story point (/sprint)?
Si el equipo dedica 1 story point por sprint a la deuda técnica, la velocidad real para el desarrollo de nuevas funciones se reduce. La nueva velocidad sería:
5 story points - 1 story point (deuda técnica) = 4 story points por sprint.

La capacidad total del proyecto se reduciría:

6 semanas: 3 sprints * 4 story points/sprint = 12 story points. Esto significa que las combinaciones de funciones del punto 1 tendrían que ajustarse a este nuevo límite.

3 semanas: 1.5 sprints * 4 story points/sprint = 6 story points. Las combinaciones del punto 2 tendrían que ajustarse a este nuevo límite.

7 semanas: 3.5 sprints * 4 story points/sprint = 14 story points. Las combinaciones del punto 3 tendrían que ajustarse a este nuevo límite.

## 6)Realice un resumen corto del artículo “What Do Software Developers Need to Know about Business” del Prof. Dr. Warren Harrison. ¿Cuál es en 
## su opinión la relevancia del mismo a los temas discutidos sobre alcance de un proyecto?
El articulo habla sobre que aunque muchos desarrolladores creen que pueden aprender negocios sin esfuerzo, entender el contexto económico de la empresa es crucial. Conocer conceptos como costos hundidos, valor del dinero en el tiempo y métricas financieras básicas ayuda a tomar mejores decisiones y evitar pérdidas. Además, propone que las propuestas de proyecto deben entender el retorno esperado y la tasa mínima aceptable de inversión para ser viables.

Sobre su relevancia en temas del alcance de un proyecto, es fundamental porque:
Comprender el contexto financiero ayuda a definir un alcance realista y alineado a los recursos disponibles.
Permite evaluar bien los beneficios versus costos, evitando proyectos con expectativas poco claras o inviables.
Facilita negociar prioridades y decidir qué incluir o excluir del alcance para maximizar valor y minimizar riesgos financieros.
Promueve una gestión del proyecto más informada y alineada con los objetivos económicos de la organización.
Por tanto, este conocimiento financiero y de gestión es clave para delimitar, controlar y ajustar el alcance de proyectos software con éxito.

## 7). Realice un resumen corto del artículo “Subjective Consistency” del Dr. Pedro Colla. ¿Cuál es en su opinión la relevancia del mismo a los temas discutidos sobre estimación?
El articulo aborda la importancia y dificultad de estimar el esfuerzo en proyectos de software. Aunque muchos métodos usan métricas históricas para modelar estimaciones, estas no siempre se aplican bien debido a la variabilidad entre equipos y tecnologías, y a la falta de datos suficientes. En estos casos, la estimación por expertos sigue siendo la principal forma, aunque con un margen de error alrededor del ±30%.

Se señala que la inconsistencia en las estimaciones de los expertos es común, y que métodos como el Proceso Analítico Jerárquico (AHP) pueden ayudar a evaluar la consistencia de estas estimaciones subjetivas mediante comparaciones por pares y criterios matemáticos.

El paper propone usar AHP para mejorar la coherencia en estimaciones y facilitar la identificación de áreas de mejora, incluso con evaluaciones simples hechas por expertos sin modelos complejos.

## 8)Supuesto que dispone como información histórica del mismo dataset utilizado en el taller denominado “Modelos dinámicos” modifique el programa PNR_sistemis.py para realizar las siguientes acciones:
a. Derive un programa similar que acepte el esfuerzo del proyecto expresado en personas-mes (PM) y grafique los valores del dataset
histórico de calibración, los valores del modelo obtenido por mejor ajuste desde el dataset, la curva aplicando el modelo PNR para el
valor de esfuerzo aceptado.
b. Utilice el programa del punto anterior para calcular la distribución de esfuerzo en el tiempo para un proyecto de 72 PM de esfuerzo
total, grafique junto a los puntos de datos históricos y el modelo suavizado. Comente las diferencias que observa.
c. Que ocurre si arbitrariamente decide utilizar un valor de “a” que es el cuadruple del valor obtenido por calibración.¿Cual es el efecto
observable? ¿Qué estima ocurrirá con el proyecto respecto al concepto de “Zona imposible”? 

c)Interpretación qué se observa:

La curva se vuelve más estrecha, más alta y desplazada hacia tiempos más tempranos: el mismo K concentrado en menos meses.

Resultado observable: más intensidad de personal en menos tiempo (picos más altos), menor duración efectiva del trabajo activo.

Consecuencias sobre la viabilidad y la “Zona imposible”:

Si el pico requerido 𝐸𝑚𝑎𝑥 supera la capacidad máxima disponible de recursos humanos (por ejemplo, la cantidad de personas que se pueden asignar/coordinar), entonces el plan pasa a la zona imposible: no se puede ejecutar con los recursos reales sin incumplir condiciones.
Entonces si cuadruplicar a aumenta la probabilidad de caer en la zona imposible (o zona de alto riesgo) porque exige un pico de personal mayor y reduce el tiempo disponible para pruebas/QA.

## 10 .Supuesto que el valor de un proyecto se deteriora cuanto mas riesgosa es su ejecución.¿Porque el implementar un proyecto en etapas o fases al final de las cuales se evalúa si se continúa aumenta el valor del proyecto para su patrocinante?
Implementar un proyecto por fases y evaluar al final de cada una si se sigue adelante permite al patrocinante controlar y reducir el riesgo. Así, puede invertir de manera más segura, detener el proyecto antes de gastar demasiado dinero si no es conveniente seguir, o modificar el enfoque según lo que se va aprendiendo. Esto incrementa el valor del proyecto porque cada decisión se toma con datos reales, y el riesgo de grandes pérdidas o fracaso se reduce considerablemente, haciendo que la inversión sea más eficiente y adaptable.

## 11 .La contabilidad de una empresa, y por extensión la de un proyecto dentro de la misma ¿captura las acciones de índole financiera de la empresa?
## (acciones relacionadas con el momento en que se reflejan los actos económicos con un criterio devengado).
Sí, la contabilidad de una empresa y también la de los proyectos internos capturan las acciones financieras usando el criterio devengado. Según este criterio, los ingresos y gastos se registran en el momento en que se generan, es decir, cuando ocurre el hecho económico, independientemente de cuándo se cobre o se pague realmente.

## 12 .El realizar un proyecto de software bajo un régimen de promoción impositiva que reduce el impuesto a las ganancias incentiva o desalienta
## la utilización del mecanismo de apalancamiento impositivo? ¿Por qué?.

Menor incentivo para apalancarse: Los proyectos sujetos a promoción impositiva ya pagan menos impuesto a las ganancias por sus actividades promovidas, por lo que las estrategias para “apalancar” impositivamente (como endeudarse para deducir intereses o buscar estructuras que permitan mayor deducción fiscal) pierden relevancia y utilidad.

Beneficio directo y seguro: La reducción y estabilidad fiscal que otorga el régimen promocional es directa y garantizada, sin necesidad de asumir los costos y riesgos de herramientas de apalancamiento financiero, que suelen implicar endeudamiento o complejidad administrativa.

Contabilidad separada: Las empresas deben llevar contabilidad separada para actividades promovidas, lo que dificulta aún más la utilización de mecanismos indirectos de apalancamiento para obtener más deducciones fiscales sobre el impuesto a las ganancias.

Realizar un proyecto bajo un régimen de promoción impositiva que reduce el impuesto a las ganancias desalienta el uso del mecanismo de apalancamiento impositivo, porque el régimen ya brinda el beneficio principal: pagar menos impuesto. Utilizar apalancamiento financiero para buscar deducciones pierde sentido, ya que el ahorro de impuestos por promoción suele ser mayor, más simple y más seguro que apalancarse. Por eso, en estos contextos, las empresas prefieren aprovechar el beneficio directo de la promoción y no recurrir a estrategias de apalancamiento que pueden agregar costos o riesgos innecesarios.

## Las variaciones de un proyecto resultado en incertidumbre en las estimaciones puede ser de +/- 30%, ¿por qué se considera razonable solo
## tomar contingencias de hasta un +5%?
Aunque las estimaciones en proyectos de software pueden variar hasta un 30%, es razonable limitar la contingencia a un 5% porque su función es cubrir los riesgos probables y concretos, no la totalidad de la incertidumbre. Si la contingencia fuera mayor sin justificación, el presupuesto se inflaría y se perdería eficiencia. Por eso, se recomienda reservar un monto moderado y mejorar la gestión de riesgos y estimaciones para tratar la incertidumbre restante.

## 14 .Calcule la esperanza de ganar una apuesta en un juego de ruleta apostando a color. Asuma que la ruleta tiene un cero de color verde (color
## neutro). La apuesta será con la ficha mínima de $1000.
ver el codigo como EsperanzaMat.py

## 15. Una inversión muy promocionada denominada “Telar de los colores” promete un rendimiento mensual del 7% para una inversión de $1000. La
## probabilidad que la inversión produzca una ganancia (Pg) es tal que la probabilidad que produzca una pérdida (Pp) sumada a ella dará 1. Por lo
## tanto la esperanza neta de la inversión será, en el mejor de los casos, nula. Cual es la probabilidad de ganar y la de perder en una inversión ## de ésta índole
ver programa como telar.py


