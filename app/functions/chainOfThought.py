# sentimientos = ["Felicidad", "Tristeza", "Ira", "Miedo", "Sorpresa", "Asco", "Vergüenza", "Amor", "Alegría", "Preocupación", "Ansiedad", "Culpa", "Envidia", "Confusión", "Euforia", "Calma", "Esperanza", "Soledad", "Aburrimiento", "Gratitud"]

# for sentimiento in sentimientos:
#     prompt = f"{sentimiento.lower()} | {sentimiento}"
#     print(prompt)
import random

contexto_amigos = ["Fiesta", "Reunión casual", "Salida al cine", "Noche de juegos", "Vacaciones con amigos"]
contexto_formal = ["Entrevista de trabajo", "Reunión de negocios", "Presentación académica", "Cena de gala", "Conferencia"]
contexto_familiar = ["Cena familiar", "Celebración de cumpleaños", "Viaje familiar", "Reunión de Navidad", "Día en el parque"]
contexto_romantico = ["Cena romántica", "Paseo por la playa", "Escapada de fin de semana", "Noche de películas en casa", "Viaje romántico"]
contexto_educativo = ["Clase universitaria", "Seminario de desarrollo personal", "Taller de escritura creativa", "Charla científica", "Curso de idiomas"]
contexto_deporte = ["Partido de fútbol", "Entrenamiento de gimnasio", "Maratón", "Partido de baloncesto", "Clase de yoga"]
contexto_viaje = ["Excursión de montaña", "Visita a una ciudad histórica", "Playa tropical", "Ruta en carretera", "Camping en la naturaleza"]
contexto_relajacion = ["Spa y masajes", "Meditación", "Baño en aguas termales", "Escapada a un retiro", "Practicar yoga en la playa"]
contexto_creativo = ["Pintura", "Escultura", "Escritura de poesía", "Diseño gráfico", "Fotografía"]
contexto_deportivo = ["Partido de fútbol", "Competencia de natación", "Carrera de atletismo", "Partido de tenis", "Clase de fitness", "Partido de baloncesto", "Competencia de ciclismo", "Clase de yoga", "Partido de béisbol", "Entrenamiento de artes marciales"]
contexto_arte = ["Visita a una galería de arte", "Concierto en vivo", "Función de teatro", "Recital de música clásica", "Exposición de esculturas"]
contexto_voluntariado = ["Trabajo en un comedor comunitario", "Limpieza de un parque", "Visita a un hogar de ancianos", "Participación en una campaña de donación", "Enseñanza en una escuela primaria"]
contexto_ocio = ["Tarde de lectura en el parque", "Maratón de series y películas", "Juegos de mesa con la familia", "Día de compras", "Exploración de nuevas cafeterías"]
contexto_religioso = ["Ceremonia religiosa", "Retiro espiritual", "Rezo en grupo", "Festividad religiosa", "Estudio bíblico"]
contexto_technology = ["Hackathon", "Conferencia de tecnología", "Lanzamiento de producto", "Exposición de gadgets", "Taller de programación"]
contexto_social = ["Cóctel de networking", "Fiesta de cumpleaños", "Boda", "Barbacoa en el patio trasero", "Encuentro de antiguos compañeros de escuela"]
contexto_educativo = ["Excursión escolar", "Feria de ciencias", "Debate estudiantil", "Taller de robótica", "Concurso de ortografía"]
contexto_gastronomico = ["Clase de cocina", "Degustación de vinos", "Visita a un mercado local", "Festival gastronómico", "Cena en un restaurante de alta cocina"]
contexto_musical = ["Concierto de rock", "Recital de piano", "Festival de música electrónica", "Noche de karaoke", "Jam session en un bar"]
contexto_medico = ["Consulta médica", "Procedimiento quirúrgico", "Visita a un fisioterapeuta", "Terapia de rehabilitación", "Análisis de laboratorio"]
contexto_ecologico = ["Limpieza de playa", "Plantación de árboles", "Visita a un parque natural", "Charla sobre sostenibilidad", "Reciclaje en la comunidad"]
contexto_politico = ["Mitin político", "Debate presidencial", "Participación en campaña electoral", "Visita a un centro de votación", "Entrevista con un representante político"]

tipos_comunicacion = ["Conversación", "Monólogo", "Diálogo", "Presentación", "Discurso", "Debate", "Entrevista",
                      "Mensaje de texto", "Correo electrónico", "Publicación en redes sociales", "Carta", "Nota adhesiva",
                      "Graffiti", "Pintura", "Escultura", "Danza", "Música", "Teatro", "Canto", "Fotografía",
                      "Expresión facial", "Expresión corporal", "Escritura creativa", "Pensamiento reflexivo",
                      "Visualización", "Autodiálogo", "Expresión emocional", "Expresión artística", "Expresión gestual",
                      "Autoexpresión"]

contextos = { "amigos": contexto_amigos, "formal": contexto_formal, "familiar": contexto_familiar, "romantico": contexto_romantico, "educativo": contexto_educativo, "deporte": contexto_deporte, "viaje": contexto_viaje, "relajacion": contexto_relajacion, "creativo": contexto_creativo, "deportivo": contexto_deportivo, "arte": contexto_arte, "voluntariado": contexto_voluntariado, "ocio": contexto_ocio, "religioso": contexto_religioso, "technology": contexto_technology, "social": contexto_social, "educativo": contexto_educativo, "gastronomico": contexto_gastronomico, "musical": contexto_musical, "medico": contexto_medico, "ecologico": contexto_ecologico, "politico": contexto_politico }

 
THOUGHT_1 = "eres \"IA\" un generador de DATA" \
			"solo me daras un comentario, una frase o una oración " \
            "en un tipo de comunicación: {comunication}" \
            "el contexto de la situación en la que se da la comunicación es: {context}" \
            "evita mencionar {emotion}, utiliza un sinonimo en caso que lo quieras usar" \
            "la emocion es: {emotion}" \


def random_context():
    return random.choice(list(contextos.keys()))


def get_thought_1(comunication, context, emotion):
    return THOUGHT_1.format(comunication=comunication, context=context, emotion=emotion)
            
