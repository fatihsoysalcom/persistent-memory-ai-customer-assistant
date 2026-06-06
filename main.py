import json
import os

# Define the file where customer memory will be stored
MEMORY_FILE = "customer_memory.json"

def load_memory():
    """Loads customer memory from a JSON file."""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_memory(memory):
    """Saves customer memory to a JSON file."""
    with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)

def simulate_customer_interaction(customer_id, memory):
    """Simulates a customer support interaction with persistent memory."""
    print(f"\n--- Müşteri Destek Asistanı ({customer_id}) ---")

    # Retrieve existing data for this customer from memory
    customer_data = memory.get(customer_id, {})
    customer_name = customer_data.get("name")
    last_issue = customer_data.get("last_issue")

    # --- Core concept: Using persistent memory ---
    if customer_name:
        # If name is known, personalize the greeting
        print(f"Merhaba tekrar, {customer_name}! Size nasıl yardımcı olabilirim?")
        if last_issue:
            # If a previous issue exists, refer to it
            print(f"Geçen seferki sorununuz '{last_issue}' hakkında mıydı?")
    else:
        # If name is not known, ask for it and store it
        print("Merhaba! Size nasıl yardımcı olabilirim?")
        name_input = input("Adınız nedir? ")
        customer_name = name_input
        customer_data["name"] = customer_name # Store name in memory
        print(f"Memnun oldum, {customer_name}.")

    # Simulate reporting a new issue or continuing an old one
    issue_input = input("Lütfen sorununuzu kısaca açıklayın: ")
    customer_data["last_issue"] = issue_input # Store the current issue in memory
    print(f"Anladım, '{issue_input}' sorununuzu kaydediyorum.")
    print("Destek ekibimiz en kısa sürede sizinle iletişime geçecektir.")

    # Update the overall memory object for this customer
    memory[customer_id] = customer_data
    save_memory(memory) # --- Core concept: Saving memory after interaction ---

    print("--- Etkileşim Sonlandı ---")

if __name__ == "__main__":
    print("MemBot AI ile Kalıcı Hafızalı Müşteri Destek Asistanı Simülasyonu")
    print("----------------------------------------------------------------")

    # A fixed customer ID for demonstration purposes
    DEMO_CUSTOMER_ID = "user_123"

    # --- First Interaction ---
    print("\n--- İlk Etkileşim (Yeni Oturum Başlangıcı) ---")
    customer_memory = load_memory() # Load memory at the start of a session
    simulate_customer_interaction(DEMO_CUSTOMER_ID, customer_memory)

    # --- Second Interaction (Simulating a later, new session for the same customer) ---
    # The script will reload the *saved* memory from the file, demonstrating persistence.
    print("\n--- İkinci Etkileşim (Daha Sonraki Oturum) ---")
    customer_memory_reloaded = load_memory() # Reload memory to simulate a fresh start
    simulate_customer_interaction(DEMO_CUSTOMER_ID, customer_memory_reloaded)

    print("\nDemo tamamlandı. customer_memory.json dosyasını kontrol edebilirsiniz.")
    print("Dosyayı silip tekrar çalıştırarak sıfırdan başlamayı deneyin.")
