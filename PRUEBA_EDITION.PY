from PIL import Image
import os

# --- CONFIGURACIÓN (USA TUS RUTAS) ---
ENTRADA = 'C:/Users/jonathan.arrona/Desktop//OTRO'  # Tus fotos originales
SALIDA = 'C:/Users/jonathan.arrona/Desktop/PRUEBA2'    # Carpeta para resultados

# --- ¿CUÁNTOS CENTÍMETROS RECORTAR? (AJUSTA ESTO) ---
CENTIMETROS_A_RECORTAR = 5.0  # Cambia este número (ej: 2, 4, 5...)

# --- FUNCIÓN PRINCIPAL ---
def recortar_fotos():
    # 1. Verificar carpeta de entrada
    if not os.path.exists(ENTRADA):
        print(f"❌ Error: No existe la carpeta {ENTRADA}")
        return
    
    # 2. Crear carpeta de salida
    os.makedirs(SALIDA, exist_ok=True)
    
    # 3. Procesar cada imagen
    print(f"\n✂️ Recortando {CENTIMETROS_A_RECORTAR} cm de cada foto...")
    for archivo in os.listdir(ENTRADA):
        if archivo.lower().endswith('.jpg'):
            try:
                # Abrir imagen
                img = Image.open(os.path.join(ENTRADA, archivo))
                
                # Calcular píxeles a recortar (1 cm ≈ 37.8 píxeles)
                pixeles_a_quitar = int(CENTIMETROS_A_RECORTAR * 37.8)
                nuevo_alto = img.height - pixeles_a_quitar
                
                # Recortar (izquierda, arriba, derecha, nuevo_alto)
                img_recortada = img.crop((0, 0, img.width, nuevo_alto))
                
                # Guardar con máxima calidad
                img_recortada.save(os.path.join(SALIDA, archivo), quality=95)
                print(f"✓ {archivo} → Recortado {CENTIMETROS_A_RECORTAR} cm")
                
            except Exception as e:
                print(f"❌ Error con {archivo}: {str(e)}")
    
    print(f"\n✅ ¡Listo! Fotos recortadas en: {SALIDA}")

# --- EJECUTAR ---
if __name__ == "__main__":
    recortar_fotos()