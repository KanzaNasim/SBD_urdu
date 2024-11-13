# Function to merge all text into one large dataset
def merge_all_text(dataset):
    combined_text = ""
    for example in dataset['train']:
        combined_text += example['text'] + " "  
    return combined_text.strip()

# Function to split sentences based on "۔" and remove those with length <= 3
def filter_short_sentences(text):
    # Split the text by "۔"
    sentences = text.split('۔')
    # Filter out sentences with length <= 3
    filtered_sentences = [s.strip() for s in sentences if len(s.strip()) > 3]
    # Join the filtered sentences back with "۔" to get the cleaned text
    cleaned_text = '۔'.join(filtered_sentences)
    
    return cleaned_text

# Function to verify there are no sentences with length 3 or less
def check_short_sentences(text):
    # Split the text by "۔"
    sentences = text.split('۔')
    # Find sentences with length <= 3
    short_sentences = [s.strip() for s in sentences if len(s.strip()) <= 3]
    
    if short_sentences:
        print("Found short sentences:", short_sentences)
    else:
        print("No sentences of length 3 or less found.")

# Function to count the number of sentences based on the period "۔"
def count_sentences(text):
    sentences = text.split('۔') 
    # Filter out empty strings resulting from splitting
    return len([s for s in sentences if s.strip()])  

# Function to remove the Urdu period "۔" from the text
def remove_period(text):
    cleaned_text_without_period = text.replace('۔', '')  
    return cleaned_text_without_period